from fwt2delimited import conf_spec
import pytest


class TestConfSpec:
    def test_invalid_spec(self):
        conf_spec.ConfSpec("xyz")
        pytest.raises(AttributeError)

    def test_invalid_spec_data(self):
        f = open("data/sample_spec1.json", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(KeyError)

    def test_invalid_spec_data2(self):
        f = open("data/sample_spec2.json", "r")
        conf_spec.ConfSpec(f)
        f.close()
        pytest.raises(ValueError)
