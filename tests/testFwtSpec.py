from fwt import fwtSpec
import pytest


class TestConfSpec:
    def test_invalid_spec(self):
        fwtSpec.FwtSpec("xyz")
        pytest.raises(AttributeError)

    def test_invalid_spec_data(self):
        f = open("files/spec_invalid1.json", "r")
        fwtSpec.FwtSpec(f)
        f.close()
        pytest.raises(KeyError)

    def test_invalid_spec_data2(self):
        f = open("files/spec_invalid2.json", "r")
        fwtSpec.FwtSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_invalid_json_content(self):
        f = open("files/spec_invalid3.json", "r")
        fwtSpec.FwtSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_invalid_file_type(self):
        f = open("files/spec_invalid4.txt", "r")
        fwtSpec.FwtSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_valid_spec(self):
        f = open("files/spec_valid.json", "r")
        spec = fwtSpec.FwtSpec(f)
        f.close()
        assert len(spec.offsets) == 10
        assert len(spec.column_names) == 10
        assert spec.include_header != "", True
        assert spec.encoding_format_fwt != "", True
        assert spec.encoding_format_del != "", True
