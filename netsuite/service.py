from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

ns_config = 'ns_config'

# cache WSDL and XSD for a year
cache = SqliteCache(timeout=60*60*24*365)
transport = Transport(cache=cache)
client = Client(ns_config.WSDL_URL, transport=transport)

model = client.get_type

Passport = model('ns0:Passport')
RecordRef = model('ns0:RecordRef')
ListOrRecordRef = model('ns0:ListOrRecordRef')
ApplicationInfo = model('ns4:ApplicationInfo')
CustomerSearchBasic = model('ns5:CustomerSearchBasic')
ItemSearchBasic = model('ns5:ItemSearchBasic')
SearchPreferences = model('ns4:SearchPreferences')
SearchBooleanField = model('ns0:SearchBooleanField')
SearchStringField = model('ns0:SearchStringField')
SearchStringFieldOperator = model('ns1:SearchStringFieldOperator')
SearchMultiSelectField = model('ns0:SearchMultiSelectField')
Customer = model('ns13:Customer')
Address = model('ns5:Address')
Country = model('ns6:Country')
Account = model('ns17:Account')
CustomerPayment = model('ns23:CustomerPayment')
customTransaction = model('ns32:CustomTransaction')
itemReceipt = model('ns21:ItemReceipt')
invoice = model('ns19:Invoice')

CashSale = model('ns19:CashSale')
CashSaleItem = model('ns19:CashSaleItem')
CashSaleItemList = model('ns19:CashSaleItemList')

SalesOrder = model('ns19:SalesOrder')
SalesOrderItem = model('ns19:SalesOrderItem')
SalesOrderItemList = model('ns19:SalesOrderItemList')
