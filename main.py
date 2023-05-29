# Simple ecomerce API using Flask:

# This app lets You Manage & Scale Your Business; it allows managers to browse and calculate store's gross sales and search items from an online store

# DB: "Sales - Dez.xlsx" [ Directory - main root ]

# End Points (JSON):
# 1 -  Return cia's GROSS SALES:
# https://flaskapiecomerce.jaythree.repl.co  

# 2-  Return total for each products 
# https://flaskapiecomerce.jaythree.repl.co/sales/products

# 3 - Return the total of sale  per item 
# https://flaskapiecomerce.jaythree.repl.co/sales/products/Jeans Jackets
# answer ={ "total of sales" : 21432 }

# https://flaskapiecomerce.jaythree.repl.co/sales/products/V-Neck
# answer = { "total of sales" : 13910 }

# https://flaskapiecomerce.jaythree.repl.co/sales/products/Peter Pan Collar/
# answer = { "total of sales" : 268020  }

# Based on: hashtag treinamentos - Lira
# Editor: j3
# date : march 2023

from flask import Flask
import pandas as pd

app = Flask(__name__)
table = pd.read_excel("Sales - Dez.xlsx")


@app.route("/")
def gross_sales():
  gross_sales = float(table["total of sales"].sum())
  return {"gross_sales": gross_sales}


@app.route("/sales/products")
def sales_products():
  table_prod_sales = table[["products",
                            "total of sales"]].groupby("products").sum()
  sales_products_json = table_prod_sales.to_dict()
  return sales_products_json


@app.route("/sales/products/<item>")
def sales_per_item(item):
  table_prod_sales = table[["products", "total of sales"]].groupby("products").sum()
  if item in table_prod_sales.index:
    item_sales = table_prod_sales.loc[item]  
    sales_item_json = item_sales.to_dict()
    return sales_item_json
  else:
    return {item: "Not Found in this database"}
    

app.run(host="0.0.0.0")

# INVOICE:
# An invoice is an itemized list that records the products or services you provided to your customers, the total amount due, and a method for them to pay you for those items or services.

# GROSS SALES:
# Gross sales is a metric for the total sales of a company, unadjusted for the costs related to generating those sales. The gross sales formula is calculated by totaling all sale invoices or related revenue transactions.
