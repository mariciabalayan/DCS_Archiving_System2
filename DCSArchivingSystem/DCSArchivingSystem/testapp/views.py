#from DCSArchivingSystem.DCSArchivingSystem.models import address, college, contact, course
# patient_management.management.models import Address, Account, Doctor, Clinic, Patient, Reservation, PatientLink, Secretary, SecretaryLink, Consultation
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
# from django.template import RequestContext
from django.contrib.auth.models import User
from models import Faculty, File, Log, Transaction, Dokument, Tag
from forms import ScanForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from list_manipulations import remove_first_characters, subtract_list
import urllib2
import random,string
import re, os
import url_constants
import xlwt

# Create your views here.

# This is the function that is called by a url(...), in urls.py
#def index(request):
#    if request.user.is_authenticated():
#        return render_to_response('dashboard.html', {'user': request.user})
#    else:
#        return render_to_response('index.html')

def index(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', {'user': request.user})
    state = ""
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                print request.session
                
                state = "Login ok!"
                Log.create(user, "Logged in", None, None).save()
                return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/dashboard/")
            else:
                state = "Account not active."
        else:
            state = "* Wrong username or password."

    return render_to_response('login.html',RequestContext(request, {'state':state}))
    
@login_required
def dashboard(request):
    print request.user.is_superuser
    return render_to_response('dashboard.html', { 'user': request.user })

@login_required
def records(request):
    doc_list= Dokument.objects.filter()
    return render_to_response('records.html', {'user': request.user, 'doc_list':doc_list}, context_instance=RequestContext(request))
    
@login_required
def trash(request):
    if request.method=="POST":
        file_list = File.objects.filter(trashed=True)
        for a in file_list:
            if request.POST.get(str(a.id))!=None:
                a.trashed=False
                a.save()
                Log.create(request.user, "Restored a file", a, None).save()
        return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/trash/")
    else:
        is_admin = request.user.is_staff
        file_list = File.objects.filter(trashed=True)
        return render_to_response('trash.html', {'user': request.user, 'file_list':file_list, 'is_admin':is_admin}, context_instance=RequestContext(request))
    
@login_required
def clean_trash(request):
    file_list = File.objects.filter(trashed=True)
    print "CLEAN ALL"
    for a in file_list:
        os.remove(os.path.realpath(os.path.dirname(__file__)) + "/media/" + a.file.name)
        a.delete()
        Log.create(request.user, "Permanently deleted a file", a, None).save()
	docu_list= Dokument.objects.filter(files=None)
	for a in docu_list:
		a.delete()
        Log.create(request.user, "Document was deleted due to zero files attached", None, a).save()

    return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/trash/")
    
@login_required
def restore(request, file_number):
    file = File.objects.get(id=int(file_number))
    file.trashed = False
    file.save()
    Log.create(request.user, "Restored a file", file, None).save()
    return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/trash/")
    
def upload(request):
    if request.POST:
        userid = request.POST.get('userid')
        
        # Queries all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=datetime.now())

        # Checks if session is active
        for session in sessions:
            data = session.get_decoded()
            found_userid=data.get('_auth_user_id')

            # Prceeds when user id is validated
            if found_userid!=None and long(userid)==found_userid:
                user = User.objects.filter(id=userid)[0]
                faculty=None
                faculty=Faculty.objects.filter(id=request.POST.get('fid'))[0]
                transaction = Transaction.objects.get(id=request.POST.get('transaction'))
                document = Dokument()
                document.faculty= faculty
                document.transaction= transaction
                document.save()

                #Generates a random alphanum string for filename template
                while True:
                    fnameTemplate=''
                    fnameTemplate = ''.join(random.choice(string.ascii_lowercase))
                    fnameTemplate += ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(4)) + '_'
                    if len(File.objects.filter(filename__startswith = fnameTemplate))==0: break

                #Processes uploaded files, page by page
                for key in request.FILES:
                    files = request.FILES[key]
                    filename = fnameTemplate + key.split('_')[1] + '.bmp'
                                    
                    #On apache, use this:
                    #with open('absolute/path/to/media/files/' + filename, 'wb+') as destination:
                    #Instead of:
                    #with open('DCSArchivingSystem/testapp/media/files/' + filename, 'wb+') as destination:
                    with open(os.path.realpath(os.path.dirname(__file__)) + '/media/files/' + filename, 'wb+') as destination:
                        for chunk in files.chunks():
                            destination.write(chunk)
                        file = File()
                        file.filename = filename
                        file.file = 'files/' + filename
                        file.save()                    
                        document.files.add(file)
                    Log.create(user, "Uploaded file", file, document).save()    
                Log.create(user, "Created Document", None, document).save()    
                return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/dashboard/")
            
    else:
        return render_to_response('upload.html', context_instance=RequestContext(request))

@login_required
def create_report(request):
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Report")
    faculty = Faculty.objects.all()
    j = 0
    for f in Faculty._meta.fields:
        #write them in the excel
        i = 0
        if f.name != "user" and f.name != "id" and f.name != "photo":
            sheet1.write(i, j, f.name)
            i = i+1

            for a in faculty:
                if f.name == "course" and a.course != None:              # to handle the case of course as foreign key (not good when there is additional foreign key attribute)
                    sheet1.write(i,j, getattr(a.course, "name"))
                else:
                    sheet1.write(i,j, getattr(a, f.name))
                i = i+1
            j = j+1

    book.save("report.xls")
    return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/dashboard/")
    
@login_required
def scan(request):
    return render_to_response('scan.html')

@login_required
def view_file(request, file_number):
    file= File.objects.get(id=int(file_number))
    return render_to_response('view_file.html', {'file':file})

@login_required
def print_page(request, file_number):
    file= File.objects.get(id=int(file_number))
#    print file.file.path
    return render_to_response('print.html', {'file':file})
    
@csrf_exempt
def change(request, document_number):
    doc= Dokument.objects.get(id=int(document_number))
    prevfaculty = doc.faculty
    users_list= Faculty.objects.all()
    if request.method=='POST':
        faculty= request.POST.get('faculty')
        current_faculty = faculty
        faculty_name= faculty
        faculty= faculty.replace(',', "")
        for person in users_list:
            if faculty.split(' ')[0]==person.last_name: 
                for k in faculty.split(' '):
                    if k== person.last_name: continue
                    elif k not in person.first_name: break
                    doc.faculty_id=person.id
        doc.save()
        Log.create(request.user, "Changed owenership of a record owned by " + str(prevfaculty) + " to " + str(current_faculty), None, doc).save()
        return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/records")
    else:
        print 'hi'
        faculty_list= Faculty.objects.all()
        return render_to_response('change.html', {'doc':doc, 'faculty_list':faculty_list})

@login_required
def view(request, document_number):
    doc= Dokument.objects.get(id=int(document_number))
    for a in doc.files.all():
        print "YO",a.file.path
    file_list = doc.files.filter(trashed=False)
    return render_to_response('view.html', {'doc':doc, 'file_list':file_list})

@login_required
def scanpage(request):
    users_list= Faculty.objects.all()

    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list, 'transactions': Transaction.objects.all()}, context_instance=RequestContext(request))

@login_required
def scanpage2(request):
    users_list= Faculty.objects.all()
    transaction= faculty= state= ''
    if request.method=='POST':
        tid= request.POST.get('transaction')
        title= Transaction.objects.get(id=tid)
        faculty_name= request.POST.get('faculty')
        faculty_name= faculty_name.replace(', ', ',')
        nameParts=faculty_name.split(',',1)
        faculty= Faculty.objects.get(last_name=nameParts[0],first_name=nameParts[1])
        faculty_id= faculty.id

        httpHost = "http://%s" %(request.META.get('HTTP_HOST'))
        
        if (title!= None and title != '') and (faculty!= None and faculty!= ''):
            location = "scn://" + urllib2.quote("fid=%d&name=%s&tid=%s&title=%s&uid=%s&origin=%s" %(faculty_id,request.POST.get('faculty'),tid,title,request.session['_auth_user_id'],httpHost+url_constants.upload_url()))
            res = HttpResponse(location, status=302)
            res['Location'] = location
            return res
        
    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list, 'transaction':transaction, 'faculty':faculty, 'state':state}, context_instance=RequestContext(request))

@login_required
def view_users(request):
    users_list= Faculty.objects.all()
    return render_to_response('users.html', {'users_list': users_list}, context_instance=RequestContext(request))
    
@login_required
def view_logs(request):
    if request.user.is_staff:
        log_list= Log.objects.all()
        return render_to_response('logs.html', {'log_list': log_list})
    return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/dashboard/")
    
@login_required
def view_profile(request, faculty_number):
#    current_user = request.user
#    current_faculty = Faculty.objects.get(user_id = current_user.id)
#    return render_to_response('profile.html', {'current_user': current_user, 'current_faculty': current_faculty})
    doc_list= Dokument.objects.filter(faculty_id = int(faculty_number))
    current_faculty = Faculty.objects.get(id = int(faculty_number))
    tagged_docs = Tag.objects.filter(faculty_id = int(faculty_number))
    return render_to_response('profile.html', {'current_faculty': current_faculty, 'file_list': doc_list, 'tagged_docs':tagged_docs}, context_instance=RequestContext(request))


    
@login_required
def request(request):
    doc_list= Dokument.objects.all()
    return render_to_response('request.html', {'doc_list':doc_list})

@csrf_exempt
def request_delete(request, document_number):
    if request.method=="POST":
        doc= Dokument.objects.get(id= int(document_number))
        for k in doc.files.filter(trashed=False):
            if request.POST.get(str(k.id))!=None:
                k.trashed=1
            # else:
            #    k.trashed=0
                k.save()
                Log.create(request.user, "Deleted a file", k, doc).save()
        return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/records")
    else:
        doc= Dokument.objects.get(id= int(document_number))
        return render_to_response('request_delete.html', {'doc':doc})
    
def log_in(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', {'user': request.user})
    state = ""
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Login ok!"
                Log.create(user, "Logged in", None, None).save()
                return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/dashboard/")
            else:
                state = "Account not active."
        else:
            state = "* Wrong username or password."

    return render_to_response('login.html',RequestContext(request, {'state':state}))

def log_out(request):
    Log.create(request.user, "Logged out", None, None).save()
    logout(request)
    return HttpResponseRedirect(settings.FORCE_SCRIPT_NAME + "/")

@csrf_exempt
def search_Faculty(request):
    results = ""
    search_term = ""
    keywords = ""
    if request.GET:
        search_term = request.GET.get('term')
        keywords = search_term.split(' ')
        for x in keywords:
            FN_starts = Faculty.objects.filter(first_name__istartswith=x+" ")
            FN_ends = Faculty.objects.filter(first_name__iendswith=" "+x)
            FN_mids = Faculty.objects.filter(first_name__icontains=" "+x+" ")
            FN_exact = Faculty.objects.filter(first_name__iexact=x)
            LN_starts = Faculty.objects.filter(last_name__istartswith=x+" ")
            LN_ends = Faculty.objects.filter(last_name__iendswith=x+" ")
            LN_mids = Faculty.objects.filter(last_name__icontains=" "+x+" ")
            LN_exact = Faculty.objects.filter(last_name__iexact=x)
            results = FN_starts| FN_ends| FN_mids| FN_exact| LN_starts| LN_ends| LN_mids| LN_exact
    return render_to_response('searchFaculty.html', {'user': request.user, 'results': results, 'keyword': search_term}, context_instance=RequestContext(request))

@csrf_exempt
def search_Files(request, current_id):
    results = ""
    current_faculty = Faculty.objects.get(id = int(current_id))
    search_term = ""
    tagged_docs = ""
    x = ""
    if request.GET:
        search_term = request.GET.get('term')
        keywords = search_term.split(' ')
        for x in keywords:
            trans_starts = Dokument.objects.filter(transaction__name__istartswith=x+" ", faculty_id = int (current_id))
            trans_ends = Dokument.objects.filter(transaction__name__iendswith=" "+x, faculty_id = int (current_id))
            trans_mids = Dokument.objects.filter(transaction__name__icontains=" "+x+" ", faculty_id = int (current_id))
            trans_exact = Dokument.objects.filter(transaction__name__iexact=x, faculty_id = int (current_id))
            results = trans_starts | trans_ends | trans_mids | trans_exact
        tagged_docs = Tag.objects.filter(faculty_id = int(current_id))
    return render_to_response('searchFiles.html', {'user': request.user, 'current_faculty': current_faculty, 'results': results, 'keyword': search_term, 'tagged_docs': tagged_docs}, context_instance=RequestContext(request))

@csrf_exempt
def search_Records(request):
    results = ""
    keywords = ""
    if request.GET:
        search_term     = request.GET.get('term')
        #keywords = search_term.split(' ')
        keywords        = re.findall(r"[\w]+", search_term)
        plus            = re.findall(r"\+[\w']+", search_term)
        minus           = re.findall(r"-[\w']+", search_term)
        remove_first_characters(plus)
        remove_first_characters(minus)
        subtract_list(keywords, plus)
        subtract_list(keywords, minus)

        for x in keywords:
            trans_starts= Dokument.objects.filter(transaction__name__istartswith=x+" ")
            trans_ends  = Dokument.objects.filter(transaction__name__iendswith=" "+x)
            trans_mids  = Dokument.objects.filter(transaction__name__icontains=" "+x+" ")
            trans_exact = Dokument.objects.filter(transaction__name__iexact=x)
            results = trans_starts | trans_ends | trans_mids | trans_exact
            trans_starts= Dokument.objects.filter(transaction__search_tags__istartswith=x+" ")
            trans_ends  = Dokument.objects.filter(transaction__search_tags__iendswith=" "+x)
            trans_mids  = Dokument.objects.filter(transaction__search_tags__icontains=" "+x+" ")
            trans_exact = Dokument.objects.filter(transaction__search_tags__iexact=x)
            results = results | trans_starts | trans_ends | trans_mids | trans_exact

        for x in plus:
            trans_starts = Dokument.objects.filter(transaction__search_tags__istartswith=x+" ")
            trans_ends = Dokument.objects.filter(transaction__search_tags__iendswith=" "+x)
            trans_mids = Dokument.objects.filter(transaction__search_tags__icontains=" "+x+" ")
            trans_exact = Dokument.objects.filter(transaction__search_tags__iexact=x)
            if len(results) == 0:
                results = (trans_starts | trans_ends | trans_mids | trans_exact)
            else:
                results = results & (trans_starts | trans_ends | trans_mids | trans_exact)

        for x in minus:
            if len(results) != 0:
                results = results.exclude(transaction__search_tags__istartswith=x+" ")
                results = results.exclude(transaction__search_tags__iendswith=" "+x)
                results = results.exclude(transaction__search_tags__icontains=" "+x+" ")
                results = results.exclude(transaction__search_tags__iexact=x)
    return render_to_response('searchRecords.html', {'user': request.user, 'results': results, 'keyword': search_term}, context_instance=RequestContext(request))
