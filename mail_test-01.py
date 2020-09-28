import xlrd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


path = "C:\\Users\\rulo\\Desktop\\test.xlsx"

book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
mails = []

for r in range(1, sheet.nrows):
    name = sheet.cell_value(r, 0)
    mail = (sheet.cell_value(r, 1))
    template = sheet.cell_value(r, 2)

    print("Mail to: ", name, "Email: ", mail)
    MY_ADDRESS = os.environ.get('EMAIL_USER')
    MY_PASS = os.environ.get('EMAIL_PASS')
    HOST = 'mail.tspcontrols.com'
    PORT = 25

    print("Connecting...")
    try:
        server = smtplib.SMTP(host=HOST, port=PORT)
        if server.starttls() == False:
            print("\n Server not connection...")
            exit()

        print("\n Server connected...")

        if server.login(MY_ADDRESS, MY_PASS) == False:
            print("\n Login Failed...")
            exit()

        print("\n Login Succeed...")

        msg = MIMEMultipart()
        msg['To'] = 'contactos RS'
        msg['From'] = MY_ADDRESS
        msg['Subject'] = f"Testeando envio mail AUTOMATICO para {name} con PYTHON...!!!"
        # msg.attach(MIMEText(f'Mensaje de texto para: {name}', "plain"))
        msg.attach(MIMEText(template.format(name), "html"))

        contactos = mail

        if server.sendmail(MY_ADDRESS, contactos, msg.as_string()) == False:
            print("\n Mensaje no enviado...")
            server.quit()
        print("\n Mesnaje enviado OK ...!!!!!!!!")
        print("al siguiente mail: ", mail, "\n")

    except Exception as e:
        print("Hubo un problema y no se pudo enviar Email..!!", e)
