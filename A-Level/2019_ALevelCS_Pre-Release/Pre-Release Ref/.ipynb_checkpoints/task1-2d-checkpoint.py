size_of_class = 3
student_data = []

for x in range(size_of_class):
    name = input("What their name? ")
    email = input("What their email? ")
    dob = input("What is their DoB? ")
    student_id = input("What is their Student ID? ")

    student_data.append([name,email,dob,student_id])


# Add empty elements for testing purposes
student_data.append([])
student_data.append([])
student_data.append([])

print("Student Name,Email Address,Date of Birth, Student ID")

for y in range(size_of_class):

    # 1.2 - Ensure empty elements are not output
    if len(student_data[y]) > 0: # Only output if data is present
        print(student_data[y][0] + "," + student_data[y][1] + "," + student_data[y][2] + "," + student_data[y][3])

# 1.3 - Allow the user to search the array for a name
# 1.4 - Allow the user to serach for part of a name and return multiple results
search_term = input("Who are you looking for? ")
results = []

for z in range(size_of_class):
    if search_term in student_data[z][0]: # Search only the name of the student records
        results.append(student_data[z])

print(str(len(results)) + " record(s) found")
print("Student Name,Email Address,Date of Birth,Student ID")
for n in range(len(results)):
    print(results[n][0] + "," + results[n][1] + "," + results[n][2] + "," + results[n][3])
