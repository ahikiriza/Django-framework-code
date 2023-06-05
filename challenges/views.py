from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# from django.template.loader import render_to_string
# Create your views here.

# def index(request):
#     return HttpResponse("This works!")

# def display_month(request):
#     return HttpResponse("February works!")

# def march(request):
#     return HttpResponse("March works!")
monthly_challenges={
    "january": "This works",
    "february": "february works",
    "march": "april works",
    "april": "april works",
    "may": "april works",
    "june": "april works",
    "july": "april works",
    "august": "april works",
    "september": "april works",
    "october": "april works",
    "november": "april works",
    "december": "april works"   
    
}

# def index(request):
#     response_data = """
#         <ul>
#             <li><a href="/challenges/january">January</li>
#         </ul>    
    
#     """
#     return HttpResponse()


def monthly_challenge_by_number(request, month):
    months =list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month =months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    # try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
        # response_data =render_to_string("challenges/challenge.html")
        # # response_data =f"<h1>{challenge_text}</h1>"
        # return HttpResponse(response_data)
    # except:
        # return HttpResponseNotFound("<h1>This month is not supported</h1>")
    