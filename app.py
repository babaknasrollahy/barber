from flask import Flask, render_template , request, redirect, url_for , session
import barbers , comments , models , shops , times , users , open_times, others_sql, base_models
import sqlite3
from datetime import timedelta
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "qwerty123456barber"
app.permanent_session_lifetime = timedelta(days=120)



def GetSession(key):
   try:
    temp = session.get(key)
    print(temp,"-----------------------------------------------------")
    if temp == None:
     return ""
    return temp
   except:
    print("NULLLLLLLLLLLLL-----------------------------------------------------")
    return "no"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    
    if request.method == "POST":
        number = request.form.get("number")
        password = request.form.get("password")
        check_login = users.check_login(number)
        print(number , password , check_login)
        if check_login == f"{password}":
            session['number'] = number
            return redirect(url_for("user_info"))
        else:
            return "your number or password is not correct ."

@app.route("/table")
def create_table():
    barber = barbers.create_table()
    comment = comments.create_table()
    model = models.create_table()
    shop = shops.create_table()
    time = times.create_table()
    user = users.create_table()
    open_time = open_times.create_table()
    base_model = base_models.create_table()


    return f"{barber}  {comment}  {model}  {shop}  {time}  {user}  {open_time}  {base_model}"

@app.route("/status")
def status():
    db = sqlite3.connect('./database.sql')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    print(result)
    return result

@app.route("/")
def home():
    data_list = [ {"x": 35.722344529568815,"y": 51.420510209408484}, {"x":35.722344529568815 ,"y":51.0510209408484 }]
    return render_template("test.html", data=data_list)


########## Create User ###########
@app.route("/create_user")
def create_user():
    return render_template("create_user.html")

@app.route("/create_user_form")
def create_user_form():
    return render_template("create_user_form.html")

@app.route("/user_create", methods=["POST"])
def user_create():
    try:
        user_name = request.form.get("user_name")
        avatar = request.form.get("avatar")
        number = int(request.form.get("number"))
        email = request.form.get("email")
        password = request.form.get("password")
        if request.form.get("gender") == "Male" :
            gender = 0
        else:
            gender = 1
        full_name = request.form.get("full_name")
        print(type(user_name), type(avatar), type(number), type(email), type(password), type(gender), type(full_name))
    except:
        return "There was an error with your data !!"
    
    result = users.create_user(user_name,avatar,number,email,password,gender,full_name,role=0)
    if result == True :
        return redirect(url_for("user_info"))
    else:
        return "There was a server error ."

@app.route("/user_info/")
def user_info():
    user_id = GetSession("number")
    print(f"this is user_id ----> {user_id}")
    result = users.user_info(user_id)

    return render_template("user_info.html" , data=result[0])
#############################

####### Create Barber ##########

@app.route("/create_barber_form")
def create_barber_form():
    return render_template("create_barber_form.html")


@app.route("/barber_create", methods=["POST"])
def barber_create():
    try:
        user_name = request.form.get("user_name")
        avatar = request.form.get("avatar")
        number = int(request.form.get("number"))
        email = request.form.get("email")
        password = request.form.get("password")
        if request.form.get("gender") == "Male" :
            gender = 0
        else:
            gender = 1
        full_name = request.form.get("full_name")
        print(type(user_name), type(avatar), type(number), type(email), type(password), type(gender), type(full_name))
    except:
        return "There was an error with your data !!"
    
    result = users.create_user(user_name,avatar,number,email,password,gender,full_name,role=1)
    if result == True :
        return redirect(url_for("login"))
    else:
        return "There was a server error ."

        

@app.route("/barber_info" , methods=['GET', 'POST'])
def barber_info():
    if request.method == "GET":
        number = GetSession("number")
        user_id , role = users.get_user_id_and_role_by_number(number)
        print(user_id , role , number)
        if role == 1 :
            result = barbers.get_all_info_of_barbers(user_id)
            print(result)
            return render_template("barber_info.html" , result=result)
        else:
            return "permission denied"
    
    elif request.method == "POST":
        number = GetSession("number")
        user_id , role = users.get_user_id_and_role_by_number(number)
        print("=======================")
        if role == 1 :
            print("########################")
            image = request.form.get("image")
            national_code = request.form.get("national_code")
            age = request.form.get("age")
            experience = request.form.get("experience")
            about = request.form.get("about")
            stat = barbers.update_barber_info(user_id,image,national_code, age , experience, about)
            print(stat)
            return redirect(url_for("barber_info"))
        else:
            return "permission denied"

#######################




####### Create Shop ########
        
@app.route("/create_shop", methods=["get", "post"])
def create_shop():
    if request.method == "GET" :
        number = GetSession("number")
        user_id , role = users.get_user_id_and_role_by_number(number)
        if role == 1 :
            image , n_code , age, exp = barbers.get_nessecury_info_of_barber(user_id)
            print(image,n_code,age,type(exp))
            if image == None or n_code == None or age == None or exp == None :
                return redirect(url_for("barber_info"))
            
            else:
                stat = shops.is_shop_exist(user_id)
                print(stat)
                if stat == False :
                    print("in the false")
                    return render_template("create_shop.html")
                elif stat == True :
                    print("in the true")
                    return redirect(url_for("shop_info"))
        return "permission problem "
    
    elif request.method == "POST":
        try:
            number = GetSession("number")
            user_id , role = users.get_user_id_and_role_by_number(number)
            if role == 1 :
                image = request.form.get("image")
                location = request.form.get("location")
                shop_name = request.form.get("shop_name")
                about = request.form.get("about")
                stat = shops.create_shop(user_id,image,location,shop_name,about)
        except Exception as e:
            print(e)
            return "error in create shop"
        return "your shop created . "
    

@app.route("/shop_info" , methods=["GET", "POST"])
def shop_info():
    if request.method == "GET" :
        number = GetSession("number")
        user_id , role = users.get_user_id_and_role_by_number(number)
        shop_exist = shops.is_shop_exist(user_id)
        if role == 1 and shop_exist == True :
            result = shops.get_all_info_of_shops(user_id)
            print(result)
            if result == [] :
                result = [None, None,None,None]
                return render_template("shop_info.html", result=result)
            else:
                print("in the else")
                return render_template("shop_info.html", result=result[0])
            
    elif request.method == "POST":
        number = GetSession("number")
        user_id , role = users.get_user_id_and_role_by_number(number)
        if role == 1 :
            image = request.form.get("image")
            location = request.form.get("location")
            shop_name = request.form.get("shop_name")
            about = request.form.get("about")
            stat = shops.update_shop_info(user_id,image,location,shop_name,about)
            print(stat)
            return redirect(url_for("shop_info"))

    return "test"

###########################


####### Create Models ########

@app.route("/models")
def list_models():
    number = GetSession("number")
    user_id , role = users.get_user_id_and_role_by_number(number)
    shop_id = shops.get_shop_id_by_user_id(user_id)
    if role == 1 :
        data = models.get_models_for_a_shop(shop_id)
        return render_template("models.html" , data=data)

@app.route("/create_model" , methods=["GET", "POST"])
def create_model():
    number = GetSession("number")
    user_id , role = users.get_user_id_and_role_by_number(number)
    has_shop = shops.is_shop_exist(user_id)
    if role == 1 and has_shop == True:
        if request.method == "GET" :
            data = base_models.get_base_model()
            return render_template("create_model.html" , data=data)
        
        elif request.method == "POST" :
                shop_id = shops.get_shop_id_by_user_id(user_id)
                model_name = request.form.get("model_name")
                price = request.form.get("price")
                time = request.form.get("time")
                base_model_name = request.form.get("base_model_name")
                base_model_id = base_models.get_base_model_id(base_model_name)
                stat = models.create_model(model_name,price,shop_id,time,base_model_id)
                return f"{stat}"
    return "You don't have permission. please check your role and shop . "

@app.route("/base_model")
def base_model():
    return render_template("base_model.html")


@app.route("/create_base_model", methods=["GET", "POST"])
def create_base_model():
    if request.method == "GET" : 
        return render_template("create_base_model.html")
    
    elif request.method == "POST" :
        model_name = request.form.get("model_name")
        stat = base_models.create_base_model(model_name)
        return f"{stat}"




##############################


####### List Shops #########
    
@app.route("/shop_list")
def shop_list():
    data = shops.get_all_shops()
    return render_template("shop_list.html", data=data)

@app.route("/shops_models/<int:shop_id>")
def shops_models(shop_id):
    data = models.get_models_for_a_shop(shop_id)
    if data == [] :
        return "This shop doesn't have any model."
    
    print(data)
    return render_template("shops_models.html", data=data)

@app.route("/shop_models/<int:shop_id>/<int:model_id>/get_time")
def kdfjkdfj(shop_id, model_id):
    return render_template("create_order.html")

#############################


###### Open Times #######

@app.route("/open_times")
def open_times_list():
    number = GetSession("number")
    user_id , role = users.get_user_id_and_role_by_number(number)
    has_shop = shops.is_shop_exist(user_id)
    if role == 1 and has_shop == True :
        if request.method == "GET" :
                shop_id = shops.get_shop_id_by_user_id(user_id)
                data = open_times.get_open_time_by_shop_id(shop_id)
                return render_template("open_times.html" , data=data)
    else:
        return "You don't have permission to see this page .\n please check your role and your creation of a shop"
    
@app.route("/create_open_times",methods=["GET","POST"])
def create_open_times():
    number = GetSession("number")
    user_id , role = users.get_user_id_and_role_by_number(number)
    has_shop = shops.is_shop_exist(user_id)
    if role == 1 and has_shop == True :

        if request.method == "GET" :
            return render_template("create_open_times.html")
        
        elif request.method == "POST" :
            day = request.form.get("day")
            start_time = request.form.get("start_time")
            end_time = request.form.get("end_time")
            shop_id = shops.get_shop_id_by_user_id(user_id)
            result = open_times.create_open_time(shop_id,day,start_time, end_time)
            if result == True:
                return redirect(url_for("open_times_list"))
            else:
                return f"There is bug in query"
        
#########################



@app.route("/users")
def get_users():
    res = users.get_all_users()
    return res



@app.route("/trigger")
def trigger():
    res = others_sql.after_create_shop()
    print(res)
    return f"{res}"

@app.route("/get_barbers")
def get_barbers():
    res = barbers.get_all_barbers()
    print(res)
    return f"{res}"

@app.route("/query")
def query():
    try:
        db = sqlite3.connect("./database.sql")
        cursor = db.cursor()
        query = """SELECT * FROM open_times"""
        res = cursor.execute(query).fetchall()
        db.commit()
        cursor.close()
        db.close()
        return res
    except Exception as e:
        print("=================\n", e)
        return "error"

@app.route("/test")
def test():
    # result = base_models.get_base_model()
    return render_template("all_shops.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
