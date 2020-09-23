# fwt2delimited
Transform Fixed Width Text to Delimited

### Getting started

Package available here: https://github.com/kavyabuvarma/fwt2delimited

Unzip the bundle and navigate to the scripts directory: fwt2delimited/scripts

Add the bundle directory path to the "PYTHONPATH" environment variable

### Executing the script

##### Generate a fixed width file using a FWT specification file

```
python FWTGenerator.py \
       -s path_to_fwt_spec_file \
       -f path_to_output_fwt_file \
       -n number_of_records \
       -l logs_level \
       -r use_random_values \              
```
- The parameters are all optional.
- The default values are:
    1. **path_to_fwt_spec_file** - fwt2delimited/config/spec.json
    2. **path_to_output_fwt_file** - fwt_file.txt in the current directory
    3. **number_of_records** - 20
    4. **logs_level** - INFO
    5. **use_random_values** - False
- To get help, run **`FWTGenerator.py -h`**

##### Convert a fixed width file to a delimited file using a FWT specification file

```
python FWTConverter.py \
       -s path_to_fwt_spec_file \
       -f path_to_fwt_file \
       -o path_to_output_delimited_file \
       -d delimiter
       -l logs_level \         
```
            
- The parameters except for **path_to_fwt_file** are all optional.
- The default values for other parameters are:
    1. **path_to_fwt_spec_file** - fwt2delimited/config/spec.json
    2. **path_to_output_delimited_file** - delimited_file.csv in the current directory
    3. **delimiter** - ","
    4. **logs_level** - INFO
- To get help, run **`FWTConverter.py -h`**