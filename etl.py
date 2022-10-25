from calendar import month
from itertools import product
from xmlrpc.client import _HostType
import mysql.connector

dbNorthwind = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="northwind"
)
dbNorthwindDatawarehouse = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="northwind_datawarehouse"
)

kursorNorthwind = dbNorthwind.cursor()
kursorNorthwindDatawarehouse = dbNorthwindDatawarehouse.cursor()

#ekstrak product
sqlExtractProduct = """select distinct id, product_name
                        from product """
kursorNorthwind.execute(sqlExtractProduct)
extrackProduk = kursorNorthwind.fetchall()

#load product
for rowExtrackProduct in extrackProduk:
    product_id= rowExtrackProduct[0]
    product_name = rowExtrackProduct[1]
    sqlLoadProduct = """ insert into product (id_products,
    product_name) Values (%s, %s)"""
    valLoadProduct = (product_id, product_name)
    kursorNorthwindDatawarehouse.execute(sqlLoadProduct, valLoadProduct)
    
#extrack supliers
sqlExtractSupliers = """ select distinct id, company 
                        from suppliers """
kursorNorthwind.execute(sqlExtractSupliers)
ExtractSuplier = kursorNorthwind.fetchall()

for rowExtractSuplier in ExtractSuplier:
    suplier_id = rowExtractSuplier[0]
    company = rowExtractSuplier[1]
    sqlLoadSuplier = """ insert into supliers (id_supliers, company)
                        Values (%s,%s)"""
    valLoadSuplier = (suplier_id, company)
    kursorNorthwindDatawarehouse.execute(sqlExtractSupliers, valLoadSuplier)

#dimensi bulan
sqlMounth = "INSERT INTO months (id_months, purchase_month) VALUES (%s,%s)"
valMounth = {
                [1, 'January'],
                [2, 'February'],
                [3, 'Maret'],
                [4, 'April'],
                [5, 'Mei'],
                [6, 'Juni'],
                [7, 'Juli'],
                [8, 'Agustust'],
                [9, 'September'],
                [10, 'Oktober'],
                [11, 'November'],
                [12, 'Desember']
            }
kursorNorthwindDatawarehouse.execute(sqlMounth , valMounth)
extrackPurchase = kursorNorthwind.fetchall()

#extract facts
for rowExtractPurchase in extrackPurchase:
    suplier_id = rowExtractPurchase[0]
    month = rowExtractPurchase[1]
    product_id = rowExtractPurchase[2]
    quantity = rowExtractPurchase[3]
    list_price = rowExtractPurchase[4]
    sqlLoadFact = """insert into facts(id_product, id_supliers,
    id_mounths, quantity, list_price) Values (%s,%s,%s,%s)"""
    valLoadFact = (product_id, suplier_id, month, quantity, list_price)
    kursorNorthwindDatawarehouse.execute(sqlLoadFact, valLoadFact)

dbNorthwindDatawarehouse.commit()
