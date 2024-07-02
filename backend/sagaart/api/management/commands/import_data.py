from pathlib import Path
import csv

from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.utils import IntegrityError

from api.constants import ARTOBJECTS_APP_LABEL


class FileOpenException(Exception):
    """Вызов исключения при некорректном открытии файла."""

    pass


class Command(BaseCommand):
    """Команда для загрузки тестовых данных в базу данных"""

    help = "Загрузка данных для тестирования"

    def handle(self, *args, **kwargs):
        files = [
            "category.csv",
            "genre.csv",
            "style.csv",
            "objectauthor.csv",
            "authoraward.csv",
            "authorshow.csv",
            "artobject.csv",
        ]
        for file in files:
            model_name = Path(file).stem
            model_class = apps.get_model(ARTOBJECTS_APP_LABEL, model_name)
            try:
                with open(f"static/data/{file}", newline="", encoding='utf-8') as f:
                    dataframe = csv.DictReader(f)
                    for row in dataframe:
                        try:
                            if file == "artobject.csv":
                                category = row.pop("category")
                                style = row.pop("style")
                                genre = row.pop("genre")
                                result = model_class.objects.create(**row)
                                result.category.set(category)
                                result.style.set(style)
                                result.genre.set(genre)
                            else:
                                model_class.objects.create(**row)
                        except IntegrityError:
                            self.stdout.write(
                                f'Object {model_name} ID:'
                                f'{row.get("id")} already exists'
                            )
                            continue
                    self.stdout.write(
                        f"Data import finished for model: {model_name}"
                    )
            except FileOpenException as error:
                self.stdout.write(f"Ошибка при открытии файла: {error}")
                continue
