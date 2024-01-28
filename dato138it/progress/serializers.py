from rest_framework import serializers
from .models import Progress
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
class ProgressSerializer(serializers.ModelSerializer):
	user=serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model=Progress
		fields="__all__"
