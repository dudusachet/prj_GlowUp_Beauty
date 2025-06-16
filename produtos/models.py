from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.categoria.nome} > {self.nome}"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    validade = models.DateField()
    cor = models.CharField(max_length=50)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome
