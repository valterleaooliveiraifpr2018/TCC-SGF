from django.db import models
from django.contrib.auth.models import User

SETOR_CHOICES = (
    ('1', 'Agricultura'),
    ('2', 'Infraestrutura'),
    ('3', 'Saúde'),
)


CARGO_CHOICES = (
    ('1', 'Operador de Maquinas Pesadas'),
    ('2', 'Administrativos'),
    ('3', 'Ajudante Geral'),
)


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{}/{}".format(self.nome, self.estado)


# class Cargo(models.Model):

#     def __str__(self):
#         return "{}".format(self.nome)


class Funcionario(models.Model):
    cargo = models.CharField(max_length=5, choices=CARGO_CHOICES, verbose_name="Cargo do Trabalhador")

    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    setor = models.CharField(max_length=5, choices=SETOR_CHOICES, verbose_name="Setor de Trabalho")
    telefone_celular = models.CharField(max_length=15, blank=True, null=True)
    telefone_fixo = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=14, verbose_name="RG")
    email = models.CharField(max_length=50, blank=True, null=True)
    cnh = models.CharField(max_length=13, verbose_name="CNH")
    # cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} -- {}/{}".format(self.nome, self.cargo, self.setor, self.cidade)

    class Meta:
        verbose_name = "Funcionário"        
        ordering = ['nome']


class Maquina(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição", 
        help_text="Descreva a máquina em detalhes, ex: modelo, marca, nome, etc.")
    ano = models.CharField(max_length=4, verbose_name="Ano da Máquina")
    horimetro = models.IntegerField(verbose_name="Horímetro")
    prefixo = models.CharField(max_length=50, help_text="Identificação da máquina, placa, número, etc.")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "Máquina: {}/{} ({})".format(self.descricao, self.prefixo, self.ano)

    class Meta:
        verbose_name = "Máquina"
        ordering = ['-ano']


class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    razao_social = models.CharField(max_length=50, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=50, verbose_name="Nome Fantasia")
    vendedor = models.CharField(max_length=50, verbose_name="Nome do vendedor")
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    site = models.CharField(max_length=50, verbose_name="URL do Site", null=True, blank=True)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} -- {}".format(self.cnpj, self.nome_fantasia)


class Produto(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome ou descrição do produto.")
    quantidade_atual = models.DecimalField(decimal_places=2, max_digits=6, help_text="Essa quantidade vai ser atualizada pelo movimento de entrada e saída.")
    quantidade_minima = models.IntegerField(verbose_name="Quantidade mínima", 
        help_text="Informe a quantidade mínima para gerar um alerta de estoque.")
    def __str__(self):
        return "{}".format(self.nome)


class Entrada(models.Model):
    detalhes = models.CharField(max_length=100, help_text="Informe mais detalhes da entrada, como NF, Nº do Pedido, etc.")
    data = models.DateField(verbose_name="Data de entrada")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    valor_total = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return "#{} - {}/{}".format(self.pk, self.detalhes, self.data)

    class Meta:
        verbose_name = "Movimentação da entrada"



class Produtos_Entrada(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Preço unitário")


class Saida(models.Model):
    detalhes = models.CharField(max_length=100, help_text="Informe mais detalhes da saída, Nº do Pedido, Ordem de serviço, etc.")
    data = models.DateField(auto_now_add=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT, verbose_name="máquina")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, help_text="Informe o funcionário que fez esta solicitação de saída.")
    
    def __str__(self):
        return "#{} - {}/{}".format(self.pk, self.detalhes, self.data)

    class Meta:
        verbose_name = "Movimentação de retirada/saída"
    

class Produtos_Saida(models.Model):
    saida = models.ForeignKey(Saida, on_delete= models.PROTECT) 
    produto = models.ForeignKey(Produto, on_delete= models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Quantidade retirada")
    




# class Itens_Mov(models.Model):
#     saida = models.ForeignKey(Saida, on_delete=models.PROTECT)
#     entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT)

#     qtde = models.DecimalField(
#         decimal_places=2, max_digits=5, verbose_name="Quantidade")
#     preco = models.DecimalField(
#         decimal_places=2, max_digits=5, verbose_name="Preço")
#     idloteprod = models.IntegerField(verbose_name="Lote do produto")



# class EmailSuport(models.Model):

#     nome = models.CharField(max_length=50,
#                             verbose_name="Funcionario")
#     email = models.CharField(max_length=50,
#                              verbose_name="Email")
#     telefoneCelular = models.IntegerField(
#         verbose_name="TelefoneCelular", null=True, blank=True)
#     telefoneFixo = models.IntegerField(
#         verbose_name="TelefoneFixo", null=True, blank=True)

#     descricao = models.CharField(
#         max_length=150, verbose_name="Descrição")

#     def __str__(self):
#         return "".format(self.nome, self.email, self.telefoneCelular, self.telefoneFixo, self.descricao)

