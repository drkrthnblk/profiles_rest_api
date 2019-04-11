from rest_framework import serializers

# for model serializer
from . import models

class HelloSerializer(serializers.Serializer):
    """
        Serializes a name for testing our APIView
    """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """
        à SERIALIZER FOR OUR USER PROFILE OBJECTS
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """
            create and  return a new user
        """
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

