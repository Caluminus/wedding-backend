from tortoise import models, fields

class Guest(models.Model):
    id = fields.UUIDField(pk=True, unique=True)
    first_name = fields.CharField(max_length=64)
    last_name = fields.CharField(max_length=64)