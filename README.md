 Software_Engineering_Project

The University Dispensary Attendance Monitoring System is designed to efficiently manage and monitor student attendance at the university's dispensary. The system provides various features and functionalities to facilitate student registration, check-in, medical attention recording, check-out, and reporting. Additionally, it adheres to essential non-functional requirements to ensure privacy, security, usability, performance, and reliability.

 Features


1 Student Registration

Description: The system allows students to register their personal information to be included in the attendance monitoring system.

Requirements
- The system  provides a user interface for student registration.
- During registration, the system  collects the following information:
  - Student ID
  - Name
  - Contact details
- The system  validates and store the registered student information in the database.
- Each registered student is assigned a unique identification number.

2 Application Login

Description: The system enables dispensary staff to securely log in to the application to access the attendance monitoring system.

requirements
- The system  provides a login interface for dispensary staff.
- Before granting access, the system  verifies the staff's credentials.
- The system  enforces appropriate security measures, such as password hashing and session management.

3 Student Check-in

Description :The system facilitates the check-in process when a student visits the dispensary for medical attention.

Requirements
- The system  provides a user interface for staff to perform student check-in.
- Staff is able to search and identify students by their unique identification number or university identification card.
- The system  records the check-in time and date for each student.
- The student's attendance record is updated accordingly.

4 Medical Attention

Description: The system supports the recording of medical attention provided to students.

Requirements
- The system  provides a user interface for staff to record medical attention details.
- Staff is able to enter the medical services provided, such as diagnosis, treatment, and medications.
- The system links the medical attention details to the student's attendance record.

5 Check-out and Attendance Update

Description: The system facilitates the check-out process and updates the student's attendance record accordingly.

Requirements
- The system  provides a user interface for staff to perform student check-out.
- The system  records the check-out time and date for each student.
- The student's attendance record is updated to indicate the completion of medical attention.

6 Reporting and Analytics

Description:The system offers reporting and analytics capabilities to generate insights from the captured attendance data.

Requirements:
- The system  provides predefined reports on student attendance patterns, such as daily, weekly, and monthly attendance summaries.
- It  supports customized report generation based on selected parameters, such as date range, specific students, or medical services provided.
- Attendance data is presented in a clear and meaningful visualizations, including charts and graphs.




 Installation

1. Clone the repository to your local machine:

   
   git clone https://github.com/your-username/Software_Engineering_Project.git
   

2. Change to the project directory:


   cd Software_Engineering_Project
  
3. Create a Virtual Environment:

   
   py -m venv env
   
4. Activate Virtual Environment :

   
   .\env\Scripts\activate
   

5. Install the required dependencies:


   pip install -r requirements.txt
   

6. Run the application:

   
   python app.py
  

7. Access the application through your web browser at `http://localhost:5000`.

Usage

1. Open the application in your web browser.

2. Enter your student credentials to authenticate yourself.

3. Fill in the required details such as the date, time, and reason for your visit.

4. Click the "Submit" button to log your attendance.

5. Optionally, explore the reporting and analytics features to gain insights into student attendance patterns and related metrics.

Contributing

Contributions to the university dispensary attendance tracker are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   
   git checkout -b feature/your-feature-name
   

3. Make the necessary changes and commit them:


   git commit -am 'Add some feature'
   

4. Push the changes to your branch:

   
   git push origin feature/your-feature-name
   

5. Open a pull request describing your changes.

