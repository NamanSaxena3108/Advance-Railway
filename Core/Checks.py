#  This Module has all the required functions to perform the operations on the database
import mysql.connector as con
from mysql.connector.errors import ProgrammingError,Error
import Core.InsertData as Insert

def CheckDatabase():
    print("Checking Database Requirement..")
    db = con.connect(
        host = "127.0.0.1",
        user = "root",
        database = " ",
        password = "Saxena@2004"
        )
    cur = db.cursor()
    result = None

    try : 
        cur.execute("USE testdb;")
    except ProgrammingError:
        print("Database does not exist")
        result = False
    else:
        result = True
    
    if result is True:
        print("Database Exists!")
    else:
        print("Creating Database with required Tables")
        print("Please Wait for a while")
        cur.execute("CREATE DATABASE testdb;")
        cur.execute("USE testdb;")
        CreateTable()
        print("Database and Tables Created")
    cur.close()
    db.close()

def CreateTable():
    db = con.connect(host="127.0.0.1",
                     user="root",
                     database="testdb",
                     password="Saxena@2004")
    cur = db.cursor()
    cur.execute("CREATE TABLE train_info (Train_No VARCHAR(10) NOT NULL, Station_Code VARCHAR(20) NOT NULL, Station_Name VARCHAR(30) NOT NULL, Arrival_Time VARCHAR(20) NOT NULL, Departure_Time VARCHAR(20) NOT NULL, Distance VARCHAR(10) NOT NULL, Source_Station_Code VARCHAR(20) NOT NULL, Source_Station_Name VARCHAR(70) NOT NULL, Destination_Station_Code VARCHAR(20) NOT NULL, Destination_Station_Name VARCHAR(60) NOT NULL);")
    cur.execute("CREATE TABLE bookings (Train_No INT NOT NULL, Passenger_Name VARCHAR(30) NOT NULL, Mobile_No VARCHAR(10) NOT NULL, Passenger_Adhaar VARCHAR(12) NOT NULL, Date_Of_Booking VARCHAR(20) NOT NULL, PNR_No VARCHAR(13) NOT NULL, Class VARCHAR(20) NOT NULL, Date_Of_Travel VARCHAR(20) NOT NULL, Age INT NOT NULL);")
    Insert.InsertTrainData()
    cur.close()
    db.close()

def CheckConnection():
    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(
            host = "127.0.0.1",
            user = "root",
            database = " ",
            password = "Saxena@2004")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)
    except Error as e:
        print(e)
        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True