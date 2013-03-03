from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('DCSArchivingSystem.testapp.views',
    # 'DCSArchivingSystem.testapp.views' is a prefix
    # If prefix is empty (Eg. ''), we will need to use
    # DCSArchivingSystem.testapp.views.main_page instead of just main_page
    
    # Examples:
    # url(r'^$', 'DCSArchivingSystem.views.home', name='home'),
    # url(r'^DCSArchivingSystem/', include('DCSArchivingSystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #view
    url(r'^records/(?P<document_number>[0-9]+)/view/$', 'view'),

    
	#Records
    url(r'^records/$', 'records'),

    #Request
    url(r'^request/$', 'request'),
	
    # Logged in
    url(r'^dashboard/$', 'dashboard'),
    
    # Login/Logout
    url(r'^login/$', 'log_in'),
    url(r'^logout/$', 'log_out'),

    # Scan Page
    url(r'^scanpage/$', 'scanpage'),
    url(r'^scanpage2/$', 'scanpage2'),
        
    # Scan
    url(r'^scan/$', 'scan'),
    
    #Faculty Search Page
    url(r'^users/search/$', 'search_Faculty'),
	
	#Files Search Page
	url(r'^users/(?P<current_id>[0-9]+)/profile/search/$', 'search_Files'),
	
	#Records Search Page
	url(r'^records/search/$', 'search_Records'),
	
    #Users Page
    url(r'^users/$', 'view_users'),
    
    # Upload
    url(r'^upload/$', 'upload'),
    
    # Logs
    url(r'^logs/$', 'view_logs'),
    
    #Profile
    url(r'^users/(?P<faculty_number>[0-9]+)/profile/$', 'view_profile'),
    
    #Request Delete
    url(r'^request/(?P<document_number>[0-9]+)/delete/$', 'request_delete'),
    url(r'^records/(?P<document_number>[0-9]+)/delete/$', 'request_delete'),
    
    #print
    url(r'^print/(?P<file_number>[0-9]+)/$', 'print_page'),

    url(r'^files/(?P<file_number>[0-9]+)/$', 'view_file'),

    
    # Main Page
    url(r'^$', 'index'),
    

    
    # URL format:
    # If browser url is www.mypage.com/pathInBrowser
    # Just add url(r'^pathInBrowser$', 'function in views.py'),
    # Don't forget the comma at the end of url(...),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
