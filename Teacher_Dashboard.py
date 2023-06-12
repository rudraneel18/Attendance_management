from imports import * 
from streamlit_option_menu import option_menu
import Registration



def teacher_dashboard(username, role, db, storage, auth):
    st.success("You are logged in as a Teacher")
    #################################session_states############################
    data = db.child("teacher").child(username).get().val()
    if 'user_details' not in st.session_state:
        id= st.session_state.login_details["username"]
        st.session_state.user_details={"picture_taken":True,
                                        "matched":False,
                                        "attendance":False,
                                        "user_id":id
                                        }
        st.session_state.user_details.update(data)  
    #st.write(st.session_state.user_details)
    # if 'picture_clicked' not in st.session_state:
    #     st.session_state.picture_clicked = False
    # if 'matched' not in st.session_state:
    #     st.session_state.matched = False
    # if 'attendance' not in st.session_state:
    #     st.session_state.attendance = False
    # if 'usersname' not in st.session_state:
    #     st.session_state.usersname = data["name"]
    # if 'user_id' not in st.session_state:
    #     st.session_state.user_id = username
    # if 'age' not in st.session_state:
    #     st.session_state.age = data["age"]
    # if 'date_of_birth' not in st.session_state:
    #     st.session_state.date_of_birth = data["date_of_birth"]
    # if 'phone' not in st.session_state:
    #     st.session_state.phone = data["phone"]
    # if 'whatsapp' not in st.session_state:
    #     st.session_state.whatsapp = data["whatsapp"]
    # if 'email' not in st.session_state:
    #     st.session_state.email = data["email"]
    # if 'gender' not in st.session_state:
    #     st.session_state.gender=data["gender"]
    # if 'course' not in st.session_state:
    #     st.session_state.course=data["course"]
    # if 'departments' not in st.session_state:
    #     st.session_state.departments=data["departments"]
    # st.write(st.session_state.departments)

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
        st.write(f"Welcome {st.session_state.user_details['name']}! You are logged in as a {role}.")
        col1, col2= st.columns([1, 1])
        with col1:
            st.write(f"Name:\t\t{st.session_state.user_details['name']}")
            st.write(f"Teacher ID:\t\t{st.session_state.user_details['user_id']}")
            #st.write("Adhar No.:")
            st.write(f"Email ID:\t\t{st.session_state.user_details['email']}")
            st.write(f"Age: \t\t{st.session_state.user_details['age']}")
            st.write(f"Gender: \t\t{st.session_state.user_details['gender']}")
            st.write(f"DOB: \t\t{st.session_state.user_details['date_of_birth']}")
            st.write(f"Phone No.: \t\t{st.session_state.user_details['phone']}")
            st.write(f"WhatsApp No.: \t\t{st.session_state.user_details['whatsapp']}")
            #st.write("Subjects:")
        with col2:
            
            st.write(f"Course: \t\t{st.session_state.user_details['course']}")
            departments=st.session_state.user_details['departments']
            for department,years in departments.items():
                st.write(department)
                for year, sections in years.items():
                    st.write(year)
                    for section, subjects in sections.items():
                        st.write(section+": "+", ".join(subjects))
                        
                        
                        
            
            #st.write(f"Stream: \t{st.session_state.stream}")
            #st.write(f"Section: \t{st.session_state.section}")
        

        x = st.columns([1, 1, 1])
        x[1] = Registration.register()
        storage.child(f'teacher/{str(st.session_state.user_details["user_id"])}/images/reg_img1.jpg').put(fr"images\1.jpg")
        storage.child(f'teacher/{str(st.session_state.user_details["user_id"])}/images/reg_img2.jpg').put(fr"images\2.jpg")
        storage.child(f'teacher/{str(st.session_state.user_details["user_id"])}/images/reg_img3.jpg').put(fr"images\3.jpg")
        

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
