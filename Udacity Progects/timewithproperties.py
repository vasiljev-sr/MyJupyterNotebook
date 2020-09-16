from decimal import Decimal
class Time:
    '''Класс Time со свойствами, доступными для чтения/записи'''
    def __init__(self,hour = 0,minute = 0, sec = 0):
        '''Инициализация каждого атрибута'''
        self.hour = hour
        self.minute = minute
        self.sec = sec
    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self,hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Hour ({minute}) must be 0-59')
        self._minute = minute

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, sec):
        if not (0 <= sec < 60):
            raise ValueError(f'Hour ({sec}) must be 0-59')
        self._sec = sec

    def set_time(self,hour=0,minute = 0, sec = 0):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __repr__(self):
        """Возвращает строку Time для repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
            f'second={self.sec})')

    def __str__(self):
        """Выводит объект Time в 12-часовом формате времени."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
            f':{self.minute:0>2}:{self.sec:0>2}' +
            (' AM' if self.hour < 12 else ' PM'))