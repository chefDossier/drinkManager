from django.db import models

# Create your models here.

# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('client', 'Client'),
#         ('entreprise', 'Entreprise'),
#         ('admin', 'Administrateur'),
#     )
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

#     def __str__(self):
#         return f"{self.username} ({self.get_user_type_display()})"
#je travaille sur next js 14 j'aimerais aue tu me fournissent un code pour ma page.tsx qui me permettra d'avoir une interface que demande a l'utilisateur son type et qui dissimule le formulaire qui le correspond pour son  
class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_d_embauche = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateField()
    employe = models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Commande {self.id} - {self.date_commande}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Approvisionnement(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_approvisionnement = models.DateField()
    quantite = models.IntegerField()

    def __str__(self):
        return f"Approvisionnement {self.id} - {self.date_approvisionnement}"