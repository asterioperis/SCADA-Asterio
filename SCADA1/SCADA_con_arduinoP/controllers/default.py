# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import time
import math
import datetime
import sys
path = "C:\Users\Aster\Desktop\web2py\site-packages"
if path not in sys.path:
    sys.path.append(path)
import serial
PuertoSerie= serial.Serial('COM5', 9600)
PuertoSerie.close()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Bienvenido al SCADA de Asterio")
    return dict(message=T('Hello World'))

def recibe_datos():
    operando1=(request.vars.estado1)
    try:
        PuertoSerie.open()
        PuertoSerie.write(operando1)
        if operando1=="H": 
            resultado={'estado1': "L"}
        if operando1=="L":
            resultado={'estado1': "H"}
        PuertoSerie.close()
        return resultado
    except:
        resultado={'estado1': operando1}
        return resultado
        pass

def recibe_datos2():    
    operando2=(request.vars.estado2)
    try:
        PuertoSerie.open()  
        PuertoSerie.write(operando2)
        if operando2=="A":
            resultado2={'estado2':"B"}
        if operando2=="B":
            resultado2={'estado2':"A"}
        PuertoSerie.close()
        return resultado2
    except:
        resultado2={'estado2': operando2}
        return resultado2
        pass
    
def recibe_datos3():    
    try:
        PuertoSerie.open()
        PuertoSerie.write("N")
        a=PuertoSerie.readline()
        b=a.split()
        c=b[0]
        PuertoSerie.close()
        return c
    except:
        c=[0,0,0]
        return c
        pass
    
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
