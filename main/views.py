from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        # Send email
        send_mail(
            subject,
            f"From: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}",
            email,
            ['ajanshul2001@gmail.com'],  # Replace with the recipient's email address
        )
        return redirect('index')  # Redirect to a success page

    return render(request, 'main/contact.html')

def skills(request):
    context={}
    return render(request,'main/skills.html',context)

def about(request):
    context={}
    return render(request,'main/about.html',context)



debug=True