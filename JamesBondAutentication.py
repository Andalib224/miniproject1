# mytuple=(4,5,6,"Hello")
# item1,item2,item3,item4 = mytuple
# print(item1)
# print(item4)

# l1=['hello',5.6,(2,3),["MyName","Squid Game"]]
# a1,a2,a3,a4=l1
# print(a3)
# print(a4)

# mystr="Welc"

# s1,s2,s3,s4=mystr
# print(s2)

# list1=["Myname",2.5,56,{"name":"andalib","rollono":45},[28,65]]

# name1,num1,*rest=list1
# print(name1)
# print(num1)
# print(rest)


# records = [
#  ('foo', 1, 2),
#  ('bar', 'hello'),
#  ('foo', 3, 4)]

# for i,*j in records:
#      if i == 'foo':
#          print(j)
#      elif i == 'bar':
#          print(j)

# address = 'https://www.google.com/search?q=rest+api+call+python+&rlz=1C1CHBF_enIN975IN975&ei=JsKIYcHRKMrFrQG8-'
# h1,*h2,h3=address.split('+')
# print(h1)
# print(h2)
# print(h3)

# p1=['hello',22,34,(22,9,2019),'yellow']
# p2,*_,(*_,year),_=p1
# print(year)

# mystr="Hello {}".format(1+2)
# hello=" I am a simple {} and mul of {},{}={}".format("String",3,4,3*4)

# print(mystr)
# print(hello)

# yes_vote=42_344_213
# no_vote=54_365_1544
# # print(yes_vote)
# percentage=yes_vote/(yes_vote + no_vote)
# print(percentage)

# print("hello {:-4}  {:2.2%}".format(yes_vote,percentage))


# import json

# dummy_json='''{
#     "id": 1,
#     "name": "Leanne Graham",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#       "street": "Kulas Light",
#       "suite": "Apt. 556",
#       "city": "Gwenborough",
#       "zipcode": "92998-3874",
#       "geo": {
#         "lat": "-37.3159",
#         "lng": "81.1496"
#       }
#     }
# }'''

# mydic={
#     "name" : "andalib",
#     "rollno":56

# }

# converted_to_json=json.dumps(mydic)

# print(converted_to_json)
# print(json.dumps(True))
# print(json.dumps(['orange','apple',22,45,'juliya']))
# # converted_json_python=json.loads(dummy_json)

# # back_to_json=json.dumps(converted_json_python)

# # print(converted_json_python)

# # print(converted_json_python["address"])
# # print(back_to_json)

# import json

# dummy={
#     "names":["andalib","suriya","poonam"],
#      "age":25,
#      "height":5.8,
#      "cars":["suv","yahoo","bmw"]
# }

# names_to_json=json.dumps(dummy,indent=4,separators=(", "," = "),sort_keys=True)
# print(names_to_json)

# import re

# myfile= "Alien is a good friend"

# # x=re.search("*friend",myfile)
# # if (x):
# #     print("We got the match!!!!!!")

# myfile1=re.findall('is',myfile)
# print(myfile1)

# from re import findall


# try:
#     print("How are you today!!!!!")

# except NameError:
#     print("x is not defiened")  
# except:
#     print("Exceptin occured")
# else:
#     print("Every thing is all right!!!!!!")
# finally:
#     print("You can't stop me to execute it!!!!!")

# try:
#     f=open("myfile.txt")
# except FileNotFoundError:
#     print("FIle doesn't exist!!!!!")
# finally:
#     print("You just can't stop me!!!!!!!")

# x=15
# if x>14:
#     raise Exception("Sorry x can't be less than 15")

# mystr="Welcome"

# if not type(mystr) is int:
#     raise TypeError("Sorry str shouldn't be string!!!!!!!!!")

# try:
#     new_file=open("Candy1.txt","a")
    
#     new_file.write("One line has benn added")

# except FileExistsError:
#     raise Exception("File exists")

# # finally:
# #     new_file.close()

# def total_overs(bowling):
#     return bowling//6 + bowling%6/10
    
    

    
   


# full_over=total_overs(5)
# print(full_over)

# def area_of_country(country,area):
#     total_land_mass=148_940_000
    
#     our_area_land_mass=(area/total_land_mass) * 100
#     return round(our_area_land_mass,2)

    



# =area_of_country("Russia",17098242)


# def format_date(date_as_input):
#     x=date_as_input.split("/")
#     print(x[2]+""+x[1]+""+x[0])
    

    



# format_date("11/12/2019")


# print(2**3 + 8//4)




# print((4-2)**3 + (8//2)**2)
# print(             2+       2)

# print('hello')

# print('Hello'+ "joy")
# print("ANdalib  " * (8//2))

# print("What is \nyour name \nand age")
# print("My name is Andalib",end="\t")
# print("Let's sse")

# print(int(-9.65))

# print(int('48'))

# # print(42==00042.00)

# print('I have ice-cream ' + str(22) + ' and only ')


# def add(str1,str2):
#     if(str1=="" or str2=="" or str1==None or str2==None):
#         return "Invalid operation"
#     else:
#          result=str(int(str1)+ int(str2))
#          return result



# output=add("90","10")
# print(output)

# name=''
# while name !='rahul':
#     name=input()
#     print(f"You have entered your name={name}")

# print(f"Now your name is {name}")
secret_number=4895
def grant(name,pass_key):
    if name=="James Bond" and pass_key==secret_number:
        return "Granted"
    else:
        return "Not Granted"



has_granted = False
number_of_attemtp=0

while not has_granted:
    print("Who are you?")
    name = input("Enter your name: ")
    if name != "James Bond":
        number_of_attemtp +=1
        print("Please Try again")
        if number_of_attemtp ==3:
            print("Sorry!, you have exceed the limit!!")
            break
        continue
    elif name == "James Bond":
        number_of_attemtp = 2
        print("Thank you Mr. Bond")
        safe_secret_number=int(input("Please Enter your safe Secret number:  "))
        
        if safe_secret_number == secret_number:
            print("Thank you for providing safe secret numbers, Here is your locker..")
            has_granted=True
            break
        elif safe_secret_number != secret_number:
               
            while number_of_attemtp>0:
                
                print(f''' You have this amount of attempts {number_of_attemtp},
                 Think hard tik tik, tik tik.. ''')
                number_of_attemtp -=1
                safe_secret_number=int(input("Please Enter your safe Secret number Again:  "))
                is_eligible=grant(name,safe_secret_number)
                
                if (is_eligible == "Granted"):
                    has_granted=True
                    break
                
                if (number_of_attemtp ==0):
                    print("Sorry Mr. Bond You have exceed the limit you are arrested")
                    has_granted=True
                    break
            
                
        # elif number_of_attemtp ==2:
        #     has_granted = True



        
