"""
This example shows how to communicate with Thorlabs KDC101, KCube DC Servo.
"""

# this "if" statement is used so that Sphinx does not execute this script when the docs are being built
if __name__ == '__main__':
    import os
    import time

    from msl.equipment import EquipmentRecord, ConnectionRecord, Backend
    from msl.equipment.resources.thorlabs.kinesis.enums import UnitType

    from msl.equipment import EquipmentRecord, ConnectionRecord, Backend

    # you must update the following values
    kinesis_path = 'C:/Program Files/Thorlabs/Kinesis'
    serial_number = '27251265'

    # the Thorlabs.MotionControl.KCube.DCServo.dll depends on other DLLs from Thorlabs
    # make sure to add the Kinesis folder to the environment PATH
    os.environ['PATH'] += os.pathsep + kinesis_path

    record = EquipmentRecord(
        manufacturer='Thorlabs',
        model='KDC101',
        serial=serial_number,
        connection=ConnectionRecord(
            backend=Backend.MSL,
            address='SDK::KCubeDCServo::Thorlabs.MotionControl.KCube.DCServo.dll',
        ),
    )

    motor = record.connect()
    print(motor)

    motor.start_polling(200)
    time.sleep(1)

    info = motor.get_hardware_info()
    print('Found device: {}'.format(info.notes))

    motor_params = motor.get_motor_params_ext()
    print('Motor Parameters : {}, {}, {}'.format(*motor_params))

    pos = motor.get_position()
    print('Current position [device units]= {}'.format(pos))
    print('Current position [mm]= {}'.format(motor.get_real_value_from_device_unit(pos, UnitType.DISTANCE)))

    print('Go home...')
    motor.home()

    vmax, acc = motor.get_vel_params()
    print('Max Velocity [device units], Acceleration [device units]= {}, {}'.format(vmax, acc))
    vmax_real = motor.get_real_value_from_device_unit(vmax, UnitType.VELOCITY)
    acc_real = motor.get_real_value_from_device_unit(acc, UnitType.ACCELERATION)
    print('Max Velocity [real-world units], Acceleration [real-world units]= {} mm/s, {} mm/s^2'.format(vmax_real, acc_real))

    print('Move to 5 mm')
    new_position = motor.get_device_unit_from_real_value(5.0, UnitType.DISTANCE)
    motor.move_to_position(new_position)
    pos = motor.get_position()
    print('Position [device units]= {}'.format(pos))
    print('Position [real-world units]= {}'.format(motor.get_real_value_from_device_unit(pos, UnitType.DISTANCE)))

    motor.stop_polling()
