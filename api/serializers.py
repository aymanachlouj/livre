from rest_framework import serializers
from .models import Livre

class LivreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['titre','auteur','description','image']