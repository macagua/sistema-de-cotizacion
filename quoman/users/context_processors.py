from django.conf import settings

def project_name(request):
    ''' return the PROJECT_NAME constant value from the settings. '''
    return {'PROJECT_NAME': settings.PROJECT_NAME}
