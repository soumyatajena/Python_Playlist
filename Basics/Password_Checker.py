# Task : Print the username and masked password with the password length

user_name=input('Username:')
password= input('Password:')
hidden_pwd='*'*len(password)

print(f'{user_name} your password {hidden_pwd} is {len(password)} letters long')