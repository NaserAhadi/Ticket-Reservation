import random
print('*'*30)
print('Orders:')
print('new : use to add new person')
print('info : use to get flight and passengers information')
print('find : use to search and find ticket')
print('show : use to show flight number information')
print('edit name : use to editing person name')
print('edit id : use to editing person id')
print('exit : use to exit the program')
print('cancel : use to cancel ticket')
print('*'*30)

def info():
    try:
        with open ("C:/Users/user/Desktop/data.txt","r") as f:
            line = f.readline()
            get_info=input('which information do you want? "Flight Information" or "Passengers Information" or both of them? please enter f or p or b: \n')
            if get_info.lower().startswith('f'):
                print("Flight Information:\n")
                while line:
                    data_length = len(line.split()[0])
                    if data_length == 6 :
                        print(line)
                        line=f.readline()
                    else:
                        line=f.readline()
            elif get_info.lower().startswith('p'):
                print("Passengers Information:\n")
                while line:
                    data_length = len(line.split()[0])
                    if data_length != 9 :
                        line=f.readline()
                    else:
                        print(line)
                        line=f.readline()
            elif get_info.lower().startswith('b'):
                print("Flight Information And Passengers Information:\n")
                while line:
                    print(line)
                    line=f.readline()
            else:
                print('please enter "f" as "Flight Information" and "p" as "Passengers Information" or "b" to get both of them.')
    except IndexError as error:
        print('')


class Flights:
    def __init__(self,origin,destination,flightnumber,seatsnumber):
        self.origin = origin
        self.destination = destination
        self.flightnumber = flightnumber
        self.seatsnumber = seatsnumber

a = Flights('Tehran','Shiraz',100198 ,list(range(1,177)))
b = Flights('Tehran','Tabriz',100199 ,list(range(1,21)))
c = Flights('Esfahan','Mashhad',100219 ,list(range(1,350)))


def check(filename,param):
    with open (f"C:/Users/user/Desktop/{filename}.txt","r") as f:
        line=f.read()
        for item in line.split('\n'):
            if str(param) in item.split():
                return True
        return False


def random_digit():
    range_start = 10**4
    range_end = 10**5
    number =random.randint(range_start,range_end)
    num = '7989'+str(number)
    if check('data',num):
        random_digit()
    else:
        return num


def texting_append(filename,lst):
    d = lst
    dnum =''
    for num in d:
        dnum +=' '+str(num)
    with open (f'C:/Users/user/Desktop/{filename}.txt','a') as f:
        f.write(dnum)

def texting_write(filename,lst):
    d = lst
    dnum =''
    for num in d:
        dnum +=' '+str(num)
    with open (f'C:/Users/user/Desktop/{filename}.txt','w') as f:
        f.write(dnum)


def text_sold(filename,filename2,seatnum):
    try:
        global seatnumber
        seatnumber=''
        with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
            line = f.read()

        seatlst = line.split()
        soldlst=[]
        for i in range(seatnum):
            soldlst.append(seatlst[i])

        for num in soldlst:
            if num in seatlst:
                del seatlst[seatlst.index(num)]

        for num in soldlst:
            seatnumber +=' '+str(num)

        texting_write(filename,seatlst)
        texting_append(filename2,soldlst)
    except:
        if seatnum > len(seatlst):
            print('there is not enough space')


def origin_func(origin,destination):
    global txtfile,txtfile1,flightnum
    if origin == 'Tehran' and destination == 'Tabriz':
        txtfile ='teh_tab'
        txtfile1='teh_tab_sold'
        flightnum = b.flightnumber
    elif origin == 'Tehran' and destination == 'Shiraz':
        txtfile ='teh_shir'
        txtfile1='teh_shir_sold'
        flightnum = a.flightnumber
    elif origin == 'Esfahan' and destination == 'Mashhad':
        txtfile ='esf_mash'
        txtfile1='esf_mash_sold'
        flightnum = c.flightnumber
    else:
        pass

def find_id(filename='data'):
    person_id = input("input person's id : \n")
    with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
        line = f.read()
        lst=line.split('\n')
        for item in lst:
            try:
                if item.split()[3]==person_id:
                    print(f'name: {item.split()[2]}')
                    print(f'ID: {item.split()[3]}')
                    print(f'flight number: {item.split()[0]}')
                    if item.split()[-1]=='C':
                        print(f'seat numbers: {item.split()[4:-1]}')
                    else:
                        print(f'seat number: {item.split()[4:]}')
            except IndexError as error:
                print('')


def show(filename='data'):
    flightnum = input("What is flight number : \n")
    if check(filename,flightnum):
        with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
            line = f.read()
            lst=line.split('\n')
            for item in lst:
                if item.split()[0]==flightnum:
                    return(f'origin city: {item.split()[1]}\ndestination city: {item.split()[2]}')
    else:
        return(f'there is no flight')

def edit_name(filename='data'):
    person_name = input("input person's name : \n").capitalize()
    editname = input("input edited person's name : \n").capitalize()
    if check(filename,person_name):
        with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
            line = f.read()
            line=line.replace(person_name,editname)
            with open(f'C:/Users/user/Desktop/{filename}.txt','w') as f:
                f.write(line)
            print('Edit Done')
            print(line)
    else:
        print(f'there is no name like {person_name}')

def edit_id(filename='data'):
    person_id = input("input person's id : \n")
    editid = input("input person's edited id : \n")
    if check(filename,person_id):
        with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
            line = f.read()
            line=line.replace(person_id,editid)
            with open('C:/Users/user/Desktop/data.txt','w') as f:
                f.write(line)
            print('Edit Done')
            print(line)
    else:
        print(f'there is no id like {person_id}')

def cancel(filename='data'):
    ask=input('are you sure?(y/n) \n')
    try:
        if ask.lower().startswith('y'):
            ticket_sellnum = input('please input ticket sell number : \n')
            with open(f'C:/Users/user/Desktop/{filename}.txt','r') as f:
                newtxt2=''
                cancelitem=''
                line = f.read()
                sp_line = line.split('\n')
                for i in sp_line:
                    if i[:9]== ticket_sellnum:
                       item_index=line.split('\n').index(i)
                       cancelitem = line.split('\n')[item_index]+'  cancel '

                for char in sp_line[:item_index]:
                    newtxt2+=char+'\n'
                newtxt2+=cancelitem+'\n'
                for char in sp_line[item_index+1:]:
                    newtxt2+=char+'\n'

                with open(f'C:/Users/user/Desktop/{filename}.txt','w') as f:
                    f.write(newtxt2)
                    print(f'{ticket_sellnum} was canceled!')
        else:
            pass
    except:
        if len(ticket_sellnum)>9:
            print('ticket sellnumber have more than 9 character')
        elif i[:9] != ticket_sellnum:
            print('there is no sell number')
        else:
            print('something went wrong')


while True:
    order = input("input order: ")
    if order.lower() == 'new':
        name = input("input Name: ").capitalize()
        id_codes = input("input id_code:").capitalize()
        origin = input("input origin:").capitalize()
        destination = input("input destination:").capitalize()
        num_of_seats = int(input("input number of reserved seats:"))
        situation_state = ''
        txtfile = ''
        txtfile1=''
        sell_number = random_digit()
        origin_func(origin,destination)
        with open(f'C:/Users/user/Desktop/{txtfile}.txt','r') as f:
            line = f.read()
        if num_of_seats > len(line.split()):
            print('there is not enough space')
            break
        else:
            if num_of_seats > 1:
                situation_state = 'C'
                text_sold(txtfile,txtfile1,num_of_seats)

            else:
                text_sold('teh_tab','teh_tab_sold',num_of_seats)


        with open ('data.txt','a') as f:
            f.write('\n'+sell_number + ' ' + str(flightnum) +' '+name+' '+str(id_codes) + ' '+ seatnumber+' '+situation_state)

        with open (f"C:/Users/user/Desktop/data.txt","r") as f:
            line=f.read()
            pp = line.split('\n')[-1]
            if pp.split()[-1]=='C':
                print(f'Done-sell number: {pp.split()[0]} \nseats ={pp.split()[4:-1]} ')
            else:
                print(f'Done-sell number: {pp.split()[0]} \nseats ={pp.split()[4:]} ')



    elif order.lower() == 'info':
        info()
        continue

    elif order.lower() == 'find':
        find_id()
        continue

    elif order.lower() == 'show':
        print(show())
        continue

    elif order.lower() == 'edit name':
        edit_name()
        continue

    elif order.lower() == 'edit id':
        edit_id()
        continue

    elif order.lower() == 'cancel':
        cancel()
        continue

    elif order.lower() == 'exit':
        break

    else:
        print('please input right order!!')
        continue


