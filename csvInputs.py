import csv  # Imports the 'csv' module, which provides functionality for working with CSV files (reading and writing).
import random  # Imports the 'random' module, which provides functions for generating random numbers and making random choices.


def get_data():
    """
    Returns a dictionary containing all the data needed for student generation.

    This function defines the structure of colleges, departments, courses, and sample names 
    that will be used to create student profiles. It returns a dictionary containing 
    this data for use by other functions.

    Returns:
        dict: A dictionary containing the following keys:
            - 'colleges': A nested dictionary representing the university structure with colleges, departments, and courses.
            - 'first_names': A list of sample first names for students.
            - 'middle_names': A list of sample middle names for students.
            - 'last_names': A list of sample last names for students.
    """

    # Ensure all departments have 40 courses
    colleges = {
        "Engineering": {
            "departments": {
                "Mechanical Engineering": [
                    "Statics", "Dynamics", "Fluid Mechanics", "Thermodynamics", "Strength of Materials",
                    "Mechanical Design", "Vibration Analysis", "Materials Science", "Heat Transfer",
                    "Machine Elements", "Manufacturing Processes", "Mechatronics", "Control Systems",
                    "Engineering Materials", "Design of Experiments", "Advanced Manufacturing", "Finite Element Analysis",
                    "Heat Exchangers", "Nanotechnology in Engineering", "Advanced Thermodynamics", "Computational Fluid Dynamics",
                    "Power Plant Engineering", "Hydraulic Systems", "Internal Combustion Engines", "Robotics",
                    "Machine Learning for Engineering", "Simulation and Modeling", "Engineering Dynamics", "Energy Conversion",
                    "Measuring Systems in Engineering", "Energy Systems Engineering", "Advanced Fluid Mechanics"
                ],
                "Civil Engineering": [
                    "Structural Analysis", "Concrete Technology", "Soil Mechanics", "Fluid Mechanics", "Environmental Engineering",
                    "Transportation Engineering", "Geotechnical Engineering", "Construction Management", "Water Resources Engineering",
                    "Advanced Structural Analysis", "Urban Planning", "Renewable Energy Systems", "Advanced Geotechnical Engineering",
                    "Engineering Project Management", "Smart Cities", "Sustainable Infrastructure", "Advanced Materials for Construction",
                    "Environmental Impact Assessment", "Hydraulics Engineering", "Building Information Modeling (BIM)", "Traffic Flow Analysis",
                    "Design of Reinforced Concrete Structures", "Advanced Soil Mechanics", "Geotechnical Site Investigation", "Hydrology",
                    "Construction Safety Management", "Seismic Engineering", "Foundation Engineering", "Tunneling and Underground Engineering"
                ],
                "Aerospace Engineering": [
                    "Fluid Dynamics", "Aerodynamics", "Propulsion Systems", "Avionics", "Flight Mechanics", "Space Systems Engineering",
                    "Rocketry", "Aircraft Design", "Unmanned Aerial Vehicles", "Aircraft Structures", "Control Systems",
                    "Navigation Systems", "Astronautics", "Space Robotics", "Advanced Materials for Aerospace", "Combustion Engineering",
                    "Aircraft Performance", "Spacecraft Design", "Systems Engineering for Aerospace", "Wind Tunnel Testing",
                    "Control and Guidance Systems", "Space Exploration", "Satellite Systems", "Aircraft Maintenance", "Flight Simulation"
                ]
            }
        },
        "Science": {
            "departments": {
                "Physics": [
                    "Classical Mechanics", "Quantum Mechanics", "Electromagnetism", "Thermodynamics", "Statistical Mechanics",
                    "Relativity", "Nuclear Physics", "Particle Physics", "Astrophysics", "Solid-State Physics",
                    "Optics", "Plasma Physics", "Computational Physics", "Biophysics", "Condensed Matter Physics",
                    "Molecular Physics", "Physics of Materials", "Mathematical Methods in Physics", "Applied Physics",
                    "Nanotechnology", "High Energy Physics", "Quantum Field Theory", "Advanced Fluid Dynamics",
                    "Electronics for Physicists", "Geophysics", "Environmental Physics", "Experimental Physics",
                    "Physics of Nanostructures", "Quantum Information", "Medical Physics", "Photonic Materials",
                    "Laser Physics", "Nonlinear Dynamics", "Nanomaterials", "Surface Physics", "Theoretical Physics"
                ],
                "Biology": [
                    "General Biology", "Ecology", "Evolutionary Biology", "Genetics", "Cell Biology", "Molecular Biology",
                    "Microbiology", "Biochemistry", "Biophysics", "Physiology", "Immunology", "Developmental Biology",
                    "Marine Biology", "Human Anatomy", "Genomics", "Bioinformatics", "Cancer Biology", "Neurobiology",
                    "Structural Biology", "Pharmacology", "Plant Biology", "Evolutionary Ecology", "Biotechnology",
                    "Environmental Biology", "Genetic Engineering", "Biotechnology in Agriculture", "Systems Biology",
                    "Molecular Genetics", "Computational Biology", "Medical Microbiology", "Biological Chemistry",
                    "Plant Physiology", "Stem Cell Biology", "Bioethics", "Bioengineering", "Microbial Ecology",
                    "Endocrinology", "Forensic Biology", "Biology of Aging", "Animal Behavior"
                ],
                "Chemistry": [
                    "General Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry",
                    "Biochemistry", "Medicinal Chemistry", "Polymer Chemistry", "Industrial Chemistry", "Environmental Chemistry",
                    "Surface Chemistry", "Green Chemistry", "Quantum Chemistry", "Chemical Engineering Principles", "Nano-Chemistry",
                    "Materials Chemistry", "Solid-State Chemistry", "Chemical Kinetics", "Catalysis", "Reaction Mechanisms",
                    "Instrumental Analysis", "Pharmaceutical Chemistry", "Computational Chemistry", "Chemical Thermodynamics",
                    "Chemical Bonding", "Advanced Organic Synthesis", "Applied Environmental Chemistry", "Water Chemistry",
                    "Electrochemistry", "Photochemistry", "Chemical Toxicology", "Organometallic Chemistry", "Chemical Data Analysis",
                    "Laboratory Techniques", "Chemical Safety", "Process Control in Chemistry"
                ]
            }
        },
        "Arts": {
            "departments": {
                "Literature": [
                    "World Literature", "English Literature", "American Literature", "Shakespeare", "Modern Poetry",
                    "Literary Theory", "Creative Writing", "Film Studies", "Drama", "Contemporary Fiction",
                    "Gender and Literature", "Postcolonial Literature", "Renaissance Literature", "Narrative Theory",
                    "Philosophy of Literature", "Literature and Politics", "Comparative Literature", "Writing for Stage and Screen",
                    "Digital Humanities", "History of English Language", "Literature of the Romantic Period", "Literature and Identity",
                    "Science Fiction", "Children's Literature", "Theatre History", "Cultural Studies", "Gender Studies",
                    "Textual Criticism", "Writing and Rhetoric", "Mythology", "Poetry Writing", "Contemporary Drama"
                ],
                "Fine Arts": [
                    "Drawing", "Painting", "Sculpture", "Photography", "Printmaking", "Art History", "Modern Art",
                    "Art and Technology", "Art Criticism", "Public Art", "Contemporary Art", "Mixed Media Art",
                    "Art and Culture", "Film and Media Arts", "Studio Art", "Digital Art", "Graphic Design", "Installation Art",
                    "Art Theory", "Color Theory", "Art and Architecture", "Performance Art", "Photography Techniques",
                    "Fashion Design", "Museum Studies", "Ceramics", "Print Design", "Art in the 21st Century",
                    "Art Exhibitions", "Art Education", "Fine Art Foundations", "Visual Art and Society"
                ],
                "Music": [
                    "Music Theory", "Music History", "Composition", "Orchestration", "Conducting", "Digital Music Production",
                    "Jazz Studies", "World Music", "Ethnomusicology", "Opera", "Music Technology", "Music Performance",
                    "Vocal Performance", "Instrumental Performance", "Music Composition for Film", "Music Education",
                    "Popular Music Studies", "Choral Conducting", "Classical Music Appreciation", "Music and Society",
                    "Songwriting", "Electronic Music Production", "Advanced Music Theory", "Musical Theatre", "Sound Design",
                    "Music Pedagogy", "Music Therapy", "Percussion Studies", "Brass and Woodwind Studies", "String Studies"
                ]
            }
        },
        "Business": {
            "departments": {
                "Business Administration": [
                    "Principles of Management", "Marketing Management", "Organizational Behavior", "Financial Accounting",
                    "Managerial Accounting", "Operations Management", "Human Resource Management", "Business Ethics",
                    "Entrepreneurship", "Strategic Management", "Marketing Research", "Business Law", "Project Management",
                    "Business Communication", "Business Analytics", "Leadership in Organizations", "Global Business",
                    "Supply Chain Management", "Risk Management", "Business Statistics", "E-Commerce", "Corporate Finance",
                    "International Business", "Consumer Behavior", "Management Information Systems", "Sustainability in Business",
                    "Financial Markets", "Behavioral Economics", "Public Relations", "Negotiation Skills", "Corporate Social Responsibility",
                    "Corporate Governance", "Retail Management", "Event Planning", "Marketing Strategy", "Digital Marketing"
                ],
                "Economics": [
                    "Microeconomics", "Macroeconomics", "International Economics", "Development Economics", "Labor Economics",
                    "Public Economics", "Monetary Economics", "Environmental Economics", "Industrial Organization", "Econometrics",
                    "Game Theory", "Behavioral Economics", "Financial Economics", "Agricultural Economics", "Health Economics",
                    "Economics of Education", "Economics of Innovation", "Political Economy", "Global Trade", "Economic Development",
                    "Urban Economics", "Economics of Inequality", "Market Structures", "Regional Economics", "Economics of Technology",
                    "Managerial Economics", "Financial Crises", "Investment Theory", "Economics of Health Policy", "Advanced Microeconomics"
                ]
            }
        }
    }  # End of the 'colleges' dictionary.

    # Sample names for generating unique student names
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Emily", "David", "Sophia", "Michael", "Olivia"]  # List of first names to be used for generating student names.
    middle_names = ["Alex", "Taylor", "Jordan", "Morgan", "Quinn", "Reese", "Riley", "Casey", "Parker", "Hayden"]  # List of middle names to be used for generating student names.
    last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Clark"]  # List of last names to be used for generating student names.

    # Return a dictionary containing all the generated data
    return {  # Returns a dictionary containing the college structure, first names, middle names, and last names.
        "colleges": colleges,  # Key 'colleges', value is the 'colleges' dictionary defined above.
        "first_names": first_names,  # Key 'first_names', value is the 'first_names' list defined above.
        "middle_names": middle_names,  # Key 'middle_names', value is the 'middle_names' list defined above.
        "last_names": last_names  # Key 'last_names', value is the 'last_names' list defined above.
    }  # End of the return statement.


# Generate a unique three-part name for each student
def generate_student_name(data):  # Defines a function named 'generate_student_name' that takes a 'data' dictionary as input.
    """
    Generates a random student name using the provided data.

    This function randomly selects a first name, middle name, and last name from the 
    provided data dictionary and combines them to create a full student name.

    Args:
        data (dict): A dictionary containing lists of first names, middle names, and last names.

    Returns:
        str: A randomly generated student name in the format "FirstName MiddleName LastName".
    """
    # Randomly select a first, middle, and last name from the data
    return f"{random.choice(data['first_names'])} {random.choice(data['middle_names'])} {random.choice(data['last_names'])}"  # Returns a formatted string containing the randomly chosen first, middle, and last names.



# Generate student ID
def generate_student_id():  # Defines a function named 'generate_student_id'.
    """
    Generates a random student ID.

    This function creates a random student ID in the format "YYYY0X000", where:
    - YYYY represents a random year between 2010 and 2024.
    - X represents a random digit between 0 and 9.

    Returns:
        str: A randomly generated student ID.
    """
    # Create a random student ID in the specified format
    return str(random.randint(2010, 2024)) + "0" + str(random.randint(0, 9)) + "000"  # Returns a string containing the randomly generated student ID.


# Generate degree
def generate_degree(level, department):  # Defines a function named 'generate_degree' that takes 'level' and 'department' as input.
    """
    Generates a degree string based on the student's level and department.

    Args:
        level (str): The student's academic level ('U' for Undergraduate, 'G' for Graduate, 'D' for Doctorate).
        department (str): The student's department (e.g., 'Mechanical Engineering', 'Physics').

    Returns:
        str: A string representing the student's degree (e.g., 'BSME' for Bachelor of Science in Mechanical Engineering).
    """
    # Determine the degree based on the level (U, G, PhD) and department
    level_code = "BS" if level == "U" else "MS" if level == "G" else "PhD"  # Assigns a level code ('BS', 'MS', or 'PhD') based on the 'level' input.
    dept_code = {  # Creates a dictionary named 'dept_code' to map department names to their respective codes.
        "Mechanical Engineering": "ME",  # Key 'Mechanical Engineering', value 'ME'.
        "Civil Engineering": "CE",  # Key 'Civil Engineering', value 'CE'.
        "Aerospace Engineering": "AE",  # Key 'Aerospace Engineering', value 'AE'.
        "Physics": "PH",  # Key 'Physics', value 'PH'.
        "Biology": "BI",  # Key 'Biology', value 'BI'.
        "Chemistry": "CH",  # Key 'Chemistry', value 'CH'.
        "Computer Science": "CS",  # Key 'Computer Science', value 'CS'.
        "Electrical Engineering": "EE",  # Key 'Electrical Engineering', value 'EE'.
        "Business Administration": "BA",  # Key 'Business Administration', value 'BA'.
        "Economics": "EC",  # Key 'Economics', value 'EC'.
        "Literature": "LI",  # Key 'Literature', value 'LI'.
        "Fine Arts": "FA",  # Key 'Fine Arts', value 'FA'.
        "Music": "MU"  # Key 'Music', value 'MU'.
    }  # End of the 'dept_code' dictionary.
    # Return the combined degree code
    return level_code + dept_code.get(department, "NA")  # Returns the combined degree code (level code + department code), or 'NA' if the department is not found in the 'dept_code' dictionary.



# Generate courses for a student
def generate_courses(level, department, data):  # Defines a function named 'generate_courses' that takes 'level', 'department', and 'data' as input.
    """
    Generates a list of courses for a student based on their level, department, and provided data.

    This function randomly selects major courses from the student's department and minor courses 
    from other departments, ensuring a variety of courses and avoiding over-sampling. 
    It returns a list of lists, where each inner list represents a course with details 
    like term, course name, course ID, type (Major/Minor), credit hours, and grade.

    Args:
        level (str): The student's academic level ('U' for Undergraduate, 'G' for Graduate, 'D' for Doctorate).
        department (str): The student's department (e.g., 'Mechanical Engineering', 'Physics').
        data (dict): A dictionary containing the university structure with colleges, departments, and courses.

    Returns:
        list: A list of lists, where each inner list represents a course with the following details:
            - term (int): The term in which the course was taken.
            - course_name (str): The name of the course.
            - course_id (str): The ID of the course.
            - course_type (str): The type of course ('Major' or 'Minor').
            - credit_hours (int): The number of credit hours for the course.
            - grade (int): The grade received in the course.

    Raises:
        ValueError: If the specified department is not found in the provided data.
    """
    # Ensure the department exists within the colleges dictionary
    colleges = data['colleges']  # Assigns the 'colleges' dictionary from the 'data' input to a variable named 'colleges'.
    department_courses = []  # Initializes an empty list named 'department_courses' to store the courses offered by the student's department.
    for college in colleges.values():  # Iterates through the values of the 'colleges' dictionary (which are dictionaries representing each college).
        for dept, courses in college["departments"].items():  # Iterates through the items (key-value pairs) of the 'departments' dictionary within each college.
            if dept == department:  # Checks if the current department name (key) matches the input 'department'.
                department_courses = courses  # If the department matches, assign the list of courses for that department to 'department_courses'.

    if not department_courses:  # Checks if 'department_courses' is empty, meaning the department was not found in the data.
        raise ValueError(f"Department {department} not found in colleges data.")  # If the department is not found, raise a ValueError with an informative message.

    # Safely sample courses, ensuring no over-sampling
    major_courses_count = min(32, len(department_courses))  # Determines the number of major courses to generate, limited to 32 or the total number of courses in the department, whichever is smaller.
    major_courses = random.sample(department_courses, major_courses_count)  # Randomly selects 'major_courses_count' courses from the 'department_courses' list and assigns them to 'major_courses'.

    # Get all other courses for minor, excluding the courses of the selected department
    other_courses = []  # Initializes an empty list named 'other_courses' to store courses from other departments (potential minor courses).
    for college in colleges.values():  # Iterates through the values of the 'colleges' dictionary (dictionaries representing each college).
        for dept, courses in college["departments"].items():  # Iterates through the items (key-value pairs) of the 'departments' dictionary within each college.
            if dept != department:  # Checks if the current department name (key) is not the same as the input 'department'.
                other_courses.extend(courses)  # If the department is different, extend the 'other_courses' list with the courses from that department.

    minor_courses_count = min(8, len(other_courses))  # Determines the number of minor courses to generate, limited to 8 or the total number of courses in 'other_courses', whichever is smaller.
    minor_courses = random.sample(other_courses, minor_courses_count)  # Randomly selects 'minor_courses_count' courses from the 'other_courses' list and assigns them to 'minor_courses'.

    all_courses = []  # Initializes an empty list named 'all_courses' to store all the generated courses for the student.
    # Determine the maximum number of terms based on the level
    max_term = 8 if level == 'U' else random.randint(4, 8) if level == 'G' else random.randint(6, 14)  # Determines the maximum number of terms based on the student's level ('U', 'G', or 'D').
    terms = list(range(1, max_term + 1))  # Creates a list of terms from 1 to the maximum term.

    # Generate major courses
    for _ in range(major_courses_count):  # Iterates 'major_courses_count' times to generate the specified number of major courses.
        term = random.choice(terms)  # Randomly selects a term from the 'terms' list for the current major course.
        course = major_courses.pop()  # Removes and assigns a course from the 'major_courses' list to the 'course' variable.
        course_id = course[:3].upper() + str(random.randint(100, 999))  # Generates a course ID by taking the first 3 letters of the course name, converting them to uppercase, and appending a random 3-digit number.
        all_courses.append([term, course, course_id, "Major", random.randint(1, 4), random.randint(75, 100)])  # Appends a list representing the course details to the 'all_courses' list.

    # Generate minor courses
    for _ in range(minor_courses_count):  # Iterates 'minor_courses_count' times to generate the specified number of minor courses.
        term = random.choice(terms)  # Randomly selects a term from the 'terms' list for the current minor course.
        course = minor_courses.pop()  # Removes and assigns a course from the 'minor_courses' list to the 'course' variable.
        course_id = course[:3].upper() + str(random.randint(100, 999))  # Generates a course ID by taking the first 3 letters of the course name, converting them to uppercase, and appending a random 3-digit number.
        all_courses.append([term, course, course_id, "Minor", random.randint(1, 4), random.randint(75, 100)])  # Appends a list representing the course details to the 'all_courses' list.

    return all_courses  # Returns the 'all_courses' list, which contains all the generated courses for the student.



# Generate student details and CSVs
def generate_student_details(data):  # Defines a function named 'generate_student_details' that takes a 'data' dictionary as input.
    """
    Generates student details and saves them to CSV files.

    This function creates a dataset of student details, including their names, IDs, 
    colleges, departments, levels, degrees, and courses. It then saves this data 
    to individual student CSV files (named after their student ID) and a master 
    'studentDetails.csv' file containing a summary of all students.

    Args:
        data (dict): A dictionary containing the university structure, sample names, and other data needed for student generation.
    """

    students = []  # Initializes an empty list named 'students' to store the details of each student.
    serial = 1  # Initializes a variable named 'serial' to 1, used for assigning serial numbers to students.

    student_count = 10  # Sets the number of students to generate to 10.

    for _ in range(student_count):  # Iterates 'student_count' times to generate the specified number of students.
        std_id = generate_student_id()  # Calls the 'generate_student_id' function to generate a unique student ID.
        name = generate_student_name(data)  # Calls the 'generate_student_name' function to generate a random student name using the provided data.
        college = random.choice(list(data['colleges'].keys()))  # Randomly selects a college from the keys of the 'colleges' dictionary in the 'data'.
        department = random.choice(list(data['colleges'][college]["departments"].keys()))  # Randomly selects a department from the keys of the 'departments' dictionary within the chosen college.

        # Randomly decide levels for the student
        levels = sorted(random.sample(["U", "G", "D"], k=random.randint(1, 3)))  # Randomly selects 1 to 3 academic levels ('U', 'G', 'D') for the student and sorts them.
        all_courses = []  # Initializes an empty list named 'all_courses' to store the courses for the current student.

        major_terms = {}  # Initializes an empty dictionary named 'major_terms' to store the terms in which major courses were taken.
        minor_terms = {}  # Initializes an empty dictionary named 'minor_terms' to store the terms in which minor courses were taken.
        minor_courses = []  # Initializes an empty list named 'minor_courses' to store the names of the minor courses taken by the student.

        for level in levels:  # Iterates through the selected academic levels for the current student.
            degree = generate_degree(level, department)  # Calls the 'generate_degree' function to determine the student's degree based on the current level and department.
            courses = generate_courses(level, department, data)  # Calls the 'generate_courses' function to generate a list of courses for the student based on their level, department, and the provided data.

            # Sort courses by term to ensure ordered terms in the CSV
            courses.sort(key=lambda x: x[0])  # Sorts the generated courses by their term number.

            # Group courses by degree in the final student data
            for course in courses:  # Iterates through the generated courses for the current level.
                term, course_name, course_id, course_type, credit_hours, grade = course  # Unpacks the course details from the current course list.
                if course_type == "Major":  # Checks if the course type is "Major".
                    major_terms[course_name] = term  # If it's a major course, store the term in which it was taken in the 'major_terms' dictionary.
                else:  # If the course type is not "Major" (it's "Minor").
                    minor_terms[course_name] = term  # Store the term in which the minor course was taken in the 'minor_terms' dictionary.
                    minor_courses.append(course_name)  # Add the name of the minor course to the 'minor_courses' list.

                all_courses.append([level, degree, term, course_name, course_id, course_type, credit_hours, grade])  # Appends the course details to the 'all_courses' list for the current student.

        # Save student courses in individual {stdID}.csv
        with open(f'{std_id}.csv', 'w', newline='', encoding='utf-8') as student_file:  # Opens a CSV file named after the student ID ('std_id') in write mode ('w'), with newline='' to prevent extra blank lines, and using UTF-8 encoding.
            writer = csv.writer(student_file)  # Creates a csv.writer object to write data to the CSV file.
            # Write headers for individual CSV
            writer.writerow(["Level", "Degree", "Term", "coursename", "courseID", "courseType", "credithours", "grade"])  # Writes the header row to the CSV file.
            writer.writerows(all_courses)  # Writes all the courses for the current student to the CSV file.

        # Add student courses to overall details
        for course in all_courses:  # Iterates through the 'all_courses' list for the current student.
            # Get the corresponding term for major and minor courses
            major_term = major_terms.get(course[3], "")  # Gets the term for the current course from the 'major_terms' dictionary, or an empty string if not found.
            minor_term = minor_terms.get(course[3], "")  # Gets the term for the current course from the 'minor_terms' dictionary, or an empty string if not found.

            # Minor field will be filled if the student has taken a minor course
            minor = course[3] if course[3] in minor_courses else ""  # Assigns the course name to 'minor' if it's in the 'minor_courses' list, otherwise assigns an empty string.

            # Now add to studentDetails with duplicate student data for each course
            students.append([serial, std_id, name, college, department,
                             course[0], course[1], course[3], minor, major_term, minor_term])  # Appends the student details and course information to the 'students' list.
            serial += 1  # Increments the 'serial' number by 1 for the next student or course entry.

    # Write all student details to a single studentDetails.csv
    with open('studentDetails.csv', 'w', newline='', encoding='utf-8') as file:  # Opens a CSV file named 'studentDetails.csv' in write mode ('w'), with newline='' to prevent extra blank lines, and using UTF-8 encoding.
        writer = csv.writer(file)  # Creates a csv.writer object to write data to the CSV file.
        writer.writerow([  # Writes the header row to the CSV file.
            "Serial", "stdID", "Name", "College", "Department", "Level",
            "Degree", "Major", "Minor", "Term of Major", "Term of Minor"
        ])  # End of the header row.
        writer.writerows(students)  # Writes all the student details from the 'students' list to the CSV file.

    print("All CSV files generated successfully!")  # Prints a message indicating that the CSV files have been generated successfully.


# Main execution block
if __name__ == "__main__":  # Checks if the script is being run as the main program (not imported as a module).
    data = get_data()  # Calls the 'get_data' function to retrieve the data needed for student generation and assigns it to the 'data' variable.
    generate_student_details(data)  # Calls the 'generate_student_details' function, passing the 'data' dictionary as input, to generate and save student details to CSV files.

