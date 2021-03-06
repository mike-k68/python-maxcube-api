import json


MAX_CUBE = 0
MAX_THERMOSTAT = 1
MAX_THERMOSTAT_PLUS = 2
MAX_WALL_THERMOSTAT = 3
MAX_WINDOW_SHUTTER = 4
MAX_PUSH_BUTTON = 5

MAX_DEVICE_MODE_AUTOMATIC = 0
MAX_DEVICE_MODE_MANUAL = 1
MAX_DEVICE_MODE_VACATION = 2
MAX_DEVICE_MODE_BOOST = 3

MAX_DEVICE_BATTERY_OK = 0
MAX_DEVICE_BATTERY_LOW = 1


class MaxDevice(object):
    def __init__(self):
        self.rf_address = None
        self.type = None
        self.room_id = None
        self.firmware = None
        self.serial = None
        self.name = None
        self.initialized = None
        self.battery = None

    def is_thermostat(self):
        return self.type in (MAX_THERMOSTAT, MAX_THERMOSTAT_PLUS)

    def is_wallthermostat(self):
        return self.type == MAX_WALL_THERMOSTAT

    def is_windowshutter(self):
        return self.type == MAX_WINDOW_SHUTTER

    def is_room(self):
        return False

    def to_dict(self):
        data = {}
        
        keys = ['rf_address', 'type', 'room_id', 'firmware', 'serial', 'name', 'initialized',
                'battery', 'comfort_temperature', 'eco_temperature', 'max_temperature',
                'min_temperature', 'target_temperature', 'actual_temperature',
                'locked', 'mode', 'vacation_until', 'temperature_offset', 'window_open_temperature',
                'window_open_duration', 'boost_duration', 'boost_valve_position', 'decalcification', 
                'max_valve_setting', 'valve_offset', 'valve_position', 'programme']
        for key in keys:
            data[key] = getattr(self, key, None)
        data['rf_address'] = self.rf_address
        return data
