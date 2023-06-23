from django.db import models
from django.utils.translation import gettext_lazy as _

class Restaurant(models.Model):
    id = models.IntegerField(_("id"), primary_key=True)
    name = models.CharField(_("name"), max_length=100)
    location = models.CharField(_("location"), max_length=100)
    items = models.TextField(_("items"))
    lat_long = models.CharField(_("lat_long"), max_length=100)
    full_details = models.TextField(_("full_details"))
