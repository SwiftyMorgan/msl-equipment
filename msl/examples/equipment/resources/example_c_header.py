"""
Example showing how to extract information from a C/C++ header file.
"""

# this "if" statement is used so that Sphinx does not execute this script when the docs are being built
if __name__ == '__main__':

    from msl.equipment.resources.utils import CHeader

    path = r'C:\Program Files\Pico Technology\SDK\inc\ps5000aApi.h'
    fcn_regex = 'PREF0\s+PREF1\s+(\w+)\s+PREF2\s+PREF3\s+\((\w+)\)'

    header = CHeader(path)

    print('***** Constants *****')
    constants = header.constants()
    for key, value in constants.items():
        print(key, value)
    print()

    print('***** Enums *****')
    enums = header.enums()
    for key, value in enums.items():
        print(key, value)
    print()

    print('***** Structs *****')
    structs = header.structs()
    for key, value in structs.items():
        print(key, value)
    print()

    print('***** Callbacks *****')
    callbacks = header.callbacks()
    for key, value in callbacks.items():
        print(key, value)
    print()

    print('***** Functions *****')
    fcns = header.functions(fcn_regex)
    for key, value in fcns.items():
        print(key, value)
