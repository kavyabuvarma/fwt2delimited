import getopt
import sys
import logging
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
        print("Error starting FWT Parser. The arguments supported are:"
              " \n '-s' - path to the FWT specification file"
              " \n '-f' - path to the FWT file - MANDATORY"
              " \n '-o' - path to the delimited file"
              " \n '-d' - delimiter to be used"
              " \n '-l' - FWTParser system logs level"
              " \n Default values will be considered for the optional arguments if not provided.")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('scripts/FWTParser.py -s <path_to_fwt_spec_file> \\'
                  '\n -f <path_to_fwt_file> \\'
                  '\n -o <path_to_delimited_file> \\'
                  '\n -d <delimiter> \\'
                  '\n -l <system_logs_level>')
            sys.exit(1)
        elif opt in ('-s', '--specfwt'):
            fwt_spec_path = arg
        elif opt in ('-f', '--fwtfilepath'):
            if fwt_file_path is None:
                sys.exit("Please provide the mandatory param FWT file path: -f or --fwtfilepath")
            fwt_file_path = arg
        elif opt in ('-o', '--delimitedfilepath'):
            delimited_file_path = arg
        elif opt in ('-d', '--delimiter'):
            delimiter = str(arg)
        elif opt in ('-l', '--loglevel'):
            system_logs_level = arg.upper()
            if system_logs_level not in ["DEBUG", "INFO", "ERROR"]:
                sys.exit("Provided system logs level is not supported. Supported levels are DEBUG, INFO and ERROR")

    if fwt_file_path is None:
        print("Error starting FWT Parser, missing MANDATORY arguments. The arguments supported are:"
              " \n '-s' - path to the FWT specification file"
              " \n '-f' - path to the FWT file - MANDATORY"
              " \n '-o' - path to the delimited file"
              " \n '-d' - delimiter to be used"
              " \n '-l' - FWTParser system logs level"
              " \n Default values will be considered for the optional arguments if not provided.")
        sys.exit(1)
        
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=system_logs_level)

    if fwt_spec_path is None:
        fwtParser = FwtParser()
        logging.info("Parsing the provided FWT file against default specification - config/spec.json."
                     " Use -s or --specfwt to provide a specification file")
    else:
        fwtParser = FwtParser(fwt_spec_path)
    delimited_file = fwtParser.fwt_to_delimited(fwt_file=fwt_file_path, delimited_file=delimited_file_path,
                                                delimiter=delimiter)
    if delimited_file is None:
        logging.error("Error while converting FWT to delimited.")
    else:
        logging.info("Delimited file generated: %s", delimited_file)
