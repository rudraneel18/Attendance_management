from imports import *
import time
import pyrebase
import datetime

def login(auth, db, storage):
    '''return true or false'''
    side = st.sidebar
    stat = False
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
            #forgot_password = login_expander.button("Forgot Password")
            spinner = st.spinner("Authenticating...")

            if submit_button:
                with spinner:
                    # user_data = ref.child(role.lower()).get()
                    # if username in user_data and user_data[username]["password"] == password:
                    if role == "Student":
                        '''add something'''
                        try:
                            user=auth.sign_in_with_email_and_password(username+"@student.com",password)
                            login_expander.success("Logged in successfully!")
                            return True, username, role
                        except:
                            not_registered = login_expander.error(
                                "Invalid credentials.")
                            time.sleep(5)
                            not_registered.empty()
                            return False,"",""
                    elif role == "Teacher":
                        try:
                            user=auth.sign_in_with_email_and_password(username+"@teacher.com",password)
                            login_expander.success("Logged in successfully!")
                            return True, username, role
                        except:
                            not_registered=login_expander.error("Invalid credentials")
                            time.sleep(5)
                            not_registered.empty()
                            return False,"",""
                    elif role == "Admin":
                        try:
                            user=auth.sign_in_with_email_and_password(username+"@admin.com",password)
                            login_expander.success("Logged in successfully as Admin!")
                            return True, username, role
                        except:
                            not_registered=login_expander.error("Invalid credentials")
                            time.sleep(5)
                            not_registered.empty()
                            return False,"",""

            #if forgot_password:
            #    username=st.text_input("Enter your unique ID/ enrollment ID/ Teacher ID")
            #    reset_password = st.button("Reset Password")
            #    if username and reset_password:
            #        college_email=db.child('student').child(username).get('college_mail')
            #        st.info(college_email)
                    #user = auth.send_password_reset_email(college_email)

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
            role = signup_expander.selectbox(
                "Select your role", ["Student", "Teacher", "Admin"], key='signup_role')
            if role == "Student":
                # returns true if no error
                x = student_signup(auth, db, storage,role)
                if x!=None:
                    stat,username=x
                    signup_expander.empty()
            elif role == "Teacher":
                x=teacher_signup(auth, db, storage,role)
                if x!=None:
                    stat,username = x
                    signup_expander.empty()
            elif role == "Admin":
                stat,username = True,"123"  # admin_signup()
        return stat, username, role


data = {
    "students": {},
    "teachers": {},
    "admin": {}
}


def student_signup(auth, db, storage,signup_role):
    enrollment_id = st.text_input("Enrollment ID")
    name = st.text_input("Name")
    age = st.number_input("Age",min_value=18,value=18)
    course = st.selectbox(label="Course", options=[
                          "B.Tech", "B.B.A", "B.C.A", "M.Tech", "MBA", "MCA"])
    stream = st.selectbox(label="Stream/Department", options=[
        "CSE", "CSBS", "AIML", "IOT", "ECE", "IT"])
    registration_id = st.text_input("Registration ID")
    #subjects = st.text_input("Subjects (comma separated)").split(",")
    section = st.selectbox(
        'section', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    phone = st.text_input("Phone Number")
    whatsapp = st.text_input("WhatsApp Number")
    start_year = st.number_input("Start Year", value=2015, min_value=2015,max_value=datetime.datetime.now().year)
    end_year = st.number_input("End Year", value=2015, min_value=2015)
    email = st.text_input("Email")
    college_mail = st.text_input("College Email")
    # if not college_mail.endswith("@iem.edu.in"):
    #     st.error("enter the correct college email")
    gender = st.selectbox('Sex', ['Male', 'Female', 'Others'])
    date_of_birth = st.date_input("Date of Birth", datetime.date(2001, 11, 18))
    adhar_number = st.number_input("Adhar Number",value=100000000000, min_value=100000000000,max_value=999999999999)
    #passport_number = st.text_input("GPS Location")
    password = st.text_input("Password", type="password")
    submit_button = st.button("Submit", key='student_submit_button')
    if submit_button:
        try:
            uid = str(enrollment_id)+f"@{signup_role.lower()}.com"
            user = auth.create_user_with_email_and_password(uid, password)
            user = auth.sign_in_with_email_and_password(uid, password)

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
            db.child('student').child(str(enrollment_id)).child("current_year").set(datetime.datetime.now().year - start_year)
            db.child('student').child(str(enrollment_id)).child("email").set(email)
            db.child('student').child(str(enrollment_id)).child("college_mail").set(college_mail)
            db.child('student').child(str(enrollment_id)).child("gender").set(gender)
            db.child('student').child(str(enrollment_id)).child(
                "date_of_birth").set(date_of_birth.strftime('%Y-%m-%d'))
            db.child('student').child(str(enrollment_id)).child("adhar_number").set(adhar_number)
            db.child('student').child(str(enrollment_id)).child("password").set(password)
            storage.child(f'{signup_role.lower()}/{str(enrollment_id)}/records/record.csv').put('record.csv')
            #storage.child(f'{signup_role.lower()}/{str(enrollment_id)}/pictures')
            # db.child(user['student']).child(str(enrollment_id)).child("passport_number").set()
            # "subjects": subjects,
        except Exception as e:
            st.error(e)
            print(f"Error log \n {'-'*20}\n",e)
            return False,"0"

        st.success("Student account created!")
        st.info(data)
        celebrate = st.balloons()
        time.sleep(3)
        celebrate.empty()
        return True,str(enrollment_id)
    


def teacher_signup(auth, db, storage,signup_role):
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
    depts = st.multiselect(label="Stream/Department", options=[
        "CSE", "CSBS", "AIML", "IOT", "ECE", "IT"])
    data = {}
    for ind1, dept in enumerate(depts):
        years = st.multiselect(f'{dept} department years', [
            '1st', '2nd', '3rd', '4th'], key=str(ind1))
        y = {}
        for ind2, year in enumerate(years):
            sections = st.multiselect(f'Sections you are assigned for {year} year', [
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], key=str(ind1) + str(ind2))
            s = {}
            for ind3, section in enumerate(sections):
                subjects = st.multiselect(f'Subjects that you teach in {year} year section {section}', ['English', 'Maths', 'Chemistry', 'Physics', 'Computer Organisation and Architecture',
                                                                                                        'Data Structure and Algorithms', 'Design and Analysis of Algorithms', 'Operating Systems', 'Compiler Design', 'Computer Network'], key=str(ind1) + str(ind2) + str(ind3))
                s[section] = subjects
            y[year] = s
        data[dept] = y
    teacher_submit_button = st.button("Submit", key='teacher_submit_button')
    if teacher_submit_button:
        try:
            uid = str(teacher_id)+f"@{signup_role.lower()}.com"
            user = auth.create_user_with_email_and_password(uid, password)
            user = auth.sign_in_with_email_and_password(uid, password)
            db.child('teacher').child(str(teacher_id)).child("name").set(name)
            db.child('teacher').child(str(teacher_id)).child("age").set(age)
            db.child('teacher').child(str(teacher_id)).child(
                "date_of_birth").set(date_of_birth.strftime('%Y-%m-%d'))
            db.child('teacher').child(str(teacher_id)).child("phone").set(phone)
            db.child('teacher').child(str(teacher_id)).child(
                "whatsapp").set(whatsapp)
            db.child('teacher').child(str(teacher_id)).child("email").set(email)
            db.child('teacher').child(str(teacher_id)).child(
                "password").set(password)
            db.child('teacher').child(str(teacher_id)).child("gender").set(gender)
            db.child('teacher').child(str(teacher_id)).child("course").set(course)
            db.child('teacher').child(str(teacher_id)
                                    ).child("departments").set(data)
            db.child('teacher').child(str(teacher_id)).child("age").set(age)
            storage.child(f'{signup_role.lower()}/{str(teacher_id)}/records/record.csv').put('record.csv')
        # storage.child(f'{signup_role.lower()}/{str(teacher_id)}/pictures')
        except Exception as e:
            st.error(e)
            print(f"Error log \n {'-'*20}\n",e)
            return False,"0"
        st.success("Teacher account created!")
        st.info(data)
        celebrate = st.balloons()
        time.sleep(3)
        celebrate.empty()
        return True,str(teacher_id)