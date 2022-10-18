from django.shortcuts import redirect, render
from django.http import HttpResponse
from. models import Feature
from django.views.decorators.csrf import csrf_exempt
import  smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.
@csrf_exempt
def contact(request):
# set your email and password
# please use App Password
    subject = request.POST['subject']
    body = request.POST['name'] + "\n"+request.POST['message']+"\n"+request.POST['email']
    sender_email = "manollasacollage@gmail.com"
    receiver_email = "mccshr552@gmail.com"
    password="huuvwmjawkgpahbb"
    # password = "manollasacollage@1"

    
    def send_email(user, pwd, recipient, subject, body):
    

        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

    # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(user, pwd)
            smtpserver.sendmail(FROM, TO, message)
            smtpserver.close()
            print ('successfully sent the mail')
            
        except Exception as e:
    
            print ("failed to send mail",e)
        
        
    send_email(sender_email,password,receiver_email,subject,body)
    



@csrf_exempt
def index(request):
    feature1=Feature()
    feature1.id=0
    feature1.name='Fast'
    feature1.details='Our Servics is Very Quick'


    if request.method=='POST':
        contact(request)
     
    return render(request, 'index.html',{'feature':feature1})

def inner(request):
    return render(request, 'inner-page.html')
    
def courses(request):
	return render(request,'courses.html')
	
    
def bcom(request):
	return render(request,'bcom.html')

    
def bba(request):
	return render(request,'bba.html')


    
def bsw(request):
	return render(request,'bsw.html')

    
def bsc(request):
	return render(request,'bsc.html')

    
def blis(request):
	return render(request,'blis.html')

    
def mlis(request):
	return render(request,'mlis.html')

    
def mba(request):
	return render(request,'mba.html')

    
def ma(request):
	return render(request,'ma.html')


	
	
	
	
	
	

