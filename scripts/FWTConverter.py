import getopt
import sys
from fwt.fwtUtils import FwtParser

if __name__ == "__main__":

    # default values
    delimited_file_path = "delimited_file.csv"
    system_logs_level = "INFO"
    delimiter = ","

    fwt_file_path = None
    fwt_spec_path = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:f:o:d:l:h', ['specfwt=', 'fwtfilepath=', 'delimitedfilepath=',
                                                                 'delimiter=', 'loglevel=', 'help'])
    except getopt.GetoptError:
        print("Error starting FWT Parser. The following arguments should be provided:"
              " \n '-s' - path to the FWT specification file"
              " \n '-f' - path to the FWT file"
              " \n '-o' - path to the delimited file"
              " \n '-d' - delimiter to be used"
              " \n '-l' - FWTParser system logs level"
              " \n Or no arguments at all in order to use default values")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('FWTParser.py -s <path_to_fwt_spec_file> -f <path_to_fwt_file> -o <path_to_delimited_file> '
                  '-d <delimiter> -l <system_logs_level>')
            sys.exit(2)
        elif opt in ('-s', '--specfwt'):
            fwt_spec_path = arg
        elif opt in ('-f', '--fwtfilepath'):
            fwt_file_path = arg
        elif opt in ('-o', '--delimitedfilepath'):
            delimited_file_path = arg
        elif opt in ('-d', '--delimiter'):
            delimited_file_path = arg
        elif opt in ('-l', '--loglevel'):
            system_logs_level = arg.upper()
            if system_logs_level not in ["DEBUG", "INFO", "ERROR"]:
                sys.exit("Provided system logs level is not supported. Supported levels are DEBUG, INFO and ERROR")

    if fwt_file_path is None:
        sys.exit("Please provide the FWT file path: -f or --fwtfilepath")

    if fwt_spec_path is None:
        fwtParser = FwtParser()
        print("Parsing the provided FWT file against default specification - config/spec.json"
              "\nUse -s or --specfwt to provide a specification file")
    else:
        fwtParser = FwtParser(fwt_spec_path)
    delimited_file = fwtParser.fwt_to_delimited(fwt_file=fwt_file_path, delimited_file=delimited_file_path,
                                                delimiter=delimiter)
    if delimited_file is None:
        sys.exit("Error while converting FWT to delimited.")
    else:
        print("Delimited file generated:", delimited_file)
