"""
    This file will trigger the the whole application
"""

from patient import *
from settings import *
from patient import app,db
app.app_context().push()
db.create_all()
print('done')
