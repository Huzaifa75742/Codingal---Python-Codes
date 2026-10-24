import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

password = ''.join(random.choice(lowercase + uppercase + digits) for _ in range(12))
