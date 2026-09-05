from django.shortcuts import render


def home(request):
    goals = [
        {"name": "Complete my Information Systems degree", "completed": False},
        {"name": "Squat 600 pounds", "completed": False},
        {"name": "Become a firefighter", "completed": False},
        {"name": "Learn to juggle", "completed": True},
        {"name": "Play the guitar more", "completed": True},
    ]

    context = {
        "goals": goals,
    }

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")