"""
This file creates your application.
"""
import os
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    # "index.html" is a file found in the "templates" folder. It is mostly regular
    # HTML with some special templating syntax mixed in. The templating
    # language is called Jinja.
    return render_template('layout.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello World!'

@app.route('/lti/testlaunch', methods=['GET', 'POST'])
def lti_test_launch():
  # POST parameters
  # print request.form.keys()
  print request.args.keys()
  return render_template('lti_test_launch.html', post=request.form, get=request.args)

# I like to make certain values available on any rendered template without
# explicitly naming them. While these values won't change very often, I would
# rather not keep track of where they are used so I don't have to remember to
# change the value everywhere.  Programmers are lazy :)
@app.context_processor
def inject_app_info():
  return {
      'version':"0.0.2-step2",
      'project_name':'LTI Starter'
      }

if __name__ == '__main__':
  ''' IP and PORT are two environmental variables configured in Cloud9. They
  can change occasionally without warning so the application must be able to
  dynamically detect the change on each startup. Reasonable default values of 
  hostname 0.0.0.0 and port 5000 are set as well.'''

  app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',5000)))    
