from fwt2delimited.fwt_utils import Fwt
from fwt2delimited import conf_spec, fwt_utils
import os
from pathlib import Path


class TestFwt:

    def test_gen_fwt_with_random_data(self):

        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()
        records = 10

        fwt = Fwt(spec)

        filepath = Path(__file__).parent / "data/rand_val_fwt.txt"
        print(str(filepath))
        fwt.generate_fwt_file(num_of_records=records, file_path=str(filepath))
        assert os.path.exists(str(filepath)), True

        out_file = open(filepath, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(spec.offsets_int)
        for line in lines:
            assert len(line), exp_record_len

        assert len(lines), records

    def test_gen_fwt_with_sample_data(self):

        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()
        records = 30

        fwt = Fwt(spec)

        sample_val_json = fwt_utils.get_sample_values("../data/sample_values.json")
        filepath = Path(__file__).parent / "data/sample_data_fwt.txt"

        fwt_file = fwt.generate_fwt_file(num_of_records=records, file_path=str(filepath),
                                         sample_values_json_str=sample_val_json,
                                         random_data=False)

        assert os.path.exists(str(filepath)), True

        out_file = open(fwt_file, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(spec.offsets_int)
        for line in lines:
            assert len(line), exp_record_len

        assert len(lines), records

        col1_array = ["EAT", "WORK", "SLEEP", "WALK"]
        line2 = lines[1]
        assert line2[0: spec.offsets_int[0]].rstrip() in col1_array, True

    def test_gen_convert_fwt(self):
        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()
        records = 5

        fwt = Fwt(spec)

        fwt_filename = fwt.generate_fwt_file(num_of_records=records, random_data=False)
        fn = fwt_filename
        delimited_filename = fwt.fwt_to_delimited(fn)

        f = open(delimited_filename)
        del_content = f.read().split("\n")
        f.close()
        assert len(del_content), records

        f = open(fwt_filename)
        fwt_content = f.read().split("\n")
        f.close()

        for i in range(0, records):
            assert del_content[i].replace(' ', '').replace(',', ''), fwt_content[i].replace(' ', '')

    def test_convert_invalid(self):
        filename = str("thisfiledoesntexist.txt")

        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()

        fwt = Fwt(spec)
        delim_file = fwt.fwt_to_delimited(f)
        assert delim_file is None, True
