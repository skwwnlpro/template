from tortoise import fields, models


class Movie(models.Model):
    movie_id = fields.BigIntField(pk=True)
    movie_name = fields.CharField(max_length=255)

    class Meta:
        table = "movie"
