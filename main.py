import secrets, string, random, time



def generate_pas():
    all_chars = string.ascii_letters + string.punctuation + string.digits
    res = ''.join(secrets.choice(all_chars) for i in range(12))
    return print("Password: ",res)


def generate_mail():
    valid_chars = string.ascii_lowercase + string.digits
    login_lens = random.randint(4,15)
    login = ''
    for i in range(login_lens):
        pos = random.randint(0,len(valid_chars) - 1)
        login = login + valid_chars[pos]
    if login[0].isnumeric():
        pos = random.randint(0,len(valid_chars) - 10)
        login = valid_chars[pos] + login
    base = ['@gmail','@yahoo','@redmail','@hotmail','@bing']
    base_choice = random.randint(0, len(base) - 1)
    email = login + base[base_choice]
    ends = ['.com','.in','.gov','.ac.in','.net','.org']
    ends_pos = random.randint(0,len(ends) - 1)
    email = email + ends[ends_pos]
    return print('Email: ',email)

while True:
    print('Generating mail...')
    time.sleep(2)
    generate_mail()
    print("Generating pass...")
    time.sleep(2)
    generate_pas()
    a = input('More?(Y/N) ')
    if a == 'Y':
        continue
    else:
        break






