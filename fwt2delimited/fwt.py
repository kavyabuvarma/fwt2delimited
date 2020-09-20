import logging
import json
from pathlib import Path
import random
import string


def get_sample_values(filepath) -> str:
    if filepath == "":
        filepath = "../data/sample_values.json"
    path = Path(__file__).parent / filepath
    with path.open() as f:
        f = open(path)
        sample_values = f.read()
        return sample_values


def generate_rand_value() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, 20)))


class Fwt:

    def __init__(self, spec):
        self.spec = spec

    def add_header_if_true(self):
        if self.spec.include_header == "True":
            fields_array = []
            for key in self.spec.spec_dict:
                fields_array.append(str.ljust(key, self.spec.spec_dict.get(key)))
            return ''.join(fields_array)
        else:
            return None

    def generate_rand_dataset(self, num_of_records) -> [str]:
        lines = []
        try:
            header = self.add_header_if_true()
            if header is not None:
                lines.append(header)
            for i in range(1, num_of_records):
                values_array = []
                for offset in self.spec.offsets_int:
                    values_array.append(str.ljust(generate_rand_value(), offset)[0:offset])
                lines.append(''.join(values_array))
        except Exception as e:
            logging.error("Error generating FWT file with random data. %s", e.message)
        return lines

    def generate_dataset_from_sample(self, num_of_records, sample_values_json_str) -> [str]:
        lines = []
        try:
            sample_values_json_obj = json.loads(sample_values_json_str)

            header = self.add_header_if_true()
            if header is not None:
                lines.append(header)

            for i in range(1, num_of_records):
                values_array = []
                for key in self.spec.spec_dict:
                    if key in sample_values_json_obj.keys():
                        rand_values = sample_values_json_obj[key]
                    else:
                        rand_values = [generate_rand_value(), generate_rand_value(), generate_rand_value()]
                    values_array.append(str.ljust(random.choice(rand_values), self.spec.spec_dict.get(key)))
                lines.append(''.join(values_array))
        except Exception as e:
            logging.error("Error generating FWT file with sample dataset. %s", e.message)
        return lines

    def generate_fwt_file(self, random_data=True, num_of_records: int = 20, file_path: str = "data/fwt.txt",
                          sample_values_json_str: str = get_sample_values("")) -> int:
        try:
            if random_data is True:
                lines = self.generate_rand_dataset(num_of_records)
            else:
                lines = self.generate_dataset_from_sample(num_of_records, sample_values_json_str)

            fwt_file = open(file_path, "w", encoding=self.spec.encoding_format_fwt)
            fwt_file.write('\n'.join(lines))
        except Exception as e:
            logging.error("Error generating FWT file %s", e.message)
        return 0
