import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Product , Brand


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg' ]
    for x in range(n):
        Brand.objects.create(
          name  = fake.name(),
          image = f"brands/{images[random.randint(0,9)]}"
        )

    print(f'{n} brands seeded successfully')


seed_brand(50)