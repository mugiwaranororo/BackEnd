from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Sunglasses
from django.views.generic.edit import UpdateView, DeleteView
from .forms import SunglassesForm
from django.contrib import messages


# Create your views here.
# home page where there are all the sunglasses and the user's sunglasses
class HomeView(ListView):
    model = Sunglasses
    template_name = 'my_app/home.html'
    context_object_name = 'sunglasses_list'

#to create the sunglasses, via a form
def SunglassesCreate(request):
    if request.method == 'POST':
        form = SunglassesForm(request.POST)
        if form.is_valid():
            sunglasses = form.save()
            sunglasses.user = request.user
            brandprice = sunglasses.brand.price
            colorprice = sunglasses.color.price
            typeprice = sunglasses.type.price
            sunglasses.price = (brandprice + colorprice) * typeprice
            sunglasses.save()
            messages.success(request, 'Sunglasses created successfully')
            return redirect('/')
    else:
        form = SunglassesForm()
    return render(request, 'my_app/sunglasses.html', {'form': form})

#to update the sunglasses, via a form
class SunglassesUpdate(UpdateView):
    model = Sunglasses
    template_name = 'my_app/edit.html'
    fields = ['brand', 'color', 'type', 'image']
    success_url = '/'

    def form_valid(self, form):
        sunglasses = form.save()
        sunglasses.price = (sunglasses.brand.price + sunglasses.color.price) * sunglasses.type.price
        messages.success(self.request, 'Sunglasses updated successfully')
        return super().form_valid(form)

#to delete the sunglasses
class SunglassesDelete(DeleteView):
    model = Sunglasses
    template_name = 'my_app/delete.html'
    success_url = '/'

class SunglassesDetail(DetailView):
    model = Sunglasses
    template_name = 'my_app/sunglassesdetail.html'
    context_object_name = 'sunglasses'


    