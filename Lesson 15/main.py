class Element:
    def agg_state(self, t, v):
        if v == "fahrenheit":
            t = Iron.convert_fr(self, t)
        elif v == "kelvin":
            t = Iron.convert_cl(self, t)

        print('Температура в цельсиях: ' + str(t))

        if t < self.t_plav:
            return 'Затвердение'
        elif t >= self.t_plav and t < self.t_isp:
            return "Плавление"
        else:
            return "Испарение"

    def convert_fr(self, tem):
        return (tem * 9 / 5) + 32

    def convert_cl(self, tem):
        return tem + 273


class Iron(Element):
    t_plav = 1538
    t_isp = 2862


class Chlorine(Element):
    t_plav = -100
    t_isp = -34


class Oxygen(Element):
    t_plav = -218
    t_isp = -182


a = Iron()
print(a.agg_state(1537, "celsius"))

b = Chlorine()
print(b.agg_state(-310, 'kelvin'))

c = Oxygen()
print(c.agg_state(1, 'fahrenheit'))
