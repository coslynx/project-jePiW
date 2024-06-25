# Project Overview:
- Develop a web application to digitalize the hospitality process for group accommodation.
- Users can upload two CSV files to allocate rooms efficiently in hostels.
- Ensure group members with the same ID stay together and adhere to hostel capacities and gender-specific accommodations.

# Technical Details:
1. CSV File 1 (Group Information):
- Contains info about groups with a common ID, number of members, and gender.
- Various scenarios under the same ID: groups of different sizes, boys or girls only, or mixed groups.
- Example:
  Group ID   Members
  101           3
  102           4
  103           2
  104           5
  105           8

2. CSV File 2 (Hostel Information):
- Contains info about hostels, room capacities, and gender accommodation.
- Example:
  Hostel Name    Room Number  Capacity  Gender
  Boys Hostel A  101                    3                Boys
  Boys Hostel A  102                    4                Boys
  Girls Hostel B  201                    2                Girls
  Girls Hostel B  202                    5                Girls

3. Frontend Requirements:
- User-friendly interface to upload CSV files.
- Algorithm to allocate rooms based on criteria.
- Criteria include group members staying together, gender-specific accommodations, and room capacities not exceeded.

4. Output:
- Display of allocated rooms with group members.
- Downloadable CSV file with allocation details.
- Example output:
  Group ID  Hostel Name    Room Number   Members Allocated
  101           Boys Hostel A   101                     3
  102           Girls Hostel B   202                     4

5. Enhancements:
- Utilize Django for backend development.
- Style the application using CSS for a visually appealing interface.

# Technical Details:
- Programming Languages: Python, HTML, CSS
- Backend Framework: Django
- Frontend: HTML, CSS
- Database: SQLite

CSV File Handling:
- Pandas library for reading and manipulating CSV files.
- Latest version: Pandas 1.3.3

Frontend Development:
- Bootstrap for responsive design and layout.
- Latest version: Bootstrap 5.1.1
- Dropzone.js for drag-and-drop file uploads.
- Latest version: Dropzone.js 5.9.2

Backend Development:
- Django framework for handling file uploads and room allocation logic.
- Django REST framework for API development.
- Latest version: Django 3.2.8, Django REST framework 3.12.4

Room Allocation Algorithm:
- Logic to group members with the same ID together.
- Algorithm to assign members to rooms based on gender and capacity constraints.

Output Generation:
- Django template to display allocated rooms with group members.
- Django CSV module to generate downloadable CSV file with allocation details.

Enhancements:
- Django chosen for backend due to its robustness and scalability for web applications.
- Pandas for CSV handling due to its efficiency in data manipulation.
- Bootstrap for frontend design to ensure a user-friendly interface.
- Django REST framework for API development to facilitate communication between frontend and backend components.
- Dropzone.js for easy file uploads enhancing user experience.