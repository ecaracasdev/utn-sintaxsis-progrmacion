def crearMed():
    medicamento = ["","","",0]
    return medicamento


#asigna nombre genérico, nombre comercial, laboratorio y precio al remedio r - 
def cargarMed(r,nomg,nomcom,lab,prec):
    r[0] = nomg
    r[1] = nomcom
    r[2] = lab
    r[3] = prec


#retorna el nombre genérico del remedio r - 
def verNomGen(r):
    return r[0]


#retorna el nombre comercial de r -    
def verNomCom(r):
    return r[1]


#retorna el laboratorio de r - 
def verLab(r):
    return r

# #retorna el precio de r - 
def verPrecio(r):
    return r[3]

#modifica el nombre genérico de r  - 
def modNomGen(r, otroNG):
    r[0] = otroNG

#modifica el nombre comercial de r - 
def modNomCom(r, otroNC):
    r[1] = otroNC
    
#modifica el laboratorio de r - 
def modLab(r, otroL):
    r[2] = otroL

# #modifica el precio de r - 
def modPrecio(r,otroP):
    r[3] = otroP 

def copiar(r1,r2):
    r2 = r1.copy()
    return r2 