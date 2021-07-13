#Centro de Diversion Nocturna
import time

print("Welcome")
time.sleep(1)

print("Sign in to start your experience")
time.sleep(0.7)

user_name = input("Please tell me your name: ")
user_name_capitalize = user_name.capitalize()
if "" in user_name_capitalize:
    user_name_capitalize = user_name_capitalize.strip()

user_last_name = input("{0}, tell me your last name: ".format(user_name_capitalize))
user_last_name_capitalize = user_last_name.capitalize()
time.sleep(0.5)

age_info = int(input("{0}, how old are you? ".format(user_name_capitalize)))
time.sleep(0.5)

sex_info = input("Male/Female: ")
sex_info_capitalize = sex_info.capitalize()
time.sleep(1.2)

name_def = "{0} {1}".format(user_name_capitalize, user_last_name_capitalize)

general_info = """
Name: {0}
Age: {1} years old
Sex: {2}""".format(name_def, age_info, sex_info_capitalize)
print(general_info)
time.sleep(0.5)

print("""
Analyzing...""")
time.sleep(2.7)

if age_info > 18:
    print("""
{}, welcome to this nightlife center.""".format(user_name_capitalize))
elif age_info == 18:
    print("""
{}, welcome to this nightlife center.""".format(user_name_capitalize))
else:
    print("""
{}, it seems that your too young for this site.""".format(user_name_capitalize))
    print("It's a shame but you are not allow to enter.")





