import streamlit as st
from Core import User_info
import os

def main():
    st.title("Login and Signup Page")

    menu = ["User Login", "User Signup", "Admin Login", "Admin Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "User Login":
        st.subheader("User Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if User_info.login(username, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.write("You are now logged in.")
                os.system('streamlit run train.py')
            else:
                st.error("Invalid username or password.")

    elif choice == "User Signup":
        st.subheader("User Signup")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Signup"):
            if User_info.signup(new_username, new_password):
                st.success("Signup successful! You can now log in.")
            else:
                st.error("Signup failed. Username may already exist.")

    elif choice == "Admin Login":
        st.subheader("Admin Login Section")
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type='password')
        security_code = st.text_input("Security Code", type='password')

        if st.button("Admin Login"):
            if User_info.admin_login(admin_username, admin_password, security_code):
                st.session_state.admin_logged_in = True
                st.success("Admin login successful!")
                st.write("You are now logged in as admin.")
                os.system('streamlit run admin.py')
            else:
                st.error("Invalid admin credentials or security code.")

    elif choice == "Admin Signup":
        st.subheader("Admin Signup")
        new_admin_username = st.text_input("New Admin Username")
        new_admin_password = st.text_input("New Admin Password", type='password')
        new_security_code = st.text_input("New Security Code", type='password')

        if st.button("Admin Signup"):
            if User_info.admin_signup(new_admin_username, new_admin_password, new_security_code):
                st.success("Admin signup successful! You can now log in.")
            else:
                st.error("Admin signup failed. An admin already exists or username may already exist.")

if __name__ == '__main__':
    main()