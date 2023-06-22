import os, sys

base = '/var/opt/labs/qakbhs/'
base_parent = os.path.dirname(base)


# Remember original sys.path.
prev_sys_path = list(sys.path)


#new path...
if base not in sys.path:
    sys.path.append(base)
if base_parent not in sys.path:
    sys.path.append(base_parent)

env_path = os.path.join(base_parent, 'env/lib/python3.5/site-packages')

# Activate your virtual env
activate_env=os.path.join(base_parent, 'env/bin/activate_this.py')
exec(compile(open(activate_env).read(), activate_env, 'exec'), dict(__file__=activate_env))

#---------------
# add the virtualenv site-packages path to the sys.path
if env_path not in sys.path:
    sys.path.append(env_path)

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
