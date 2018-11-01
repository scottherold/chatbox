from django.db import models
from ..users.models import User

# Create your models here.
class PokeManager(models.Manager):
    def add_poke(self, form):        
        poke_user = User.objects.get(id=form['poke_user_id'])
        poke_from = User.objects.get(id=form['user_id'])
        try:
            add_poke = self.get(poke_from=poke_from, poke_user=poke_user)
            add_poke.poke_count += 1
            add_poke.save()
            poke_user.total_pokes +=1
            poke_user.save()
            print(add_poke.__dict__)

        except:
            self.create(poke_from=poke_from, poke_user=poke_user, poke_count=1)
            poke_user.total_pokes +=1
            poke_user.save()


class Poke(models.Model):
    poke_from = models.ForeignKey(User, related_name="poked_from_user")
    poke_user = models.ForeignKey(User, related_name="poked_user")
    poke_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PokeManager()