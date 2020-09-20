from fwt2delimited import conf_spec

if __name__ == '__main__':
    f = open("tests/data/sample_spec1.json")
    x = conf_spec.ConfSpec(f)
    f.close()

    # print(x is None)
