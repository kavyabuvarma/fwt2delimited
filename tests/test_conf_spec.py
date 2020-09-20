from fwt2delimited import conf_spec
import pytest


class TestConfSpec:
    def test_invalid_spec(self):
        conf_spec.ConfSpec("xyz")
        pytest.raises(AttributeError)

    def test_invalid_spec_data(self):
        f = open("data/spec_invalid1.json", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(KeyError)

    def test_invalid_spec_data2(self):
        f = open("data/spec_invalid2.json", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_invalid_json_content(self):
        f = open("data/spec_invalid3.json", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_invalid_file_type(self):
        f = open("data/spec_invalid4.txt", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(ValueError)

    def test_valid_spec(self):
        f = open("data/spec_valid.json", "r")
        spec = conf_spec.ConfSpec(f)
        f.close()
        assert len(spec.offsets) == 10
        assert len(spec.column_names) == 10
        assert spec.include_header is not ""
        assert spec.encoding_format_fwt is not ""
        assert spec.encoding_format_del is not ""
