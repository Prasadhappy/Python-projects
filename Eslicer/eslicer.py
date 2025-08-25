email = input('enter your email-id ').strip()  # taking email id and strip is to remove space from start and end

username = email[:email.index('@')]

domain = email[email.index('@')+1:]

result = "Your username = {} \n Your domain name = {}".format(username, domain)     

print(result)