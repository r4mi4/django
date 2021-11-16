from rest_framework import serializers

from .models import Person


# class PersonSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     age = serializers.IntegerField()
#     email = serializers.EmailField()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email')
        extra_kwargs = {
            'email': {'write_only': True}
        }

    def validate_name(self, value):
        if value == 'admin':
            raise serializers.ValidationError("the name cant be admin !")
        return value
