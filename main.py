import psycopg2
import os

dbname='codecooler'
user='codecooler'
host='localhost'
password='1234'


def make_default():
    '''
    Restoring default state of APPLICANTS table
    '''
    connect_str = "dbname="+dbname+" user="+user+" host="+host+" password="+password
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(open("default.sql", "r").read())


def psql_executer(psql_command):
    '''
    For Execute PSQL commands
    '''
    try:
        connect_str = "dbname="+dbname+" user="+user+" host="+host+" password="+password
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(psql_command)
    except Exception as e:
        return ('Error: ' + str(e))


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
        colnames = [desc[0] for desc in cursor.description]
        rows = list(cursor.fetchall())
        rows.insert(0, colnames)
        return rows
    except Exception as e:
        return ('Error: ' + str(e))


def print_table(input_table):
    '''
    Printing list in list
    '''
    # search widths
    widths = []
    for i in range(len(input_table[0])):
        widths.append(0)
    for i in range(len(input_table)):
        for j in range(len(input_table[i])):
            if len(str(input_table[i][j])) > widths[j]:
                widths[j] = len(str(input_table[i][j])) + 4

    # print query line by line 
    for i in range(len(input_table)):
        temp_string = ''
        for j in range(len(input_table[i])):
            temp_string += str(input_table[i][j]).ljust(widths[j])
        temp_string += '\n'
        print(temp_string)
    input('\nPress any key to continue')


def main():
    while True:
        os.system('clear')
        # menu
        print('(1) Show mentors')
        print('(2) Miskolc mentors nicknames')
        print('(3) Carol <something> phone number')
        print('(4) Carol reccomendation')
        print('(5) Insert New Data and Select that')
        print('(6) Update Jemima Foreman phone number')
        print('(7) Remove maurise.net APPLICANTS')
        print('(8) Show APPLICANTS table')
        print('(9) Set back to default APPLICANTS table')
        print('(q) Quit\n')

        # input Choic key
        c = input('Your Choice? ')
        c = c.lower()
        os.system('clear')
        if len(c) == 1:
            if c == ('q'):
                break
            elif c == ('1'):
                print_table(psql_query('select first_name, last_name from mentors'))
            elif c == ('2'):
                print_table(psql_query("select first_name, last_name, nick_name from mentors where lower(city) like('misk%')"))
            elif c == ('3'):
                print_table(psql_query("select first_name||' '||last_name as full_name, phone_number from applicants where first_name like 'Carol'"))
            elif c == ('4'):
                print_table(psql_query("select first_name||' '||last_name as full_name, phone_number from applicants where email like '%@adipiscingenimmi.edu'"))
            elif c == ('5'):
                sql_query = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) select fnm, lnm, tel, email, aid from (Select 'Markus' as fnm, 'Schaffarzyk' as lnm, '003620/725-2666' as tel, 'djnovus@groovecoverage.com' as email, 54823 as aid) ss where 54823 not in (select application_code from applicants)" 
                psql_executer(sql_query)
                sql_query = "Select * from applicants where application_code=54823"
                print_table(psql_query(sql_query))
            elif c == ('6'):
                sql_query = "update applicants set phone_number='003670/223-7459' where first_name='Jemima' and last_name='Foreman'"
                psql_executer(sql_query)
                sql_query = "Select * from applicants where first_name='Jemima' and last_name='Foreman'"
                print_table(psql_query(sql_query))
            elif c == ('7'):
                sql_query = "delete from applicants where email like('%@mauriseu.net')"
                psql_executer(sql_query)
                input('Delete complete. Press any key to continue')
            elif c == ('8'):
                print_table(psql_query('select * from applicants'))
            elif c == ('9'):
                make_default()
                input('Restored default state of APPLICANTS table')

if __name__ == '__main__':
    main()