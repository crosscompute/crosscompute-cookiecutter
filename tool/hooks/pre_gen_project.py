import re
import sys

PACKAGE_PATTERN = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

tool_name_slug = '{{ cookiecutter.tool_name_slug }}'

if not PACKAGE_PATTERN.match(tool_name_slug):
    sys.exit(f'tool_name: is not valid')
