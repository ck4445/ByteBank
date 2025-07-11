import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.encoders import encode_base64
import os.path
import py7zr
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Create a 7z archive named 'target.7z' and add the contents of 'source_dir'
with py7zr.SevenZipFile('ByteBank.7z', 'w') as archive:
    archive.writeall('/home/pi/Python_Projects/ByteBank', arcname='optional_name_in_archive')



# Replace with the actual path to your .7z file
file_path = '/home/pi/Python_Projects/ByteBank/backups/ByteBank.7z'
def delete7z():
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to delete file '{file_path}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")
        

# Email settings
sender_email = 'youbackupsemail@gmail.com'
sender_password = ''  # Use an app password, not your Gmail password
receiver_email = 'youbackupsemai@gmail.com'
subject = 'Email with 7z attachment'
body = 'Please find the attached 7z file.'
file_path = '/home/pi/Python_Projects/ByteBank/backups/ByteBank.7z'  # Replace with the actual path

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add the email body
msg.attach(MIMEText(body, 'plain'))

# Attach the 7z file
with open(file_path, 'rb') as file:
    part = MIMEApplication(file.read(), Name=os.path.basename(file_path))
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
    msg.attach(part)

# Encode the attachment
#encoders.encode_base64(part)

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
        delete7z()
except Exception as e:
    print(f'Error sending email: {e}')
    delete7z()
    