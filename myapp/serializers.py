from rest_framework import serializers

from .models import Campaign, CampaignAcceptance, Deliverable
from django.contrib.auth import get_user_model


User = get_user_model()

class BrandInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'brand_pet_focus', )

class CampaignListSerializer(serializers.ModelSerializer):
    brand = BrandInfoSerializer(read_only=True)
    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignAcceptance
        fields = '__all__'


class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = '__all__'

