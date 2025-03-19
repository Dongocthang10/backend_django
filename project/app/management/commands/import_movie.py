from django.core.management.base import BaseCommand
from django.apps import apps
import pandas as pd 

class Command(BaseCommand):
    help = """ Import Movies CSV into Django Models
           usage:
           python manage.py import_movie --path movies.csv
           """
    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type = str,
            help = "file path",
            default = "movies.csv",
        )

    def handle(self, *arg, **options):
        file_path = options["path"]
        _model = apps.get_model("app", "Model")
        df = pd.read_csv(file_path)
        df_records = df.to_dict("records")

        model_instances = [_model(
                id = record.get("id"),
                title = record.get("title"),
                overview = record.get("overview"),
                release_date = record.get("release_date"),
                popularity = record.get("popularity"),
                vote_average = record.get("vote_average"),
                vote_count = record.get("vote_count"),
        ) for record in df_records]
        _model.objects.bulk_create(model_instances)
        print("Finished Importing Data")

