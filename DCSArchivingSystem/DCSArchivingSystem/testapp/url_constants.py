from django.conf import settings

#Upload link. Needs to be here for scanner app.
def upload_url():
    return settings.FORCE_SCRIPT_NAME + '/upload/'
