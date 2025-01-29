# This work done by group 6:
# Pasco Jeremy Lars C. , 202404675 (33.33%)
# Cosca Charlise Dorothy C. , 202401102 (33.33%)
# Santos Dianna Marie D. , 202403548(33.33%)
# Upano James Erik, (%)
import pandas as pd  # Imports the Pandas library for data manipulation and analysis (used for CSV files)
import datetime  # Imports the datetime module for working with dates and times (used for logging)
import time  # Imports the time module for introducing pauses in the program execution
import os  # Imports the os module for interacting with the operating system (e.g., checking file existence)
import csv  # Imports the csv module for reading and writing CSV files
import sys  # Imports the sys module for system-specific parameters and functions (potentially for exiting)
from datetime import datetime  # Imports the datetime class from the datetime module (for current date/time)


# Load student details from studentDetails.csv
def loadStudentDetails(stdID):
    """
    Loads student details from the studentDetails.csv file based on the provided student ID.

    Args:
        stdID (str): The student ID to search for.

    Returns:
        dict: A dictionary containing the student's details if found, otherwise None.
    """
    try:
        with open("studentDetails.csv", 'r') as file:  # Open the studentDetails.csv file in read mode
            reader = csv.DictReader(file)  # Create a DictReader object to read the CSV as dictionaries
            for row in reader:  # Iterate through each row (student) in the CSV
                if row['stdID'] == stdID:  # Check if the current row's stdID matches the provided stdID
                    return row  # If match found, return the row (student details)
    except FileNotFoundError:  # Handle the case where the studentDetails.csv file is not found
        print("studentDetails.csv not found.")  # Print an error message
    return None  # If file not found or student not found, return None


# Load student course data from {stdID}.csv
def loadStudentCourses(stdID):
    """
    Loads student course data from a CSV file named after the student ID.

    Args:
        stdID (str): The student ID used to find the course data file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a course.
    """
    courses = []  # Initialize an empty list to store course data
    try:
        with open(f"{stdID}.csv", 'r') as file:  # Open the student's CSV file in read mode
            reader = csv.DictReader(file)  # Create a DictReader object to read the CSV as dictionaries
            for row in reader:  # Iterate through each row (course) in the CSV
                courses.append(row)  # Append the current row (course data) to the courses list
    except FileNotFoundError:  # Handle the case where the student's CSV file is not found
        print(f"Courses file for {stdID} not found.")  # Print an error message
    return courses  # Return the list of courses


# Function to log the student's request to the previous requests file
def logPreviousRequest(session, stdID, request_type):
    """
    Logs the student's request to a file named after the student ID with "PreviousRequests" appended.

    Args:
        session (dict): A dictionary storing session information, including the request count.
        stdID (str): The student ID for whom the request is logged.
        request_type (str): The type of request made by the student.
    """
    session["request_count"] += 1  # Increment the request count in the session dictionary

    current_time = datetime.now()  # Get the current date and time
    formatted_date = current_time.strftime("%d/%m/%Y")  # Format the date as dd/mm/yyyy
    formatted_time = current_time.strftime("%I:%M %p")  # Format the time as hh:mm AM/PM

    filename = f"{stdID}PreviousRequests.txt"  # Create the filename for the previous requests file

    try:
        # Check if the file exists and is not empty, to avoid overwriting the header and line
        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

        # Open the file in append mode
        with open(filename, 'a') as file:  # Open the previous requests file in append mode
            if not file_exists:  # If the file is new (doesn't exist or is empty)
                header = "Request                    Date                        Time"  # Define the header
                line = "=" * len(header)  # Create a separator line with the same length as the header
                file.write(header + "\n")  # Write the header to the file
                file.write(line + "\n")  # Write the separator line to the file

            # Write the request info
            file.write(f"{request_type:<24}{formatted_date:<26}{formatted_time}\n")  # Write the request details

    except Exception as e:  # Handle any exceptions during file writing
        print(f"Error: Unable to write to file. {e}")  # Print an error message



# Start Feature
def startFeature(session):
    """
    Handles the initial setup process, including student level and ID validation.

    Args:
        session (dict): A dictionary to store session information.

    Returns:
        str: The validated student ID.
    """
    # Reset request count at the start of the
    session["request_count"] = 0  # Reset the request counter in the session dictionary
    print("Select student level: (U)ndergraduate, (G)raduate, or (B)oth Undergraduate and Graduate")  # Print level selection prompt
    level = input("Enter level: ").upper()  # Get user input for level and convert to uppercase

    # Check for valid initial selection
    if level not in ['U', 'G', 'B']:  # Check if the entered level is valid
        print("Invalid selection. Please try again.")  # Print an error message if invalid
        return startFeature(session)  # Call the function again to re-prompt the user

    # Ask for degree selection if G or B is selected
    if level in ['G', 'B']:  # If the level is Graduate or Both
        print("Select degree: (M)aster, (D)octorate, or (B0)oth Graduate and Doctorate")  # Print degree selection prompt
        degree = input("Enter degree: ").upper()  # Get user input for degree and convert to uppercase

        # Validate degree selection
        if degree not in ['M', 'D', 'B0']:  # Check if the entered degree is valid
            print("Invalid degree selection. Please try again.")  # Print an error message if invalid
            return startFeature(session)  # Call the function again to re-prompt the user

    # Ask for student ID
    stdID = input("Enter student ID (e.g., 202006000): ")  # Get user input for student ID
    student_details = loadStudentDetails(stdID)  # Load student details using the loadStudentDetails function

    if not student_details:  # Check if student details were found
        print("Invalid student ID. Please try again.")  # Print an error message if not found
        return startFeature(session)  # Call the function again to re-prompt the user

    # Load the student's CSV file and check if the level matches
    student_transcript = pd.read_csv(f"{stdID}.csv") # Read the student's CSV file using pandas
    student_levels = student_transcript["Level"].unique() if not student_transcript.empty else [] # Get unique levels from the transcript

    # Level validation based on the student's selected level
    if level == 'U':  # If the selected level is Undergraduate
        if 'U' not in student_levels: # Check if the student has Undergraduate level in their transcript
            print(f"Student {stdID} does not have the level 'U'. Please select the correct level.") # Print error if level not found
            return startFeature(session) # Re-prompt user
        elif len(student_levels) > 1:  # If other levels are detected (like G or D), deny the request
            print(f"Student {stdID} has other levels {', '.join(student_levels)} in addition to 'U'. Please select the correct level.") # Print error if other levels found
            return startFeature(session) # Re-prompt user

    elif level == 'G': # If the selected level is Graduate
        # If student selects G, they should have G or D or both
        if 'G' not in student_levels and 'D' not in student_levels:  # Check if student has Graduate or Doctorate levels in their transcript
            print(f"Student {stdID} does not have the level 'G' or 'D'. Please select the correct level.") # Print error if levels not found
            return startFeature(session)  # Re-prompt user

    elif level == 'B':  # If the selected level is Both
        # If student selects B, they must have U and G, U and D, or U, G, and D
        if not (('U' in student_levels and 'G' in student_levels) or ('U' in student_levels and 'D' in student_levels) or ('U' in student_levels and 'G' in student_levels and 'D' in student_levels)): # Check for valid combinations of levels for "Both"
            print(f"Student {stdID} must have the correct levels for 'B' (U and G, U and D, or U, G, D). They have {', '.join(student_levels)}.") # Print error if incorrect combination found
            return startFeature(session)  # Re-prompt user


    # If G or B is selected, check the degree selection
    if level in ['G', 'B']: # If the level is Graduate or Both
        if degree == 'M' and 'G' not in student_levels:  # Check if degree selection is consistent with transcript levels
            print(f"Student {stdID} is not a graduate student. They have {', '.join(student_levels)}.")  # Print error if inconsistent
            return startFeature(session)  # Re-prompt user
        elif degree == 'D' and 'D' not in student_levels:  # Check if degree selection is consistent with transcript levels
            print(f"Student {stdID} is not a doctorate student. They have {', '.join(student_levels)}.")  # Print error if inconsistent
            return startFeature(session)  # Re-prompt user
        elif degree == 'B0' and not ('G' in student_levels and 'D' in student_levels): # Check if degree selection is consistent with transcript levels
            print(f"Student {stdID} must have both 'G' and 'D' levels to select 'B0'. They have {', '.join(student_levels)}.") # Print error if inconsistent
            return startFeature(session) # Re-prompt user

    print(f"Student {stdID} found. Proceeding to menu...") # Print success message
    time.sleep(2) # Pause for 2 seconds
    menuFeature(session, stdID)  # Call the menuFeature function to display the menu





# Menu Feature
def menuFeature(session, stdID):
    """
    Displays the menu and handles user choices.
    Tracks the number of requests in the session dictionary.

    Args:
        session (dict): Dictionary to manage session, including request count.
        stdID (str): Student ID.
    """
    print("Student Transcript Generation System")  # Print the system title
    print("=" * 40)  # Print a separator line
    print("1. Details Feature")  # Print menu option 1
    print("2. Statistics Feature")  # Print menu option 2
    print("3. Major Transcript Feature")  # Print menu option 3
    print("4. Minor Transcript Feature")  # Print menu option 4
    print("5. Full Transcript Feature")  # Print menu option 5
    print("6. Previous Requests Feature")  # Print menu option 6
    print("7. New Student Feature")  # Print menu option 7
    print("8. Terminate Feature")  # Print menu option 8
    print("=" * 40)  # Print a separator line

    choice = input("Enter Your Feature: ")  # Get user input for their choice

    if choice == '1':  # If the choice is 1
        logPreviousRequest(session, stdID, "Details")  # Log the request
        detailsFeature(stdID)  # Call the detailsFeature function
    elif choice == '2':  # If the choice is 2
        logPreviousRequest(session, stdID, "Statistics")  # Log the request
        statisticsFeature(stdID)  # Call the statisticsFeature function
    elif choice == '3':  # If the choice is 3
        logPreviousRequest(session, stdID, "Major")  # Log the request
        majorTranscriptFeature(stdID)  # Call the majorTranscriptFeature function
    elif choice == '4':  # If the choice is 4
        logPreviousRequest(session, stdID, "Minor")  # Log the request
        minorTranscriptFeature(stdID)  # Call the minorTranscriptFeature function
    elif choice == '5':  # If the choice is 5
        logPreviousRequest(session, stdID, "Full")  # Log the request
        fullTranscriptFeature(stdID)  # Call the fullTranscriptFeature function
    elif choice == '6':  # If the choice is 6
        previousRequestsFeature(stdID)  # Call the previousRequestsFeature function
    elif choice == '7':  # If the choice is 7
        newStudentFeature(session, stdID)  # Call the newStudentFeature function
    elif choice == '8':  # If the choice is 8
        terminateFeature(session)  # Call the terminateFeature function
    else:  # If the choice is invalid
        print("Invalid option. Please try again.")  # Print an error message
        time.sleep(2)  # Pause for 2 seconds
        menuFeature(session, stdID)  # Call the menuFeature function again to re-prompt the user


# Details Feature
def detailsFeature(stdID):
    """
    Displays and saves student details to a file.

    Args:
        stdID (str): The student ID.
    """
    print()  # Print a blank line

    # Load basic student details
    student_details = loadStudentDetails(stdID)  # Load student details using the loadStudentDetails function

    # Initialize variables
    total_terms = 0  # Initialize total terms to 0
    all_levels = set()  # Initialize an empty set to store all levels
    all_colleges = set()  # Initialize an empty set to store all colleges
    all_departments = set()  # Initialize an empty set to store all departments

    # Read the main studentDetails.csv to gather general information
    try:
        with open("studentDetails.csv", 'r') as file:  # Open the studentDetails.csv file in read mode
            reader = csv.DictReader(file)  # Create a DictReader object to read the CSV as dictionaries
            for row in reader:  # Iterate through each row (student) in the CSV
                if row['stdID'] == stdID:  # Check if the current row's stdID matches the provided stdID
                    all_levels.add(row['Level'])  # Add the level to the all_levels set
                    all_colleges.add(row['College'])  # Add the college to the all_colleges set
                    all_departments.add(row['Department'])  # Add the department to the all_departments set
    except FileNotFoundError:  # Handle the case where the studentDetails.csv file is not found
        print("Error: studentDetails.csv not found.")  # Print an error message
        return  # Exit the function

    # Read the {stdID}.csv file to calculate terms
    try:
        with open(f"{stdID}.csv", 'r') as file:  # Open the student's CSV file in read mode
            reader = csv.DictReader(file)  # Create a DictReader object to read the CSV as dictionaries
            degree_max_terms = {}  # Create a dictionary to store the maximum term for each degree

            for row in reader:  # Iterate through each row (course) in the CSV
                degree = row['Degree']  # Get the degree from the current row
                term = int(row['Term']) if row['Term'] else 0  # Get the term from the current row, convert to int

                # Update max term for this degree
                if degree in degree_max_terms:  # If the degree is already in the dictionary
                    degree_max_terms[degree] = max(degree_max_terms[degree], term)  # Update the maximum term if the current term is higher
                else:  # If the degree is not in the dictionary
                    degree_max_terms[degree] = term  # Add the degree and its term to the dictionary

            # Sum the max terms across all degrees
            total_terms = sum(degree_max_terms.values())  # Calculate the total terms by summing the maximum terms for each degree

    except FileNotFoundError:  # Handle the case where the student's CSV file is not found
        print(f"Error: File {stdID}.csv not found.")  # Print an error message
        return  # Exit the function

    if student_details:  # If student details were found
        # Display details
        print(f"Details for student {stdID}:")  # Print a header for the details
        print(f"Name: {student_details['Name']}")  # Print the student's name
        print(f"Level(s): {', '.join(all_levels)}")  # Print the student's level(s)
        print(f"Number of Terms: {total_terms}")  # Print the total number of terms
        print(f"College(s): {', '.join(all_colleges)}")  # Print the student's college(s)
        print(f"Department(s): {', '.join(all_departments)}")  # Print the student's department(s)

        # Save to file
        with open(f"{stdID}details.txt", 'w') as file:  # Open a file to save the details
            file.write(f"Details for student {stdID}:\n")  # Write a header to the file
            file.write(f"Name: {student_details['Name']}\n")  # Write the student's name to the file
            file.write(f"Level(s): {', '.join(all_levels)}\n")  # Write the student's level(s) to the file
            file.write(f"Number of Terms: {total_terms}\n")  # Write the total number of terms to the file
            file.write(f"College(s): {', '.join(all_colleges)}\n")  # Write the student's college(s) to the file
            file.write(f"Department(s): {', '.join(all_departments)}\n")  # Write the student's department(s) to the file
    time.sleep(2)
    menuFeature(session, stdID)



# Statistics Feature
def statisticsFeature(stdID):
    """
    Calculates and displays student statistics, saving them to a file.

    Args:
        stdID (str): The student ID.
    """
    # File names
    input_file = f"{stdID}.csv"  # Define the input file name
    output_file = f"{stdID}statistics.txt"  # Define the output file name

    try:
        # Read the CSV file
        data = pd.read_csv(input_file)  # Read the CSV file using pandas

        # Validate required columns
        if not {'Level', 'Term', 'grade'}.issubset(data.columns):  # Check if the required columns are present
            raise ValueError("The CSV file must contain 'Level', 'Term', and 'grade' columns.")  # Raise an error if columns are missing

        # Define level names
        levels_map = {  # Define a dictionary to map level codes to level names
            'U': "Undergraduate Level",
            'G': "Graduate (M) Level",
            'D': "Graduate (D) Level"
        }

        # Adjust header line length
        header_line = "=" * 60  # Define a header line
        asterisk = "*" * 14 # Define an asterisk line

        # Open the output file for writing
        with open(output_file, 'w') as file:  # Open the output file in write mode
            for level, level_name in levels_map.items():  # Iterate through the levels and their names
                # Filter data for the current level
                level_data = data[data['Level'] == level]  # Filter the data for the current level

                if not level_data.empty:  # If there is data for the current level
                    # Calculate overall and per-term statistics
                    overall_avg = level_data['grade'].mean()  # Calculate the overall average grade
                    per_term_avg = level_data.groupby('Term')['grade'].mean()  # Calculate the average grade per term

                    # Identify min/max grades and their terms
                    min_grade = level_data['grade'].min()  # Find the minimum grade
                    min_terms = level_data[level_data['grade'] == min_grade]['Term'].unique()  # Find the terms with the minimum grade
                    max_grade = level_data['grade'].max()  # Find the maximum grade
                    max_terms = level_data[level_data['grade'] == max_grade]['Term'].unique()  # Find the terms with the maximum grade

                    # Check for repeated courses
                    repeated_courses = level_data.duplicated(subset=['Term']).any()  # Check for repeated courses in the same term

                    # Write the statistics in the specified format
                    file.write(f"{header_line}\n")  # Write the header line to the file
                    file.write(f"{asterisk}{level_name.center(32)}{asterisk}\n") # Write the level name with asterisks to the file
                    file.write(f"{header_line}\n")  # Write the header line to the file
                    file.write(f"Overall average (major and minor) for all terms:\n") # Write overall average label to the file
                    for term, avg in per_term_avg.items(): # Iterate through the terms and their average grades
                        file.write(f"\tTerm {term}: {avg:.2f}\n") # Write the term and its average grade to the file
                    file.write("\n") # Write a newline to the file
                    file.write(f"Minimum grade(s): {min_grade} in term(s): {', '.join(map(str, min_terms))}\n")  # Write the minimum grade and its terms to the file
                    file.write(f"Maximum grade(s): {max_grade} in term(s): {', '.join(map(str, max_terms))}\n") # Write the maximum grade and its terms to the file
                    file.write(f"Do you have any repeated course(s)? {'Yes' if repeated_courses else 'No'}\n\n")  # Write information about repeated courses to the file

        with open(output_file, 'r') as file: # Open the output file in read mode
            print("\nGenerated Statistics:\n")  # Print a header for the statistics
            print(file.read())  # Print the content of the statistics file

    except FileNotFoundError:  # Handle the case where the input file is not found
        print(f"File '{input_file}' not found.")  # Print an error message
    except Exception as e: # Handle any other exceptions
        print(f"An error occurred: {e}")  # Print an error message
    time.sleep(2) # Pause for 2 seconds
    menuFeature(session, stdID)  # Call the menuFeature function to display the menu


# Major Transcript Feature
def majorTranscriptFeature(stdID):
    """
    Generates and displays the major transcript for a student, saving it to a file.

    Args:
        stdID (str): The student ID.
    """
    try:
        # Load data
        student_details = pd.read_csv("studentDetails.csv")  # Read the student details CSV file
        student_transcript = pd.read_csv(f"{stdID}.csv")  # Read the student's transcript CSV file
        student_transcript["Level"] = student_transcript["Level"].str.strip()  # Remove leading/trailing spaces from the "Level" column
        student_transcript["Level"] = student_transcript["Level"].str.replace(r"\s+", " ", regex=True)  # Normalize spaces in the "Level" column
        student_transcript["Level"] = student_transcript["Level"].fillna("")  # Replace NaN values with empty strings in the "Level" column

        # Debug: Check unique levels
        print("Unique levels in the data:", student_transcript["Level"].unique())  # Print the unique levels in the transcript

        # Map levels for display
        level_map = {"U": "U", "G": "M", "D": "D"}  # Define a dictionary to map level codes to display values
        levels_order = ["U", "G", "D"]  # Ensure levels are in order
        # Check if student exists in studentDetails.csv
        student_row = student_details[student_details["stdID"] == int(stdID)]  # Find the row for the student in the student details DataFrame
        if student_row.empty:  # If the student is not found
            raise ValueError(f"Student with ID {stdID} not found in 'studentDetails.csv'.")  # Raise a ValueError

        # Extract student info
        student_info = student_row.iloc[0]  # Get the first row (student info) as a Series
        name = student_info["Name"]  # Extract the student's name
        college = student_info["College"]  # Extract the student's college
        department = student_info["Department"]  # Extract the student's department
        degree_max_terms = {'U': 0, 'G': 0, 'D': 0}  # Initialize a dictionary to store the maximum term for each degree

        # Process each row in the transcript
        for index, row in student_transcript.iterrows():  # Iterate through the rows of the student's transcript DataFrame
            level = row["Level"]  # Get the level from the current row
            term = int(row["Term"]) if pd.notna(row["Term"]) else 0  # Get the term from the current row, convert to int if not NaN

            # Update max term for each degree
            if level in degree_max_terms:  # If the level is in the degree_max_terms dictionary
                degree_max_terms[level] = max(degree_max_terms[level], term)  # Update the maximum term for the level if the current term is higher

        # Total terms is the sum of the highest terms per degree
        total_terms = degree_max_terms['U'] + degree_max_terms['G'] + degree_max_terms['D']  # Calculate the total terms

        # Filter transcript data and sort by level and term
        sorted_transcript_data = student_transcript.sort_values(by=["Level", "Term"])  # Sort the transcript data by level and term

        # Prepare header
        header_line = "=" * 70  # Define a header line
        asterisk = "*" * 14  # Define an asterisk line

        # Count major courses only
        major_count = (sorted_transcript_data["courseType"] == "Major").sum()  # Count the number of major courses

        # Start building transcript content
        output = []  # Initialize an empty list to store the transcript content
        output.append(header_line)  # Append the header line
        output.append(f"Name: {name:<30}   stdID: {stdID}")  # Append the student's name and ID
        output.append(f"College: {college:<30}Department: {department}")  # Append the student's college and department
        output.append(f"Major: {major_count:<30}")  # Append the number of major courses
        output.append(f"Level: {', '.join([k for k in degree_max_terms if degree_max_terms[k] > 0]):<30}  Number of terms: {total_terms}")  # Append the level(s) and total terms
        output.append(header_line)  # Append the header line

        # Process each level and term
        for level in levels_order:  # Iterate through the levels in order
            level_data = sorted_transcript_data[sorted_transcript_data["Level"] == level]  # Filter data for the current level
            if not level_data.empty:  # If there is data for the current level
                for term in sorted(level_data["Term"].unique()):  # Iterate through the terms for the current level
                    term_data = level_data[level_data["Term"] == term]  # Filter data for the current term

                    output.append(f"{asterisk}{f'Term {term}'.center(42)}{asterisk}")  # Append the term header
                    output.append(header_line)  # Append the header line
                    output.append(f"{'Course ID':<15} {'Course Name':<30} {'Credit Hours':<15} {'Grade'}")  # Append the course header

                    for _, row in term_data.iterrows():  # Iterate through the rows for the current term
                        output.append(f"{row['courseID']:<15} {row['coursename']:<30} {row['credithours']:<15} {row['grade']}")  # Append the course information

                    # Calculate averages (Major only)
                    major_avg = term_data[term_data["courseType"] == "Major"]["grade"].mean()  # Calculate the average grade for major courses in the current term
                    term_avg = term_data["grade"].mean()  # Calculate the average grade for all courses in the current term
                    overall_avg = level_data["grade"].mean()  # Calculate the overall average grade for the current level

                    major_avg_str = f"{major_avg:.2f}" if not pd.isna(major_avg) else ""  # Format the major average, handling NaN values
                    term_avg_str = f"{term_avg:.2f}" if not pd.isna(term_avg) else ""  # Format the term average, handling NaN values

                    output.append(f"Major Average: {major_avg_str:<20} Overall Average: {overall_avg:.2f}")  # Append the averages
                    output.append(header_line)  # Append the header line

                # End of level section
                output.append(f"{asterisk}{f'End of Transcript for Level ({level_map[level]})'.center(32)}{asterisk}")  # Append the end of level section
                output.append(header_line)  # Append the header line

        # Write to file
        transcript_filename = f"{stdID}MajorTranscript.txt"  # Define the transcript filename
        with open(transcript_filename, "w") as file:  # Open the transcript file in write mode
            file.write("\n".join(output))  # Write the transcript content to the file

        print(f"Major Transcript successfully generated: {transcript_filename}")  # Print a success message
        with open(f"{stdID}MajorTranscript.txt", 'r') as file:  # Open the transcript file in read mode
            print(file.read())  # Print the content of the transcript file

    except FileNotFoundError as e:  # Handle FileNotFoundError
        print(f"Error: {e}")  # Print the error message
    except ValueError as e:  # Handle ValueError
        print(f"Error: {e}")  # Print the error message
    except Exception as e:  # Handle other exceptions
        print(f"Unexpected error: {e}")  # Print the error message
    time.sleep(2)  # Pause for 2 seconds
    menuFeature(session, stdID)  # Call the menuFeature function

# Minor Transcript Feature
def minorTranscriptFeature(stdID):
    """
    Generates and displays the minor transcript for a student, saving it to a file.

    Args:
        stdID (str): The student ID.
    """
    try:
        # Load data
        student_details = pd.read_csv("studentDetails.csv")  # Load student details from the CSV file.
        student_transcript = pd.read_csv(f"{stdID}.csv")  # Load student transcript data from the CSV file.
        student_transcript["Level"] = student_transcript["Level"].str.strip()  # Remove leading/trailing spaces from the "Level" column.
        student_transcript["Level"] = student_transcript["Level"].str.replace(r"\s+", " ", regex=True)  # Normalize spaces in the "Level" column.
        student_transcript["Level"] = student_transcript["Level"].fillna("")  # Replace NaN values with empty strings in the "Level" column.

        # Debug: Check unique levels
        print("Unique levels in the data:", student_transcript["Level"].unique())  # Print unique levels for debugging purposes.

        # Map levels for display
        level_map = {"U": "U", "G": "M", "D": "D"}  # Map level codes to display values.
        levels_order = ["U", "G", "D"]  # Define the order of levels for display.

        # Check if student exists in studentDetails.csv
        student_row = student_details[student_details["stdID"] == int(stdID)]  # Find the row for the student in the details DataFrame.
        if student_row.empty:  # Check if the student row is empty (student not found).
            raise ValueError(f"Student with ID {stdID} not found in 'studentDetails.csv'.")  # Raise an error if the student is not found.

        # Extract student info
        student_info = student_row.iloc[0]  # Get the first row (student info) as a Series.
        name = student_info["Name"]  # Extract the student's name.
        college = student_info["College"]  # Extract the student's college.
        department = student_info["Department"]  # Extract the student's department.
        degree_max_terms = {'U': 0, 'G': 0, 'D': 0}  # Initialize a dictionary to store the maximum term for each degree.

        # Process each row in the transcript
        for index, row in student_transcript.iterrows():  # Iterate through the rows of the student's transcript DataFrame.
            level = row["Level"]  # Get the level from the current row.
            term = int(row["Term"]) if pd.notna(row["Term"]) else 0  # Get the term, convert to int if not NaN.

            # Update max term for each degree
            if level in degree_max_terms:  # Check if the level is in the degree_max_terms dictionary.
                degree_max_terms[level] = max(degree_max_terms[level], term)  # Update the maximum term for the level.

        # Total terms is the sum of the highest terms per degree
        total_terms = degree_max_terms['U'] + degree_max_terms['G'] + degree_max_terms['D']  # Calculate the total terms.

        # Filter transcript data and sort by level and term
        sorted_transcript_data = student_transcript.sort_values(by=["Level", "Term"])  # Sort the transcript data by level and term.

        # Prepare header
        header_line = "=" * 70  # Define a header line.
        asterisk = "*" * 14  # Define an asterisk line.

        # Count minor courses only
        minor_count = (sorted_transcript_data["courseType"] == "Minor").sum()  # Count the number of minor courses.

        # Start building transcript content
        output = []  # Initialize an empty list to store the transcript content.
        output.append(header_line)  # Append the header line.
        output.append(f"Name: {name:<30}   stdID: {stdID}")  # Append the student's name and ID.
        output.append(f"College: {college:<30}Department: {department}")  # Append the student's college and department.
        output.append(f"Minor: {minor_count:<30}")  # Append the number of minor courses.
        output.append(f"Level: {', '.join([k for k in degree_max_terms if degree_max_terms[k] > 0]):<30}  Number of terms: {total_terms}")  # Append the level(s) and total terms.
        output.append(header_line)  # Append the header line.

        # Process each level and term
        for level in levels_order:  # Iterate through the levels in order.
            level_data = sorted_transcript_data[sorted_transcript_data["Level"] == level]  # Filter data for the current level.
            if not level_data.empty:  # Check if there is data for the current level.
                for term in sorted(level_data["Term"].unique()):  # Iterate through the terms for the current level.
                    term_data = level_data[level_data["Term"] == term]  # Filter data for the current term.

                    # Filter for minor courses only
                    term_data_minor = term_data[term_data["courseType"] == "Minor"]  # Filter data for minor courses in the current term.

                    if not term_data_minor.empty:  # Only print term if there are minor courses.
                        output.append(f"{asterisk}{f'Term {term}'.center(42)}{asterisk}")  # Append the term header.
                        output.append(header_line)  # Append the header line.
                        output.append(f"{'Course ID':<15} {'Course Name':<30} {'Credit Hours':<15} {'Grade'}")  # Append the course header.

                        for _, row in term_data_minor.iterrows():  # Iterate through the rows for the current term.
                            output.append(f"{row['courseID']:<15} {row['coursename']:<30} {row['credithours']:<15} {row['grade']}")  # Append the course information.

                        # Calculate averages (Minor only)
                        minor_avg = term_data_minor["grade"].mean()  # Calculate the average grade for minor courses in the current term.
                        overall_avg = level_data[level_data["courseType"] == "Minor"]["grade"].mean()  # Calculate the overall average grade for minor courses in the current level.

                        minor_avg_str = f"{minor_avg:.2f}" if not pd.isna(minor_avg) else ""  # Format the minor average, handling NaN values.

                        output.append(f"Minor Average: {minor_avg_str:<20} Overall Average: {overall_avg:.2f}")  # Append the averages.
                        output.append(header_line)  # Append the header line.

                # End of level section
                output.append(f"{asterisk}{f'End of Transcript for Level ({level_map[level]})'.center(32)}{asterisk}")  # Append the end of level section.
                output.append(header_line)  # Append the header line.

        # Write to file
        transcript_filename = f"{stdID}MinorTranscript.txt"  # Define the transcript filename.
        with open(transcript_filename, "w") as file:  # Open the transcript file in write mode.
            file.write("\n".join(output))  # Write the transcript content to the file.

        print(f"Minor Transcript successfully generated: {transcript_filename}")  # Print a success message.
        with open(f"{stdID}MinorTranscript.txt", 'r') as file:  # Open the transcript file in read mode.
            print(file.read())  # Print the content of the transcript file.

    except FileNotFoundError as e:  # Handle FileNotFoundError.
        print(f"Error: {e}")  # Print the error message.
    except ValueError as e:  # Handle ValueError.
        print(f"Error: {e}")  # Print the error message.
    except Exception as e:  # Handle other exceptions.
        print(f"Unexpected error: {e}")  # Print the error message.
    time.sleep(2)  # Pause for 2 seconds.
    menuFeature(session, stdID)  # Call the menuFeature function.


# Full Transcript Feature
def fullTranscriptFeature(stdID):
    """
    Generates and displays the full transcript for a student, saving it to a file.

    Args:
        stdID (str): The student ID.
    """
    try:
        # Load data 
        student_details = pd.read_csv("studentDetails.csv")  # Load student details from CSV.
        student_transcript = pd.read_csv(f"{stdID}.csv")  # Load student transcript from CSV.
        student_transcript["Level"] = student_transcript["Level"].str.strip()  # Remove leading/trailing spaces from "Level" column.
        student_transcript["Level"] = student_transcript["Level"].str.replace(r"\s+", " ", regex=True)  # Normalize spaces in "Level" column.
        student_transcript["Level"] = student_transcript["Level"].fillna("")  # Replace NaN values with empty strings in "Level" column.

        # Debug: Check unique levels
        print("Unique levels in the data:", student_transcript["Level"].unique())  # Print unique levels for debugging.

        # Map levels for display
        level_map = {"U": "U", "G": "M", "D": "D"}  # Map level codes to display values.
        levels_order = ["U", "G", "D"]  # Define the order of levels for display.

        # Check if student exists in studentDetails.csv
        student_row = student_details[student_details["stdID"] == int(stdID)]  # Find the row for the student in the details DataFrame.
        if student_row.empty:  # Check if the student row is empty (student not found).
            raise ValueError(f"Student with ID {stdID} not found in 'studentDetails.csv'.")  # Raise an error if student is not found.

        # Extract student info
        student_info = student_row.iloc[0]  # Get the first row (student info) as a Series.
        name = student_info["Name"]  # Extract the student's name.
        college = student_info["College"]  # Extract the student's college.
        department = student_info["Department"]  # Extract the student's department.
        degree_max_terms = {'U': 0, 'G': 0, 'D': 0}  # Initialize a dictionary to store the maximum term for each degree.

        # Process each row in the transcript
        for index, row in student_transcript.iterrows():  # Iterate through the rows of the student's transcript DataFrame.
            level = row["Level"]  # Get the level from the current row.
            term = int(row["Term"]) if pd.notna(row["Term"]) else 0  # Get the term, convert to int if not NaN.

            # Update max term for each degree
            if level in degree_max_terms:  # Check if the level is in the degree_max_terms dictionary.
                degree_max_terms[level] = max(degree_max_terms[level], term)  # Update the maximum term for the level.

        # Total terms is the sum of the highest terms per degree
        total_terms = degree_max_terms['U'] + degree_max_terms['G'] + degree_max_terms['D']  # Calculate the total terms.

        # Filter transcript data and sort by level and term
        sorted_transcript_data = student_transcript.sort_values(by=["Level", "Term"])  # Sort the transcript data by level and term.

        # Prepare header
        header_line = "=" * 70  # Define a header line.
        asterisk = "*" * 14  # Define an asterisk line.

        # Start building transcript content
        output = []  # Initialize an empty list to store the transcript content.
        output.append(header_line)  # Append the header line.
        output.append(f"Name: {name:<30}   stdID: {stdID}")  # Append the student's name and ID.
        output.append(f"College: {college:<30}Department: {department}")  # Append the student's college and department.
        output.append(f"Level: {', '.join([k for k in degree_max_terms if degree_max_terms[k] > 0]):<30}  Number of terms: {total_terms}")  # Append the level(s) and total terms.
        output.append(header_line)  # Append the header line.

        # Process each level and term
        for level in levels_order:  # Iterate through the levels in order.
            level_data = sorted_transcript_data[sorted_transcript_data["Level"] == level]  # Filter data for the current level.
            if not level_data.empty:  # Check if there is data for the current level.
                for term in sorted(level_data["Term"].unique()):  # Iterate through the terms for the current level.
                    term_data = level_data[level_data["Term"] == term]  # Filter data for the current term.

                    output.append(f"{asterisk}{f'Term {term}'.center(42)}{asterisk}")  # Append the term header.
                    output.append(header_line)  # Append the header line.
                    output.append(f"{'Course ID':<15} {'Course Name':<30} {'Credit Hours':<15} {'Grade'}")  # Append the course header.

                    for _, row in term_data.iterrows():  # Iterate through the rows for the current term.
                        output.append(f"{row['courseID']:<15} {row['coursename']:<30} {row['credithours']:<15} {row['grade']}")  # Append the course information.

                    # Calculate averages for the term (all courses)
                    term_avg = term_data["grade"].mean()  # Calculate the average grade for all courses in the current term.
                    overall_avg = level_data["grade"].mean()  # Calculate the overall average grade for the current level.

                    term_avg_str = f"{term_avg:.2f}" if not pd.isna(term_avg) else ""  # Format the term average, handling NaN values.

                    output.append(f"Term Average: {term_avg_str:<20} Overall Average: {overall_avg:.2f}")  # Append the averages.
                    output.append(header_line)  # Append the header line.

                # End of level section
                output.append(f"{asterisk}{f'End of Transcript for Level ({level_map[level]})'.center(32)}{asterisk}")  # Append the end of level section.
                output.append(header_line)  # Append the header line.

        # Write to file
        transcript_filename = f"{stdID}FullTranscript.txt"  # Define the transcript filename.
        with open(transcript_filename, "w") as file:  # Open the transcript file in write mode.
            file.write("\n".join(output))  # Write the transcript content to the file.

        print(f"Full Transcript successfully generated: {transcript_filename}")  # Print a success message.
        with open(f"{stdID}FullTranscript.txt", 'r') as file:  # Open the transcript file in read mode.
            print(file.read())  # Print the content of the transcript file.

    except FileNotFoundError as e:  # Handle FileNotFoundError.
        print(f"Error: {e}")  # Print the error message.
    except ValueError as e:  # Handle ValueError.
        print(f"Error: {e}")  # Print the error message.
    except Exception as e:  # Handle other exceptions.
        print(f"Unexpected error: {e}")  # Print the error message.
    time.sleep(2)  # Pause for 2 seconds.
    menuFeature(session, stdID)  # Call the menuFeature function.


# Previous Requests Feature
def previousRequestsFeature(stdID):
    """
    Displays the previous requests of a student with a header and separator.

    Args:
        stdID (str): The student ID.
    """
    filename = f"{stdID}PreviousRequests.txt"  # Create the filename using the student ID.
    header = "Request                    Date                        Time"  # Define the header string.
    line = "=" * len(header)  # Create a separator line with the same length as the header.

    try:
        # Check if the file exists and read the requests
        if os.path.exists(filename) and os.path.getsize(filename) > 0:  # Check if the file exists and is not empty.
            with open(filename, 'r') as file:  # Open the file in read mode.
                requests = file.readlines()  # Read all lines from the file and store them in a list.

            # Write header and line to the console
            print(header)  # Print the header.
            print(line)  # Print the separator line.

            # Display each request from the file in the correct format
            for request in requests[2:]:  # Iterate through the requests, skipping the header and separator lines.
                print(request.strip())  # Print each request, removing leading/trailing whitespace.

        else:
            print(f"No previous requests found for student ID {stdID}.")  # Print a message if no previous requests are found.

    except Exception as e:  # Handle any exceptions that might occur.
        print(f"An error occurred: {e}")  # Print the error message.

    # Clear screen and redirect to the menu after a delay
    time.sleep(2)  # Pause for 2 seconds.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen (Windows or other OS).
    menuFeature(session, stdID)  # Call the menuFeature function to return to the main menu.


# New Student Feature
def newStudentFeature(session, stdID):
    """
    Resets the system for a new student and starts a new session.

    Args:
        session (dict): The current session dictionary.
        stdID (str): The ID of the previous student (used for the message).
    """
    session["request_count"] = 0  # Resets the request count for the new student's session.
    print(f"Student {stdID} finished the session, deleting all previous data.....")  # Prints a message indicating the previous session is ending.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen (works on Windows, Linux, and macOS).
    print("Hello! New Student!")  # Prints a welcome message for the new student.
    time.sleep(2)  # Pauses for 2 seconds to give the user time to read the messages.
    startFeature(session)  # Calls the startFeature function to begin the setup process for the new student.

# Terminate Feature
def terminateFeature(session):
    """
    Terminates the program and displays the total number of requests made during the session.

    Args:
        session (dict): A dictionary containing session information, including the request count.
    """
    try:
        # Display the total number of requests made during this session
        print(f"Total number of requests made during this session: {session['request_count']}")  # Print the total request count from the session dictionary.
    except Exception as e:  # Handle any exceptions that might occur.
        print(f"An error occurred: {e}")  # Print the error message.
    finally:  # This block is always executed, regardless of whether an exception occurred or not.
        print("Terminating the program. Goodbye!")  # Print a termination message.
        sys.exit()  # Exit the program.


if __name__ == "__main__":# This block is the entry point of the program. It is executed when the script is run directly (not imported as a module).
    # Initialize the session dictionary
    session = {"request_count": 0}  # Create a dictionary to store session information, starting with a request count of 0.
    # Start the menu loop
    stdID = startFeature(session)  # Call startFeature to get the student ID and initialize the session.
    while True:  # Enter an infinite loop to keep the program running until terminated.
        menuFeature(session, stdID)  # Call menuFeature to display the menu and handle user choices.