#from DCSArchivingSystem.DCSArchivingSystem.models import address, college, contact, course
# patient_management.management.models import Address, Account, Doctor, Clinic, Patient, Reservation, PatientLink, Secretary, SecretaryLink, Consultation
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from models import Faculty, File, Log, Transaction
from forms import ScanForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import uuid, M2Crypto

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

                #Add session id
                request.session['_auth_sess_id'] = uuid.UUID(bytes = M2Crypto.m2.rand_bytes(16))
                
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

def upload(request):
    if request.POST:
        sessid = request.POST.get('sessid')
        
        # Query all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=datetime.now())

        # Checks if session is active
        for session in sessions:
            data = session.get_decoded()
            found_sessid=data.get('_auth_sess_id')
            if found_sessid!=None and uuid.UUID(sessid)==found_sessid:
                user = User.objects.filter(id=data.get('_auth_user_id'))[0]
                # Prceeds when session id is validated
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
                for key in request.FILES:
                    files = request.FILES[key]
                    with open('DCSArchivingSystem/testapp/media/files/' + filename + key.split('_')[1] + '.bmp', 'wb+') as destination:
                        for chunk in files.chunks():
                            destination.write(chunk)
                        ######################### now okay ###################
                        file = File()
                        file.filename = filename
                        file.faculty = faculty                     
                        file.transaction = transaction
                        file.file = 'files/' + filename
                        file.save()                                
                        ########################################################
                    Log.create(user, "Uploaded file", file).save()    
                return HttpResponseRedirect("/dashboard/")
            
    else: return render_to_response('upload.html', context_instance=RequestContext(request))
    
@login_required
def scan(request):
    return render_to_response('scan.html')

@login_required
def scanpage(request):
    users_list= Faculty.objects.all()
    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list}, context_instance=RequestContext(request))

@login_required
def scanpage2(request):
    users_list= Faculty.objects.all()
    title= faculty= pages= state= ''
    if request.method=='POST':
        title= request.POST.get('title')
        faculty= request.POST.get('faculty')
        pages= request.POST.get('pages')
        sessid= request.session['_auth_sess_id']
        faculty_name= faculty
        faculty= faculty.replace(',', "")
        for person in users_list:
            if faculty.split(' ')[0]==person.last_name: faculty_id=person.id
        if (title!= None and title != '') and (faculty!= None and faculty!= '') and pages!='' and pages!= None:
            if int(pages)<0:
                state= 'Invalid number of pages.'

            else:
                return render_to_response('scanpage2.html', { 'user': request.user, 'faculty_list': users_list, 'title':title, 'faculty':faculty_name, 'fid':faculty_id, 'sessid':request.session['_auth_sess_id'], 'state':state}, context_instance=RequestContext(request))
        
    return render_to_response('scanpage.html', { 'user': request.user, 'faculty_list': users_list, 'title':title, 'pages':pages, 'faculty':faculty, 'state':state}, context_instance=RequestContext(request))

@login_required
def view_users(request):
    users_list= Faculty.objects.all()
    return render_to_response('users.html', {'users_list': users_list})
    
@login_required
def view_logs(request):
    log_list= Log.objects.all()
    return render_to_response('logs.html', {'log_list': log_list})
    
@login_required
def view_profile(request, faculty_number):
#    current_user = request.user
#    current_faculty = Faculty.objects.get(user_id = current_user.id)
#    return render_to_response('profile.html', {'current_user': current_user, 'current_faculty': current_faculty})
    file_list= File.objects.filter(faculty_id = int(faculty_number))
    current_faculty = Faculty.objects.get(id = int(faculty_number))
    return render_to_response('profile.html', {'current_faculty': current_faculty, 'file_list': file_list})
    
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
    
"""def log_in(request):
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
                return HttpResponseRedirect("/dashboard/")
            else:
                state = "Account not active."
        else:
            state = "* Wrong username or password."

    return render_to_response('login.html',RequestContext(request, {'state':state}))

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')"""

@csrf_exempt
def search(request):
    state = ""
    if request.POST:
        search_term = request.POST.get('term')
        results = Faculty.objects.filter(first_name__icontains=search_term) or Faculty.objects.filter(last_name__icontains=search_term)
        if results is not None:
            state = "Results available"
        else:
            state = "No results found."
    return render_to_response('search.html', {'user': request.user, 'state': state, 'results': results}, context_instance=RequestContext(request))
