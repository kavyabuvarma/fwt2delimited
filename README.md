# fwt2delimited
Convert Fixed Width Text to Delimited

This application converts a fixed width text (FWT) file to a delimited file according to a specification.
Specification - a JSON object that specifies the list of column names, their lengths and encoding methods. Sample - fwt2delimited/config/spec.json.
This application can be used to 
(i) generate an FWT file 
(ii) convert an FWT file to delimited file

#### Assumptions
1. The values for the keys "FixedWidthEncoding" and "DelimitedEncoding" will be valid Python 3 Codecs

### Run

#### Setup :

1. Ensure Python 3 is installed
2. Ensure application path is added to the environment variable "PYTHONPATH"
3. Navigate to application directory - fwt2delimited

##### 1. Generate a fixed width text file

```
python scripts/FWTGenerator.py \
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
    5. **use_random_values** - False, uses a sample data set to generate FWT - values from fwt2delimited/config/sample_values.json
- To get help, run **`FWTGenerator.py -h`**

##### 2. Convert a fixed width file to a delimited file using a FWT specification file

```
python scripts/FWTConverter.py \
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

### Docker

To run via Docker, navigate to the application directory and execute
```
 docker build -t fwt2delimited .

 docker run fwt2delimited
```

### Possible improvements
1. 