from django.db import models

class Text(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True, db_index=True)
