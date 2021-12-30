import random, string

def rndstr(output_number):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=output_number))