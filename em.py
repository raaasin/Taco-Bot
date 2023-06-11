import random
import smtplib
import pandas as pd

def register():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        username = 'tacobotbynano@gmail.com'
        password = 'wqhlwiewlohojxgt'
        server.login(username, password)
        
        otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        
        sender = 'tacobotbynano@gmail.com'
        receiver = 'razia971@gmail.com'
        subject = 'OTP Verification'
        message = f'Hello, Your OTP is {otp}'
        
        email = f'From: {sender}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{message}'
        server.sendmail(sender, receiver, email)
        
        server.quit()
        print("Email sent successfully.")
        
        # Store email details in the database (CSV file)
        data = {'Sender': [sender], 'Receiver': [receiver], 'otp': [otp]}
        df = pd.DataFrame(data)
        df.to_csv('email_database.csv', mode='a', index=False, header=False)  # Append to the existing CSV file
        
    except Exception as e:
        print("An error occurred while sending the email:", e)

register()
