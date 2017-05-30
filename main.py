from flask import Flask, render_template, url_for, redirect, request
import psycopg2
import os

app = Flask(__name__, static_url_path='/static')

dbname = 'flashback'
user = 'flashback'
host = 'localhost'
password = '1234'


@app.route('/mentors')
def mentors():
    """On this page you should show the result of a query that returns the name of the mentors plus the name
    and country of the school (joining with the schools table) ordered by the mentors id column 
    (columns: mentors.first_name, mentors.last_name, schools.name, schools.country)."""
    list_title = "Mentors and schools page"
    mentors_data_set = psql_query("SELECT m.first_name || ' ' || m.last_name as Mentor_Name, schools.name, schools.country FROM mentors m left join schools on m.city = schools.city order by m.id;")
    return render_template('list.html', datas=mentors_data_set, title=list_title)


@app.route('/all-school')
def all_school():
    """On this page you should show the result of a query that returns the name of the mentors 
    plus the name and country of the school (joining with the schools table) ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country"""
    list_title = "All school page "
    mentors_data_set = psql_query("SELECT m.first_name || ' ' || m.last_name as Mentor_Name, schools.name, schools.country FROM mentors m right join schools on m.city = schools.city order by m.id;")
    return render_template('list.html', datas=mentors_data_set, title=list_title)


@app.route('/mentors-by-country')
def mentors_by_country():
    """On this page you should show the result of a query that returns the number of the mentors
    per country ordered by the name of the countries columns: country, count"""
    list_title = "Mentors by Country"
    mentors_data_set = psql_query("SELECT count(m.first_name), s.country FROM mentors m left join schools s on m.city = s.city group by s.country order by s.country")
    return render_template('list.html', datas=mentors_data_set, title=list_title)


@app.route('/contacts')
def contacts():
    """On this page you should show the result of a query that returns the name of the school 
    plus the name of contact person at the school (from the mentors table) ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name"""
    list_title = "Contacts page"
    mentors_data_set = psql_query("select s.name, m.first_name || ' ' || m.last_name as Mentor_Name from schools s inner join mentors m on m.id=s.contact_person order by s.name")
    return render_template('list.html', datas=mentors_data_set, title=list_title)


@app.route('/applicants')
def applicants_page():
    """On this page you should show the result of a query that returns the first name 
    and the code of the applicants plus the creation_date of the application 
    (joining with the applicants_mentors table) ordered by the creation_date in descending order
    BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date"""
    list_title = "Applicants page"
    mentors_data_set = psql_query("select a.first_name, a.application_code, am.creation_date from applicants a inner join applicants_mentors am on a.id=am.applicant_id where am.creation_date>to_date('2016-01-01', 'YYYY-MM-DD')")
    return render_template('list.html', datas=mentors_data_set, title=list_title)
    

@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    """On this page you should show the result of a query that returns the first name 
    and the code of the applicants plus the name of the assigned mentor 
    (joining through the applicants_mentors table) ordered by the applicants id colum
    Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string 'None' instead of the mentor name
    columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name"""
    list_title = "Applicants and mentors page"
    mentors_data_set = psql_query("select a.first_name, a.application_code, case when am.mentor_id>0 then (select m.first_name || ' ' || m.last_name as mn from mentors m where am.mentor_id=m.id) end as Mentor_name from applicants a left join applicants_mentors am on am.applicant_id=a.id")
    return render_template('list.html', datas=mentors_data_set, title=list_title)


def make_default():
    '''
    Restoring default state of APPLICANTS table
    '''
    connect_str = "dbname="+dbname+" user="+user+" host="+host+" password="+password
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(open("application_process_sample_data_2", "r").read())


def psql_query(psql_command):
    '''
    For Execute PSQL querie and get back the result with column names 
    '''
    try:
        connect_str = "dbname="+dbname+" user="+user+" host="+host+" password="+password
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(psql_command)
        if (psql_command[:6].upper() == "SELECT"):
            colnames = [desc[0] for desc in cursor.description]
            rows = list(cursor.fetchall())
            rows.insert(0, colnames)
            return rows
        return "Command executed"
    except Exception as e:
        return ('Error: ' + str(e))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()