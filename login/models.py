from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
#from django.contrib.auth.backends import ModelBackend  erro：添加后会覆盖login_users
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(email,
                               username,
                               password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# users数据



class users(AbstractBaseUser):

    is_anonymous = models.BooleanField(default = False)
    is_authenticated = models.BooleanField(default = False)
    date_of_birth = models.DateField(default=timezone.now())
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length = 255,unique=True)  #用户名
    password = models.CharField(max_length = 255)  #密码
    email = models.EmailField(max_length = 255,unique=True)  #邮箱地址

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('-username',)

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, login_users):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
