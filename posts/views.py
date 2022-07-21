from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from posts.permissions import IsOwnerOrReadOnly
# Create your views here.

class WritePermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id==request.user
        
class PostList(generics.ListCreateAPIView):
    queryset=Localite.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Localite.objects.all()
    serializer_class=PostSerializer

class AffecterList(generics.ListCreateAPIView):
    queryset=Affecter.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostAffectationSerializer
    # def perform_create(self,serializer):
    #     serializer.save(owner=self.request.user)
  
class AffecterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[WritePermission]
    queryset=Affecter.objects.all()
    serializer_class=PostAffectationSerializer

class ConjointList(generics.ListCreateAPIView):
    queryset=Conjoint.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostConjointSerializer
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)
  
class ConjointDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAuthenticated]
    queryset=Affecter.objects.all()
    serializer_class=PostConjointSerializer
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)

class ChefMenageList(generics.ListCreateAPIView):
    queryset=Chef_menage.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostChefMSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChefMenageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]
    queryset=Chef_menage.objects.all()
    serializer_class=PostChefMSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EmigrationList(generics.ListCreateAPIView):
    queryset=Emigration.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EmigrationS
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)
  
class EmigrationDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Emigration.objects.all()
    serializer_class=EmigrationS
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)

class RecenserList(generics.ListCreateAPIView):
    queryset=Recenser.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=RecensementS
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)
  
class RecenserDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Recenser.objects.all()
    serializer_class=RecensementS
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)

class EnfantList(generics.ListCreateAPIView):
    queryset=Enfant.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EnfantS
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)
  
class EnfantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Enfant.objects.all()
    serializer_class=EnfantS
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)

class CommoditeList(generics.ListCreateAPIView):
    queryset=Commodite.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=CommoditeS
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)
  
class CommoditeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Commodite.objects.all()
    serializer_class=CommoditeS
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)

class EquipementList(generics.ListCreateAPIView):
    queryset=Equipement.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EquipementS
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)
  
class EquipementDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Equipement.objects.all()
    serializer_class=EquipementS
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)

class MigrantList(generics.ListCreateAPIView):
    queryset=Migrant.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=MigrantS
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)
  
class MigrantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Migrant.objects.all()
    serializer_class=MigrantS
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)

class DecesList(generics.ListCreateAPIView):
    queryset=Deces.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=DeceS
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)
  
class DecesDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Deces.objects.all()
    serializer_class=DeceS
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)

class ChargeList(generics.ListCreateAPIView):
    queryset=Charge.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostChargeSerializer
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)
  
class ChargeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Charge.objects.all()
    serializer_class=PostChargeSerializer
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)

class RecensementView(APIView):
    permission_classes=[IsAuthenticated]
    analyse={}
    def post(self,request):
        data = JSONParser().parse(request)
        if data['Chef_menage']:
            for chef_menage in data['chef_menage']:
                serializerch = PostChefMSerializer(data=chef_menage)
                if serializerch.is_valid():
                    serializerch.save()
                    analyse['capital_humain']=[chef_menage['sexes'],chef_menage['annee_naissance']]
        if data['Conjoint']:
            for conjoint in data['Conjoint']:
                serializerco = PostConjointSerializer(data=conjoint)
                if serializerco.is_valid():
                    serializerco.save()
        if data['Emigration']:
            for emigration in data['Emigration']:
                serializeremi = EmigrationS(data=emigration)
                if serializeremi.is_valid():
                    serializeremi.save()
        if data['Recenser']:
            for recenser in data['Recenser']:
                serializerr = RecensementS(data=recenser)
                if serializerr.is_valid():
                    serializerr.save()
        if data['Enfant']:
            for enfant in data['Enfant']:
                serializere=EnfantS(data=enfant)
                if serializere.is_valid():
                    serializere.save()

        if data['Charge']:
            for charge in data['Charge']:
                serializere=PostChargeSerializer(data=charge)
                if serializerg.is_valid():
                    serializerg.save()

        if data['Commodite']:
            for commodite in data['Commodite']:
                serializerc=CommoditeS(data=commodite)
                if serializerc.is_valid():
                    serializerc.save()
        if data['Equipement']:
            for equipement in data['Equipement']:
                serializereq=EquipementS(data=equipement)
                if serializereq.is_valid():
                    serializereq.save()
        if data['Migrant']:
            for migrant in data['Migrant']:
                serializerm=MigrantS(data=data['migrant'])
                if serializerm.is_valid():
                    serializerm.save()
        if data['Deces']:
            for deces in data['Deces']:
                serializerd=DeceS(data=deces)
                if serializerd.is_valid():
                    serializerd.save()
            return JsonResponse(serializerp.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 