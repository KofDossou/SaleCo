#Tables that make up the SaleCo. Database System

#Vendor Table
db.define_table('VENDOR',
    Field("V_CODE",'integer'),
    Field('V_NAME','string'),
    Field('V_CONTACT','string'),
    Field('V_AREACODE','integer'),
    Field('V_PHONE','string'),
    Field('V_STATE','string'),
    Field('V_ORDER','string')
    )
#Product Table
db.define_table('PRODUCT',
    Field("P_CODE",'string'),
    Field('P_DESCRIPTION','string'),
    Field('P_INDATE','date'),
    Field('P_QOH','integer'),
    Field('P_MIN','integer'),
    Field('P_PRICE','double'),
    Field('P_DISCOUNT','double'),
    Field('V_CODE','integer','reference VENDOR')
   )

#Customer Table
db.define_table('CUSTOMER',
    Field("CUS_CODE"),
    Field('CUS_LNAME','string'),
    Field('CUS_FNAME','string'),
    Field('CUS_INITIAL','string'),
    Field('CUS_AREACODE','integer'),
    Field('CUS_PHONE','string'),
    Field('CUS_BALANCE','double')
  )
#Customer_2 table
db.define_table('CUSTOMER_2',
    Field("CUS_CODE",'integer'),
    Field('CUS_LNAME','string'),
    Field('CUS_FNAME','string'),
    Field('CUS_INITIAL','string'),
    Field('CUS_AREACODE','integer'),
    Field('CUS_PHONE','string'),
    Field('CUS_BALANCE','integer')
  )
#Invoice Table
db.define_table('INVOICE',
    Field("INV_NUMBER",'integer'),
    Field('CUS_CODE','integer','reference CUSTOMER (CUS_CODE)'),
    Field('INV_DATE','date'),
 )
#Line Table
db.define_table('LINE',
    Field("INV_NUMBER",'integer','reference INVOICE (INV_NUMBER)'),
    Field('LINE_NUMBER','integer'),
    Field('P_CODE','string'),
    Field('LINE_UNIT','integer'),
    Field('LINE_PRICE','string'),
 )
#Prodmaster Table
db.define_table('PRODMASTER',
    Field("PROD_ID",'string'),
    Field('P_DESC','string'),
    Field('P_QOH','integer'),
 )
#Prodsales Table
db.define_table('PRODSALES',
    Field("PROD_ID",'string'),
    Field('PS_QTY','integer'),
 )

#Job Table
db.define_table('JOB',
    Field("JOB_CODE",'integer','reference VENDOR'),
    Field('JOB_DESCRIPTION','integer'),
    Field("JOB_CHG_HOUR",'double'),
    Field('JOB_LAST_UPDATE','date'),
)

#Employee Table
db.define_table('EMPLOYEE',
    Field("EMP_NUM",'string'),
    Field('EMP_LNAME','string'),
    Field("EMP_FNAME",'string'),
    Field('EMP_HIREDATE','date'),
    Field('JOB_CODE','integer','reference JOB (JOB_CODE)'),
 )

#Project Table
db.define_table('PROJECT',
    Field("PROJ_NUM",'string'),
    Field('PROJ_NAME','string'),
    Field("PROJ_VALUE",'double'),
    Field('PROJ_BALANCE','double'),
    Field('EMP_NUM','integer','reference EMPLOYEE (EMP_NUM)'),
 )

#Allocation Table
db.define_table('ALLOCATION',
    Field("ALLOCATN_NUM",'integer'),
    Field('ALLOCATN_DATE','date'),
    Field('PROJ_NUM','integer','reference PROJECT (PROJ_NUM)'),
    Field("ALLOCATN_JOB",'string'),
    Field('ALLOCATN_CHG_HR','double'),
    Field("ALLOCATN_HOURS",'integer'),
    Field('ALLOCATN_CHARGES','double'),    
    Field('EMP_NUM','integer','reference EMPLOYEE (EMP_NUM)'),
 )

db.VENDOR.V_CODE.requires = IS_NOT_EMPTY()
db.VENDOR.V_NAME.requires = IS_NOT_EMPTY()
db.VENDOR.V_CONTACT.requires = IS_NOT_EMPTY()
db.VENDOR.V_AREACODE.requires = IS_NOT_EMPTY()
db.VENDOR.V_PHONE.requires = IS_NOT_EMPTY()
db.VENDOR.V_STATE.requires = IS_NOT_EMPTY()
db.VENDOR.V_ORDER.requires = IS_NOT_EMPTY()

db.PRODUCT.P_CODE.requires = IS_NOT_EMPTY()
db.PRODUCT.P_DESCRIPTION.requires = IS_NOT_EMPTY()
db.PRODUCT.P_INDATE.requires = IS_NOT_EMPTY()
db.PRODUCT.P_QOH.requires = IS_NOT_EMPTY()
db.PRODUCT.P_MIN.requires = IS_NOT_EMPTY()
db.PRODUCT.P_PRICE.requires = IS_NOT_EMPTY()
db.PRODUCT.P_DISCOUNT.requires = IS_NOT_EMPTY()
db.PRODUCT.V_CODE.requires = IS_NOT_EMPTY()
