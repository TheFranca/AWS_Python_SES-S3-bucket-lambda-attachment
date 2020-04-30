#PS: Is possible to make an lambda function/azure function with this code. Just replace the correctly fields and see its working
#OBS: É possível criar uma lambda function/azure function com esse código. Basta substituir os campos corretamente e observar esse código funcionando.

#IMPORTANT: If you are using SES service of AWS is extremly important that you configure an email sender into the panel of SES Configuration into AWS platform (site)
#IMPORTANTE: Se você estiver usando o serviço SES da AWS é extremamente importante que você configure o email de envio no painel de configurações do SES na plataforma da AWS (site)

import boto3
import os
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#s3 configu
#The next 3 lines of code is essentials to pick the data, from the bucket, that will be attachet in the mail.
#As próximas três linhas são necessárias para que se busque o arquivo que se localiza no bucket e que será anexado
s3 = boto3.resource('s3')
obj = s3.Object('name_of_the_bucket', 'key_name_of_archive.extension')
bodi = obj.get()['Body'].read()

#Regions config to find the bucket
#Configuração de região necessárias para encontrar o bucket
AWS_REGION = 'sa-east-1'
client = boto3.client('ses',region_name=AWS_REGION)

#Must to be a list because the field 'Data' in RawMessage only accept list as data
#Deve ser uma lista porque o comapo 'Data' do 'RawMessage' só aceita listas como entrada de dados
to_email = ['email_address_1','email_address_2','email_address_3', 'how many do you want'] 

#Conteudo do email (Pode ser um html também)
mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''

sender_address = 'email addresse sender' #Address of who will send an email. (Email de quem enviará o email)
receiver_address = to_email[0] #Reciver Address from the list 'to_email(line 28)'. (Email para quem será enviado, vindo da lista de emails 'to_mail'(linha 28))
attachment = 'item_into_bucket.extension' #Name of archive in the bucket that will be send as attachment. MUST BE EXACTLY NAME THAT APPEARS IN THE BUCKET. (Nome do arquivo que está no bucket. O NOME TEM QUE SER IGUAL AO QUE ESTÁ NO BUCKET)

#Message['item'] --> só por padrão mesmo, porque não faz falta se retirr
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Testando envio de email com anexo'
message['attachment'] = attachment
message.attach(MIMEText(mail_content, 'plain'))

#part is responsable to build/attach itens(text, archive, etc) into the email. MIMEApplication do this work. (part é responsavél por construi/anexar itens(textos, arquivos, etc) no email. MIMEApplication faz esse trabalho)
part = MIMEApplication(bodi)
part.add_header('Content-Disposition', 'attachment', filename='item_from_bucket.pdf')#filename is responsible to give a name to the attachment.(filename é responsável por dar um nome para o anexo)
message.attach(part)

try:
	response = client.send_raw_email(
		Source=sender_address,
		Destinations=to_email,
		RawMessage={'Data':message.as_string()}
		)
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])


