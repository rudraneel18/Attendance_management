from imports import *
import streamlit as st 
import hydralit as hy
from streamlit_option_menu import option_menu
import pandas

def student_dashboard(username, role, db, storage, auth):
    
    #################################session_states############################
    if 'picture_clicked' not in st.session_state:
        st.session_state.picture_clicked = False
    if 'matched' not in st.session_state:
        st.session_state.matched = False
    if 'attendance' not in st.session_state:
        st.session_state.attendance = False
    if 'usersname' not in st.session_state:
        st.session_state.usersname = db.child("student").child(username).child("name").get().val()
    if 'registration_id' not in st.session_state:
        st.session_state.registration_id = db.child("student").child(username).child("registration_id").get().val()
    if 'enrollment_id' not in st.session_state:
        st.session_state.enrollment_id = db.child("student").child(username).child("enrollment_id").get().val()
    if 'adhar_number' not in st.session_state:
        st.session_state.adhar_number = db.child("student").child(username).child("adhar_number").get().val()
    if 'email' not in st.session_state:
        st.session_state.email = db.child("student").child(username).child("email").get().val()
    if 'college_mail' not in st.session_state:
        st.session_state.college_mail = db.child("student").child(username).child("college_mail").get().val()
    if 'age' not in st.session_state:
        st.session_state.age = db.child("student").child(username).child("age").get().val()
    if 'gender' not in st.session_state:
        st.session_state.gender = db.child("student").child(username).child("gender").get().val()
    if 'date_of_birth' not in st.session_state:
        st.session_state.date_of_birth = db.child("student").child(username).child("date_of_birth").get().val()
    if 'start_year' not in st.session_state:
        st.session_state.start_year = db.child("student").child(username).child("start_year").get().val()
    if 'end_year' not in st.session_state:
        st.session_state.end_year = db.child("student").child(username).child("end_year").get().val()
    if 'phone' not in st.session_state:
        st.session_state.phone = db.child("student").child(username).child("phone").get().val()
    if 'whatsapp' not in st.session_state:
        st.session_state.whatsapp = db.child("student").child(username).child("whatsapp").get().val()
    if 'course' not in st.session_state:
        st.session_state.course = db.child("student").child(username).child("course").get().val()
    if 'stream' not in st.session_state:
        st.session_state.stream = db.child("student").child(username).child("stream").get().val()
    if 'current_year' not in st.session_state:
        st.session_state.current_year = db.child("student").child(username).child("current_year").get().val()
    if 'section' not in st.session_state:
        st.session_state.section = db.child("student").child(username).child("section").get().val()
    #################################session_states_ends############################
    def Home_page(username, role, db, storage):
        title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Student Dashboard</h1>", unsafe_allow_html=True)
        st.warning("If you have not registered your images, please go to Details tab")
        cam=st.camera_input("Click your picture")
        if cam is not None:
            st.session_state.picture_clicked = True
            '''attendance neva hobe'''

    def Details_page(username, role, db, storage):
        st.subheader("Student Details")
        name = db.child("student").child(username).child("name").get().val()
        st.write(f"Welcome {name}! You are logged in as a {role}.")
        col1, col2,col3,col4= st.columns([1, 1,1,1])
        with col1:
            st.write("Name:")
            st.write("Enrollment No.:")
            st.write("Registration No.:")
            st.write("Adhar No.:")
            st.write("Email ID:")
            st.write("College Email ID:")
            st.write("Age:")
            st.write("Gender:")
            #st.write("Subjects:")
        with col2:
            st.write(st.session_state.usersname)
            st.write(st.session_state.enrollment_id)
            st.write(st.session_state.registration_id)
            st.write(st.session_state.adhar_number)
            st.write(st.session_state.email)
            st.write(st.session_state.college_mail)
            st.write(st.session_state.age)
            st.write(st.session_state.gender)  
        with col3:
            st.write("DOB:")
            st.write("Start Year:")
            st.write("End Year:")
            st.write("Phone No.:")
            st.write("WhatsApp No.:")
            st.write("Course:")
            st.write("Stream:")
            st.write("Current Year:")
            st.write("Section:")
        with col4:
            st.write(st.session_state.date_of_birth)
            st.write(st.session_state.start_year)
            st.write(st.session_state.end_year)
            st.write(st.session_state.phone)
            st.write(st.session_state.whatsapp)
            st.write(st.session_state.course)
            st.write(st.session_state.stream)
            st.write(st.session_state.current_year)
            st.write(st.session_state.section)

        x = st.columns([1, 1, 1])
        cam_inp = x[1].camera_input("Register your images here")
        camcol1, camcol2, camcol3 = st.columns([1,1,1.5])
        if cam_inp:
            with camcol1:
                st.image(cam_inp)
            with camcol2 :
                st.image(cam_inp)
            with camcol3 and cam_inp:
                st.image(cam_inp)   
            
    def Records_page(username, role, db, storage):
        st.write(pd.read_csv('record.csv', index_col=False))
        source_firebase=fr"/student/{username}/record.csv"
        dest_local = fr"D:\Desktop\att\Attendance_management\user_temp"
        storage.child(
            f"student/{username}/records/record.csv").download(path=source_firebase,filename=fr"user_temp/record.csv")
        #st.write(storage.download(path='gs://attendance-management-672ad.appspot.com/student/111111/records',))
        df=pd.read_csv(fr"D:\Desktop\att\Attendance_management\user_temp\record.csv")
        if st.session_state.picture_clicked and st.session_state.matched:
            pass
    navbar=option_menu(menu_title="Navbar",options=['Home','Details','Records'],
                    menu_icon='cast',icons=['house','book','envelope'],default_index=0,orientation='horizontal')
    if navbar=='Home':
        Home_page(username, role, db, storage)
    if navbar=='Details':
        Details_page(username, role, db, storage)
    if navbar=='Records':
        Records_page(username, role, db, storage)
        
        st.success('Attendance Records')
        
