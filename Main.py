from imports import *
from config import *


def main():
    firebaseConfig = firebaseConfig1
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()
    if 'login_details' not in st.session_state:
        st.session_state['login_details'] = {
            'username': None,
            'password': None,
            'role': None,
            'logged_in':False
        }
    if not st.session_state.login_details["logged_in"]:
        is_logged_in,username,role=Login.login(auth, db, storage)
        if is_logged_in:
            st.session_state.login_details["logged_in"]=is_logged_in
            st.session_state.login_details["username"]=username
            st.session_state.login_details["role"]=role.lower()
    if st.session_state.login_details["logged_in"]:
        if st.session_state.login_details["role"]=='student':
            Student_Dashboard.student_dashboard(st.session_state.login_details["username"], st.session_state.login_details["role"], db, storage, auth)
        if st.session_state.login_details["role"]=='teacher':
            Teacher_Dashboard.teacher_dashboard(st.session_state.login_details["username"], st.session_state.login_details["role"], db, storage, auth)

if __name__=="__main__":
    main()