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

def verify(uid, otp):
    try:
        colnames = ['UserID', 'email', 'otp', 'verified']
        df = pd.read_csv('email_database.csv', names=colnames, header=None)
        existing_data = df.loc[df['UserID'] == uid]

        if not existing_data.empty:
            verified_status = existing_data.iloc[0]['verified']

            if verified_status == 0:
                if str(existing_data.iloc[0]['otp']) == otp:
                    # Update verified status to 1 and save the CSV
                    df.loc[df['UserID'] == uid, 'verified'] = 1
                    df.to_csv('email_database.csv', index=False, header=False)
                    return "OTP verified successfully!"
                else:
                    return "Wrong OTP, use /signup resend_otp or Change email using /signup change_emai"


            elif verified_status == 1:
                return "You are already a registered user."

    except Exception as e:
        print("An error occurred while verifying OTP:", e)
        return "OTP not verified due to " + str(e)
    
def ce(uid, email):
    try:
        colnames = ['UserID', 'email', 'otp', 'verified']
        df = pd.read_csv('email_database.csv', names=colnames, header=None)
        existing_data = df.loc[df['UserID'] == uid]

        if not existing_data.empty:
            # Update the email to the new one
            df.loc[df['UserID'] == uid, 'email'] = email
            df.loc[df['UserID'] == uid, 'verified'] = 0
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

            email_content = f'From: {sender}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{message}'
            server.sendmail(sender, receiver, email_content)

            server.quit()
            print("Email sent successfully.")

            # Update the OTP in the DataFrame
            df.loc[df['UserID'] == uid, 'otp'] = otp

            # Save the updated DataFrame to the CSV
            df.to_csv('email_database.csv', index=False, header=False)

            return "Email updated, please verify OTP using /signup verify"

        else:
            return "You are not a registered user, please use /signup register"

    except Exception as e:
        print("An error occurred while changing email:", e)
        return "Email not updated due to " + str(e)

def rotp(uid):
    try:
        colnames = ['UserID', 'email', 'otp', 'verified']
        df = pd.read_csv('email_database.csv', names=colnames, header=None)
        existing_data = df.loc[df['UserID'] == uid]

        if not existing_data.empty:
            # Update the email to the new one
            email = existing_data.iloc[0]['email']

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

            email_content = f'From: {sender}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{message}'
            server.sendmail(sender, receiver, email_content)

            server.quit()
            print("Email sent successfully.")

            # Update the OTP in the DataFrame
            df.loc[df['UserID'] == uid, 'otp'] = otp

            # Save the updated DataFrame to the CSV
            df.to_csv('email_database.csv', index=False, header=False)

            return "OTP resent successfully, please verify OTP using /signup verify"

        else:
            return "You are not a registered user, please use /signup register"

    except Exception as e:
        print("An error occurred while resending OTP:", e)
        return "OTP not resent due to " + str(e)