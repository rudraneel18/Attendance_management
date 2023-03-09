from imports import * 
from streamlit_option_menu import option_menu



def teacher_dashboard(username, role, db, storage, auth):
    st.success("You are logged in as a Teacher")
    #################################session_states############################
    data = db.child("teacher").child(username).get().val()    
    if 'picture_clicked' not in st.session_state:
        st.session_state.picture_clicked = False
    if 'matched' not in st.session_state:
        st.session_state.matched = False
    if 'attendance' not in st.session_state:
        st.session_state.attendance = False
    if 'usersname' not in st.session_state:
        st.session_state.usersname = data["name"]
    if 'teacher_id' not in st.session_state:
        st.session_state.teacher_id = username
    if 'age' not in st.session_state:
        st.session_state.age = data["age"]
    if 'date_of_birth' not in st.session_state:
        st.session_state.date_of_birth = data["date_of_birth"]
    if 'phone' not in st.session_state:
        st.session_state.phone = data["phone"]
    if 'whatsapp' not in st.session_state:
        st.session_state.whatsapp = data["whatsapp"]
    if 'email' not in st.session_state:
        st.session_state.email = data["email"]
    if 'gender' not in st.session_state:
        st.session_state.gender=data["gender"]
    if 'course' not in st.session_state:
        st.session_state.course=data["course"]
    if 'departments' not in st.session_state:
        st.session_state.departments=data["departments"]
    #st.write(st.session_state.departments)

    def Home_page(username, role, db, storage):
        title = st.markdown(
            "<h1 style='text-align: center; color: #ffa31a;'>Teacher Dashboard</h1>", unsafe_allow_html=True)
        st.warning(
            "If you have not registered your images, please go to Details tab")
        cam = st.camera_input("Click your picture")
        if cam is not None:
            st.session_state.picture_clicked = True
            '''attendance neva hobe'''

    def Details_page(username, role, db, storage):
        st.subheader("Teacher Details")
        st.write(f"Welcome {st.session_state.usersname}! You are logged in as a {role}.")
        col1, col2= st.columns([1, 1])
        with col1:
            st.write(f"Name:        {st.session_state.usersname}")
            st.write(f"Teacher ID:      {st.session_state.teacher_id}")
            #st.write("Adhar No.:")
            st.write(f"Email ID: \t{st.session_state.email}")
            st.write(f"Age: \t{st.session_state.age}")
            st.write(f"Gender: \t{st.session_state.gender}")
            #st.write("Subjects:")
        with col2:
            st.write(f"DOB: \t{st.session_state.date_of_birth}")
            st.write(f"Phone No.: \t{st.session_state.phone}")
            st.write(f"WhatsApp No.: \t{st.session_state.whatsapp}")
            st.write(f"Course: \t{st.session_state.course}")
            #st.write(f"Stream: \t{st.session_state.stream}")
            #st.write(f"Section: \t{st.session_state.section}")
        

        x = st.columns([1, 1, 1])
        cam_inp = x[1].camera_input("Register your images here")
        camcol1, camcol2, camcol3 = st.columns([1, 1, 1.5])
        if cam_inp:
            with camcol1:
                st.image(cam_inp)
            with camcol2:
                st.image(cam_inp)
            with camcol3 and cam_inp:
                st.image(cam_inp)

    def Records_page(username, role, db, storage):
        st.write(pd.read_csv('record.csv', index_col=False))
        source_firebase = fr"/teacher/{username}/record.csv"
        dest_local = fr"D:\Desktop\att\Attendance_management\user_temp"
        storage.child(
            f"teacher/{username}/records/record.csv").download(path=source_firebase, filename=fr"user_temp/record.csv")
        #st.write(storage.download(path='gs://attendance-management-672ad.appspot.com/teacher/111111/records',))
        df = pd.read_csv(
            fr"D:\Desktop\att\Attendance_management\user_temp\record.csv")
        if st.session_state.picture_clicked and st.session_state.matched:
            pass
    navbar = option_menu(menu_title="Navbar", options=['Home', 'Details', 'Records'],
                         menu_icon='cast', icons=['house', 'book', 'envelope'], default_index=0, orientation='horizontal')
    if navbar == 'Home':
        Home_page(username, role, db, storage)
    if navbar == 'Details':
        Details_page(username, role, db, storage)
    if navbar == 'Records':
        Records_page(username, role, db, storage)

        st.success('Attendance Records')
