from fwt2delimited.fwt import Fwt
from fwt2delimited import conf_spec, fwt
import os
from pathlib import Path


class TestFwt:

    def test_gen_fwt_with_random_data(self):

        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()

        fwt_obj = Fwt(spec)

        filepath = Path(__file__).parent / "data/rand_val_fwt.txt"
        print(str(filepath))
        fwt_obj.generate_fwt_file(num_of_records=10, file_path=str(filepath))
        assert os.path.exists(str(filepath)), True

        out_file = open(filepath, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(spec.offsets_int)
        for line in lines:
            assert len(line), exp_record_len

        assert len(lines), 10

    def test_gen_fwt_with_sample_data(self):

        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()

        fwt_obj = Fwt(spec)

        sample_val_json = fwt.get_sample_values("../data/sample_values.json")
        filepath = Path(__file__).parent / "data/sample_data_fwt.txt"

        status = fwt_obj.generate_fwt_file(num_of_records=30, file_path=str(filepath),
                                           sample_values_json_str=sample_val_json,
                                           random_data=False)
        assert status == 0, True
        assert os.path.exists(str(filepath)), True

        out_file = open(filepath, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(spec.offsets_int)
        for line in lines:
            assert len(line), exp_record_len

        assert len(lines), 30

        col1_array = ["EAT", "WORK", "SLEEP", "WALK"]
        line2 = lines[1]
        assert line2[0: spec.offsets_int[0]].rstrip() in col1_array, True

    def test_gen_fwt_invalid_params(self):
        f = open("data/spec_valid.json")
        spec = conf_spec.ConfSpec(f)
        f.close()

        fwt_obj = Fwt(spec)
        status = fwt_obj.generate_fwt_file(num_of_records=5)
        assert status == 0, False
