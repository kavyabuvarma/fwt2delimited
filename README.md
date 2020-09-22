# fwt2delimited
Transform Fixed Width Text to Delimited

##Installation

Wheel
```
    pip install  fwt2delimited-1.0.0-py3-none-any.whl
```

PyPi - not yet available
```

```

##Usage samples
```
from fwt2delimited.fwt import Fwt
...
# construct Fwt with the default spec
fwt = Fwt()

# construct Fwt - pass the spec file name param
fwt = Fwt(spec_file_name=<>)
 
# according to the spec mentioned, 
# generate FWT - file name "fwt_file.txt" in current dir, using random dataset 
fwt_fname = fwt.generate_fwt_file() 

# generate FWT - file name in param "file_name" in current dir, default sample dataset  
fwt_fname = fwt.generate_fwt_file(random_data=False, file_name=<filename>) 

# generate FWT - file name "fwt_file.txt" in current dir, sample dataset in the param "sample_values_json_str" 
fwt_fname = fwt.generate_fwt_file(random_data=False, sample_values_json_str=<jsonstr>)

# convert FWT to delimited - default delimiter ',' , output file name "delimited_file.csv"
delim_fname = fwt.fwt_to_delimited(fwt_fname)

# convert FWT to delimited - delimiter and output file name specified in the param
delim_fname = fwt.fwt_to_delimited(fwt_fname, delimited_file=<>)
```