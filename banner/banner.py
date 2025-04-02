#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

autor = '\033[1;41;37m.:Raptx:.\033[0m'
tool = '\033[1;44;37m.:.:SIMPLE LFI SCANNER:.:.\033[0m'

# COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'
RED_NORMAL = '\033[0;31m'
GREEN_NORMAL = '\033[0;32m'


def banner():
    os.system('clear' if os.name == 'posix' else 'cls')  # Cross-platform clear screen
    print(f"""
{CYAN}██╗     ███████╗██╗{WHITE}      ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ {END}
{CYAN}██║     ██╔════╝██║{WHITE}      ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗{END}
{CYAN}██║     █████╗  ██║{WHITE}█████╗███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝{END}
{CYAN}██║     ██╔══╝  ██║{WHITE}╚════╝╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗{END}
{CYAN}███████╗██║     ██║{WHITE}      ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║{END}
{CYAN}╚══════╝╚═╝     ╚═╝{WHITE}      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{END}

                             {tool}
                                {WHITE}Github: {autor}{END}
""")
