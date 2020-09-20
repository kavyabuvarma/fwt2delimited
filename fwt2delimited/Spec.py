
class Spec:
    def __init__(self, spec_json_obj):
        self.column_names = spec_json_obj['ColumnNames']
        self.offsets = spec_json_obj['Offsets']
        self.offsets_int = [int(i) for i in self.offsets]
        self.spec_dict = dict(zip(self.column_names, self.offsets_int))
        self.include_header = spec_json_obj['IncludeHeader']
        self.encoding_format_fwt = spec_json_obj['FixedWidthEncoding']
        self.encoding_format_del = spec_json_obj['DelimitedEncoding']
