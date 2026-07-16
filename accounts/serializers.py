from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username','password','confirm_password']
        
        
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'Message' : 'Password does not match'
            })   
        return attrs
    
    
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data.get('username', ''),
            email = validated_data.get('email', ''),
            password = validated_data['password'],
        )
        
        return user