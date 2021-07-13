import time

welcome = "Welcome to this practice"
print(welcome)
time.sleep(1.3)

print("Let's start")
time.sleep(0.5)

user_name = input("Please tell me your name: ")
user_name_capitalize = user_name.capitalize()

user_last_name = input(f"{user_name_capitalize}, tell me your last name: ")
user_last_name_capitalize = user_last_name.capitalize()
time.sleep(0.5)

age = input(f"{user_name_capitalize}, how old are you? ")
time.sleep(0.5)

sex_info = input("Male/Female: ")
sex_info_capitalize = sex_info.capitalize()
time.sleep(0.5)

user_nickname = input(f"Finally, {user_name_capitalize} please tell your desired nickname: ")
time.sleep(1)
upper_case_nickname = user_nickname.upper()

welcome_info = f"{upper_case_nickname}, welcome to this program... I hope you enjoy it"
print(welcome_info)

general_info = f"""Name: {user_name_capitalize}
Last name: {user_last_name_capitalize}
Age: {age}
Sex: {sex_info_capitalize}"""
time.sleep(1.2)

print(general_info)
