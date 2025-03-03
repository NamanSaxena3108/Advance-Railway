import mysql.connector as con
from mysql.connector import Error
import os

def create_user_database():
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS user_info;")
            cursor.execute("USE user_info;")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    security_code VARCHAR(255) NOT NULL
                );
            """)
            connection.commit()
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Error: {e}")

def signup(username, password):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def login(username, password):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return True
        else:
            return False
    except Error as e:
        print(f"Error: {e}")
        return False

def admin_signup(username, password, security_code):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM admin")
        admin_count = cursor.fetchone()[0]
        if admin_count > 0:
            return False  # Admin already exists
        cursor.execute("INSERT INTO admin (username, password, security_code) VALUES (%s, %s, %s)", (username, password, security_code))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def admin_login(username, password, security_code):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s AND security_code = %s", (username, password, security_code))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return True
        else:
            return False
    except Error as e:
        print(f"Error: {e}")
        return False

# Admin functionalities
def view_users():
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"Error: {e}")
        return []

def add_user(username, password):
    return signup(username, password)

def edit_user(user_id, username, password):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET username = %s, password = %s WHERE id = %s", (username, password, user_id))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def delete_user(user_id):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def view_trains():
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM train_info")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"Error: {e}")
        return []

def add_train(train_no, station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO train_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (train_no, station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def edit_train(train_no, station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE train_info SET station_code = %s, station_name = %s, arrival_time = %s, departure_time = %s, distance = %s, source_station_code = %s, source_station_name = %s, destination_station_code = %s, destination_station_name = %s WHERE train_no = %s", 
                       (station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name, train_no))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def delete_train(train_no):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM train_info WHERE train_no = %s", (train_no,))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def view_bookings():
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT Train_No, Passenger_Name, Mobile_No, Passenger_Adhaar, Date_Of_Booking, PNR_No, Class, Date_Of_Travel, Age FROM bookings")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"Error: {e}")
        return []
    
def generate_report(start_date, end_date):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="testdb"
        )
        cursor = connection.cursor()
        query = """
        SELECT Train_No, Passenger_Name, Mobile_No, Passenger_Adhaar, Date_Of_Booking, PNR_No, Class, Date_Of_Travel, Age
        FROM bookings
        WHERE STR_TO_DATE(Date_Of_Booking, '%d-%m-%y') BETWEEN STR_TO_DATE(%s, '%Y-%m-%d') AND STR_TO_DATE(%s, '%Y-%m-%d')
        """
        cursor.execute(query, (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"Error: {e}")
        return []

def change_admin_password(username, new_password):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE admin SET password = %s WHERE username = %s", (new_password, username))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def change_admin_security_code(username, new_security_code):
    try:
        connection = con.connect(
            host="127.0.0.1",
            user="root",
            password="Saxena@2004",
            database="user_info"
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE admin SET security_code = %s WHERE username = %s", (new_security_code, username))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def backup_database():
    try:
        os.system("mysqldump -u root -pSaxena@2004 testdb > backup.sql")
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def restore_database():
    try:
        os.system("mysql -u root -pSaxena@2004 testdb < backup.sql")
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

# Ensure the database and table are created when the module is imported
create_user_database()