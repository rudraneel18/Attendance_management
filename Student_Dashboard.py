from imports import *
from streamlit_option_menu import option_menu
import Registration

def student_dashboard(username, role, db, storage, auth):
    
    #################################session_states############################
    if "user_details" not in st.session_state:
        data=db.child("student").child(username).get().val()
        st.session_state.user_details={"picture_taken":False,
                                       "matched":False,
                                       "attendance":False
                                        }
        st.session_state.user_details.update(data)
        
    #################################session_states_ends############################
    def Home_page(username, role, db, storage):
        title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Student Dashboard</h1>", unsafe_allow_html=True)
        st.warning("If you have not registered your images, please go to Details tab")
        cam=st.camera_input("Click your picture")
        if cam is not None:
            st.session_state.user_details.picture_clicked = True
            '''attendance neva hobe'''

    def Details_page(username, role, db, storage):
        st.subheader("Student Details")
        name = db.child("student").child(username).child("name").get().val()
        st.write(f"Welcome {name}! You are logged in as a {role}.")
        col1, col2,col3,col4= st.columns([1, 1,1,1])
        #st.write(st.session_state.user_details)
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
            st.write(st.session_state.user_details["name"])
            st.write(st.session_state.user_details["enrollment_id"])
            st.write(st.session_state.user_details["registration_id"])
            st.write(st.session_state.user_details["adhar_number"])
            st.write(st.session_state.user_details["email"])
            st.write(st.session_state.user_details["college_mail"])
            st.write(st.session_state.user_details["age"])
            st.write(st.session_state.user_details["gender"])  
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
            st.write(st.session_state.user_details["date_of_birth"])
            st.write(st.session_state.user_details["start_year"])
            st.write(st.session_state.user_details["end_year"])
            st.write(st.session_state.user_details["phone"])
            st.write(st.session_state.user_details["whatsapp"])
            st.write(st.session_state.user_details["course"])
            st.write(st.session_state.user_details["stream"])
            st.write(st.session_state.user_details["end_year"]-st.session_state.user_details["start_year"])
            st.write(st.session_state.user_details["section"])

        x = st.columns([1, 1, 1])
        x[1] = Registration.register()
        storage.child(f'student/{str(st.session_state.user_details["enrollment_id"])}/images/reg_img1.jpg').put(fr"images\1.jpg")
        storage.child(f'student/{str(st.session_state.user_details["enrollment_id"])}/images/reg_img2.jpg').put(fr"images\2.jpg")
        storage.child(f'student/{str(st.session_state.user_details["enrollment_id"])}/images/reg_img3.jpg').put(fr"images\3.jpg")
        
            
    def Records_page(username, role, db, storage):
        st.write(pd.read_csv('record.csv', index_col=False))
        source_firebase=fr"/student/{username}/record.csv"
        #dest_local = fr"D:\Desktop\att\Attendance_management\user_temp"
        storage.child(
            f"student/{username}/records/record.csv").download(path=source_firebase,filename=fr"user_temp/record.csv")
        #st.write(storage.download(path='gs://attendance-management-672ad.appspot.com/student/111111/records',))
        #df=pd.read_csv(fr"D:\Desktop\att\Attendance_management\user_temp\record.csv")
        if st.session_state.user_details["picture_clicked"] and st.session_state.user_details["matched"]:
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
        
