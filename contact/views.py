from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ContactForm()
    context = {'form': form, 'title': 'Contact Us'}
    return render(request, 'contact/contact.html', context)


def thank_you_view(request):
    context = {'title': 'Thank you'}
    return render(request, 'contact/thank_you.html', context)



