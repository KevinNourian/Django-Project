from django.db import models
import random
import string

# random_numbers = str(random.randint(000, 999))


def random_letters():
    return ''.join(random.choice(string.ascii_letters.upper()) for i in range(3))

def random_numbers():
	return str(random.randint(000, 999))


class Plate(models.Model):

	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	letters = models.CharField(default = random_letters, max_length = 3, unique = True)
	numbers = models.CharField(default = random_numbers, max_length = 3, unique = True)


	def __str__(self):
		return self.first_name + ' ' + self.last_name