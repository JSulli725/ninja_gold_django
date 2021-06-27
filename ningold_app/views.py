from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.

def loadHome(request):
    if "total_gold" not in request.session:
        request.session["total_gold"] = 0
        request.session["activities_history"] = []
    return render(request, 'home.html')

def findGold(request):
    if request.method == "POST":
        for name in request.POST:
            if name == "farm":
                chance = random.randint(10,20)
                # request.session["farming"] = chance
                request.session["total_gold"] += chance
                request.session["activities_history"].append(f"Earned {chance} golds from the farm!")
                return redirect("/")
            if name == "cave":
                chance = random.randint(5,10)
                # request.session["caving"] = chance
                request.session["total_gold"] += chance
                request.session["activities_history"].append(f"Earned {chance} golds from the cave!")
                return redirect("/")
            if name == "house":
                chance = random.randint(2,5)
                # request.session["house"] = chance
                request.session["total_gold"] += chance
                request.session["activities_history"].append(f"Earned {chance} golds from the house!")
                return redirect("/")
            if name == "casino":
                chance = random.randint(1,2)
                if chance == 1:
                    gains = random.randint(0,50)
                    # request.session["gambling"] = gains
                    request.session["total_gold"] += gains
                    request.session["activities_history"].append(f"Entered a casino and won {gains} golds...nice!")
                    return redirect("/")
                else:
                    losses = random.randint(0,50) * -1
                    # request.session["gambling"] = losses
                    request.session["total_gold"] += losses
                    request.session["activities_history"].append(f"Entered a casino and lost {losses} golds...Ouch..")
                    return redirect("/")

def resetGold(request):
    request.session.clear()
    return redirect("/")
