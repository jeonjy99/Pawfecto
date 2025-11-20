from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Campaign, CampaignAcceptance, Deliverable
from .serializers import CampaignListSerializer, CampaignSerializer, CampaignAcceptanceSerializer, DeliverableSerializer

# Create your views here.
# @api_view(['GET'])
# def brand_list(request):
#     if request.method == 'GET':
#         brand = AccountBrand.objects.all()
#         serializer = AccountBrandSerializer(brand, many=True)
#         return Response(serializer.data)

# def index(request):

#     return render(request, 'myapp/index.html')


@api_view(['GET', 'POST'])
def campaign_list(request):
    if request.method == "GET":
        campaigns = Campaign.objects.all()
        serializer = CampaignListSerializer(campaigns, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print(request.data)
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
