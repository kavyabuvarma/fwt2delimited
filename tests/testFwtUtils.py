from fwt.fwtSpec import FwtSpec
from fwt.fwtUtils import FwtParser, FwtGen
import os
from pathlib import Path
from fwt import fwtUtils


class TestFwt:

    def test_gen_fwt_with_random_data(self):

        f_path = filepath = Path(__file__).parent.parent / "config/spec.json"
        records = 10

        fwt_gen = FwtGen(str(f_path))

        filepath = "out/fwt_rand_val.txt"
        fwt_filename = fwt_gen.generate_fwt_file(num_of_records=records, file_name=filepath)
        assert os.path.exists(fwt_filename), True

        out_file = open(fwt_filename, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(fwt_gen.spec.offsets_int)
        lines_nonempty = (line for line in lines if len(line) != 0)
        for line in lines_nonempty:
            assert len(line), exp_record_len

        assert len(lines), records

    def test_gen_fwt_with_sample_data(self):

        f_path = filepath = Path(__file__).parent.parent / "config/spec.json"
        records = 10

        fwt_gen = FwtGen(str(f_path))

        sample_val_json = fwtUtils.get_sample_values("config/sample_values.json")
        filepath = Path(__file__).parent / "out/fwt_sample_data.txt"

        fwt_file = fwt_gen.generate_fwt_file(num_of_records=records, file_name=str(filepath),
                                             sample_values_json_str=sample_val_json,
                                             random_data=False)

        assert os.path.exists(str(filepath)), True

        out_file = open(fwt_file, "r")
        file_content = out_file.read()
        lines = file_content.split("\n")
        exp_record_len = sum(fwt_gen.spec.offsets_int)
        lines_nonempty = (line for line in lines if len(line) != 0)
        for line in lines_nonempty:
            assert len(line), exp_record_len

        assert len(lines), records

        col1_array = ["EAT", "WORK", "SLEEP", "WALK", "PLAY"]
        line2 = lines[1]
        assert line2[0: fwt_gen.spec.offsets_int[0]].rstrip() in col1_array, True

    def test_gen_convert_fwt(self):
        f_path = filepath = Path(__file__).parent.parent / "config/spec.json"
        records = 10
        fwt_gen = FwtGen(str(f_path))
        fwt_filename = fwt_gen.generate_fwt_file(num_of_records=records, random_data=False)

        fwt_parser = FwtParser(str(f_path))
        fn = fwt_filename
        delimited_filename = fwt_parser.fwt_to_delimited(fn)

        f = open(delimited_filename)
        del_content = f.read().split("\n")
        f.close()
        assert len(del_content), records

        f = open(fwt_filename)
        fwt_content = f.read().split("\n")
        f.close()

        for i in range(0, records):
            assert del_content[i].replace(' ', '').replace(',', ''), fwt_content[i].replace(' ', '')

    def test_convert_invalid_file_doesnt_exist(self):
        fwt_file = str("this_file_doesnt_exist.txt")
        delim_file = str(Path(__file__).parent / "out/op1.txt")

        fwt_parser = FwtParser()
        delimited_filename = fwt_parser.fwt_to_delimited(fwt_file, delimited_file=delim_file)
        assert (delimited_filename is None), True

    def test_convert_fwt_additional_columns(self):

        filepath = Path(__file__).parent / "files/fwt_additional_cols.txt"
        delim_file = str(Path(__file__).parent / "out/op2.txt")

        fwt_parser = FwtParser()
        delimited_filename = fwt_parser.fwt_to_delimited(filepath, delimited_file=delim_file)

        assert (delimited_filename is None), True

    def test_convert_fwt_missing_columns(self):

        filepath = Path(__file__).parent / "files/fwt_missing_cols.txt"
        delim_file = str(Path(__file__).parent / "out/op3.txt")

        fwt_parser = FwtParser()
        delimited_filename = fwt_parser.fwt_to_delimited(filepath, delimited_file=delim_file)

        assert (delimited_filename is None), True

    def test_empty_fwt(self):
        filepath = Path(__file__).parent / "files/fwt_empty.txt"
        delim_file = str(Path(__file__).parent / "out/op4.txt")

        fwt_parser = FwtParser()
        delimited_filename = fwt_parser.fwt_to_delimited(filepath, delimited_file=delim_file)
        assert (delimited_filename is None), True

    def test_invalid_cols(self):
        filepath = Path(__file__).parent / "files/fwt_invalid_cols.txt"
        delim_file = str(Path(__file__).parent / "out/op5.txt")

        fwt_parser = FwtParser()
        delimited_filename = fwt_parser.fwt_to_delimited(filepath, delimited_file=delim_file)
        assert (delimited_filename is None), True

