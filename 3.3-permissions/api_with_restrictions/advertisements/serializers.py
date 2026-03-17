from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class AdvertisementSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # было creator

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'author',  # было creator
                  'status', 'created_at')

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user  # было creator
        return super().create(validated_data)

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        
        if request.method == 'POST':
            open_ads_count = Advertisement.objects.filter(
                author=user,  # было creator
                status='OPEN'
            ).count()
            
            if open_ads_count >= 10:
                raise serializers.ValidationError(
                    'У пользователя не может быть больше 10 открытых объявлений'
                )
        return data