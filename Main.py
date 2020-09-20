from fwt2delimited import conf_spec
from fwt2delimited.fwt import Fwt
import json
import logging
import os
from pathlib import Path

if __name__ == '__main__':
    f = open("data/spec.json")
    spec = conf_spec.ConfSpec(f)
    f.close()
    # filepath = Path(__file__).parent / "data/rand_val_fwt.txt"
    # print(str(filepath))
    # fwt.generate_fwt_file()

    fwt_obj = Fwt(spec)
