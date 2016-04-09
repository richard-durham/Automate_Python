#! python3
# mapIt.py - Launches a map in the browser using an address form the
# command line or clipboard.

import webbrowser, sys

if len(sys.argv) > 1:
    # get address from command line
    address = ''.join(sys.argv[1:])
