class Flights:
    def __init__(self,origin,destination,flightnumber,seatsnumber):
        self.origin = origin
        self.destination = destination
        self.flightnumber = flightnumber
        self.seatsnumber = seatsnumber

a = Flights('Tehran','Shiraz',100198 ,list(range(1,177)))
b = Flights('Tehran','Tabriz',100199 ,list(range(1,21)))
c = Flights('Esfahan','Mashhad',100219 ,list(range(1,350)))


def texting_write(filename,lst):
    d = lst
    #random.shuffle(d)
    dnum =''
    for num in d:
        dnum +=' '+str(num)
    with open (f'C:/Users/user/Desktop/{filename}.txt','w') as f:
        f.write(dnum)


texting_write('teh_shir',a.seatsnumber)
texting_write('teh_tab',b.seatsnumber)
texting_write('esf_mash',c.seatsnumber)


def texting_clean(filename):
    with open (f'C:/Users/user/Desktop/{filename}.txt','w') as f:
        f.write('')


texting_clean('teh_shir_sold')
texting_clean('teh_tab_sold')
texting_clean('esf_mash_sold')
