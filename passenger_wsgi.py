# import imp
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'app.py')
# application = wsgi.application

import os
import sys
from importlib.util import spec_from_file_location, module_from_spec

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Load the app.py module
spec = spec_from_file_location("wsgi", "run.py")
wsgi = module_from_spec(spec)
spec.loader.exec_module(wsgi)

# Get the application object
application = wsgi.application
