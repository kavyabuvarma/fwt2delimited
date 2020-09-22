import json
import logging


class FwtSpec:
    def __init__(self, spec_json):

        try:
            spec_json_obj = json.load(spec_json)
            self.column_names = spec_json_obj['ColumnNames']
            self.offsets = spec_json_obj['Offsets']
            self.include_header = spec_json_obj['IncludeHeader']
            self.encoding_format_fwt = spec_json_obj['FixedWidthEncoding']
            self.encoding_format_del = spec_json_obj['DelimitedEncoding']

            self.offsets_int = [int(i) for i in self.offsets]
            if len(self.offsets) == len(self.column_names):
                self.spec_dict = dict(zip(self.column_names, self.offsets_int))
            else:
                raise ValueError("The number of columns do not match the number of offsets in the spec.")

            if self.include_header not in ["True", "False"]:
                logging.warning("Invalid value for the key 'IncludeHeader', expected one of [\"True\", \"False\"]. "
                                "Setting 'Include Header' = True.")
                self.include_header = True
        except AttributeError:
            logging.error("Invalid config param, expected : File Pointer.")
            pass
        except (KeyError, ValueError) as e:
            logging.error("Invalid config specification content.")
            logging.exception(e)
            pass
