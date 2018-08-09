from msl.equipment import resources, Backend, ConnectionRecord


def test_find_resource_class():

    record = ConnectionRecord(manufacturer='XXX', model='yyy', backend=Backend.MSL)
    cls = resources.find_resource_class(record)
    assert cls is None

    for man in ('Bentham', 'Bentham Instruments Limited', 'Bentham Instruments Ltd.'):
        for mod in ('TMc300', 'dtmc300'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.bentham.benhw64.Bentham

    for man in ('CMI', 'Czech Metrology Institute',):
        record = ConnectionRecord(manufacturer=man, model='sia3', backend=Backend.MSL)
        cls = resources.find_resource_class(record)
        assert cls == resources.cmi.sia3.SIA3

    for man in ('OMEGA', 'omega'):
        for suffix in ('w3', 'd3', 'sd', 'm', 'w', '2'):
            record = ConnectionRecord(manufacturer=man, model='ithx-'+suffix, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.omega.ithx.iTHX

    for man in ('picotech', 'Pico Tech', 'Pico Technologies', 'Pico Technology'):
        for mod in ('PicoScope 2104', '2104', '2105', '2202', '2203', '2204', '2205', '2204A', '2205A'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps2000.PicoScope2000, mod
        for mod in ('PicoScope 2205A MSO', '2205A MSO', '2205 MSO',
                    '2206', '2206A', '2206B', '2206B MSO',
                    '2207', '2207A', '2207B', '2207B MSO',
                    '2208', '2208A', '2208B', '2208B MSO',
                    '2405A', '2406B', '2407B', '2408B'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps2000a.PicoScope2000A, mod
        for mod in ('PicoScope 3204', '3204', '3205', '3206', '3224', '3424', '3425'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps3000.PicoScope3000, mod
        for mod in ('PicoScope 3203D', '3203D', '3204D', '3205D', '3206D',
                    '3403D', '3404D', '3405D', '3406D',
                    '3203D MSO', '3204D MSO', '3205D MSO', '3206D MSO',
                    '3403D MSO', '3404D MSO', '3405D MSO', '3406D MSO',
                    '3204A', '3205A', '3206A', '3207A',
                    '3204B', '3205B', '3206B', '3207B',
                    '3204 MSO', '3205 MSO', '3206 MSO',
                    '3404A', '3405A', '3406A',
                    '3404B', '3405B', '3406B',):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps3000a.PicoScope3000A, mod
        for mod in ('PicoScope 4224', '4224', '4224 IEPE', '4262', '4424'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps4000.PicoScope4000, mod
        for mod in ('PicoScope 4444', '4444', '4824'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps4000a.PicoScope4000A, mod
        for mod in ('PicoScope 5000', '5000'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps5000.PicoScope5000, mod
        for mod in ('PicoScope 5242A', '5242A', '5243A', '5244A', '5442A', '5443A', '5444A',
                    '5242B', '5243B', '5244B', '5442B', '5443B', '5444B'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps5000a.PicoScope5000A, mod
        for mod in ('PicoScope 6407', '6407', '6402C', '6402D', '6403C', '6403D', '6404C', '6404D'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.picotech.picoscope.ps6000.PicoScope6000, mod

    for man in ('Thorlabs', 'Thorlabs Inc.'):
        for mod in ('FW102C', 'FW102CNEB', 'FW212C', 'FW212CNEB'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.fwxx2c.FilterWheelXX2C
        for mod in ('BSC101', 'BSC102', 'BSC103', 'BSC201', 'BSC202', 'BSC203'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.benchtop_stepper_motor.BenchtopStepperMotor
        for mod in ('MFF101', 'MFF102', 'MFF101/M', 'MFF102/M'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.filter_flipper.FilterFlipper
        for mod in ('LTS150', 'LTS150/M', 'LTS300', 'LTS300/M',
                    'MLJ050/M', 'MLJ150', 'MLJ150', 'MLJ150/M'
                    'K10CR1', 'K10CR1/M'):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.integrated_stepper_motors.IntegratedStepperMotors
        for mod in ('KDC101', ):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.kcube_dc_servo.KCubeDCServo
        for mod in ('KSC101', ):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.kcube_solenoid.KCubeSolenoid
        for mod in ('KST101', ):
            record = ConnectionRecord(manufacturer=man, model=mod, backend=Backend.MSL)
            cls = resources.find_resource_class(record)
            assert cls == resources.thorlabs.kinesis.kcube_stepper_motor.KCubeStepperMotor

    for man in ('OptoSigma', 'Opto Sigma', 'SigmaKoki', 'SigmaKoki', 'Sigma Koki Co. LTD'):
        record = ConnectionRecord(manufacturer=man, model='SHOT-702', backend=Backend.MSL)
        cls = resources.find_resource_class(record)
        assert cls == resources.optosigma.shot702.SHOT702
