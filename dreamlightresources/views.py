from django.shortcuts import render


# Create your views here.
def Home_page(request):
    context ={
        
        }
    return render(request, "Homepage.html", context)

def Crops(request):
    context = {

    }

    return render(request, "Crops.html", context)

def Characters(request):
    context ={
         
    }
    return render(request, "Characters.html", context)

def Fishing(request):
    context= {

    }
    return render(request, "Fishing.html", context)

def Mining(request):
    context = {

    }
    return render(request, "Mining.html", context)

def SiteMap(request):
    context ={

    }
    return render(request, "SiteMap.html", context)