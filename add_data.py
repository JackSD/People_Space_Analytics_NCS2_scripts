
from datetime import datetime
import psycopg2

def send_data( num_people, allowable_people):
    connection = psycopg2.connect(user="postgres",
                                  password="xx",
                                  host="35.205.119.160",
                                  port="5432",
                                  database="computer-vision-project")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    cursor = connection.cursor()
    now = datetime.now()

    postgres_insert_query = """ INSERT INTO public.overcrowding_alerts ( LOCATION, LOGDATE,  NUM_PEOPLE, ALLOWABLE_PEOPLE) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ( 'Supermarket', now, num_people,allowable_people)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into table")

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(True)

def send_coordinates( x,y,height):
    connection = psycopg2.connect(user="postgres",
                                  password="xx",
                                  host="35.205.119.160",
                                  port="5432",
                                  database="computer-vision-project")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    cursor = connection.cursor()
    now = datetime.now()

    postgres_insert_query = """ INSERT INTO public.detected_people_coordinates ( Location, object_type,  logtime, x,y,height) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = ( 'Street', 'Person', now,  x,y,height)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into table")

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(True)
