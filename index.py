# my_num1 = 10
# my_num2 = 20

# print("my_num1 + my_num2")
# def test_func():
#     print ("something")
    
    

def my_function(food):
  for item in food:
    print(item)

food = ["apple", "banana", "cherry"]

# my_function(food)


#test after

# a= 30
# b= 20
# c= 10
# d= 10

# assert a<b,"a is not smaller than b"
# assert c==d,"{} and {} are not equal".format(c,d)

# #test after 2
# def add_num(a,b):
#     return 7

# assert add_num(2,5) == 7,"the result of the add function is not correct"
# assert add_num(2,5) == 10,"the result of the add function is not correct"


#test 3 the challenege
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
# assert count_upper_case("thIS") == 2,"the result is not equal to true neither"
assert count_upper_case("FOUNDydf") == 5,"the result is not equal to true either"
# assert count_upper_case("12345") == 0,"the result is not equal to true at all"
# assert count_upper_case(5) == 0,"the result is not equal to true at all"




# mail server python-DO NOT DELETE-----

# https://myaccount.google.com/lesssecureapps

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']= 465
# app.config['MAIL_USERNAME'] = 'digitalclickmultiplier@gmail.com'
# app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEFAULT_SENDER'] ='digitalclickmultiplier@gmail.com.com'
# mail = Mail(app)




# @app.route("/")
# def index():
#     msg = Message('Mail test', recipients = ['digitalclickmultiplier@gmail.com'])
#     msg.body ="This is a mail testing email"
#     # msg.html =
#     mail.send(msg)
#     return "Sent"
#     # render_template("index.html")
 
#  -----------------serpate code dont use together-->
 # commit command need cause you are changing some data in pipline python3 my_db.py
        # finally:
        #     connection.close()  
# -------mail----DO NOT DELETE---