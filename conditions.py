# # Python is case sensitive i.e. 'a' and "A" are different
# environment = input("Enter your environment: ")
# print(type(environment))
# change_ticket = False

# environment = environment.casefold()

# if environment == "prod":
#     change_ticket = True
#     print("Please provide a change ticket")
# elif environment == "staging":
#     print("Welcome to staging environment")
# else:
#     print("Please login using your credentials")



role = input("Enter your role: ")
role = role.casefold()

access_granted = False

if role == "admin":
    access_granted = True
    print("Full access granted")
elif role == "editor":
    print("Limited editing access granted")
else:
    print("Read-only access")

print("Access granted:", access_granted)