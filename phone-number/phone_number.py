class PhoneNumber:
    def __init__(self, number):
        cleared = []
        for i in number:
            if i.isdigit():
                cleared.append(i)
        if cleared[0] == "1":
            del cleared[0]
        if len(cleared) == 10 and int(cleared[0]) > 1 and int(cleared[3]) > 1:
            self.number = "".join(cleared)
            self.area_code = self.number[0:3]
        else:
            raise ValueError("Wrong number format")

    def pretty(self):
        return f"({self.number[0:3]}) {self.number[3:6]}-{self.number[6:10]}"
