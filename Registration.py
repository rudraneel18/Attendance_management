from imports import *

def register():    
    FRAME_WINDOW = st.image([])
    def show_camera():
        pic_no = 1
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_feed = cv2.VideoCapture(0)
        while run and pic_no <= 1:
            _, frame = video_feed.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = frame.copy()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Get the height and width of the entire image
            height, width, channels = frame.shape
            faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(int(height/2.5), int(width/2.5)))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.putText(frame, f"({x}, {y})", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x+w}, {y})", (x+w, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x}, {y+h})", (x, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x+w}, {y+h})", (x+w, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"Width: {w}", (10, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"Height: {h}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                if w/width < 0.35 or h/height < 0.35:
                    cv2.putText(frame, f"Come Closer", (530, height - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                if w/width >= 0.45 or h/height >= 0.45:
                    cv2.putText(frame, f"Click Now", (530, height - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cropped = img[y:y+h, x:x+w]
                    filename = f"images/1.jpg"
                    cv2.imwrite(filename, cropped)
                    pic_no += 1
            FRAME_WINDOW.image(frame)

        video_feed.release()

    def retake_camera():
        pic_no = 1
        os.remove("images/1.jpg")
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_feed = cv2.VideoCapture(0)
        while retake and pic_no <= 1:
            _, frame = video_feed.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = frame.copy()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Get the height and width of the entire image
            height, width, channels = frame.shape
            faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(int(height/2.5), int(width/2.5)))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.putText(frame, f"({x}, {y})", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x+w}, {y})", (x+w, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x}, {y+h})", (x, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"({x+w}, {y+h})", (x+w, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"Width: {w}", (10, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"Height: {h}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                if w/width < 0.35 or h/height < 0.35:
                    cv2.putText(frame, f"Come Closer", (530, height - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                if w/width >= 0.45 or h/height >= 0.45:
                    cv2.putText(frame, f"Click Now", (530, height - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cropped = img[y:y+h, x:x+w]
                    filename = f"images/1.jpg"
                    cv2.imwrite(filename, cropped)
                    pic_no += 1
            FRAME_WINDOW.image(frame)

        video_feed.release()
    run = st.button('Run',on_click=show_camera)
    retake = st.button('Retake',on_click=retake_camera)
