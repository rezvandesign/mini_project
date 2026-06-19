class Lamp :
    status = 'off'

    def __init__(self,color,wat):
        self.color=color
        self.wat=wat

    def on (self) :
        if self.status == 'off' :
            self.status = 'on'
            
            return 'turn on the lamp'
        return 'the lamp is on'
        
    def off (self) :
        if self.status == 'on' :
            self.status = 'off'

            return 'turn off the lamp'
        return 'the lamp is off'
    
    def switcher (self) :
        if self.status == 'off' :
            self.on()
        else:
            self.off()

lamp1=Lamp('white' , 120)

# print(lamp1.on())
# print(lamp1.on())
# print(lamp1.on())
# print(lamp1.off())
# print(lamp1.off())
# print(lamp1.off())

# وضعیت لامپ


lamp1.switcher()
lamp1.switcher()
lamp1.switcher()
lamp1.switcher()

print(lamp1.status)
        