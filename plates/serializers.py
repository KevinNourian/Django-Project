from rest_framework import serializers
from .models import Plate

class PlateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Plate
		fields = ('id', 'url', 'first_name', 'last_name', 'letters', 'numbers')