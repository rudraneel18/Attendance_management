from imports import *
import time
import pyrebase
import datetime
firebaseConfig = {
    'apiKey': "AIzaSyAtueZZOhrfS233pBFLYtqy1THVaiO0LGA",
    'authDomain': "attendance-management-672ad.firebaseapp.com",
    'databaseURL': "https://attendance-management-672ad-default-rtdb.firebaseio.com",
    'projectId': "attendance-management-672ad",
    'storageBucket': "attendance-management-672ad.appspot.com",
    'messagingSenderId': "970772118148",
    'appId': "1:970772118148:web:28701f51441c515b3be0d1",
    'measurementId': "G-4KCLJF1N65"
}
# Firebase Authentication


def login():
    '''return true or false'''
    side = st.sidebar
    stat = False
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()
    with side:
        login_expander = st.expander("Login")

        with login_expander:
            login_heading = login_expander.markdown(
                "Please enter your credentials to log in.")
            username = login_expander.text_input("Username", key='username')
            password = login_expander.text_input(
                "Password", type='password', key='password')
            role = login_expander.selectbox(
                "Select your role", ["Student", "Teacher", "Admin"])

            submit_button = login_expander.button("Submit")
            spinner = st.spinner("Authenticating...")

            if submit_button:
                with spinner:
                    # user_data = ref.child(role.lower()).get()
                    # if username in user_data and user_data[username]["password"] == password:
                    if role == "Student" and username == "s1" and password == "s1":
                        '''add something'''
                        login_expander.success("Logged in successfully!")

                    else:
                        not_registered = login_expander.error(
                            "Invalid credentials.")
                        time.sleep(3)
                        not_registered.empty()

            markdown = login_expander.markdown(
                """
                <style>
                body {
                    background-color: #f5f5f5;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
        lmarkdown = st.info("If you are a new user, please register / SignUp")
        signup_expander = st.expander("Register/Signup")

        with signup_expander:
            signup_role = signup_expander.selectbox(
                "Select your role", ["Student", "Teacher", "Admin"], key='signup_role')
            if signup_role == "Student":
                # returns true if no error
                stat = student_signup(auth, db, storage)
                if stat:
                    signup_expander.empty()
            elif signup_role == "Teacher":
                stat = teacher_signup(auth, db, storage)
            elif signup_role == "Admin":
                stat = True  # admin_signup()
        return stat, username, role


data = {
    "students": {},
    "teachers": {},
    "admin": {}
}


def student_signup(auth, db, storage):
    enrollment_id = st.text_input("Enrollment ID")
    name = st.text_input("Name")
    age = st.number_input("Age", value=0)
    course = st.text_input("Course")
    stream = st.text_input("Stream")
    registration_id = st.text_input("Registration ID")
    #subjects = st.text_input("Subjects (comma separated)").split(",")
    section = st.selectbox(
        'section', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    phone = st.text_input("Phone Number")
    whatsapp = st.text_input("WhatsApp Number")
    start_year = st.number_input("Start Year", value=2015, min_value=2015)
    end_year = st.number_input("End Year", value=2015, min_value=2015)
    email = st.text_input("Email")
    college_mail = st.text_input("College Email")
    gender = st.selectbox('Sex', ['Male', 'Female', 'Others'])
    date_of_birth = st.date_input("Date of Birth", datetime.date(2001, 11, 18))
    adhar_number = st.number_input("Adhar Number", value=0)
    #passport_number = st.text_input("GPS Location")
    password = st.text_input("Password", type="password")
    submit_button = st.button("Submit", key='student_submit_button')
    if submit_button:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user = auth.sign_in_with_email_and_password(email, password)
            db.child('student').child(str(enrollment_id)).child("name").set(name)
            db.child('student').child(str(enrollment_id)).child("age").set(age)
            db.child('student').child(str(enrollment_id)).child("course").set(course)
            db.child('student').child(str(enrollment_id)).child("stream").set(stream)
            db.child('student').child(str(enrollment_id)).child("enrollment_id").set(enrollment_id)
            db.child('student').child(str(enrollment_id)).child("registration_id").set(registration_id)
            db.child('student').child(str(enrollment_id)).child("section").set(section)
            db.child('student').child(str(enrollment_id)).child("phone").set(phone)
            db.child('student').child(str(enrollment_id)).child("whatsapp").set(whatsapp)
            db.child('student').child(str(enrollment_id)).child("start_year").set(start_year)
            db.child('student').child(str(enrollment_id)).child("end_year").set(end_year)
            db.child('student').child(str(enrollment_id)).child("email").set(email)
            db.child('student').child(str(enrollment_id)).child("college_mail").set(college_mail)
            db.child('student').child(str(enrollment_id)).child("gender").set(gender)
            db.child('student').child(str(enrollment_id)).child("date_of_birth").set(date_of_birth)
            db.child('student').child(str(enrollment_id)).child("adhar_number").set(adhar_number)
            db.child('student').child(str(enrollment_id)).child("password").set(password)
            storage.child(f'{enrollment_id}/records/record.csv').put('record.csv')
            # db.child(user['student']).child(str(enrollment_id)).child("passport_number").set()
            # "subjects": subjects,
        except Exception as e:
            st.error(e)
            return False

        st.success("Student account created!")
        st.info(data)
        celebrate = st.balloons()
        time.sleep(3)
        celebrate.empty()
        return True


def teacher_signup(auth, db, storage):
    teacher_id = st.text_input("Teacher ID")
    name = st.text_input("Name")
    age = st.number_input("Age", value=0)
    date_of_birth = st.date_input("Date of Birth", datetime.date(2001, 11, 18))
    phone = st.text_input("Phone Number")
    whatsapp = st.text_input("WhatsApp Number")
    email = st.text_input("College mail id")
    password = st.text_input("Password", type="password")
    gender = st.selectbox('Sex', ['Male', 'Female', 'Others'])
    course = st.selectbox(label="Course", options=[
                          "B.Tech", "B.B.A", "B.C.A", "M.Tech", "MBA", "MCA"])
    stream = st.multiselect(label="Stream/Department", options=[
        "CSE", "CSBS", "AIML", "IOT", "ECE", "IT"])
    data = {}
    for k, dept in enumerate(stream):
        year = st.multiselect(
            'Year',
            ['1st', '2nd', '3rd', '4th'])

        for j, y in enumerate(year):
            section = st.multiselect(
                f'Sections you are assigned for {y} year',
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
            secsub = {}
            for i, val in enumerate(section):
                secsub[dept][y][val] = st.multiselect(f'Subjects that you teach in section {val}',
                                                      ['English', 'Maths', 'Chemistry', 'Physics', 'Computer Organisation and Architecture', 'Data Structure and Algorithms', 'Design and Analysis of Algorithms', 'Operating Systems', 'Compiler Design', 'Computer Network'])
            yeardata[y] = secsub
        data[dept] = yeardata
    '''
    dept{
        year{
            section{
                subjects
            }
        }
    }
    '''
    teacher_submit_button = st.button("Submit", key='teacher_submit_button')
    if teacher_submit_button:
        user = auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)
        db.child('teacher').child(str(teacher_id)).child("name").set(name)
        db.child('teacher').child(str(teacher_id)).child("age").set(age)
        db.child('teacher').child(str(teacher_id)).child(
            "date_of_birth").set(date_of_birth)
        db.child('teacher').child(str(teacher_id)).child("phone").set(phone)
        db.child('teacher').child(str(teacher_id)).child(
            "whatsapp").set(whatsapp)
        db.child('teacher').child(str(teacher_id)).child("email").set(email)
        db.child('teacher').child(str(teacher_id)).child(
            "password").set(password)
        db.child('teacher').child(str(teacher_id)).child("gender").set(gender)
        db.child('teacher').child(str(teacher_id)).child("course").set(course)
        for dept, yeardata in data.items():
            for y, sec in yeardata.items():
                pass

        db.child('teacher').child(str(teacher_id)).child("age").set(age)

        data["teachers"][teacher_id] = {
            "name": name,
            "age": age,
            "course": course,
            "stream": stream,
            "year": {year:
                     {"section": {section: {
                         "subjects": subjects
                     }
                     }
                     }
                     },
            "phone": phone,
            "whatsapp": whatsapp,
            "email": email,
            "password": password,
        }
        st.success("Teacher account created!")
        st.info(data)
        celebrate = st.balloons()
        time.sleep(3)
        celebrate.empty()
