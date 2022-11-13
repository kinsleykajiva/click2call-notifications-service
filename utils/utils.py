import boto3
from botocore.exceptions import ClientError

fromEmail = 'no-reply@intacall.com'



def sendEmail (name: str, subject: str, toEmail: str, emailTemplate: str):
	SENDER = "Inta Call <" + fromEmail + ">"
	RECIPIENT = toEmail
	
	SUBJECT = subject
	BODY_TEXT = ('')
	BODY_HTML = emailTemplate
	CHARSET = "UTF-8"
	client = boto3.client('ses',
						  aws_access_key_id='xxxxxxxxxx',
						  aws_secret_access_key='xxxxxxxxxxx57eQ',
						  region_name='eu-west-1'
						  )
	
	# Try to send the email.
	try:
		# Provide the contents of the email.
		response = client.send_email(
			Destination={
				'ToAddresses': [
					RECIPIENT,
				],
			},
			Message={
				'Body': {
					'Html': {
						'Charset': CHARSET,
						'Data': BODY_HTML,
					},
					'Text': {
						'Charset': CHARSET,
						'Data': BODY_TEXT,
					},
				},
				'Subject': {
					'Charset': CHARSET,
					'Data': SUBJECT,
				},
			},
			Source=SENDER,
		)
	# Display an error if something goes wrong.
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email sent! Message ID:"),
		print(response['MessageId'])
