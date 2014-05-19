

#def user(): return dict(form=auth())

#Function to create vendor record
def VENDOR():
    form = SQLFORM(db.VENDOR,).process()
    session.flash = "Form Accepted !"
    if form.accepted :redirect(URL('index'))
    return locals()

#Function to create product record
def PRODUCT():
    form = SQLFORM(db.PRODUCT,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create customer record
def CUSTOMER():
    form = SQLFORM(db.CUSTOMER,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create customer_2 record
def CUSTOMER_2():
    form = SQLFORM(db.CUSTOMER_2,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create invoice record
def INVOICE():
    form = SQLFORM(db.INVOICE,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()
    
#Function to  create invoice record
def LINE():
    form = SQLFORM(db.LINE,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to prodmaster record
def PRODMASTER():
    form = SQLFORM(db.PRODMASTER,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#function to create prodsale record
def PRODSALES():
    form = SQLFORM(db.PRODSALES,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#function to create job record
def JOB():
    form = SQLFORM(db.JOB,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create employee record
def EMPLOYEE():
    form = SQLFORM(db.EMPLOYEE,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create Project record
def PROJECT():
    form = SQLFORM(db.PROJECT,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()

#Function to create allocation record
def ALLOCATION():
    form = SQLFORM(db.ALLOCATION,).process()
    session.flash = "Form Accepted !"
    if form.accepted: redirect(URL('index'))
    return locals()



def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome To Sale Co!")
    return dict(message=T('Welcome To Sale Co!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
    
# SQL smartgrid function for managing the various tables in the database 


def manage_vendortransactions():
    grid = SQLFORM.smartgrid(db.VENDOR,linked_tables=['PRODUCT'],
  user_signature=False)
    return dict (grid=grid)

def manage_producttransactions():
    grid=SQLFORM.smartgrid(db.PRODUCT,linked_tables=['VENDOR'],
 user_signature=False)
    return dict(grid=grid)

def manage_customertransactions():
    grid=SQLFORM.smartgrid(db.CUSTOMER, user_signature=False)
    return dict(grid=grid)

def manage_customer_2transactions():
    grid=SQLFORM.smartgrid(db.CUSTOMER_2,user_signature=False)
    return dict(grid=grid)

def manage_invoicetransactions():
    grid=SQLFORM.smartgrid(db.INVOICE,linked_tables=['CUSTOMER'],
    user_signature=False)
    return dict(grid=grid)

def manage_linetransactions():
    grid=SQLFORM.smartgrid(db.LINE,linked_tables=['INVOICE'],
    user_signature=False)
    return dict(grid=grid)

def manage_prodmastertransactions():
    grid=SQLFORM.smartgrid(db.PRODMASTER,user_signature=False)
    return dict(grid=grid)

def manage_prodsalestransactions():
    grid=SQLFORM.smartgrid(db.PRODSALES,user_signature=False)
    return dict(grid=grid)

def manage_jobtransactions():
    grid=SQLFORM.smartgrid(db.JOB,user_signature=False)
    return dict(grid=grid)

def manage_employeetransactions():
    grid = SQLFORM.smartgrid(db.EMPLOYEE,linked_tables=['JOB'],
  user_signature=False)
    return dict (grid=grid)

def manage_projecttransactions():
    grid = SQLFORM.smartgrid(db.PROJECT,linked_tables=['EMPLOYEE'],
  user_signature=False)
    return dict (grid=grid)

def manage_allocationtransactions():
    grid = SQLFORM.smartgrid(db.ALLOCATION,linked_tables=['EMPLOYEE','PROJECT'],
  user_signature=False)
    return dict (grid=grid)

#Selects all tables in the database using JQUERY
def form():
    if request.args(0) in db.tables:
       response.generic_patterns = ['load']
       return dict(form=SQLFORM(db[request.args(0)]).process())
    else:
       raise HTTP(404)
        
#List All tables & Records in the Database
def grid():
       response.generic_patterns = ['show']
       return dict(grid=SQLFORM.grid(db.VENDOR,db.PRODUCT,db.CUSTOMER,db.CUSTOMER_2,db.INVOICE,db.LINE,db.PRODMASTER,db.PRODSALES,db.JOB,db.EMPLOYEE,db.ALLOCATION))
