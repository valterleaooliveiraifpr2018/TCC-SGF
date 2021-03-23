from django.db import models
from django.contrib.auth.models import User

SETOR_CHOICES = (
    ('1', 'Agricultura'),
    ('2', 'Infraestrutura'),
    ('3', 'Saúde'),
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


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)


class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    setor = models.CharField(
        max_length=5, choices=SETOR_CHOICES, verbose_name="Setor de Trabalho")
    telefone_celular = models.CharField(max_length=15, blank=True, null=True)
    telefone_fixo = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=14, verbose_name="RG")
    email = models.CharField(max_length=50, blank=True, null=True)
    cnh = models.CharField(max_length=13, verbose_name="CNH")

    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    
    def __str__(self):
        return "{} {} está lotado na secretaria da {} - celular para contato {}".format(self.nome, self.cargo, self.setor, self.telefoneCelular)

    class Meta:
        verbose_name="Funcionário"        
        ordering=['nome']


class Prefixo_Maquina(models.Model):
    ndescricao= models.CharField(max_length=50, verbose_name="MDescrição), help_text="Descreva a máquina em detalhes, ex: modelo, marca, nome, etc."
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Maquina")
    ano = models.CharField(max_length=50, verbose_name="Ano da Maquina")
    horimetro = models.IntegerField(verbose_name="Horimetro")
    prefixoMaquina = models.CharField(max_length=100, verbose_name="Prefixo")

    idcid = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "Maáuina {} {} ano de {}".format(self.tipo, self.nome, self.ano)

    class Meta:
        verbose_name = "Prefixo da Máquina"
        ordering = ['nome']


class Saida(models.Model):
    data_Retirada = models.DateField(verbose_name="Data Retirada")
    quatidadeRetirada = models.DecimalField(
        decimal_places=2, max_digits=5, verbose_name="Quantidade Retirada")

    idmaquina = models.ForeignKey(PrefixoMaquina, on_delete=models.PROTECT)
    idfuncionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


class Fornecedor(models.Model):

    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    nomedocontribuinte = models.CharField(
        max_length=50, verbose_name="Nome da Razão Social")
    nome = models.CharField(max_length=50, verbose_name="Funcionario")
    email = models.CharField(max_length=50, verbose_name="Email")
    telefoneCelular = models.IntegerField(verbose_name="TelefoneCelular")
    telefoneFixo = models.IntegerField(verbose_name="TelefoneFixo")
    site = models.CharField(
        max_length=50, verbose_name="URL", null=True, blank=True)
    idcid = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "fornecedor {} de cnpj n°{} email para contato {} telefone cel{}/fixo{} site http://{}".format(self.nome, self.cnpj, self.email, self.telefoneCelular, self.telefoneFixo, self.site)


class Entrada(models.Model):
    dataVenda = models.DateField(verbose_name="Data da Venda")
    idLoteProduto = models.IntegerField(verbose_name="Data da Venda")
    preco_Total = models.IntegerField(verbose_name="Preço total")
    idform = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)


class Itens_Mov(models.Model):
    saida = models.ForeignKey(Saida, on_delete=models.PROTECT)
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT)

    qtde = models.DecimalField(
        decimal_places=2, max_digits=5, verbose_name="Quantidade")
    preco = models.DecimalField(
        decimal_places=2, max_digits=5, verbose_name="Preço")
    idloteprod = models.IntegerField(verbose_name="Lote do produto")


class Produto(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Produto")
    qtdeatual = models.IntegerField(verbose_name="Quantidade atual")
    qtdemin = models.IntegerField(verbose_name="Quantidade minima")
    precoProduto = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Preço do Produto")

    saida = models.ForeignKey(Saida, on_delete=models.PROTECT)
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT)

    def __str__(self):
        return "".format(self.nome, self.qtdeatual, self.qtdemin, self.precoProduto, self.entrada.idLoteProduto)


class EmailSuport(models.Model):

    nome = models.CharField(max_length=50,
                            verbose_name="Funcionario")
    email = models.CharField(max_length=50,
                             verbose_name="Email")
    telefoneCelular = models.IntegerField(
        verbose_name="TelefoneCelular", null=True, blank=True)
    telefoneFixo = models.IntegerField(
        verbose_name="TelefoneFixo", null=True, blank=True)

    descricao = models.CharField(
        max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "".format(self.nome, self.email, self.telefoneCelular, self.telefoneFixo, self.descricao)
