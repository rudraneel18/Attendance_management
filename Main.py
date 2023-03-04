from imports import *



def main():
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
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'username' not in st.session_state:
        st.session_state['username']=None
    if 'role' not in st.session_state:
        st.session_state['role']=None
    if not st.session_state.logged_in:
        login_status,username,role=Login.login(auth, db, storage)
        if login_status:
            st.session_state.logged_in=login_status
            st.session_state['username']=username
            st.session_state['role']=role.lower()
    if st.session_state.logged_in:
        Student_Dashboard.student_dashboard(st.session_state['username'], st.session_state['role'], db, storage, auth)
main()