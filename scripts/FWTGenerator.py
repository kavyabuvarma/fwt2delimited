import getopt
import sys
import logging
from pathlib import Path
from fwt.fwtUtils import FwtGen

if __name__ == "__main__":

    # default values
    fwt_file_path = "fwt_file.txt"
    path_sample_data_file_path = Path(__file__).parent.parent / "config/sample_values.json"
    sample_data_file_path = str(path_sample_data_file_path)
    system_logs_level = "INFO"
    number_of_records = 20

    use_random_values = False
    fwt_spec_path = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:f:n:l:r:h',
                                   ['specfwt=', 'fwtfilepath=', 'numofrecords=', 'loglevel=',
                                    "userandomvalues=", 'help'])
    except getopt.GetoptError:
        print("Error executing FWT Generator. The arguments supported are:"
              " \n '-s' - path to the FWT specification file"
              " \n '-f' - path to the output FWT file"
              " \n '-n' - number of records"
              " \n '-l' - FWTGenerator system logs level"
              " \n '-r' - set \"random\" or any value to use random data for FWT file"
              " \n Default values for the arguments will be considered when not provided.")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('scripts/FWTGenerator.py -s <path_to_fwt_spec_file> \\'
                  '-f <path_to_fwt_file> \\'
                  '-n <number_of_records> \\'
                  '-r <use_random_values> \\'
                  '-l <system_logs_level>')
            sys.exit(2)
        elif opt in ('-s', '--specfwt'):
            fwt_spec_path = arg
        elif opt in ('-f', '--fwtfilepath'):
            fwt_file_path = arg
        elif opt in ('-n', '--numofrecords'):
            number_of_records = int(arg)
        elif opt in ('-r', '--userandomvalues'):
            use_random_values = True
        elif opt in ('-l', '--loglevel'):
            system_logs_level = arg.upper()
            if system_logs_level not in ["DEBUG", "INFO", "ERROR"]:
                sys.exit("Provided system logs level is not supported. Supported levels are DEBUG, INFO and ERROR")

    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=system_logs_level)

    if fwt_spec_path is None:
        fwtGen = FwtGen()
    else:
        fwtGen = FwtGen(fwt_spec_path)

    fwt_file = fwtGen.generate_fwt_file(random_data=use_random_values, num_of_records=number_of_records,
                                        file_name=fwt_file_path)
    if fwt_file is not None:
        logging.info("FWT file generated : %s", fwt_file)
    else:
        logging.error("Error generating FWT file.")
