import csv
from pathlib import Path


class CSVStore:
    """Reusable storage for a header-based CSV file."""

    def __init__(self, path, fieldnames, key_field):
        self.path = Path(path)
        self.fieldnames = fieldnames
        self.key_field = key_field

        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.save_all([])

    def get_all(self):
        with self.path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            return list(csv.DictReader(file))

    def find(self, key):
        for row in self.get_all():
            if row[self.key_field] == str(key):
                return row

        return None

    def save_all(self, rows):
        with self.path.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=self.fieldnames,
                extrasaction="ignore"
            )

            writer.writeheader()
            writer.writerows(rows)

    def add(self, row):
        rows = self.get_all()
        rows.append(row)
        self.save_all(rows)

    def update(self, row):
        rows = self.get_all()

        for index, current in enumerate(rows):
            if current[self.key_field] == str(row[self.key_field]):
                rows[index] = row
                self.save_all(rows)
                return True

        return False
