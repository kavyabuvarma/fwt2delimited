# fwt2delimited
Transform Fixed Width Text to Delimited

## Installation

Package available here: from https://github.com/kavyabuvarma/fwt2delimited

Unzip the bundle and navigate to the scripts directory: fwt2delimited/scripts

### Executing the script

##### Generate a fixed width file using a FWT specification file
```
python FWTGenerator.py \
              -s path_to_fwt_spec_file
              -f path_to_output_fwt_file
              -n number_of_records
              -l logs_level
              -r use_random_values              
```
- The parameters are all optional.
- The default values are:
    1. path_to_fwt_spec_file - fwt2delimited/data/spec.json
    2. path_to_output_fwt_file - fwt_file.txt in the current directory
    3. number_of_records - 20
    4. logs_level - INFO
    5. use_random_values - False
- To get help, run **`FWTGenerator.py -h`**
