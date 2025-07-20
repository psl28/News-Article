import smtplib
from email.message import EmailMessage
#from MainModel import Model

class Mail():
    def __init__(self, article_dict: dict):
        self.article = article_dict

    def mail(self):

        key = list(self.article.keys())
        #main_article = self.article[key]

        sender_mail = "parthlanke28@gmail.com"
        recipients = ["parthlanke28@gmail.com", "shrutilanke13@gmail.com"]
        app_pass = "inrp gjoq teto rgml"

        message = f"""\
        <html>
        <body style="padding: 25px; font-family: Sans-Serif;">

            <div style="width: 100%; border: 5px solid black; margin: 20px auto; text-align: center; background-color: #C7E6E2">

                <h1>The Daily News</h1>
                <p style="font-size:20px;">A 5 minute read about the buzzing topics in AI & Tech</p>
            
                <a href={key[0]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[0]]}</p>
                    </div>
                </a>
                <a href={key[1]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[1]]}</p>
                    </div>
                </a>
                <a href={key[2]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[2]]}</p>
                    </div>
                </a>
                <a href={key[3]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[3]]}</p>
                    </div>
                </a>
                <a href={key[4]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[4]]}</p>
                    </div>
                </a>
                <a href={key[5]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[5]]}</p>
                    </div>
                </a>
                <a href={key[6]} style="text-decoration: none; color: inherit;">
                    <div style="padding: 10px; margin: 5px; border: 2px solid black; background-color: #F0F0F0; font-family: 'Times New Roman';">
                        <p style="font-size: 18px; line-height:1.6;">{self.article[key[6]]}</p>
                    </div>
                </a>
                                
            </div>
        </body>
        </html>
        """


        email = EmailMessage()
        email['Subject'] = "News Article"
        email['From'] = sender_mail
        email['To'] = ', '.join(recipients)
        email.set_content(message, subtype='html')

        with smtplib.SMTP_SSL ("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_mail, app_pass)
            smtp.send_message(email)
            print("Mail Sent Successfully")

#test = Mail()
#test.mail()


