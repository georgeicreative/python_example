with open('name.txt','r',encoding='utf-8') as name_file:

    with open('test.txt','r',encoding='utf-8') as body_file:
        body = body_file.read()

        for name in name_file:
            mail = "Hello " + name.strip() + "\n" + body
            with open(name.strip() + ".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)

