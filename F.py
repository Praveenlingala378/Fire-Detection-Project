import cv2
import threading
import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load the cascade classifier for fire detection
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

# Create a video capture object
vid = cv2.VideoCapture(0)  # Use '0' for the built-in camera or '1' for an external camera

# Email configuration
sender_email = "praveenlingala378@gmail.com"
sender_password = "9740699375"
recipient_email = "rlucky540@gmail.com"
subject = "Fire Detected!"
message_text = "Fire has been detected. Please take necessary action."

# Function to play the alarm sound
def play_alarm_sound_function():
    playsound.playsound(r'C:\Projects\FIRE_DETECTION-main\FIRE_DETECTION-main\Alarm Sound.mp3', True)
    print("Fire alarm end")

# Function to send an email
def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

while True:
    Alarm_Status = False
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        print("Fire detected")
        if not Alarm_Status:
            threading.Thread(target=play_alarm_sound_function).start()
            threading.Thread(target=send_email, args=(subject, message_text)).start()
            Alarm_Status = True

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
