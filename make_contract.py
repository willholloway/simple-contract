#!/usr/bin/env/python
# 
# Using the file system load
#
# We now assume we have a file in the same dir as this one called
# test_template.html
#

from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

name = 'Holloway Consulting LLC'
address = ''

def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

    name = raw_input('Consultant name: ')
    address = raw_input('Consultant address: ')
    company_name = raw_input('Company name: ')
    company_address = raw_input('Company address: ')
    county = raw_input('Legal jurisdiction County: ')
    state = raw_input('Legal jurisdiction State: ')
    print j2_env.get_template('contract.txt').render(
        name=name,
        address=address,
        company_name=company_name,
        company_address=company_address,
	county = county,
	state = state
    )

if __name__ == '__main__':
    print_html_doc()

