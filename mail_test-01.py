import xlrd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


path = "C:\\Users\\rulo\\Desktop\\test.xlsx"
book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
mails = []
cant_col = sheet.ncols
cant_fil = sheet.nrows
col_mail, col_nombre, col_template, fila = 0, 0, 0, 0

print("Cant de columnas: ", cant_col)
print("Cant de filas: ", cant_fil)

for r in range(sheet.ncols):
    val = sheet.cell_value(0, r)
    if val == 'email':
        col_mail = r
    if val == 'nombre':
        col_nombre = r
    if val == 'template':
        col_template = r

print("columna de emails: ", col_mail)
print("columna de nombre: ", col_nombre)
print("columna de template: ", col_template)


for r in range(1, sheet.nrows):
    nombre = sheet.cell_value(r, col_nombre)
    mail = sheet.cell_value(r, col_mail)
    template = sheet.cell_value(r, col_template)
    print("\n Nombre:", nombre, "Mail:", mail, "Template:", template)

    print("Mail to: ", nombre, "Email: ", mail)
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
        msg['Subject'] = f"Testeando envio mail AUTOMATICO para {nombre} con PYTHON...!!!"
        # msg.attach(MIMEText(f'Mensaje de texto para: {nombre}', "plain"))
        msg.attach(MIMEText(template.format(nombre), "html"))

        contactos = mail

        if server.sendmail(MY_ADDRESS, contactos, msg.as_string()) == False:
            print("\n Mensaje no enviado...")
            server.quit()
        print("\n Mesnaje enviado OK ...!!!!!!!!")

    except Exception as e:
        print("Hubo un problema y no se pudo enviar Email..!!", e)
