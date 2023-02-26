import psutil
import smtplib

# Settings Mails 
FROM_EMAIL = 'mail@mail.com' # Email sender
PASSWORD = 'adhijuwbaiudwa' # Password of your email (Please enable password for applications in gmail)
TO_EMAIL = 'mail@mail2.com' # Email destinatary 


# Function for send emails
def send_email(subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        msg = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg)
        print('Email sent')
        return True
    except Exception as e:
        print(f'Failed to send email: {str(e)}')
        return False
    finally:
        server.quit()

# storage units tour
try:
    correo_despachado = False
    for partition in psutil.disk_partitions():
        disk_usage = psutil.disk_usage(partition.mountpoint)
        free_space_gb = round(disk_usage.free / (1024**3), 2)
        if free_space_gb <= 150:
            message = f'The drive {partition.mountpoint} has less than 150Gb available ({free_space_gb} GB)'
            correo_despachado = send_email('Disk space warning', message)
    if correo_despachado:
        print('The mail sent correctly')
    else:
        print('The email could not be dispatched. Please check your email account settings and try again.')
except Exception as e:
    print('Error parsing storage units: ' + str(e))