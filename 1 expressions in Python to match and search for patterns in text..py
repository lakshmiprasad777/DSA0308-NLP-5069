import re
text = "Hello, my email is Lakshmi@gmail.com and my phone number is 9392009781. Another email is Lucky@gmail.com and phone number is 9876543210."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b[0-9]{10}\b'
print("Email addresses found:")
for match in re.finditer(email_pattern, text):
        print(match.group())
print("\nPhone numbers found:")
for match in re.finditer(phone_pattern, text):
        print(match.group())
