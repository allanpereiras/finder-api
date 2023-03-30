import requests
from django.core.management.base import BaseCommand, CommandError

from finder.models import Definition, Finding, Target


class Command(BaseCommand):
    help = "Retrieve a list of findings from Probely's API endpoint"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument("--id", nargs="?", type=str, default="Tt2f8EyPSTwq")

    def handle(self, *args, **options):
        # Ideally we would get the API key from the environment variables (!)
        api_key = ""
        header = {"Authorization": f"JWT {api_key}"}
        try:
            url = f"https://api.com/targets/{options['id']}/findings/"
            response = requests.get(url, headers=header)
            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS("Successfully retrieved findings"))
                self.create_objects(response)
            else:
                msg = f"Failed to retrieve findings: {response.reason}"
                self.stdout.write(self.style.ERROR(msg))
        except requests.exceptions.RequestException as e:
            raise CommandError(e) from e

    def create_objects(self, response):
        """Create Target, Definition, Finding objects from the API response"""
        data = response.json()["results"]

        target_data = [  # List comprehension
            {"id": i["target"].get("id"), "name": i["target"].get("name")} for i in data
        ]
        target_objs = [Target(**i) for i in target_data]
        Target.objects.bulk_create(target_objs, ignore_conflicts=True)
        self.stdout.write("Created Target object(s)")

        definition_data = [  # List comprehension
            {
                "id": i["definition"].get("id"),
                "name": i["definition"].get("name"),
                "desc": i["definition"].get("desc"),
            }
            for i in data
        ]
        definition_objs = [Definition(**i) for i in definition_data]
        Definition.objects.bulk_create(definition_objs, ignore_conflicts=True)
        self.stdout.write("Created Definition object(s)")

        finding_data = [  # List comprehension
            {
                "id": i["id"],
                "target_id": i["target"].get("id"),
                "definition_id": i["definition"].get("id"),
                "scans": i["scans"],
                "url": i["url"],
                "path": i["path"],
                "method": i["method"],
            }
            for i in data
        ]
        finding_objs = [Finding(**i) for i in finding_data]
        Finding.objects.bulk_create(finding_objs, ignore_conflicts=True)
        self.stdout.write("Created Finding object(s)")
        self.stdout.write("Finished.")
