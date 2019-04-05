# Task 1.1
# Input student data in the format <student_name>#<email_address>

# Task 1.2
# Find if there are empty arrays in student data and do not output this

# Task 1.3
# Allow the user to search the array by name and return the name and email

size_of_class = 3

# 1.1(1) - declare the array
student_data = []

# 1.1(5) repeat steps 2-4 for all students in the class
for x in range(size_of_class):
    # 1.1(2) - prompt for the name and email address
    name = input("What is your name? ")
    email = input("What is your email? ")

    # 1.1(3) - Put the string into the correct format
    formatted_data = name  + "#" + email

    # 1.1(4) - Add the element to the array
    student_data.append(formatted_data)


# 1.2 - Add empty elements for testing purposes
student_data.append("")
student_data.append("")
student_data.append("")
print(student_data)

# 1.1(6) - Output student data in a sensible format (CSV format)
print("Student Name,Email Address")

for y in range(size_of_class):

    # 1.2 - Ensure empty elements are not output
    if len(student_data[y]) > 0: # Only output if data is present
        single_student = student_data[y].split("#")
        print(single_student[0] + "," + single_student[1])

# 1.3 - Allow the user to search the array for a name
# 1.4 - Allow the user to serach for part of a name and return multiple results
search_term = input("Who are you looking for? ")
results = []

for z in range(size_of_class):
    single_student = student_data[z].split("#")
    if search_term in single_student[0]: # Search only the name of the student records
        results.append(single_student)

print(str(len(results)) + " record(s) found")
print("Student Name,Email Address")
for n in range(len(results)):
    print(results[n][0] + "," + results[n][1])
