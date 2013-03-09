#Just change the return values

#Url prefix. Default: ''
#Change only when deployed in apache
def url_prefix():
    return ''

#Upload link. Needs to be here for scanner app.
def upload_url():
    return url_prefix() + 'upload/'
