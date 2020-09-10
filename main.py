import smtplib


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # with open('password.txt', 'r') as x:
    #   password = x.read()
    server.login('sender_email@gmail.com', password)

    subject = "Good morning Bek Brace!"
    with open('body.txt', 'r') as n:
        body = n.read()
    # body = " Let us recreate Tanks shooter game with Pygame!"
    msg = f"subject: {subject} \n\n\n {body}"

    server.sendmail(
        'sender_email@gmail.com',
        'receiver_email@gmail.com',
        msg
    )
    print('Message is sent succesfully!')


if __name__ == "__main__":
    send_mail()
