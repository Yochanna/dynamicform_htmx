from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            extra_numbers = request.POST.getlist("phones")
            print("Extra phones:", extra_numbers)
            return render(request, "formsdemo/success.html", {"name": form.cleaned_data["name"]})
        return render(request, "formsdemo/contact_form.html", {"form": form})
    form = ContactForm()
    return render(request, "formsdemo/contact_form.html", {"form": form})

def add_phone_field(request):
    return render(request, "formsdemo/phone_field.html")
