from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, id, password, email=None):
        if not id:
            raise ValueError('Users must have an id')

        user = self.model(
            id=id,
        )

        user.set_password(password)
        user.email = email
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password):
        user = self.create_user(
            id=id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    nickName = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, null=True)
    password = models.CharField(max_length=100)
    vegiterian = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.id
