import random
import smtplib
import pandas as pd

def reg(uid, email):
    try:
        # Check if epicid or email exists in the email database
        colnames=['UserID', 'email', 'otp', 'verified']
        df = pd.read_csv('email_database.csv',names=colnames,header=None)
        existing_data = df.loc[(df['UserID'] == uid) | (df['email'] == email)]
        
        if not existing_data.empty:
            verified_status = existing_data.iloc[0]['verified']
            
            if verified_status == 0:
                return "Please verify your OTP using /verify OTP or resend OTP using /resend_otp."
            elif verified_status == 1:
                return "You are already a registered user."
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        username = 'tacobotbynano@gmail.com'
        password = 'wqhlwiewlohojxgt'
        server.login(username, password)
        
        otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        
        sender = 'tacobotbynano@gmail.com'
        receiver = email
        subject = 'OTP Verification'
        message = f'Hello, Your OTP is {otp}'
        
        email = f'From: {sender}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{message}'
        server.sendmail(sender, receiver, email)
        
        server.quit()
        print("Email sent successfully.")
        
        # Store email details in the database (CSV file)
        data = {'UserID': [uid], 'email': [receiver], 'otp': [otp], 'verified': 0}
        df = pd.DataFrame(data)
        df.to_csv('email_database.csv', mode='a', index=False, header=False)  # Append to the existing CSV file

        return "OTP sent to your email! Please use /reigster verify OTP."
        
    except Exception as e:
        print("An error occurred while sending the email:", e)
        return "OTP not sent due to " + str(e)
