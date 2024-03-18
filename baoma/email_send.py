from django.core.mail import send_mail

def send_vcode(maileaddress,vcode):
    code = send_mail(
                    "django",
                    vcode,
                    "20772026@qq.com",
                    [maileaddress],
                    fail_silently=False,
                )
    return code