#from DCSArchivingSystem.DCSArchivingSystem.models import address, college, contact, course
# patient_management.management.models import Address, Account, Doctor, Clinic, Patient, Reservation, PatientLink, Secretary, SecretaryLink, Consultation
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from models import Faculty, File, Log, Transaction, Dokument
from forms import ScanForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from itertools import *

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
                Log.create(user, "Logged in", None).save()
                return HttpResponseRedirect("/dashboard/")
            else:
                state = "Account not active."
        else:
            state = "* Wrong username or password."

    return render_to_response('login.html',RequestContext(request, {'state':state}))
    
@login_required
def dashboard(request):
    return render_to_response('dashboard.html', { 'user': request.user })

@login_required
def records(request):
    doc_list= Dokument.objects.all()
    return render_to_response('records.html', {'user': request.user, 'doc_list':doc_list} )
	
def upload(request):
    if request.POST:
        userid = request.POST.get('userid')
        
        # Queries all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=datetime.now())

        # Checks if session is active
        for session in sessions:
            data = session.get_decoded()
            print long(userid),data
            found_userid=data.get('_auth_user_id')
            if found_userid!=None and long(userid)==found_userid:
                user = User.objects.filter(id=data.get('_auth_user_id'))[0]
                # Prceeds when user id is validated
                print request.FILES
                faculty=None
                faculty_id = request.POST.get('fid')
                for person in Faculty.objects.all():
                    if int(faculty_id) is int(person.id): faculty=person;
                reqfname = request.POST.get('filename')
                filename = faculty.last_name +'_' + faculty.first_name + reqfname
                print filename, len(filename)
                page = request.POST.get('pages')
                transaction_name = request.POST.get('transaction')
                transaction = Transaction()
                transaction.name=transaction_name
                transaction.save()
                document = Dokument()
                document.faculty= faculty
                document.transaction= transaction
                document.save()
                for key in request.FILES:
                    files = request.FILES[key]
                    with open('DCSArchivingSystem/testapp/media/files/' + filename + key.split('_')[1] + '.bmp', 'wb+') as destination:
                        for chunk in files.chunks():
                            destination.write(chunk)
                        ######################### now okay ###################
                        file = File()
                        file.filename = filename
                        file.file = 'files/' + filename
                        file.save()                    
                        document.files.add(file)
                        ########################################################
                    Log.create(user, "Uploaded file", file).save()    
                Log.create(user, "Created Document", file).save()    
                return HttpResponseRedirect("/dashboard/")
            
    else:
        return render_to_response('upload.html', context_instance=RequestContext(request))
    
@login_required
def scan(request):
    return render_to_response('scan.html')

@login_required
def scanpage(request):
    users_list= Faculty.objects.all()

    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list, 'transactions': Transaction.objects.all()}, context_instance=RequestContext(request))

@login_required
def scanpage2(request):
    users_list= Faculty.objects.all()
    title= faculty= pages= state= ''
    if request.method=='POST':
        title= request.POST.get('title')
        faculty= request.POST.get('faculty')
        pages= request.POST.get('pages')
        faculty_name= faculty
        faculty= faculty.replace(',', "")
        for person in users_list:
            if faculty.split(' ')[0]==person.last_name: faculty_id=person.id
        if (title!= None and title != '') and (faculty!= None and faculty!= '') and pages!='' and pages!= None:
            if int(pages)<0:
                state= 'Invalid number of pages.'

            else:
                location = "scn://fid=%d&name=%s&title=%s&user_id=%s" %(faculty_id,request.POST.get('faculty'),title,request.session['_auth_user_id'])
                res = HttpResponse(location, status=302)
                res['Location'] = location
                return res
        
    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list, 'title':title, 'pages':pages, 'faculty':faculty, 'state':state}, context_instance=RequestContext(request))

@login_required
def view_users(request):
    users_list= Faculty.objects.all()
    return render_to_response('users.html', {'users_list': users_list})
    
@login_required
def view_logs(request):
    if request.user.is_staff:
        log_list= Log.objects.all()
        return render_to_response('logs.html', {'log_list': log_list})
    return HttpResponseRedirect("/dashboard/")
    
@login_required
def view_profile(request, faculty_number):
#    current_user = request.user
#    current_faculty = Faculty.objects.get(user_id = current_user.id)
#    return render_to_response('profile.html', {'current_user': current_user, 'current_faculty': current_faculty})
    doc_list= Dokument.objects.filter(faculty_id = int(faculty_number))
    current_faculty = Faculty.objects.get(id = int(faculty_number))
    return render_to_response('profile.html', {'current_faculty': current_faculty, 'file_list': doc_list})

    
@login_required
def request(request):
    doc_list= Dokument.objects.all()
    return render_to_response('request.html', {'doc_list':doc_list})

@csrf_exempt
def request_delete(request, document_number):
    if request.POST:
        doc= Dokument.objects.get(id= int(document_number))
        for k in doc.files.all():
#            print request.POST.get(str(k.id)), k.id
            if request.POST.get(str(k.id))!=None:
                k.delete=1
            else:
                k.delete=0
            k.save()
        return HttpResponseRedirect("#")
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
                Log.create(user, "Logged in", None).save()
                return HttpResponseRedirect("/dashboard/")
            else:
                state = "Account not active."
        else:
            state = "* Wrong username or password."

    return render_to_response('login.html',RequestContext(request, {'state':state}))

def log_out(request):
    Log.create(request.user, "Logged out", None).save()
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def search_Faculty(request):
    state = ""
    if request.POST:
        search_term = request.POST.get('term')
        keywords = search_term.split(' ')
        print "keywords: "
        print keywords
        results = ""
        for x in keywords:
            FN_starts = Faculty.objects.filter(first_name__istartswith=x+" ")
            FN_ends = Faculty.objects.filter(first_name__iendswith=" "+x)
            FN_mids = Faculty.objects.filter(first_name__icontains=" "+x+" ")
            FN_exact = Faculty.objects.filter(first_name__iexact=x)
            LN_starts = Faculty.objects.filter(last_name__istartswith=x+" ")
            LN_ends = Faculty.objects.filter(last_name__iendswith=x+" ")
            LN_mids = Faculty.objects.filter(last_name__icontains=" "+x+" ")
            LN_exact = Faculty.objects.filter(last_name__iexact=x)
            results = chain(results, FN_starts, FN_ends, FN_mids, FN_exact, LN_starts, LN_ends, LN_mids, LN_exact)
        state = "Search results for: " + search_term
    return render_to_response('searchFaculty.html', {'user': request.user, 'state': state, 'results': results}, context_instance=RequestContext(request))

@csrf_exempt
def search_Files(request, current_id):
    print "andito ako"
    state = ""
    results = ""
    current_faculty = Faculty.objects.get(id = int(current_id))
    if request.POST:
        search_term = request.POST.get('term')
        keywords = search_term.split(' ')
        print "keywords: "
        for x in keywords:
            results = File.objects.filter(faculty_id = int(current_id), filename__icontains=x)
        state = "Search results for: " + search_term
    return render_to_response('searchFiles.html', {'user': request.user, 'state': state, 'current_faculty': current_faculty, 'results': results}, context_instance=RequestContext(request))

