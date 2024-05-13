import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("success")
    except Error as e:
        print(f'the error {e} occured')
    return connection

conn = create_con('cis3368fall.c6dfb4bycouh.us-east-1.rds.amazonaws.com', 'admin', 'adminpassword', 'cis3368')
cursor = conn.cursor(dictionary=True)
def main():
    mylist = []
    while True:
        operation = input('''
Menu:  
[a] Add travel log
[d] Remove travel log
[u] Update travel log
[o] output entire log in console
[s] Save travel log to database
[q] Exit programm

''')
        if operation == 'a':  # adds record to log
            print("Add travel log info: ")
            travel_id = int(input('Enter the id:\n'))
            travel_year = int(input('Enter year of travel:\n'))
            travel_comment = input('Enter your travel comment:\n')
            travel_revisit = input('Revisit this location (yes or no)?:\n')
            travel_to_add = (travel_id, travel_year, travel_comment, travel_revisit)
            mylist.append(travel_to_add)


        elif operation == 'd':  # deletes record
            print("Type the record number you would like to remove: ")
            number = int(input())
            mylist.pop(number)  # dont forget that 0 is the first record. To delete the fifth record type 4

        elif operation == 'u':  # updates record
            print('\nUpdate travel log')
            remove_record_to_update= int(input('Type the record number you wish to update\n'))  # make sure to know what index number you want to delete. It should associate with record you want to update.
            mylist.pop(remove_record_to_update)
            new_id = int(input('Enter the updated travel id:\n'))
            new_year = int(input('Enter updated year:\n'))
            new_travel_comment = input('Enter updated travel comment:\n')
            new_travel_revisit = input('Enter updated travel revisit information:\n')
            travel_to_update= ( new_id, new_year, new_travel_comment, new_travel_revisit)
            mylist.append(travel_to_update)

        elif operation == 'o':  # output record
            print(mylist)

        elif operation == 's':  # save record
            addQuery = f"INSERT INTO log (id, year, comment, revisit) VALUES ('{travel_id}', '{travel_year}', '{travel_comment}', '{travel_revisit}')"
            print(addQuery)
            cursor.execute(addQuery)
            conn.commit()
            print('Successful')
            print("Save travel log to database")

        elif operation == 'q':  # exit menu
            break

        else:  # made a typo
            print("Please try again.")
main()