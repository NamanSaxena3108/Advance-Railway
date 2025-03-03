import streamlit as st
import Core.Checks as Check
import Core.User_function as User
import pandas as pd
import os

# Check connection and database
connection_status = Check.CheckConnection()
if not connection_status:
    st.error("Connection failed!")
    st.stop()
else:
    Check.CheckDatabase()

# Streamlit App Title
st.title("Train Booking System")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu_options = ["Available Trains", "Book Train", "Show Bookings", "Cancel Booking", "About", "Exit"]
choice = st.sidebar.selectbox("Select an option", menu_options)

#show available trains
if choice == "Available Trains":
    st.subheader("Available Trains")
    start_station = st.text_input("From (Station Code)")
    end_station = st.text_input("To (Station Code)")
    travel_date = st.date_input("Date of Travel")

    if st.button("Show Available Trains"):
        if start_station and end_station and travel_date:
            date_user = travel_date.strftime("%Y-%m-%d")
            trains = User.AvailableTrains(start_station, end_station, date_user)

            if isinstance(trains, str):
                st.error(trains)  # Handle no trains available
            else:
                st.write("Available Trains:")
                for train in trains:
                    with st.expander(f"Train Number: {train['Train Number']}"):
                        st.write(f"**Source Station:** {train['Source Station']}")
                        st.write(f"**Station:** {train['Station']}")
                        st.write(f"**Destination Station:** {train['Destination Station']}")
                        st.write(f"**Arrival Time:** {train['Arrival Time']}")
                        st.write(f"**Departure Time:** {train['Departure Time']}")
                        st.write(f"**Distance:** {train['Distance']} km")
                        
                        fare = User.calculate_fare(train['Distance'])
                        st.write("### Fare Details")
                        st.write(f"**Sleeper Fare:** {fare['Sleeper']} INR")
                        st.write(f"**Third AC Fare:** {fare['Third AC']} INR")
                        st.write(f"**Second AC Fare:** {fare['Second AC']} INR")
                        st.write(f"**First AC Fare:** {fare['First AC']} INR")
        else:
            st.error("Please fill in all fields.")
            
# Functionality to check fare
# elif choice == "Check Fare":
#     st.subheader("Check Fare")
#     start_station_code = st.text_input("From (Station Code)")
#     end_station_code = st.text_input("To (Station Code)")

#     if st.button("Check Fare"):
#         if start_station_code and end_station_code:
#             fare_info = User.CheckFare(start_station_code, end_station_code)

#             if isinstance(fare_info, str):
#                 st.error(fare_info)  # Handle no trains available
#             else:
#                 st.write("Fare Information:")
#                 # Convert fare_info to a DataFrame for better presentation
#                 fare_df = pd.DataFrame(fare_info)
#                 st.table(fare_df)  # Display fare information as a table
#         else:
#             st.error("Please fill in all fields.")
            
elif choice == "Book Train":
    st.subheader("Book a Train")
    train_number = st.text_input("Train Number")
    passenger_name = st.text_input("Passenger Name")
    mobile_number = st.text_input("Mobile Number", max_chars=10)
    adhaar_number = st.text_input("Adhaar Number", max_chars=12)
    age = st.number_input("Age", min_value=0, max_value=120)
    booking_class = st.selectbox("Class", ["Sleeper", "AC-1", "AC-2", "AC-3"])
    travel_date = st.date_input("Date of Travel")

    if st.button("Book Train"):
        if train_number and passenger_name and mobile_number and adhaar_number and age:
            pnr_no = User.BookTrain(train_number, passenger_name, mobile_number, adhaar_number, booking_class, travel_date, age)
            if isinstance(pnr_no, str) and len(pnr_no) == 13:  # Check if PNR number is a 13-digit string
                st.success(f"Train booked successfully! Your PNR number is: {pnr_no}")
            else:
                st.error(pnr_no)  # Display error message
        else:
            st.error("Please fill in all fields.")

# Functionality to show bookings
elif choice == "Show Bookings":
    st.subheader("Show Bookings")
    mobile_no = st.text_input("Enter your Mobile Number")
    if st.button("Show My Bookings"):
        if mobile_no:
            bookings = User.ShowBookings(mobile_no)
            if isinstance(bookings, str):
                st.error(bookings)  # Handle no records found
            else:
                st.write("Your Bookings:")
                # Convert bookings to a DataFrame for better presentation
                bookings_df = pd.DataFrame(bookings)
                st.table(bookings_df)  # Display bookings as a table
        else:
            st.error("Please enter your Mobile Number.")

# Functionality to cancel a booking
elif choice == "Cancel Booking":
    st.subheader("Cancel Booking")
    booking_id = st.text_input("PNR Number")
    if st.button("Cancel Booking"):
        if booking_id:
            User.CancelBooking(booking_id)
            st.success("Booking cancelled successfully!")
        else:
            st.error("Please enter a Booking ID.")
         
# Functionality for About
elif choice == "About":
    st.subheader("About This System")
    st.write("""
    The Railway Management System is a comprehensive system designed to manage various aspects of a railway network, including passenger information and station management. 
    The system aims to provide a user-friendly interface for railway staff to efficiently manage the railway network, ensuring smooth and safe operations.

    ### Features
    - **Book a Ticket**: Users can book tickets for their desired journey, specifying the source and destination stations, and the date of travel.
    - **Cancel a Ticket**: Users can cancel their booked tickets if needed.
    - **Check Fares**: Users can check the fare for their specified class by specifying the source and destination stations.
    - **Show Bookings**: Users can view their current bookings.
    - **Available Trains**: Users can see a list of available trains for their journey.
    - **About Section**: Users can access information about the application.
    - **Exit Option**: Users can exit the application gracefully.
             
    ### License
    This project is licensed under the MIT License.      
    """)
    st.write("""### Copyright (c) 2024 Naman Saxena""")

# Initialize a session state variable to track exit button click
if 'exit_clicked' not in st.session_state:
    st.session_state.exit_clicked = False

# Exit option
elif choice == "Exit":
    st.session_state.exit_clicked = True  # Set the exit clicked state to True

# Display exit message if the exit button was clicked
if st.session_state.exit_clicked:
    st.success("You can now close the window. Thank you for using our service! 😊")
    
    os.system("streamlit run app.py")
    
    st.stop()  # Stop the execution of the app

# Handle invalid selections
if choice not in menu_options:
    st.error("Please select a valid option.")