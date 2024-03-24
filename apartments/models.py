from django.db import models

class Category(models.Model):
    title=models.CharField("Имя объекта",max_length=32)

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField("Статус", max_length=16)
    description=models.TextField("Описание")

    def __str__(self):
        return self.title

class Clients(models.Model):
    bio=models.CharField("ФИО клиента",max_length=128)
    number_phone=models.SmallIntegerField("Номер телефона")
    contract=models.SmallIntegerField("Номер договора")
    status=models.ForeignKey(to=Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Flats(models.Model):
    apartment_number=models.CharField("Номер квартиры",max_length=16,default='№132')
    object=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    floor=models.SmallIntegerField("Этаж",default=1)
    square=models.DecimalField("Площадь квартиры",default=144.5,decimal_places=1,max_digits=4)
    create_date = models.DateTimeField("Дата создания",auto_now=True)
    status=models.ForeignKey(to=Status,on_delete=models.CASCADE)
    price=models.PositiveIntegerField("Цена",default=2000000)

    def __str__(self):
        return self.apartment_number

class Manager(models.Model):
    bio = models.CharField("ФИО менеджера", max_length=128)
    number_phone = models.SmallIntegerField("Номер телефона")
    email=models.EmailField("Почта")
    create_date = models.DateTimeField("Дата создания",auto_now=True)
    count=models.SmallIntegerField("Количество сделок",default=0)
    password=models.CharField("Временный пароль",max_length=32)








