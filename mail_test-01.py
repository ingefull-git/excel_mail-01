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
    mails.append(sheet.cell_value(r, 1))


print(sheet.nrows)
print(sheet.ncols)
print(mails)

MY_ADDRESS = os.environ.get('EMAIL_USER')
MY_PASS = os.environ.get('EMAIL_PASS')
HOST = 'mail.tspcontrols.com'
PORT = 25

print("Connecting...")

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
msg['Subject'] = "Testeando envio mail AUTOMATICO con PYTHON...!!!"
msg.attach(MIMEText("""

    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
      <head>
        <title>

        </title>
        <!--[if !mso]><!-- -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!--<![endif]-->
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style type="text/css">
          #outlook a { padding:0; }
          .ReadMsgBody { width:100%; }
          .ExternalClass { width:100%; }
          .ExternalClass * { line-height:100%; }
          body { margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%; }
          table, td { border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt; }
          img { border:0;height:auto;line-height:100%; outline:none;text-decoration:none;-ms-interpolation-mode:bicubic; }
          p { display:block;margin:13px 0; }
        </style>
        <!--[if !mso]><!-->
        <style type="text/css">
          @media only screen and (max-width:480px) {
            @-ms-viewport { width:320px; }
            @viewport { width:320px; }
          }
        </style>
        <!--<![endif]-->
        <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix { width:100% !important; }
        </style>
        <![endif]-->

      <!--[if !mso]><!-->
        <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Helvetica" rel="stylesheet" type="text/css">
        <style type="text/css">
          @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
@import url(https://fonts.googleapis.com/css?family=Helvetica);
        </style>
      <!--<![endif]-->



    <style type="text/css">
      @media only screen and (min-width:480px) {
        .mj-column-per-66 { width:66.66666666666666% !important; max-width: 66.66666666666666%; }
.mj-column-per-33 { width:33.333333% !important; max-width: 33.333333%; }
.mj-column-per-100 { width:100% !important; max-width: 100%; }
.mj-column-per-40 { width:40% !important; max-width: 40%; }
.mj-column-per-60 { width:60% !important; max-width: 60%; }
      }
    </style>


        <style type="text/css">



    @media only screen and (max-width:480px) {
      table.full-width-mobile { width: 100% !important; }
      td.full-width-mobile { width: auto !important; }
    }

        </style>
        <style type="text/css">.hide_on_mobile { display: none !important;}
        @media only screen and (min-width: 480px) { .hide_on_mobile { display: block !important;} }
        .hide_section_on_mobile { display: none !important;}
        @media only screen and (min-width: 480px) { .hide_section_on_mobile { display: table !important;} }
        .hide_on_desktop { display: block !important;}
        @media only screen and (min-width: 480px) { .hide_on_desktop { display: none !important;} }
        .hide_section_on_desktop { display: table !important;}
        @media only screen and (min-width: 480px) { .hide_section_on_desktop { display: none !important;} }
        [owa] .mj-column-per-100 {
            width: 100%!important;
          }
          [owa] .mj-column-per-50 {
            width: 50%!important;
          }
          [owa] .mj-column-per-33 {
            width: 33.333333333333336%!important;
          }
          p {
              margin: 0px;
          }
          @media only print and (min-width:480px) {
            .mj-column-per-100 { width:100%!important; }
            .mj-column-per-40 { width:40%!important; }
            .mj-column-per-60 { width:60%!important; }
            .mj-column-per-50 { width: 50%!important; }
            mj-column-per-33 { width: 33.333333333333336%!important; }
            }</style>

      </head>
      <body style="background-color:#FFFFFF;">


      <div style="background-color:#FFFFFF;">

      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
        <tbody>
          <tr>
            <td>


      <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:4px 0px 4px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:middle;width:399.99999999999994px;"
            >
          <![endif]-->

      <div class="mj-column-per-66 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

            <tr>
              <td align="left" style="font-size:0px;padding:0px 0px 0px 5px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#7a7a7a;">
        <p style="font-family: Helvetica, sans-serif;"><span style="color:#000000;"><span style="font-size: 11px;"> </span>Write short email preheader</span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

            <td
               class="" style="vertical-align:middle;width:199.99999999999997px;"
            >
          <![endif]-->

      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

            <tr>
              <td align="right" style="font-size:0px;padding:0px 5px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:right;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;">Can&#39;t read this email? <a href="*|WEBVERSION|*" style="color: #808080;"><span style="color:#000000;">Click here</span></a></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


            </td>
          </tr>
        </tbody>
      </table>


      <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">

        <v:rect  style="width:600px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
        <v:fill  origin="0.5, 0" position="0.5, 0" src="https://storage.googleapis.com/afuxova10642/1-13.png" color="#B1FFFF" type="tile" />
        <v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">
      <![endif]-->

      <div style="background:#B1FFFF url(https://storage.googleapis.com/afuxova10642/1-13.png) top center / cover repeat;Margin:0px auto;max-width:600px;">
        <div style="line-height:0;font-size:0;">
        <table align="center" background="https://storage.googleapis.com/afuxova10642/1-13.png" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF url(https://storage.googleapis.com/afuxova10642/1-13.png) top center / cover repeat;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:5px 0px 5px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td style="font-size:0px;word-break:break-word;">


    <!--[if mso | IE]>

        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="50" style="vertical-align:top;height:50px;">

    <![endif]-->

      <div style="height:50px;">
        &nbsp;
      </div>

    <!--[if mso | IE]>

        </td></tr></table>

    <![endif]-->


              </td>
            </tr>

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="font-size:22px;"><strong>COMPANY</strong></span></p>
      </div>

              </td>
            </tr>

            <tr>
              <td class="hide_on_mobile" style="font-size:0px;word-break:break-word;">


    <!--[if mso | IE]>

        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="67" style="vertical-align:top;height:67px;">

    <![endif]-->

      <div style="height:67px;">
        &nbsp;
      </div>

    <!--[if mso | IE]>

        </td></tr></table>

    <![endif]-->


              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
        </div>
      </div>

        <!--[if mso | IE]>
        </v:textbox>
      </v:rect>

          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#1EA5AA;background-color:#1EA5AA;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#1EA5AA;background-color:#1EA5AA;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:4px 0px 4px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:199.999998px;"
            >
          <![endif]-->

      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="color:#ffffff;"><strong>TOP PRODUCTS</strong></span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

            <td
               class="" style="vertical-align:top;width:199.999998px;"
            >
          <![endif]-->

      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="color:#ffffff;"><strong>SPECIAL OFFERS</strong></span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

            <td
               class="" style="vertical-align:top;width:199.999998px;"
            >
          <![endif]-->

      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="color:#ffffff;"><strong>OUR BLOG</strong></span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#B1FFFF;background-color:#B1FFFF;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF;background-color:#B1FFFF;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:0px 0px 0px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 5px 0px 5px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="font-size:64px;">SUMMER SALE<br>
<strong>1+1 FREE</strong></span><strong> </strong></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#B1FFFF;background-color:#B1FFFF;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF;background-color:#B1FFFF;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:0px 0px 0px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
        <tbody>
          <tr>
            <td style="width:414px;">

      <img height="auto" src="https://storage.googleapis.com/afuxova10642/Webp.net-gifmaker.gif" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="414">

            </td>
          </tr>
        </tbody>
      </table>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#B1FFFF;background-color:#B1FFFF;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF;background-color:#B1FFFF;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:3px 0px 3px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="left" style="font-size:0px;padding:0px 14px 0px 14px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="font-size:16px;">Lorem ipsum dolor sit amet, consectetuer adipiscing elit.<br>
<strong>Mauris dictum facilisis augue.</strong><br>
<br>
Ut enim ad minim veniam, quis nostrud exercitation <strong>ullamco laboris</strong><br>
nisi ut aliquip ex ea commodo consequat. </span></p>
      </div>

              </td>
            </tr>

            <tr>
              <td align="center" vertical-align="middle" style="font-size:0px;padding:7px 7px 7px 7px;word-break:break-word;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
        <tr>
          <td align="center" bgcolor="#ff080a" role="presentation" style="border:0px solid #000;border-radius:none;cursor:auto;mso-padding-alt:10px 30px;background:#ff080a;" valign="middle">
            <a href="https://google.com" style="display:inline-block;background:#ff080a;color:#ffffff;font-family:Helvetica, sans-serif;font-size:15px;font-weight:normal;line-height:100%;Margin:0;text-decoration:none;text-transform:none;padding:10px 30px;mso-padding-alt:0px;border-radius:none;" target="_blank">
              SHOP NOW >>
            </a>
          </td>
        </tr>
      </table>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#1EA5AA;background-color:#1EA5AA;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#1EA5AA;background-color:#1EA5AA;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:0px 0px 0px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td style="font-size:0px;word-break:break-word;">


    <!--[if mso | IE]>

        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="10" style="vertical-align:top;height:10px;">

    <![endif]-->

      <div style="height:10px;">
        &nbsp;
      </div>

    <!--[if mso | IE]>

        </td></tr></table>

    <![endif]-->


              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#B1FFFF;background-color:#B1FFFF;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF;background-color:#B1FFFF;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:7px 0px 7px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:240px;"
            >
          <![endif]-->

      <div class="mj-column-per-40 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
        <tbody>
          <tr>
            <td style="width:130px;">

      <img height="auto" src="https://storage.googleapis.com/afuxova10642/5a2c3229180bb4.8821238415128458650985.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="130">

            </td>
          </tr>
        </tbody>
      </table>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

            <td
               class="" style="vertical-align:top;width:360px;"
            >
          <![endif]-->

      <div class="mj-column-per-60 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="left" style="font-size:0px;padding:5px 10px 5px 9px;word-break:break-word;">

      <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="font-size:18px;"><strong>FREE DELIVERY</strong></span><br>
<br>
<span style="font-size:16px;">Lorem ipsum dolor sit amet, consectetuer<br>
<strong>From 10.8. till 13.8.2020</strong></span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="background:#1EA5AA;background-color:#1EA5AA;Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#1EA5AA;background-color:#1EA5AA;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:2px 0px 2px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;"><span style="font-size:18px;"><span style="color:#ffffff;">ENJOY FREE SHIPPING AND FREE RETURNS</span></span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">

        <v:rect  style="width:600px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
        <v:fill  origin="0.5, 0" position="0.5, 0" src="https://storage.googleapis.com/afuxova10642/2-8.png" color="#B1FFFF" type="tile" />
        <v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">
      <![endif]-->

      <div style="background:#B1FFFF url(https://storage.googleapis.com/afuxova10642/2-8.png) top center / cover repeat;Margin:0px auto;max-width:600px;">
        <div style="line-height:0;font-size:0;">
        <table align="center" background="https://storage.googleapis.com/afuxova10642/2-8.png" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#B1FFFF url(https://storage.googleapis.com/afuxova10642/2-8.png) top center / cover repeat;width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:47px 0px 47px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:10px 10px 10px 10px;word-break:break-word;">


     <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>

              <td>
            <![endif]-->
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">

      <tr>
        <td style="padding:4px;">
          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:transparent;border-radius:3px;width:35px;">
            <tr>
              <td style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                <a href="https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/PROFILE" target="_blank">
                    <img height="35" src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/outlined/facebook.png" style="border-radius:3px;display:block;" width="35">
                  </a>
                </td>
              </tr>
          </table>
        </td>

      </tr>

              </table>
            <!--[if mso | IE]>
              </td>

              <td>
            <![endif]-->
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">

      <tr>
        <td style="padding:4px;">
          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:transparent;border-radius:3px;width:35px;">
            <tr>
              <td style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                <a href="https://twitter.com/home?status=https://www.twitter.com/PROFILE" target="_blank">
                    <img height="35" src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/outlined/twitter.png" style="border-radius:3px;display:block;" width="35">
                  </a>
                </td>
              </tr>
          </table>
        </td>

      </tr>

              </table>
            <!--[if mso | IE]>
              </td>

              <td>
            <![endif]-->
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">

      <tr>
        <td style="padding:4px;">
          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:transparent;border-radius:3px;width:35px;">
            <tr>
              <td style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                <a href="https://www.linkedin.com/shareArticle?mini=true&url=[[SHORT_PERMALINK]]&title=&summary=&source=" target="_blank">
                    <img height="35" src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/outlined/linkedin.png" style="border-radius:3px;display:block;" width="35">
                  </a>
                </td>
              </tr>
          </table>
        </td>

      </tr>

              </table>
            <!--[if mso | IE]>
              </td>

              <td>
            <![endif]-->
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">

      <tr>
        <td style="padding:4px;">
          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:transparent;border-radius:3px;width:35px;">
            <tr>
              <td style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                <a href="[[SHORT_PERMALINK]]" target="_blank">
                    <img height="35" src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/outlined/instagram.png" style="border-radius:3px;display:block;" width="35">
                  </a>
                </td>
              </tr>
          </table>
        </td>

      </tr>

              </table>
            <!--[if mso | IE]>
              </td>

              <td>
            <![endif]-->
              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">

      <tr>
        <td style="padding:4px;">
          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:transparent;border-radius:3px;width:35px;">
            <tr>
              <td style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                <a href="https://www.youtube.com" target="_blank">
                    <img height="35" src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/outlined/youtube.png" style="border-radius:3px;display:block;" width="35">
                  </a>
                </td>
              </tr>
          </table>
        </td>

      </tr>

              </table>
            <!--[if mso | IE]>
              </td>

          </tr>
        </table>
      <![endif]-->


              </td>
            </tr>

            <tr>
              <td style="font-size:0px;word-break:break-word;">


    <!--[if mso | IE]>

        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="56" style="vertical-align:top;height:56px;">

    <![endif]-->

      <div style="height:56px;">
        &nbsp;
      </div>

    <!--[if mso | IE]>

        </td></tr></table>

    <![endif]-->


              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
        </div>
      </div>

        <!--[if mso | IE]>
        </v:textbox>
      </v:rect>

          </td>
        </tr>
      </table>
      <![endif]-->


      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
        <tbody>
          <tr>
            <td>


      <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


      <div style="Margin:0px auto;max-width:600px;">

        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:1px 0px 1px 0px;text-align:center;vertical-align:top;">
                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">

        <tr>

            <td
               class="" style="vertical-align:middle;width:600px;"
            >
          <![endif]-->

      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

            <tr>
              <td align="center" style="font-size:0px;padding:3px 3px 3px 3px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif;">Please enter your address and your contact here.<br>
Explain why your subscribers are receiving this email.</p>
      </div>

              </td>
            </tr>

            <tr>
              <td align="center" style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">

      <div style="font-family:Helvetica, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#000000;">
        <p style="font-family: Helvetica, sans-serif; font-size: 11px;">If you do not want to receive any more information from us, please <span style="color: rgb(0, 0, 0);"><a href="*|UNSUB|*" style="color: #000000;">click this link</a>.</span></p>
      </div>

              </td>
            </tr>

      </table>

      </div>

          <!--[if mso | IE]>
            </td>

        </tr>

                  </table>
                <![endif]-->
              </td>
            </tr>
          </tbody>
        </table>

      </div>


      <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


            </td>
          </tr>
        </tbody>
      </table>

      </div>

      </body>
    </html>

""", "html"))

contactos = mails

if server.sendmail(MY_ADDRESS, contactos, msg.as_string()) == False:
    print("\n Mensaje no enviado...")
    server.quit()
print("\n Mesnaje enviado OK ...!!!!!!!!")
print("\n a los siguientes mails: ", mails)
