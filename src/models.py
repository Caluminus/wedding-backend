from tortoise import models, fields

class MealType(models.Model):
    name = fields.CharField(max_length=64)

class Meal(models.Model):
    name = fields.CharField(max_length=255)
    type = fields.ForeignKeyField('models.MealType')

class Guest(models.Model):
    id = fields.UUIDField(pk=True, unique=True)
    first_name = fields.CharField(max_length=64)
    last_name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=255)
    extra_guests = fields.ManyToManyField('models.Guest')
    coming = fields.BooleanField(default=False)
    travel_needs = fields.CharField(max_length=65535, null=True)
    meals = fields.ManyToManyField("models.Meal")
