# parse_services
Searches /etc/services for services that *matches exactly* the supplied string.
Returns a json list containing dicts. 

Each dict is a key of IP port type and port

Example usage:

**python parse_services.py ntp** Will search through all services for the those with the name ntp and return 

[{'udp': '123'}, {'tcp': '123'}]

Will return an empty list if no matching services are found.

Ends with exit code 1 on error along with the Exception text, otherwise exit code 0