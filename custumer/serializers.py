from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    list_chef_menage = serializers.HyperlinkedRelatedField(many=True, view_name='chef_menage-detail',read_only=True)
    list_equipement = serializers.HyperlinkedRelatedField(many=True, view_name='equipement-detail',read_only=True)
    list_commodite = serializers.HyperlinkedRelatedField(many=True, view_name='commodite-detail',read_only=True)
    list_emigration = serializers.HyperlinkedRelatedField(many=True, view_name='emigration-detail',read_only=True)
    list_enfant = serializers.HyperlinkedRelatedField(many=True, view_name='enfant-detail',read_only=True)
    list_deces = serializers.HyperlinkedRelatedField(many=True, view_name='deces-detail',read_only=True)
    list_migrant = serializers.HyperlinkedRelatedField(many=True, view_name='migrant-detail',read_only=True)
    list_conjoint = serializers.HyperlinkedRelatedField(many=True, view_name='conjoint-detail',read_only=True)
    list_recenser = serializers.HyperlinkedRelatedField(many=True, view_name='recenser-detail',read_only=True)
    list_charge = serializers.HyperlinkedRelatedField(many=True, view_name='charge-detail',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = NewUser
        fields=['email','user_name','first_name','password','adresse','city','about_me','is_active','is_staff','is_superuser','owner','list_chef_menage','list_equipement','list_commodite','list_emigration','list_enfant','list_deces','list_migrant','list_conjoint','list_recenser','list_charge']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance