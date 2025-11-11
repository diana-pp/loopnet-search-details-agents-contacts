thonimport json
import logging

class Exporter:
    def __init__(self):
        self.file_path = "data/sample_output.json"

    def export(self, data, filename=None, append=False):
        if filename:
            self.file_path = filename

        mode = 'a' if append else 'w'

        logging.info(f"Exporting data to {self.file_path}...")
        with open(self.file_path, mode) as file:
            json.dump(data, file, indent=4)

        logging.info("Data exported successfully!")