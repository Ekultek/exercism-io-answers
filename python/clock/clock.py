class Clock:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.hour > 23:
            self.hour %= 24

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

        if self.hour < 0:
            self.hour %= 24

    def __str__(self):
        if self.hour < 10:
            hour_string = "0{}".format(str(self.hour))
        else:
            hour_string = str(self.hour)
        if self.minute < 10:
            minute_string = "0{}".format(str(self.minute))
        else:
            minute_string = str(self.minute)

        return "{}:{}".format(hour_string, minute_string)

    def __eq__(self, other):
        if self.hour != other.hour:
            return False
        if self.minute != other.minute:
            return False
        else:
            return True

    def add(self, m):
        tot_min = (self.hour * 60) + self.minute
        tot_min += m
        self.hour = (tot_min // 60) % 24
        self.minute = tot_min % 60
        return self

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute
