from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template

from accounts.forms import ContactForm
from privacy_policy.models import PrivacyPolicy


def index(request):
    return render(request, 'index.html')


def page3(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New message for you",
                content,
                "AraChef admin" + '',
                ['aratoys@mail.ru'],
                headers={'Reply To': contact_email}
            )

            email.send()

            return redirect('success')
    return render(request, 'page3.html', {'form': Contact_Form})

def Success(request):
    return render(request, 'contact_success.html')


def page4(request):
    return render(request, 'page4.html')
