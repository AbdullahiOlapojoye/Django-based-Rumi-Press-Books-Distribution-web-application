import pandas as pd
from django.core.management.base import BaseCommand
from books.models import BookCategory, Book
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Import books from an Excel file'

    def handle(self, *args, **kwargs):
        def parse_date(date_str):
            for fmt in ('%m/%d/%Y', '%Y-%m-%d'):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    pass
            return None  # Return None if no valid date format found

        # Use the absolute path to the file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../../../Copy of Books Distribution Expenses.xlsx')
        
        # Read the Excel file
        data = pd.read_excel(file_path)

        for _, row in data.iterrows():
            category_name = row['category']
            category, created = BookCategory.objects.get_or_create(name=category_name)

            # Adjust the date format to match possible formats
            published_date = parse_date(str(row['published_date']).split(" ")[0])
            if not published_date:
                self.stdout.write(self.style.WARNING(f"Invalid date format for row: {row['published_date']} - Skipping row"))
                continue  # Skip the row if the date is invalid

            Book.objects.create(
                title=row['title'],
                subtitle=row.get('subtitle', ''),
                authors=row['authors'],
                publisher=row['publisher'],
                published_date=published_date,
                category=category,
                distribution_expense=row['distribution_expense']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))