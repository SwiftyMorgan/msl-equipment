"""
This example shows how to communicate with Thorlabs FW102C Series or
FW212C Series Motorized Filter Wheels.
"""

# this "if" statement is used so that Sphinx does not execute this script when the docs are being built
if __name__ == '__main__':
    from msl.equipment import EquipmentRecord, ConnectionRecord, Backend

    # rather than reading the EquipmentRecord from a database we can create it manually
    record = EquipmentRecord(
        manufacturer='Thorlabs',
        model='FW212C',  # specify FW102C is you are using the 6-position filter wheel (can also include the NEB suffix)
        connection=ConnectionRecord(
            backend=Backend.MSL,
            address='SDK::C:/Program Files/Thorlabs/FilterWheel102_win64.dll',  # update the location of the DLL
            properties={'port': 'COM4'},  # update the port number
        ),
    )

    # connect to the Filter Wheel
    wheel = record.connect()

    position = wheel.get_position()
    print('The initial filter position was {}'.format(position))

    # make the Filter Wheel return to the start position if it is at the last position
    if position == wheel.get_position_count():
        position = 0

    wheel.set_position(position+1)
    print('The current filter position is now {}'.format(wheel.get_position()))

    # disconnect from the Filter Wheel
    wheel.disconnect()
