import os
import time

import psycopg2
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 21):
            self.stdout.write(f"Connecting to DB, try #{i} out of 20:")
            try:
                conn = psycopg2.connect(
                    f"dbname={os.environ.get('POSTGRES_DB')} "
                    f"user={os.environ.get('POSTGRES_USER')} "
                    f"host={os.environ.get('POSTGRES_HOST')} "
                    f"password={os.environ.get('POSTGRES_PASSWORD')} "
                    f"port={os.environ.get('POSTGRES_PORT')}"
                )
                conn.close()
                self.stdout.write("Connected to DB successfully")
                break
            except psycopg2.OperationalError:
                self.stdout.write(
                    "Connection to DB failed, trying again in 2 seconds..."
                )
                time.sleep(2)
        else:
            self.stderr.write(
                "Connection to DB failed for 20 tries."
            )
