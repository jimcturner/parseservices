import sys

helptext = \
"""
Searches /etc/services for services that *matches exactly* the supplied string.
Returns a json list containing dicts. Each dict is a key of IP port type and port

Example usage:

python parseservices.py ntp

Will search through all services for the those with the name ntp and return [{'udp': '123'}, {'tcp': '123'}]
"""

def get_port_and_protocol(needle: str)->list:
    """
    Searches the /etc/services file for the string needle

    Returns a list containing dicts keyed with the IP type (eg udp or tcp) with the values set to the
    port number registered to that service.

    eg for f('ntp') >>>> [{'udp': '123'}, {'tcp': '123'}]
    :param needle:
    :return:
    """
    SERVICES_FILENAME = '/etc/services'

    # Lines starting with the following characters will be ignored
    ignoreLines = ["#", " "]

    results = []

    if not isinstance(needle, str):
        raise Exception(f"parse_services() excpects a string. Value {needle} of type {type(needle)} supplied")

    # Use context manager to guarantee that the file will be closed properlym even if an Exception is raised
    with open(SERVICES_FILENAME) as f:
        # Infinite loop to implement a do-while
        while True:
            # Read one line at a time from the stream into memory
            line = f.readline()

            # Exit conditions
            if line is None or len(line) == 0:
                break

            # Ignore comments or any other lines starting with special characters
            if line[0] in ignoreLines:
                pass

            else:
                fields = line.split()
                # Test fields[0] to see if we have a match
                # Validate no of fields. Should be at least 'service name', 'port/type', 'description'
                if len(fields) >= 3:
                    # Explicit implementation: needle *has to match* the service name exactly
                    if fields[0] == needle:
                        portType = fields[1].split('/')
                        if len(portType) == 2:
                            # Create the result dict for this service, and append to results
                            result = {portType[1]: portType[0]}
                            results.append(result)
                        else:
                            raise Exception(f"Unexpected port no/port type: {portType}")
                else:
                    raise Exception(f"Failed to parse line {line}")
    return results

def main(argv):
    try:
        if len(argv) == 0:
            raise Exception("No search term provided.  Use -h or --help for usage.")
        if argv[0] in ['-h', '--help']:
            print(helptext)
        else:
            print(get_port_and_protocol(argv[0]))
            exit(0)

    except Exception as e:
        print(f"{e}")
        exit(1)


# Invoke main() method (entry point for Python script)
if __name__ == "__main__":
    # Call main. Pass all *additional* command line args only
    main(sys.argv[1:])