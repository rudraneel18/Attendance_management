from imports import *

if 'logged_in' not in st.session_state:
    st.session_state['logged_in']=False
def main():
    if not st.session_state.logged_in:
        login_status,username,role=Login.login()
        if login_status:
            st.session_state.logged_in=login_status
            if 'username' not in st.session_state:
                st.session_state['username']=username
            if 'role' not in st.session_state:
                st.session_state['role']=role
    if st.session_state.logged_in:
        Student_Dashboard.student_dashboard()
main()