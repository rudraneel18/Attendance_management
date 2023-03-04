from imports import *
import streamlit as st 
import hydralit as hy
from streamlit_option_menu import option_menu


def student_dashboard(username, role, db, storage, auth):

    def Home_page():
        title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Student Dashboard</h1>", unsafe_allow_html=True)
        cam=st.camera_input("Click your picture")


    def Edit_Details_page(username, role, db, storage):
        st.subheader("Student Details")
        name = db.child("student").child(username).child("name").get().val()
        st.write(f"Welcome {name}! You are logged in as a {role}.")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("Name:")
            st.write("Enrollment No.:")
            st.write("Registration No.:")
            st.write("Adhar No.:")
            st.write("Email ID:")
            st.write("College Email ID:")
            st.write("Age:")
            st.write("Gender:")
            st.write("DOB:")
            st.write("Start Year:")
            st.write("End Year:")
            st.write("Phone No.:")
            st.write("WhatsApp No.:")
            st.write("Course:")
            st.write("Stream:")
            st.write("Current Year:")
            st.write("Section:")
            #st.write("Subjects:")
        with col2:
            st.write(db.child("student").child(username).child("name").get().val())
            st.write(db.child("student").child(username).child("enrollment_id").get().val())
            st.write(db.child("student").child(username).child("registration_id").get().val())
            st.write(db.child("student").child(username).child("adhar_number").get().val())
            st.write(db.child("student").child(username).child("email").get().val())
            st.write(db.child("student").child(username).child("college_mail").get().val())
            st.write(db.child("student").child(username).child("age").get().val())
            st.write(db.child("student").child(username).child("gender").get().val())
            st.write(db.child("student").child(username).child("date_of_birth").get().val())
            st.write(db.child("student").child(username).child("start_year").get().val())
            st.write(db.child("student").child(username).child("end_year").get().val())
            st.write(db.child("student").child(username).child("phone").get().val())
            st.write(db.child("student").child(username).child("whatsapp").get().val())
            st.write(db.child("student").child(username).child("course").get().val())
            st.write(db.child("student").child(username).child("stream").get().val())
            st.write(db.child("student").child(username).child("current_year").get().val())
            st.write(db.child("student").child(username).child("section").get().val())


    def Records_page():
        pass
    navbar=option_menu(menu_title="Navbar",options=['Home','Details','Records'],
                    menu_icon='cast',icons=['house','book','envelope'],default_index=0,orientation='horizontal')
    if navbar=='Home':
        Home_page()
    if navbar=='Details':
        Edit_Details_page(username, role, db, storage)
    if navbar=='Records':
        st.success('Attendance Records')
