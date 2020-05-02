from django.contrib.auth import get_user_model , authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """user object serializer"""
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = get_user_model()
        fields = ('email','password','name','last','username','created_at')
        extra_kwargs = {'password':{'write_only': True, 'min_length': 8}}
        
    def create(self, validated_data):
        """ Create new user + encrypt password """
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """update user"""
        password = validated_data.pop('password', None)
        user = super().update(instance,validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user
    
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )
    
    def validate(self , attrs):
        """ Validate and authenticate the user"""
        email= attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            username= email,
            password= password
        )
        if not user:
            msg = _('Unable to authenticate credentials')
            raise serializers.ValidationError(msg, code='authetication')
        
        attrs['user'] = user
        return attrs