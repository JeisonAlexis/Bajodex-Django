from django.db import models

class babosas(models.Model):

    tipo =(

        ('1', 'Malvadas'),
        ('2', 'Elementales'),
        ('3', 'Megamorficas'),
        ('4', 'Guardianas'), 
        ('5', 'Extra')
    )

    elemento =(

        ('1', 'Aire'),
        ('2', 'Tierra'),
        ('3', 'Fuego'),
        ('4', 'Energia'), 
        ('5', 'Agua'),
        ('6', 'Desconocido')
    )

    codigoBabosa = models.CharField('Codigo Babosa', max_length=10, unique=True)
    NombreBabosa = models.CharField('Nombre Babosa', max_length=100, unique=True)
    tipoBabosa = models.CharField('Tipo Babosa', max_length=1, choices=tipo)
    elementoBabosa = models.CharField('Elemento Babosa', max_length=1, choices=elemento)

    Protoforma = models.ImageField(upload_to='protoforma', blank=True, null=True)
    Transformacion = models.ImageField(upload_to='transformacion', blank=True, null=True)

    def getTipo(self)->str:
        rta = 'Malvada'
        if(self.tipoBabosa  == '2'):
            rta= 'Elemental'
        if(self.tipoBabosa  == '3'):
            rta = 'Megamorfica'
        if(self.tipoBabosa  == '4'):
            rta = 'Guardiana'
        if(self.tipoBabosa  == '5'):
            rta = 'Extra'
        return rta
    
    def getElemento(self)->str:
        rta = 'Aire'
        if(self.elementoBabosa == '2'):
            rta= 'Tierra'
        if(self.elementoBabosa == '3'):
            rta = 'Fuego'
        if(self.elementoBabosa == '4'):
            rta = 'Energia'
        if(self.elementoBabosa == '5'):
            rta = 'Agua'
        if(self.elementoBabosa == '6'):
            rta = 'Desconocido'
        return rta
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.codigoBabosa + ' - ' + self.NombreBabosa + ' - ' + self.getTipo() + ' - ' + self.getElemento()





