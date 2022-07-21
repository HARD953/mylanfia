from rest_framework import serializers
from .models import *

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localite
        fields = '__all__'

class PostAffectationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Affecter
        fields ='__all__'

class PostConjointSerializer(serializers.HyperlinkedModelSerializer):
    owner1 = serializers.ReadOnlyField(source='owner1.user_name')
    class Meta:
        model = Conjoint
        fields=['owner1','id','url','nom','prenom','annee_naissance','lieu_de_naissance','nationalite','numero_cni','sexes','ethnie','numero','niveau_etude','occupation','idc']

class PostChargeSerializer(serializers.HyperlinkedModelSerializer):
    owner9 = serializers.ReadOnlyField(source='owner9.user_name')
    class Meta:
        model = Charge
        fields=['owner9','id','url','nom','prenom','annee_naissance','lieu_de_naissance','nationalite','numero_cni','sexes','ethnie','numero','niveau_etude','occupation','parentg']

class PostChefMSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = Chef_menage
        fields=['owner','id','url','nom','prenom','annee_naissance','lieu_de_naissance','nationalite','numero_cni','sexes','ethnie','numero','type_menage','nombre_enfant','nombre_enfant_v','nom_personne_charge','emigre']

class EmigrationS(serializers.HyperlinkedModelSerializer):
    owner2 = serializers.ReadOnlyField(source='owner2.user_name')
    class Meta:
        model = Emigration
        fields =['owner2','id','url','parentd','sexesd','date_depart','motif','age_depart']

class RecensementS(serializers.HyperlinkedModelSerializer):
    owner3 = serializers.ReadOnlyField(source='owner3.user_name')
    class Meta:
        model = Recenser
        fields=['url','id','branche_activite','situation_occupation','occupation_actuelle','status_occupation','niveau_instruction','alphabetisation','survie_de_pere','survie_de_mere','handicap','religion','nombre_enfant_v','parent','owner3','situation_matrimoniale','nombre_enfant']
        
class EnfantS(serializers.HyperlinkedModelSerializer):
    owner4 = serializers.ReadOnlyField(source='owner4.user_name')
    class Meta:
        model = Enfant
        fields=['owner4','url','nom','prenom','annee_naissance','lieu_de_naissance','nationalite','numero_cni','sexes','ethnie','numero','parentf','ecolier']

class CommoditeS(serializers.HyperlinkedModelSerializer):
    owner5 = serializers.ReadOnlyField(source='owner5.user_name')
    class Meta:
        model = Commodite
        fields =['owner5','id','url','loyer','evacuation_eau','evacuation_ordure','cuisson','eclairage','temps_acces_eau','parentc','nombre_piece','nombre_piece_dormir','nature_mur','nature_toit','lieu_aisance','nature_sol','alimentation_eau']

class EquipementS(serializers.HyperlinkedModelSerializer):
    owner6 = serializers.ReadOnlyField(source='owner6.user_name')
    class Meta:
        model = Equipement
        fields =['owner6','id','url','parente','moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']

class MigrantS(serializers.HyperlinkedModelSerializer):
    owner7 = serializers.ReadOnlyField(source='owner7.user_name')
    class Meta:
        model = Migrant
        fields =['owner7','id','url','parentm','deplace','lieu_residence_a','annee_deplace','intention_ret']

class DeceS(serializers.HyperlinkedModelSerializer):
    owner8 = serializers.ReadOnlyField(source='owner8.user_name')
    class Meta:
        model = Deces
        fields =['owner8','id','url','parentd','sexesd','age_deces','nom_decede','prenom_decede','annee_deces']
