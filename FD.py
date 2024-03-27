import cv2
import threading
import playsound  # Add this line to import the playsound module

# Load the cascade classifier for fire detection
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

# Create a video capture object
vid = cv2.VideoCapture(0)  # Use '0' for the built-in camera or '1' for an external camera

# Function to play the alarm sound
def play_alarm_sound_function():
    playsound.playsound('Alarm Sound.mp3', True)
    print("Fire alarm end")

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
        threading.Thread(target=play_alarm_sound_function).start()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
