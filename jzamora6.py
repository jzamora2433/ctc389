#Josue Zamora
#lab 6

student = ["Naomi", "Johnathan", "Jesse", "Analicia","Ruby"] 

for i in student:
    print (i)

print("please select one of the following:")
print("option 1: Add a student")
print("option 2: Modify a student name")
print("option 3: Remove a student")

option = input("Enter your option number 1,2,3: ")

if option == "1":
    addname = input("enter a students name: ")
    student.append(addname)

    for i in student:
        print(i)
elif option == "2":
    print("0", student[0])
    print("1", student[1])
    print("2", student[2])
    print("3", student[3])
    print("4", student[4])

    x = int(input("give me a index number you want to modify: "))
    y = input("what is the name you want to modify it to: ")
    student[x] = y

    print("New List")
    for i in student:
        print(i)
elif option== "3":
    print("0", student[0])
    print("1", student[1])
    print("2", student[2])
    print("3", student[3])
    print("4", student[4])
    
    x = int(input("give me a index number you want to remove: "))
    student.pop(x)

    print("New List: ")
    for i in student:
        print(i)
