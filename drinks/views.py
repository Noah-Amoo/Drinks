from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):

    #Step 1: get all the drinks
    drinks = Drink.objects.all()
    
    #Step 2: serialize them
    serializer = DrinkSerializer(drinks, many=True)

    #Step 3: return json
    return JsonResponse(serializer.data)