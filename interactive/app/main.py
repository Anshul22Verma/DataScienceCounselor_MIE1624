from flask import render_template, url_for, g, session, request, redirect, flash, send_from_directory
from app import webapp
import mysql.connector
import os, re, io
from werkzeug.utils import secure_filename
from app.verification import Unique_Name, allowed_file, User_Authentication
from app.Hashing_n_Checking import hash_password
from datetime import timedelta

from app.config import db_config, root_loc
from app.analysis import extract_from_resume

webapp.secret_key = '\x80\xa9s*\x12\xc7x\xa9d\x1f(\x03\xbeHJ:\x9f\xf0!\xb1a\xaa\x0f\xee'

#functions to connect to data-base
def connect_to_database():
    return mysql.connector.connect(user=db_config['user'],
                                   password=db_config['password'],
                                   host=db_config['host'],
                                   database=db_config['database'])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@webapp.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#login page with its route
@webapp.route('/',methods=['GET'])
@webapp.route('/Login', methods = ['POST', 'GET'])
def main():
    if (request.method == 'POST' and 'username' in request.form and 'password' in request.form):
        username = request.form.get('username', "")
        password = request.form.get('password', "")
        #Because we allow only numeric and character based passwords
        password = str(password)
        cnx = get_db()
        cursor = cnx.cursor(buffered=True)

        Authenticate, msg, ID = User_Authentication(cursor, username, password)
        if Authenticate:

            session['loggedin'] = True
            session['id'] = ID
            session['username'] = username
            flash('Login Successful', 'isa_info')
            session.permanent = True
            webapp.permanent_session_lifetime = timedelta(hours=24)
            return redirect(url_for('home', username = username))
        else:
            flash(msg, 'isa_err')
            return render_template('main.html', username=username)
    return render_template('main.html')

@webapp.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('username', "")
        password = request.form.get('password', "")
        #Because only numeric usernames and passwords are allowed
        password = str(password)
        username = str(username)

        cnx = get_db()
        cursor = cnx.cursor(buffered=True)
        query = "SELECT id FROM user WHERE username = %s"
        cursor.execute(query, (username,))
        account = cursor.fetchone()
        if account is not None:
            flash("Username already exists if its your then please Login or use a different username.", 'isa_info')
            return render_template('register.html', username = username)
        else:
            if username == '' or password == '':
                flash('Please enter a valid Username and Password', 'isa_err')
                return redirect(url_for('register'))
            elif (len(username) > 100):
                    flash ('Maximum length of allowed username is 100', 'isa_err')
                    return redirect(url_for('register'))
            else:
                flash('Registeration Successful !', 'isa_info')
                hashedpass = hash_password(password)
                query = 'INSERT INTO user (id, username, password) VALUES (NULL, %s, %s)'
                cursor.execute(query, (username, hashedpass))
                cnx.commit()
                return render_template('main.html', username=username)
    return render_template('register.html')

@webapp.route('/<username>/home', methods = ['POST', 'GET'])
def home(username):
    if 'loggedin' in session:
        cnx = get_db()
        cursor = cnx.cursor(buffered=True)
        query = '''SELECT r.resume_loc
                    FROM user u, resume r 
                    WHERE u.username = %s AND u.id = r.userId'''
        cursor.execute(query, (username,))
        resume = cursor.fetchone()
        suggestions, matching_jobs = extract_from_resume(resume)
        print(suggestions)
        print(matching_jobs)
        return render_template("home.html", username=username, S=suggestions, MJ=matching_jobs)
    return redirect(url_for('main', username=username))

@webapp.route('/upload', methods = ['POST', 'GET'])
def upload():
    if 'loggedin' in session:
        cnx = get_db()
        cursor = cnx.cursor(buffered=True)
        username = session['username']
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file found!', 'isa_err')
                return redirect(url_for('home', username=username))
            else:
                pdf = request.files['file']
                #pdf.seek(0, os.SEEK_END)
                #size = pdf.tell()
                #if size > (100 * (1e6)) or size == None:
                #    flash('Can not accept the file', 'isa_err')
                #pdf = request.files['file']
                if pdf.filename == "":
                    flash('No selected file!', 'isa_err')
                    return redirect(url_for('home', username=username))
                elif pdf and allowed_file(pdf.filename):
                    #pdf = request.files['file']
                    filename = secure_filename(pdf.filename)
                    #Logged in user can use other users credentials but uploaded pic will only be accessible to the logged in user ID
                    ID = session['id']

                    [name, ext] = filename.rsplit('.', 1)
                    name = str(ID) + name
                    # Generating a unique file name based on what is existing in the database
                    nxt_unq_name = Unique_Name(cursor, ID, name, ext)
                    nxt_unq_name = nxt_unq_name + '.' + ext

                    # saving the resume
                    pdf_loc = os.path.join(root_loc, nxt_unq_name)
                    #Deleting all the previous resume uplaoded by the user
                    query = '''SELECT r.resume_loc FROM user u, resume r
                                WHERE r.userId = u.id AND u.id = %s'''
                    cursor.execute(query, (ID,))
                    old_resume_locs = cursor.fetchall()
                    for old_rlocs in old_resume_locs:
                        os.remove(old_rlocs[0])
                    #Removing the old entries from the resume table
                    query = '''DELETE FROM resume WHERE userId = %s'''
                    cursor.execute(query, (ID,))
                    cnx.commit()

                    # Saving the new resume
                    pdf.save(pdf_loc)
                    query = '''INSERT into resume (userId, resume, resume_loc)
                                VALUES(%s, %s, %s)'''
                    cursor.execute(query, (ID, nxt_unq_name, pdf_loc))
                    cnx.commit()
                    query = '''SELECT r.resume_loc
                                FROM user u, resume r 
                                WHERE u.username = %s AND u.id = r.userId'''
                    cursor.execute(query, (username,))
                    resume = cursor.fetchone()
                    suggestions, matching_jobs = extract_from_resume(resume)

                    flash('Resume Uploaded', 'isa_info')
                    return render_template("home.html", username=username, S=suggestions, MJ=matching_jobs)
                else:
                    flash('Only enter .pdf type files!', 'isa_err')
                    return redirect(url_for('home', username=username))
        return redirect(url_for('home', username=username))
    return render_template("main.html")

@webapp.route('/home/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    flash('Logged Out!', 'isa_info')
    return redirect(url_for('main'))
