import pickle
import json
import pandas as pd
import numpy as np
import config


class SalesData():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type):

        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Item_Type = "Item_Type_" + Item_Type
        self.Outlet_Type = "Outlet_Type_" + Outlet_Type

    def load_file(self):
        
        with open(config.PICKLE_FILE_PATH,'rb') as f:
            self.sales_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_sale(self):

        self.load_file()    # calling method
        
        Item_Type_index = self.json_data['columns'].index(self.Item_Type)
        Outlet_Type_index = self.json_data['columns'].index(self.Outlet_Type)

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.Item_Weight
        array[1] = self.json_data['Item_Fat_Content'][self.Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.Item_MRP
        array[4] = self.json_data['Outlet_Establishment_Year'][self.Outlet_Establishment_Year]
        array[5] = self.json_data['Outlet_Size'][self.Outlet_Size]
        array[6] = self.json_data['Outlet_Location_Type'][self.Outlet_Location_Type]
        array[Item_Type_index] = 1 
        array[Outlet_Type_index] = 1


        print("Test array-->\n",array)
        predicted_sales = self.sales_model.predict([array])[0]
        return np.around(predicted_sales,2)



if __name__ == "__main__":
    
    Item_Weight = 10.25
    Item_Fat_Content = 'Low Fat'
    Item_Visibility = 0.03685
    Item_MRP = 315.25
    Outlet_Establishment_Year = '1999'
    Outlet_Size = 'Small'
    Outlet_Location_Type ='Tier 1'

    Item_Type = 'Health and Hygiene'
    Outlet_Type= 'Grocery Store'

    sal_out = SalesData(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)
    sales = sal_out.get_predicted_sale()

    print(f"Predicted Sales of Particular Outlet is {sales} only")