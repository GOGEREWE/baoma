"""四位随即验证码生成器"""

import random
def get_vcode():
    checkcode = ''
    for i in range(4):
        index = random.randrange(0,3)
        if index != i and index+1 !=i:
            checkcode += chr(random.randint(97,122))
        elif index+1 == i:
            checkcode += chr(random.randint(65,90))
        else:
            checkcode += str(random.randint(1,9))
    return checkcode