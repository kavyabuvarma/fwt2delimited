# fwt2delimited
Convert Fixed Width Text to Delimited

This application converts a fixed width text (FWT) file to a delimited file according to a specification.

Specification - a JSON object that specifies the list of column names in the FWT file, their lengths and encoding methods. Sample file - fwt2delimited/config/spec.json.

This application can be used to 
 
(i) generate an FWT file
 
(ii) convert an FWT file to delimited file

#### Assumptions
1. The specification file is valid : 
   - the values for the keys "FixedWidthEncoding" and "DelimitedEncoding" in specification will be valid Python 3 Codecs
   - the number of column names and lengths are matching, no duplicate column names
2. The FWT file with additional columns are valid - only the columns in specification are considered for conversion.
3. A valid delimiter is used - no limitation on the value for delimiter.  
### Run

#### Setup :

1. Ensure Python 3 is installed
2. Ensure application path is added to the environment variable "PYTHONPATH"
3. Navigate to application directory: fwt2delimited

Note : if **`python --version`** does not show 3.X.X , please use "python3" instead of "python" in the commands below 
##### 1. Generate a fixed width text file

```
python scripts/FWTGenerator.py \
       -s path_to_spec_file \
       -f path_to_fwt_file \
       -n number_of_records \
       -l logs_level \
       -r use_random_values \              
```
- The parameters are all optional.
- The default values are:
    1. **path_to_spec_file** - "config/spec.json"
    2. **path_to_fwt_file** - "fwt_file.txt" in the current directory
    3. **number_of_records** - 20
    4. **logs_level** - INFO
    5. **use_random_values** - False, uses a sample data set to generate FWT - values from fwt2delimited/config/sample_values.json
- To get help, run **`scripts/FWTGenerator.py -h`**

##### 2. Convert a fixed width file to a delimited file using a FWT specification file

```
python scripts/FWTConverter.py \
       -s path_to_spec_file \
       -f path_to_fwt_file \
       -o path_to_delimited_file \
       -d delimiter
       -l logs_level \         
```
            
- The parameters except for **path_to_fwt_file** are all optional.
- The default values for other parameters are:
    1. **path_to_spec_file** - "config/spec.json"
    2. **path_to_delimited_file** - "delimited_file.csv" in the current directory
    3. **delimiter** - ","
    4. **logs_level** - INFO
- To get help, run **`FWTConverter.py -h`**

### Docker

To run via Docker, navigate to the application directory and execute
```
 docker build -t fwt2delimited .

 docker run fwt2delimited
```
This generates an FWT file according to default spec, using sample values and converts the same to delimited file.

To check the generated FWT and delimited files in the container, execute
```
 docker run -ti fwt2delimited /bin/sh

 cat fwt_file.txt
 cat delimited_file.txt
```

### Improvements
1. Make it available as a module on PyPI
2. Add more validation checks of specification file
3. Support additional interfaces apart from file
4. Refactor the test suite

#### Gotcha
The generated FWT file displays some characters in a skewed manner due to the difference in encoding - FWT file would be in "windows-1252" format. 
Check the generated delimited file, which would be in "utf-8" format, to validate the results.