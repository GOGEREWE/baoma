from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def crate_user(self,email,username,password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def crate_superuser(self,email,username,password):
        user = self.crate_user(email,
                               username,
                               password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# users数据

class users(AbstractBaseUser):

    is_anonymous = models.BooleanField(default = False)
    is_authenticated = models.BooleanField(default = False)
    date_of_birth = models.DateField(default='0000-00-00')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length = 255,unique=True)  #用户名
    password = models.CharField(max_length = 255)  #密码
    eamil = models.EmailField(max_length = 255,unique=True)  #邮箱地址

    objects = UserManager()

    USERNAME_FIELD = 'eamil'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('-username',)

    def __str__(self):
        return self.users