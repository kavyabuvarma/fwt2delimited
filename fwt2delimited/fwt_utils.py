import logging
import json
from pathlib import Path
import random
import string
import codecs


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

    def get_records_fwt_file(self, fwt_file):
        try:
            encoding_format = self.spec.encoding_format_del
            f = codecs.open(fwt_file, "r", encoding_format)
            records = f.read().split("\n")
        except TypeError:
            logging.error("Error while reading FWT file.")
            logging.exception("message")
        else:
            return records

    def convert_records(self, records_fwt, delimiter):
        try:
            records_delimited = []
            for record_fwt in records_fwt:
                index_start = 0
                values = []
                for offset in self.spec.offsets_int:
                    index_end = index_start + offset
                    values.append(record_fwt[index_start: index_end].rstrip())
                    index_start = index_end
                records_delimited.append(delimiter.join(values))
        except (IOError, ValueError, KeyError, LookupError):
            logging.error("Error while converting fwt to delimited.")
            logging.exception("message")
        else:
            return records_delimited

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
        except (IOError, ValueError, KeyError, LookupError):
            logging.error("Error while generating FWT file with random data.")
            logging.exception("message")
        else:
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
        except (IOError, ValueError, KeyError, LookupError):
            logging.error("Error while generating FWT file with sample dataset.")
            logging.exception("message")
        else:
            return lines

    def generate_fwt_file(self, random_data=True, num_of_records: int = 20, file_path: str = "data/fwt.txt",
                          sample_values_json_str: str = get_sample_values("")) -> str:
        try:
            if random_data is True:
                lines = self.generate_rand_dataset(num_of_records)
            else:
                lines = self.generate_dataset_from_sample(num_of_records, sample_values_json_str)

            fwt_file = open(file_path, "w", encoding=self.spec.encoding_format_fwt)
            fwt_file.write('\n'.join(lines))
        except (IOError, ValueError, KeyError, LookupError):
            logging.error("Error while generating FWT file.")
            logging.exception("message")
        else:
            return fwt_file.name

    def fwt_to_delimited(self, fwt_file: str, delimiter: str = ',', delimited_file: str = "data/delimited.csv") -> str:
        try:
            records_fwt = self.get_records_fwt_file(fwt_file)
            records_delimited = self.convert_records(records_fwt, delimiter)

            delimited_file = open(delimited_file, "w", encoding=self.spec.encoding_format_del)
            delimited_file.write('\n'.join(records_delimited))
        except (IOError, ValueError, KeyError, LookupError):
            logging.error("Error while generating delimited file.")
            logging.exception("message")
        else:
            return delimited_file.name
