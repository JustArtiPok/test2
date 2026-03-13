import csv
import os
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'
    
    def handle(self, *args, **options):
        # Очищаем существующие записи
        Phone.objects.all().delete()
        
        csv_file = 'phones.csv'
        
        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR(f'File {csv_file} not found!'))
            return
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            # Указываем разделитель ;
            reader = csv.DictReader(file, delimiter=';')
            
            count = 0
            for row in reader:
                try:
                    # Преобразуем строковые значения в нужные типы
                    name = row['name']
                    price = float(row['price'])
                    image = row['image']
                    release_date = row['release_date']
                    lte_exists = row['lte_exists'].lower() == 'true'
                    slug = slugify(name)
                    
                    # Создаем запись
                    phone = Phone.objects.create(
                        name=name,
                        price=price,
                        image=image,
                        release_date=release_date,
                        lte_exists=lte_exists,
                        slug=slug
                    )
                    
                    count += 1
                    self.stdout.write(f"✓ Импортирован: {phone.name}")
                    
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"✗ Ошибка при импорте: {e}"))
                    self.stdout.write(f"   Данные: {row}")
            
            self.stdout.write(self.style.SUCCESS(f'Импортировано {count} телефонов'))