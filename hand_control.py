import cv2
import mediapipe as mp
import serial

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/cu.usbmodem14101', 9600)  # Change to your Arduino's port

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize camera
cap = cv2.VideoCapture(0)

# Flags to keep track of finger states
thumb_down = False
index_finger_down = False
middle_finger_down = False
ring_finger_down = False
pinky_finger_down = False

# Define a threshold for thumb bending (adjust as needed)
THUMB_BEND_THRESHOLD = 0.1

# Initialize a variable to store the reference thumb x-coordinate
thumb_open_x = None

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image to get hand landmarks
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the thumb landmarks
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                
                # Check if thumb is positioned to the left of the index finger
                if thumb_tip < index_tip:
                    if not thumb_down:
                        ser.write(b'0')  # Send signal to Arduino to turn on servo
                        thumb_down = True
                else:
                    if thumb_down:
                        ser.write(b'1')  # Send signal to Arduino to turn off servo
                        thumb_down = False

                # Get landmarks for index finger, middle finger, ring finger, and pinky finger
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_y = index_tip.y * frame.shape[0]  # Convert normalized y-coordinate to pixel value
                
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                middle_y = middle_tip.y * frame.shape[0]  # Convert normalized y-coordinate to pixel value

                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                ring_y = ring_tip.y * frame.shape[0]

                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                pinky_y = pinky_tip.y * frame.shape[0]

                # Check if index finger is down
                if index_y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * frame.shape[0]:
                    if not index_finger_down:
                        ser.write(b'2')  # Send signal to Arduino to turn on LED
                        index_finger_down = True
                else:
                    if index_finger_down:
                        ser.write(b'3')  # Send signal to Arduino to turn off LED
                        index_finger_down = False

                # Check if middle finger is down
                if middle_y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * frame.shape[0]:
                    if not middle_finger_down:
                        ser.write(b'4')  # Send signal to Arduino to turn on servo
                        middle_finger_down = True
                else:
                    if middle_finger_down:
                        ser.write(b'5')  # Send signal to Arduino to turn off servo
                        middle_finger_down = False
                # Check if ring finger is down
                if ring_y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * frame.shape[0]:
                    if not ring_finger_down:
                        ser.write(b'6')  # Send signal to Arduino to turn on servo
                        ring_finger_down = True
                else:
                    if ring_finger_down:
                        ser.write(b'7')  # Send signal to Arduino to turn off servo
                        ring_finger_down = False
                # Check if pinky finger is down
                if pinky_y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * frame.shape[0]:
                    if not pinky_finger_down:
                        ser.write(b'8')  # Send signal to Arduino to turn on servo
                        pinky_finger_down = True
                else:
                    if pinky_finger_down:
                        ser.write(b'9')  # Send signal to Arduino to turn off servo
                        pinky_finger_down = False

                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
