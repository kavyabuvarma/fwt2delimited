import getopt
import sys

if __name__ == "__main__":
    # default values
    fwt_spec_path = "../fwt2delimited/data/spec.json"
    fwt_file_path = "fwt_file.txt"
    delimited_file_path = "delimited_file.csv"
    sample_data_file_path = "../fwt2delimited/data/sample_values.json"
    system_logs_level = "INFO"

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:f:d:l:h', ['specfwt=', 'fwtfilepath=', 'delimitedfilepath=',
                                                               'loglevel=', "userandomvalues=", 'help'])
    except getopt.GetoptError:
        print("Error starting FWT Parser. The following arguments should be provided:"
              " \n '-s' - path to the fwt specification file"
              " \n '-f' - path to the FWT file"
              " \n '-d' - path to the delimited file"
              " \n '-l' - FWTParser system logs level"
              " \n '-v' - set \"random\" or any value to use random data for FWT file"
              " \n Or no arguments at all in order to use default values")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('FWTParser.py -s <path_to_fwt_spec_file> -f <path_to_fwt_file> -d <path_to_delimited_file> '
                  '-l <system_logs_level>')
            sys.exit(2)
        elif opt in ('-s', '--specfwt'):
            fwt_spec_path = arg
        elif opt in ('-f', '--fwtfilepath'):
            fwt_file_path = arg
        elif opt in ('-d', '--delimitedfilepath'):
            delimited_file_path = arg
        elif opt in ('-v', '--userandomvalues'):
            use_random_values = True
        elif opt in ('-l', '--loglevel'):
            system_logs_level = arg.upper()
            if system_logs_level not in ["DEBUG", "INFO", "ERROR"]:
                sys.exit("Provided system logs level is not supported. Supported levels are DEBUG, INFO and ERROR")



    print("fwt2delimited")
