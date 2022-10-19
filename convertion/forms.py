from django import forms
from .models import *

class OrdonnanceForm(forms.ModelForm):
    
    class Meta: 
        model = Ordonnance
        fields = ['centre_soins','medecin','patient','medicament1','medicament2','medicament3','medicament4','medicament5',
                    'medicament6','medicament7','medicament8','medicament9','medicament10','forme_med1','forme_med2',
                    'forme_med3','forme_med4','forme_med5','forme_med6','forme_med7','forme_med8','forme_med9','forme_med10',
                    'prise_min1','prise_min2','prise_min3','prise_min4','prise_min5','prise_min6','prise_min7','prise_min8',
                    'prise_min9','prise_min10','prise_max1','prise_max2','prise_max3','prise_max4','prise_max5','prise_max6',
                    'prise_max7','prise_max8','prise_max9','prise_max10','unite1','unite2','unite3','unite4','unite5','unite6',
                    'unite7','unite8','unite9','unite10','qte1','qte2','qte3','qte4','qte5','qte6','qte7','qte8','qte9','qte10']
        labels = {
            'centre_soins': 'Centre Soins',
            'medecin': 'Medecin',
            'patient': 'Patient',
            'medicament1': 'Médicament 1',
            'medicament2': 'Médicament 2',
            'medicament3': 'Médicament 3',
            'medicament4': 'Médicament 4',
            'medicament5': 'Médicament 5',
            'medicament6': 'Médicament 6',
            'medicament7': 'Médicament 7',
            'medicament8': 'Médicament 8',
            'medicament9': 'Médicament 9',
            'medicament10': 'Médicament 10',
            'forme_med1': 'Forme',
            'forme_med2': 'Forme',
            'forme_med3': 'Forme',
            'forme_med4': 'Forme',
            'forme_med5': 'Forme',
            'forme_med6': 'Forme',
            'forme_med7': 'Forme',
            'forme_med8': 'Forme',
            'forme_med9': 'Forme',
            'forme_med10': 'Forme',
            'prise_min1': 'Min jour/semaine/mois',
            'prise_min2': 'Min jour/semaine/mois',
            'prise_min3': 'Min jour/semaine/mois',
            'prise_min4': 'Min jour/semaine/mois',
            'prise_min5': 'Min jour/semaine/mois',
            'prise_min6': 'Min jour/semaine/mois',
            'prise_min7': 'Min jour/semaine/mois',
            'prise_min8': 'Min jour/semaine/mois',
            'prise_min9': 'Min jour/semaine/mois',
            'prise_min10': 'Min jour/semaine/mois',
            'prise_max1': 'Max jour/semaine/mois',
            'prise_max2': 'Max jour/semaine/mois',
            'prise_max3': 'Max jour/semaine/mois',
            'prise_max4': 'Max jour/semaine/mois',
            'prise_max5': 'Max jour/semaine/mois',
            'prise_max6': 'Max jour/semaine/mois',
            'prise_max7': 'Max jour/semaine/mois',
            'prise_max8': 'Max jour/semaine/mois',
            'prise_max9': 'Max jour/semaine/mois',
            'prise_max10': 'Max jour/semaine/mois',
            'unite1': 'Type de mesure',
            'unite2': 'Type de mesure',
            'unite3': 'Type de mesure',
            'unite4': 'Type de mesure',
            'unite5': 'Type de mesure',
            'unite6': 'Type de mesure',
            'unite7': 'Type de mesure',
            'unite8': 'Type de mesure',
            'unite9': 'Type de mesure',
            'unite10': 'Type de mesure',
            'qte1': 'Quantité par prise',
            'qte2': 'Quantité par prise',
            'qte3': 'Quantité par prise',
            'qte4': 'Quantité par prise',
            'qte5': 'Quantité par prise',
            'qte6': 'Quantité par prise',
            'qte7': 'Quantité par prise',
            'qte8': 'Quantité par prise',
            'qte9': 'Quantité par prise',
            'qte10': 'Quantité par prise',
        }

    def __init__(self, *args, **kwargs):
            super(OrdonnanceForm,self).__init__(*args, **kwargs)
            self.fields['medicament1'].empty_label = "Choisir"
            self.fields['medicament2'].empty_label = "Choisir"
            self.fields['medicament3'].empty_label = "Choisir"
            self.fields['medicament4'].empty_label = "Choisir"
            self.fields['medicament5'].empty_label = "Choisir"
            self.fields['medicament6'].empty_label = "Choisir"
            self.fields['medicament7'].empty_label = "Choisir"
            self.fields['medicament8'].empty_label = "Choisir"
            self.fields['medicament9'].empty_label = "Choisir"
            self.fields['medicament10'].empty_label = "Choisir"
            self.fields['forme_med1'].empty_label = "Choisir"
            self.fields['forme_med2'].empty_label = "Choisir"
            self.fields['forme_med3'].empty_label = "Choisir"
            self.fields['forme_med4'].empty_label = "Choisir"
            self.fields['forme_med5'].empty_label = "Choisir"
            self.fields['forme_med6'].empty_label = "Choisir"
            self.fields['forme_med7'].empty_label = "Choisir"
            self.fields['forme_med8'].empty_label = "Choisir"
            self.fields['forme_med9'].empty_label = "Choisir"
            self.fields['forme_med10'].empty_label = "Choisir"
            self.fields['unite1'].empty_label = "Choisir"
            self.fields['unite2'].empty_label = "Choisir"
            self.fields['unite3'].empty_label = "Choisir"
            self.fields['unite4'].empty_label = "Choisir"
            self.fields['unite5'].empty_label = "Choisir"
            self.fields['unite6'].empty_label = "Choisir"
            self.fields['unite7'].empty_label = "Choisir"
            self.fields['unite8'].empty_label = "Choisir"
            self.fields['unite9'].empty_label = "Choisir"
            self.fields['unite10'].empty_label = "Choisir"
            self.fields['qte1'].empty_label = "Choisir"
            self.fields['qte2'].empty_label = "Choisir"
            self.fields['qte3'].empty_label = "Choisir"
            self.fields['qte4'].empty_label = "Choisir"
            self.fields['qte5'].empty_label = "Choisir"
            self.fields['qte6'].empty_label = "Choisir"
            self.fields['qte7'].empty_label = "Choisir"
            self.fields['qte8'].empty_label = "Choisir"
            self.fields['qte9'].empty_label = "Choisir"
            self.fields['qte10'].empty_label = "Choisir"

class MedicamentForm(forms.ModelForm):
    
    class Meta:
        model = Medicament
        fields = ['medicament']
        labels = {
            'medicament': 'Médicament',
        }

class FormeMedForm(forms.ModelForm):
    
    class Meta:
        model = FormeMed
        fields = ['forme_med']
        labels = {
            'forme_med': 'Forme',
        }

class UniteForm(forms.ModelForm):
    
    class Meta:
        model = Unite
        fields = ['unite']
        labels = {
            'unite': 'Unite',
        }

class QuantiteForm(forms.ModelForm):
    
    class Meta:
        model = Quantite
        fields = ['qte']
        labels = {
            'qte': 'Qté',
        }