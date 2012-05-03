#!/usr/bin/python
# Copyright (c) 2010 Alon Swartz <alon@turnkeylinux.org> - all rights reserved
"""Configure ejabberd and speeqe

Options:
    --pass=      if not provided, will ask interactively
    --domain=    if not provided, will ask interactively
                 DEFAULT=example.com
"""

import sys
import getopt
import subprocess
from subprocess import PIPE

from dialog_wrapper import Dialog

def fatal(s):
    print >> sys.stderr, "Error:", s
    sys.exit(1)

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

DEFAULT_DOMAIN="example.com"

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'domain='])
    except getopt.GetoptError, e:
        usage(e)

    domain = ""
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--domain':
            domain = val


    if not domain:
        d = Dialog('TurnKey Linux - First boot configuration')
        domain = d.get_input(
            "Ejabberd Domain",
            "Enter top-level domain to associate with ejabberd and speeqe.",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN

    if not password:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        password = d.get_password(
            "Ejabberd Password",
            "Enter new password for ejabberd 'admin@%s' account." % domain)

    command = ["/usr/local/bin/ejabberd-config", domain, password]
    p = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, shell=False)
    stderr = p.wait()
    if stderr:
        fatal(stderr)


if __name__ == "__main__":
    main()

