"""
The user is using cloud-ide-kubernetes tools to complete the Developing AI Applications with Python and Flask course.
"""

from flask import Flask

app = Flask(__name__)

# Import routes to register them with the app
from your_package import app_routes  # Replace 'your_package' with your actual package name
application = app
