from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#tabela

class Evento(models.Model):
    # campos da tabela tipo chracter, text e data
    titutlo = models.CharField(max_length=100)
    #pode ser em branco(blank) ou vazio(null)
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # auto_now atualiza sempre para a hora atual
    data_criacao = models.DateTimeField(auto_now=True)
    # modifica uma classe para usar como delete através da foreign key
    # on_delete = models.CASCADE para excluir os eventos do usuario
    # escolher 1, valor 1 (admin), setar 1
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #classe para nomear a tabela
    class Meta:
        db_table = 'evento'
    
    #função para nomear objeto do evento

    def __str__(self):
        return self.titutlo
    
    # formatar a data e hora para pt-br
    def get_data_evento(self):
        return self.data_evento.strftime('%d-%m-%Y %H:%M')