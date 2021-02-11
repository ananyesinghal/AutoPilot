import cv2

# Our Image
img_file = "./img/carImage.jpg"
video_file = cv2.VideoCapture("./video/DashCamtrimmed3.mp4")

# Our pre-trained classifier
classifier_file = "car_detector.xml"
classifier_file_ped = "ped_detector.xml"

while True:
    # Read frame
    (read_sucessful, frame) = video_file.read()

    if read_sucessful:
        # Convert frame to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Create classifier
    car_tracker = cv2.CascadeClassifier(classifier_file)
    ped_tracker = cv2.CascadeClassifier(classifier_file_ped)

    # Detect Car/Ped
    cars = car_tracker.detectMultiScale(frame)
    peds = ped_tracker.detectMultiScale(frame)

    # Draw Rectangles
    for car in cars:
        (x, y, w, h) = car
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    for ped in peds:
        (x, y, w, h) = ped
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the image
    cv2.imshow("Self Driving", frame)

    # For image to stay until key is pressed
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video_file.release()


# Create opencv image
img = cv2.imread(img_file)

# Convert to grayscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# Detect Car
cars = car_tracker.detectMultiScale(black_n_white)

# Draw Rectangles
for car in cars:
    (x, y, w, h) = car
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


# Display the image
cv2.imshow("Self Driving image", img)

# For image to stay until key is pressed
cv2.waitKey()


print("Code Completed")