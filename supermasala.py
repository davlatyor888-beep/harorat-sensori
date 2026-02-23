class haroratSensori:
    def __init__(self,sensor_id, joylashuv):
        self.__sensor_id = sensor_id
        self.__joylashuv = joylashuv
        self.__olchovlar = []
        self.__min_harorat = -50
        self.__max_harorat = 150


    def get_sensor_id(self):
        return self.__sensor_id
    def joylasuv(self):
        return self.__joylashuv
    def olchov_qosh(self,harorat, vaqt):
        if not(self.__min_harorat <= harorat <= self.__max_harorat):
            print("xato: harorat -50 dan 150 gacha bolishi kerak")
            return
        else:
            self.__olchovlar.append({"harorat": harorat, "vaqt": vaqt})

    def oxirgi_olchov(self):
        if not self.__olchovlar:
            return "hali olchov yoq"
        return self.__olchovlar[-1].copy

    def ortacha_harorat(self):
        if not self.__olchovlar:
            return 0.0
        jami=sum(o["harorat"] for o in self.__olchovlar)
        return round(jami / len(self.__olchovlar),2)
    def olchovlar_soni(self):
        return len(self.__olchovlar)
    def hisobot(self):
        oxirgi = self.oxirgi_olchov()
        if isinstance(oxirgi, str):
            oxirgi_str = "yoq"
        else:
            oxirgi_str = f"{oxirgi['harorat']} C, ({oxirgi['vaqt']})"
        return (
            f"Sensor: {self.__sensor_id} | joylashuv: {self.__joylashuv}\n"
            f"olchovlar soni: {self.olchovlar_soni()}\n"
            f"ortacha harorat: {self.ortacha_harorat()} C\n"
            f"oxirgi olchov: {oxirgi_str} \n"
            )

sensor = haroratSensori("S-001", "1-1")
sensor.olchov_qosh(22.5, "08:00")
sensor.olchov_qosh(25.3, "12:00")
sensor.olchov_qosh(19.8, "18:00")
sensor.olchov_qosh(200, "20:00")

print(sensor.oxirgi_olchov())
print(sensor.ortacha_harorat())
print(sensor.olchovlar_soni())
print(sensor.hisobot())
