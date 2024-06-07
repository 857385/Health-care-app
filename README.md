# Health-care-app







Testing :
Here are some testing comments and scenarios to ensure the healthcare management system functions as expected:
 Testing Comments and Scenarios
 1. User Registration and Authentication
- Test Case 1: Successful Registration
  - Action: Register a new user with a unique username and password.
  - Expected Result: User registration should succeed, and a success message should be displayed.
- Test Case 2: Duplicate Registration
  - Action: Register a user with a username that already exists.
  - Expected Result: Registration should fail, and an error message indicating duplicate username should be displayed.
- Test Case 3: Successful Login
  - Action: Log in with valid credentials.
  - Expected Result: Login should succeed, and the main window should be displayed.
- Test Case 4: Failed Login
  - Action: Log in with invalid credentials.
  - Expected Result: Login should fail, and an error message indicating invalid credentials should be displayed.
 2. Patient Management
- Test Case 5: Add Patient
  - Action: Add a new patient with valid details.
  - Expected Result: Patient should be added successfully, and the patient list should be updated.
- Test Case 6: View Patients
  - Action: View the list of patients.
  - Expected Result: The patient list should display all registered patients with their details.

- Test Case 7: Edit Patient
  - Action: Select a patient and edit their details.
  - Expected Result: Patient details should be updated successfully, and the changes should be reflected in the patient list.

- Test Case 8: Delete Patient
  - Action: Select a patient and delete their record.
  - Expected Result: Patient should be deleted successfully, and the patient list should be updated.

 3. Appointment Scheduling

- Test Case 9: Book Appointment
  - Action: Book an appointment with valid patient ID, provider ID, date, and time.
  - Expected Result: Appointment should be booked successfully, and the appointment list should be updated.

- Test Case 10: View Appointments
  - Action: View the list of scheduled appointments.
  - Expected Result: The appointment list should display all scheduled appointments with their details.

 4. Diagnostics

- Test Case 11: Calculate BMI
  - Action: Enter valid weight and height values and calculate BMI.
  - Expected Result: The BMI should be calculated correctly, and the result should be displayed.

 5. General UI and Navigation

- Test Case 12: Navigation Between Tabs
  - Action: Navigate between "Patient Management", "Appointment Scheduling", and "Diagnostics" tabs.
  - Expected Result: The application should navigate smoothly between tabs without any errors.

- Test Case 13: UI Responsiveness
  - Action: Resize the application window.
  - Expected Result: The UI components should adjust and remain usable within the resized window.
