import streamlit as st
from Core import User_info
import pandas as pd

def main():
    st.title("Admin Page")

    admin_options = ["View Users", "Add User", "Edit User", "Delete User", "Manage Trains", "View All Bookings", "Generate Report", "Admin Dashboard", "Security Management", "Database Management"]
    admin_action = st.selectbox("Admin Actions", admin_options)

    if admin_action == "View Users":
        users = User_info.view_users()
        users_df = pd.DataFrame(users, columns=["ID", "Username", "Password"])
        st.write(users_df)

    elif admin_action == "Add User":
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')
        if st.button("Add User"):
            if User_info.add_user(new_username, new_password):
                st.success("User added successfully!")
            else:
                st.error("Failed to add user.")

    elif admin_action == "Edit User":
        user_id = st.number_input("User ID", min_value=1)
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')
        if st.button("Edit User"):
            if User_info.edit_user(user_id, new_username, new_password):
                st.success("User edited successfully!")
            else:
                st.error("Failed to edit user.")

    elif admin_action == "Delete User":
        user_id = st.number_input("User ID", min_value=1)
        if st.button("Delete User"):
            if User_info.delete_user(user_id):
                st.success("User deleted successfully!")
            else:
                st.error("Failed to delete user.")

    elif admin_action == "Manage Trains":
        train_options = ["View Trains", "Add Train", "Edit Train", "Delete Train"]
        train_action = st.selectbox("Train Actions", train_options)

        if train_action == "View Trains":
            trains = User_info.view_trains()
            trains_df = pd.DataFrame(trains, columns=["Train No", "Station Code", "Station Name", "Arrival Time", "Departure Time", "Distance", "Source Station Code", "Source Station Name", "Destination Station Code", "Destination Station Name"])
            st.write(trains_df)

        elif train_action == "Add Train":
            train_no = st.text_input("Train Number")
            station_code = st.text_input("Station Code")
            station_name = st.text_input("Station Name")
            arrival_time = st.text_input("Arrival Time")
            departure_time = st.text_input("Departure Time")
            distance = st.text_input("Distance")
            source_station_code = st.text_input("Source Station Code")
            source_station_name = st.text_input("Source Station Name")
            destination_station_code = st.text_input("Destination Station Code")
            destination_station_name = st.text_input("Destination Station Name")
            if st.button("Add Train"):
                if User_info.add_train(train_no, station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name):
                    st.success("Train added successfully!")
                else:
                    st.error("Failed to add train.")

        elif train_action == "Edit Train":
            train_no = st.text_input("Train Number")
            station_code = st.text_input("Station Code")
            station_name = st.text_input("Station Name")
            arrival_time = st.text_input("Arrival Time")
            departure_time = st.text_input("Departure Time")
            distance = st.text_input("Distance")
            source_station_code = st.text_input("Source Station Code")
            source_station_name = st.text_input("Source Station Name")
            destination_station_code = st.text_input("Destination Station Code")
            destination_station_name = st.text_input("Destination Station Name")
            if st.button("Edit Train"):
                if User_info.edit_train(train_no, station_code, station_name, arrival_time, departure_time, distance, source_station_code, source_station_name, destination_station_code, destination_station_name):
                    st.success("Train edited successfully!")
                else:
                    st.error("Failed to edit train.")

        elif train_action == "Delete Train":
            train_no = st.text_input("Train Number")
            if st.button("Delete Train"):
                if User_info.delete_train(train_no):
                    st.success("Train deleted successfully!")
                else:
                    st.error("Failed to delete train.")

    elif admin_action == "View All Bookings":
        bookings = User_info.view_bookings()
        bookings_df = pd.DataFrame(bookings, columns=["Train No", "Passenger Name", "Mobile No", "Passenger Adhaar", "Date Of Booking", "PNR No", "Class", "Date Of Travel", "Age"])
        st.write(bookings_df)

    elif admin_action == "Generate Report":
        st.subheader("Generate Report")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        if st.button("Generate Report"):
            report = User_info.generate_report(start_date, end_date)
            report_df = pd.DataFrame(report, columns=["Train No", "Passenger Name", "Mobile No", "Passenger Adhaar", "Date Of Booking", "PNR No", "Class", "Date Of Travel", "Age"])
            st.write(report_df)
            csv = report_df.to_csv(index=False)
            st.download_button(label="Download Report as CSV", data=csv, file_name='report.csv', mime='text/csv')

    elif admin_action == "Admin Dashboard":
        st.write("Admin dashboard with statistics and analytics.")

    elif admin_action == "Security Management":
        security_options = ["Change Admin Password", "Change Admin Security Code"]
        security_action = st.selectbox("Security Actions", security_options)

        if security_action == "Change Admin Password":
            username = st.text_input("Admin Username")
            new_password = st.text_input("New Password", type='password')
            if st.button("Change Password"):
                if User_info.change_admin_password(username, new_password):
                    st.success("Password changed successfully!")
                else:
                    st.error("Failed to change password.")

        elif security_action == "Change Admin Security Code":
            username = st.text_input("Admin Username")
            new_security_code = st.text_input("New Security Code", type='password')
            if st.button("Change Security Code"):
                if User_info.change_admin_security_code(username, new_security_code):
                    st.success("Security code changed successfully!")
                else:
                    st.error("Failed to change security code.")

    elif admin_action == "Database Management":
        db_options = ["Backup Database", "Restore Database"]
        db_action = st.selectbox("Database Actions", db_options)

        if db_action == "Backup Database":
            if st.button("Backup Database"):
                if User_info.backup_database():
                    st.success("Database backup successful!")
                else:
                    st.error("Failed to backup database.")

        elif db_action == "Restore Database":
            backup_file = st.file_uploader("Upload Backup File")
            if st.button("Restore Database") and backup_file is not None:
                if User_info.restore_database(backup_file):
                    st.success("Database restored successfully!")
                else:
                    st.error("Failed to restore database.")

if __name__ == '__main__':
    main()