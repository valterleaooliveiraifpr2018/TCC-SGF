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
UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)

# Create your models here.

class Cidade(models.Model):
    
    nome = models.CharField(max_length=50)
    estado = models.CharField(choices=UF_CHOICES, max_length=50)
    
    
    def __str__(self):
        return "{}/{}".format(self.nome, self.estado)


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
        return "{}/Prefixo: {} ({})".format(self.descricao, self.prefixo, self.ano)

    class Meta:
        verbose_name = "Máquina"
        ordering = ['-ano']


class Controle_Maquina(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    ultimo_horimetro = models.IntegerField(verbose_name="Último Horimetro")

    def __str__(self):
        return "Máquina: {}/Prefixo: {} ({})Horimetro atual: {} / Ultimo Horimetro: {}".format(self.maquina.descricao, self.maquina.prefixo, self.maquina.ano, self.maquina.horimetro, self.ultimo_horimetro)

    class Meta:
        verbose_name = "Máquina"
        

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
        return "CNPJ:{} -- {}".format(self.cnpj, self.nome_fantasia)


class Produto(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome ou descrição do produto.")
    quantidade_atual = models.DecimalField(decimal_places=2, max_digits=6, help_text="Essa quantidade vai ser atualizada pelo movimento de entrada e saída.")
    quantidade_minima = models.IntegerField(verbose_name="Quantidade mínima", 
        help_text="Informe a quantidade mínima para gerar um alerta de estoque.")
    def __str__(self):
        return "{} - Estoque atual: {}".format(self.nome, self.quantidade_atual)


class Entrada(models.Model):
    # detalhes = models.ForeignKey(Produto, on_delete=models.PROTECT)
    detalhes = models.CharField(max_length=100, help_text="Informe mais detalhes da entrada, como NF, Nº do Pedido, etc.")
    data = models.DateField(verbose_name="Data de entrada")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    valor_total = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return "Id: {} - {}/{}".format(self.pk, self.detalhes, self.data)

    class Meta:
        verbose_name = "Movimentação da entrada"


class Produtos_Entrada(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Preço unitário")

    def __str__(self):
        return "Produto '{}' da Entrada #'{}'".format(self.produto.nome, self.entrada.pk)


class Saida(models.Model):
    # detalhes = models.ForeignKey(Produtos_Entrada, on_delete=models.PROTECT)
    detalhes = models.CharField(max_length=100, help_text="Informe mais detalhes da saída, Nº do Pedido, Ordem de serviço, etc.")
    data = models.DateField(auto_now_add=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT, verbose_name="máquina")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, help_text="Informe o funcionário que fez esta solicitação de saída.")
    
    def __str__(self):
        return "Id: {} - {}/{}".format(self.pk, self.detalhes, self.data)

    class Meta:
        verbose_name = "Movimentação de retirada/saída"
        ordering = ["-pk"]
    

class Produtos_Saida(models.Model):
    saida = models.ForeignKey(Saida, on_delete= models.PROTECT) 
    produto = models.ForeignKey(Produto, on_delete= models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Quantidade retirada")
    
    def __str__(self):
        return "Produto '{}' da Saída #'{}'".format(self.produto.nome, self.saida.pk)
