from django.db import models

# Create your models here.

class Medicament(models.Model):
    medicament = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.medicament

class FormeMed(models.Model): # examples: pillule, comprimé
    forme_med = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.forme_med

class Unite(models.Model): # examples: goutte, Litre
    unite = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.unite

class Quantite(models.Model): # examples: Boite, plaquette
    qte = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.qte

class Ordonnance(models.Model):
    centre_soins = models.CharField(max_length=150, null=True)
    medecin = models.CharField(max_length=150, null=True)
    patient = models.CharField(max_length=150, null=True)
    medicament1 = models.ForeignKey(Medicament, related_name='medicament1', on_delete=models.CASCADE)
    medicament2 = models.ForeignKey(Medicament, related_name='medicament2', on_delete=models.CASCADE, null=True)
    medicament3 = models.ForeignKey(Medicament, related_name='medicament3', on_delete=models.CASCADE, null=True)
    medicament4 = models.ForeignKey(Medicament, related_name='medicament4', on_delete=models.CASCADE, null=True)
    medicament5 = models.ForeignKey(Medicament, related_name='medicament5', on_delete=models.CASCADE, null=True)
    medicament6 = models.ForeignKey(Medicament, related_name='medicament6', on_delete=models.CASCADE, null=True)
    medicament7 = models.ForeignKey(Medicament, related_name='medicament7', on_delete=models.CASCADE, null=True)
    medicament8 = models.ForeignKey(Medicament, related_name='medicament8', on_delete=models.CASCADE, null=True)
    medicament9 = models.ForeignKey(Medicament, related_name='medicament9', on_delete=models.CASCADE, null=True)
    medicament10 = models.ForeignKey(Medicament, related_name='medicament10', on_delete=models.CASCADE, null=True)
    forme_med1 = models.ForeignKey(FormeMed, related_name='form_med1', on_delete=models.CASCADE)
    forme_med2 = models.ForeignKey(FormeMed, related_name='form_med2', on_delete=models.CASCADE, null=True)
    forme_med3 = models.ForeignKey(FormeMed, related_name='form_med3', on_delete=models.CASCADE, null=True)
    forme_med4 = models.ForeignKey(FormeMed, related_name='form_med4', on_delete=models.CASCADE, null=True)
    forme_med5 = models.ForeignKey(FormeMed, related_name='form_med5', on_delete=models.CASCADE, null=True)
    forme_med6 = models.ForeignKey(FormeMed, related_name='form_med6', on_delete=models.CASCADE, null=True)
    forme_med7 = models.ForeignKey(FormeMed, related_name='form_med7', on_delete=models.CASCADE, null=True)
    forme_med8 = models.ForeignKey(FormeMed, related_name='form_med8', on_delete=models.CASCADE, null=True)
    forme_med9 = models.ForeignKey(FormeMed, related_name='form_med9', on_delete=models.CASCADE, null=True)
    forme_med10 = models.ForeignKey(FormeMed, related_name='form_med10', on_delete=models.CASCADE, null=True)
    prise_min1 = models.FloatField()
    prise_min2 = models.FloatField(null=True)
    prise_min3 = models.FloatField(null=True)
    prise_min4 = models.FloatField(null=True)
    prise_min5 = models.FloatField(null=True)
    prise_min6 = models.FloatField(null=True)
    prise_min7 = models.FloatField(null=True)
    prise_min8 = models.FloatField(null=True)
    prise_min9 = models.FloatField(null=True)
    prise_min10 = models.FloatField(null=True)
    prise_max1 = models.FloatField()
    prise_max2 = models.FloatField(null=True)
    prise_max3 = models.FloatField(null=True)
    prise_max4 = models.FloatField(null=True)
    prise_max5 = models.FloatField(null=True)
    prise_max6 = models.FloatField(null=True)
    prise_max7 = models.FloatField(null=True)
    prise_max8 = models.FloatField(null=True)
    prise_max9 = models.FloatField(null=True)
    prise_max10 = models.FloatField(null=True)
    unite1 = models.ForeignKey(Unite, related_name='unite1', on_delete=models.CASCADE)
    unite2 = models.ForeignKey(Unite, related_name='unite2', on_delete=models.CASCADE, null=True)
    unite3 = models.ForeignKey(Unite, related_name='unite3', on_delete=models.CASCADE, null=True)
    unite4 = models.ForeignKey(Unite, related_name='unite4', on_delete=models.CASCADE, null=True)
    unite5 = models.ForeignKey(Unite, related_name='unite5', on_delete=models.CASCADE, null=True)
    unite6 = models.ForeignKey(Unite, related_name='unite6', on_delete=models.CASCADE, null=True)
    unite7 = models.ForeignKey(Unite, related_name='unite7', on_delete=models.CASCADE, null=True)
    unite8 = models.ForeignKey(Unite, related_name='unite8', on_delete=models.CASCADE, null=True)
    unite9 = models.ForeignKey(Unite, related_name='unite9', on_delete=models.CASCADE, null=True)
    unite10 = models.ForeignKey(Unite, related_name='unite10', on_delete=models.CASCADE, null=True)
    qte1 = models.ForeignKey(Quantite, related_name='qte1', on_delete=models.CASCADE)
    qte2 = models.ForeignKey(Quantite, related_name='qte2', on_delete=models.CASCADE, null=True)
    qte3 = models.ForeignKey(Quantite, related_name='qte3', on_delete=models.CASCADE, null=True)
    qte4 = models.ForeignKey(Quantite, related_name='qte4', on_delete=models.CASCADE, null=True)
    qte5 = models.ForeignKey(Quantite, related_name='qte5', on_delete=models.CASCADE, null=True)
    qte6 = models.ForeignKey(Quantite, related_name='qte6', on_delete=models.CASCADE, null=True)
    qte7 = models.ForeignKey(Quantite, related_name='qte7', on_delete=models.CASCADE, null=True)
    qte8 = models.ForeignKey(Quantite, related_name='qte8', on_delete=models.CASCADE, null=True)
    qte9 = models.ForeignKey(Quantite, related_name='qte9', on_delete=models.CASCADE, null=True)
    qte10 = models.ForeignKey(Quantite, related_name='qte10', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.patient + ' ' + self.medecin + ' ' + self.centre_soins
