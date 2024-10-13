from tortoise import fields, models


class Event(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "event"
