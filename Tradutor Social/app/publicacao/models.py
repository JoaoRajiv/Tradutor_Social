from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    CLASSIFICACAO = (
        (1,'Iniciante'),
        (2,'Experiente'),
        (3,'Mestre do inglês'),
    )

    age = models.IntegerField(verbose_name='Idade', null=True)
    scholarity= models.CharField(max_length=150 , verbose_name='Escolaridade')
    points= models.IntegerField(verbose_name="Pontos", default = '0', null=True)
    rank = models.IntegerField(choices = CLASSIFICACAO, default= 1, verbose_name='Rank', null=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Publication(models.Model):

    account = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Conta', related_name='Account')
    text_p =  models.TextField(verbose_name='Texto', null=True)
    text_e = models.TextField(verbose_name='Texto Inglês', null=True)
    data = models.DateTimeField(auto_now_add= True, null= True)
    
    def __str__(self):
        return ('Publicação de ' f'{self.account.username}'' as 'f'{self.data}')

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

class Correction(models.Model):
    
    corrector = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name='Comentarista')
    publications = models.ManyToManyField(Publication)
    correction = models.TextField(verbose_name='Correção', null=True)
    data = models.DateTimeField(auto_now_add= True, null= True)

    def __str__(self):
        return f'{self.data}'
    
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários' 


class Evaluation(models.Model):

    AVALIACAO = [
        (1,'Like'),
        (2,'Deslike')
    ]
    name= models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank= True, verbose_name='Avaliador', related_name='Avaliação')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null = True, blank= True, verbose_name="Publicação")
    avaliation= models.IntegerField(choices = AVALIACAO, verbose_name='Avaliação')
    

    def __str__(self):
        return ('Avaliação de ' f'{self.name.user.username}')
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'  





