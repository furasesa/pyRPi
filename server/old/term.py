version = '0.0.1'
import argparse

parser = argparse.ArgumentParser(description='raspberry GPIO config editor')

parser.add_argument('-show',
                    action="store_true",
                    default=False,
                    dest='show_config',
                    help='print GPIO config')

parser.add_argument('-v', '-version',
                    action="store_true",
                    default=False,
                    dest='show_version',
                    help='print vesion')

parser.add_argument('-term',
                    action="store_true",
                    default=False,
                    dest='shell_mode',
                    help='shell mode')

r = parser.parse_args()

if r.show_config:
    print('show config')

if r.show_version:
    print('version', version)

while r.shell_mode:
    term = input('rpi>> ')
    if term == 'quit':
        break
    if term == 'show':
        print('show config')
    print(term)
