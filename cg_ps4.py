# # 1
# no = [0,25,5,40,15]
# lar = max(no)
# print(UnboundLocalError)
# # 2
# no = []
# for i in range(5):
#     n = int(input("enter no:"))
    
#     no.append(n)
#     print(sum(no))
# # 
# with open("student.txt", "w") as file:
#     file.write("Rahul\n")
#     file.write("Priya\n")

# with open("student.txt", "r") as file:
#     data = file.read()
# print(data)

# with open("student.txt", "a") as file:
#     file.write("Amit\n")

# file = open("student.txt", "r")
# data = file.read()
# file.close()

# with open("student.txt", "w") as file:
#     file.write("Name: Rahul\n")
#     file.write("Course: Python")

# with open("student.txt", "r") as file:
#     data = file.read()

# print(data)

# 1
file = open("student.txt", "w")

file.write("Name: Sohel\n")
file.write("College: ABC College\n")

file.close()

print("Data written successfully")

# 2
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()

# 3
file = open("student.txt", "a")

file.write("Course: BCA\n")

file.close()

print("Course added successfully")