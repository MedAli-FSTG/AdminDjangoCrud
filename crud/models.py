from django.db import models

# Create your models here.


class motif(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=40)
    motif_Img = models.ImageField(upload_to='images/')
    description = models.TextField()

    class Meta:
        db_table = "motifs"
