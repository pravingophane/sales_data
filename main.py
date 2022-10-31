
from flask import Flask, jsonify, render_template, request
from Sales_data.utils import SalesData
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Sales data outlet")
    return render_template("index.html")

@app.route("/predict_sales", methods = ["POST","GET"])
def get_predicted_sales():

    if request.method == "GET":
        print("We are using GET method")

        data = request.form
        print("Data-->",data)

        # Item_Weight = eval(data['Item_Weight'])
        # Item_Fat_Content = data['Item_Fat_Content']
        # Item_Visibility = eval(data['Item_Visibility'])
        # Item_MRP = eval(data['Item_MRP'])
        # Outlet_Establishment_Year = data['Outlet_Establishment_Year']
        # Outlet_Size = data['Outlet_Size']
        # Outlet_Location_Type = data['Outlet_Location_Type']
        # Item_Type = data['Item_Type']
        # Outlet_Type = data['Outlet_Type']

        Item_Weight = float(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Establishment_Year = request.args.get("Outlet_Establishment_Year")
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Item_Type = request.args.get("Item_Type")
        Outlet_Type =request.args.get("Outlet_Type")

        print("Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type\n",Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)

        sal_out = SalesData(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)
        sales = sal_out.get_predicted_sale()
        return render_template("index.html", prediction = sales)

        # return jsonify({"Result":f"Predicted sales of particular outlet is {sales} only"})


    else:
        print("We are using POST Method")

        Item_Weight = float(request.form.get("Item_Weight"))
        Item_Fat_Content = request.form.get("Item_Fat_Content")
        Item_Visibility = float(request.form.get("Item_Visibility"))
        Item_MRP = float(request.form.get("Item_MRP"))
        Outlet_Establishment_Year = request.form.get("Outlet_Establishment_Year")
        Outlet_Size = request.form.get("Outlet_Size")
        Outlet_Location_Type = request.form.get("Outlet_Location_Type")
        Item_Type = request.form.get("Item_Type")
        Outlet_Type =request.form.get("Outlet_Type")

        print("Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type\n",Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)
        sal_out = SalesData(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)
        sales = sal_out.get_predicted_sale()
        return render_template("index.html", prediction = sales)

    # return jsonify({"Result":f"Predicted sales of particular outlet is {sales} only"})


if __name__ == "__main__":
    app.run(host ='0.0.0.0',port = config.PORT_NUMBER, debug = True)