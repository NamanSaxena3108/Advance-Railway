# This module contain all the functions that can be performed by the user to do some task's.
import mysql.connector
import datetime
from mysql.connector import DataError
import random

sleeper_charge = int(1.5)
third_ac_charge = int(2)
second_ac_charge = int(3)
first_ac_charge = int(4)

current_date = datetime.date.today()

max_date = current_date + datetime.timedelta(days=120)

def AvailableTrains(start, final, date_user):
    mn = mysql.connector.connect(host="127.0.0.1", user="root",
                                 password="Saxena@2004", database="testdb")
    cur = mn.cursor()
    query = '''
    SELECT DISTINCT t1.Train_No, t1.Source_Station_Code, t1.Source_Station_Name, t1.Station_Name, t1.Destination_Station_Code, t1.Destination_Station_Name, t1.Arrival_Time, t1.Departure_Time, t1.Distance
    FROM train_info t1
    JOIN train_info t2 ON t1.Train_No = t2.Train_No
    WHERE t1.Source_Station_Code = %s AND t2.Station_Code = %s
    OR t1.Station_Code = %s AND t2.Destination_Station_Code = %s
    '''
    cur.execute(query, (start, final, start, final))
    result = cur.fetchall()
    cur.close()
    mn.close()
    if len(result) == 0:
        return "No Train Available!"
    else:
        trains = []
        for train in result:
            trains.append({
                "Train Number": train[0],
                "Source Station": train[2],
                "Station": train[3],
                "Destination Station": train[5],
                "Arrival Time": train[6],
                "Departure Time": train[7],
                "Distance": train[8]
            })
        return trains

# def CheckFare(start, final):
#     mn = mysql.connector.connect(host="127.0.0.1", user="root",
#                                  password="Saxena@2004", database="testdb")
#     cur = mn.cursor()

#     # Execute the SQL query to get the distance and fare information along with station names
#     cur.execute(
#         '''
#         SELECT DISTINCT t1.Train_No, t1.Source_Station_Code, t1.Source_Station_Name, t1.Station_Name, t1.Destination_Station_Code, t1.Destination_Station_Name, t1.Arrival_Time, t1.Departure_Time, t1.Distance
#         FROM train_info t1
#         JOIN train_info t2 ON t1.Train_No = t2.Train_No
#         WHERE t1.Source_Station_Code = %s AND t2.Station_Code = %s
#         OR t1.Station_Code = %s AND t2.Destination_Station_Code = %s
#         ''', (start, final, start, final))
#     result_fare = cur.fetchall()
#     cur.close()
#     mn.close()

#     # Prepare fare information
#     fare_info = []
#     if len(result_fare) == 0:
#         return "No Available Train"
    
#     for train in result_fare:
#         distance = train[8]
#         fare = calculate_fare(distance)
#         fare_info.append({
#             "Train Number": train[0],
#             "Source Station": train[2],
#             "Station": train[3],
#             "Destination Station": train[5],
#             "Arrival Time": train[6],
#             "Departure Time": train[7],
#             "Distance": distance,
#             "Fare": fare
#         })
#     return fare_info

def calculate_fare(distance):
    sleeper_fare = int(distance) * sleeper_charge
    third_ac_fare = int(distance) * third_ac_charge
    second_ac_fare = int(distance) * second_ac_charge
    first_ac_fare = int(distance) * first_ac_charge
    return {
        "Sleeper": sleeper_fare,
        "Third AC": third_ac_fare,
        "Second AC": second_ac_fare,
        "First AC": first_ac_fare
    }
    
def ShowBookings(mobile_no):
    mn = mysql.connector.connect(host="127.0.0.1", user="root",
                                 password="Saxena@2004", database="testdb")
    cur = mn.cursor()

    cur.execute('SELECT Train_No, Passenger_Name, Mobile_No, Date_Of_Booking, PNR_No, Class, Date_Of_Travel FROM bookings WHERE Mobile_No="{}"'.format(mobile_no))
    result = cur.fetchall()
    if len(result) == 0:
        return "No Record Found!"
    else:
        bookings = []
        for x in result:
            bookings.append({
                "Train Number": x[0],
                "Passenger Name": x[1],
                "Mobile Number": x[2],
                "Date Of Booking": x[3],
                "PNR Number": x[4],
                "Class": x[5],
                "Date Of Travel": x[6]
            })
        return bookings
def BookTrain(train_no, name, mobile, adhaar, booking_class, travel_date, age):
    mn = mysql.connector.connect(host="127.0.0.1", user="root",
                                 password="Saxena@2004", database="testdb")
    cur = mn.cursor()

    Time_of_Booking = datetime.datetime.now()
    date = Time_of_Booking.date()
    date = date.strftime("%d-%m-%y")

    # Generate a 13-digit PNR number
    pnr_no = str(random.randint(1000000000000, 9999999999999))

    # Check if the PNR number already exists and has less than 6 bookings
    cur.execute("SELECT COUNT(*) FROM bookings WHERE PNR_No = %s", (pnr_no,))
    count = cur.fetchone()[0]

    while count >= 6:
        pnr_no = str(random.randint(1000000000000, 9999999999999))
        cur.execute("SELECT COUNT(*) FROM bookings WHERE PNR_No = %s", (pnr_no,))
        count = cur.fetchone()[0]

    try:
        # Use parameterized query to prevent SQL injection and handle data types
        cur.execute("INSERT INTO bookings (Train_No, Passenger_Name, Mobile_No, Passenger_Adhaar, Date_Of_Booking, PNR_No, Class, Date_Of_Travel, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (train_no, name, mobile, adhaar, date, pnr_no, booking_class, travel_date, age))
        mn.commit()
        return pnr_no  # Return the PNR number
    except mysql.connector.Error as err:
        return f"Error in Booking: {err}"  # Return error message
    finally:
        cur.close()
        mn.close()
        
def CancelBooking(pnr_no):
    mn = mysql.connector.connect(host="127.0.0.1", user="root",
                                 password="Saxena@2004", database="testdb")
    cur = mn.cursor()

    # Check if the booking exists
    cur.execute("SELECT * FROM bookings WHERE PNR_No='{}'".format(pnr_no))
    result = cur.fetchall()
    
    if len(result) == 0:
        return "No Booking Found!"
    
    # If booking exists, delete it
    cur.execute("DELETE FROM bookings WHERE PNR_No='{}'".format(pnr_no))
    mn.commit()
    cur.close()
    mn.close()
    
    return "Booking cancelled successfully!"

