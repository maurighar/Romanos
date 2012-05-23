#####################################################################
#   
#   Conversion de numero romanos
#   
#   Romano   Decimal
#   I        1 
#   V        5 
#   X        10 
#   L        50 
#   C        100 
#   D        500 
#   M        1.000 
#####################################################################


#####################################################################
#  
#  Defino Variables
texto_plano = ''
_Equivaliencias = [
    ('M',1000),
    ('D',500),
    ('C',100),
    ('L',50),
    ('X',10),
    ('V',5),
    ('I',1),
    ('', 0)]
#####################################################################

#texto_plano = input('Valor: ')
texto_plano = 'CXCIX'

def Calcula_valor(texto_a_buscar):
    #############################################################
    #
    # Calcula el valor de la letra
    #
    #############################################################
    for romano,decimal in _Equivaliencias:
        if romano == texto_a_buscar:
            break
        
    return decimal

def RomanoADecimal (texto):
    #############################################################
    #
    #   Convierte de numeros romanos a decimales
    #
    #############################################################
    _procesado = 0
    valor_anterior = 0
    
    for caracter in texto:
        valor = Calcula_valor(caracter)
        if valor > valor_anterior:
            _procesado = _procesado + valor - (valor_anterior * 2)
        else:
            _procesado = _procesado + valor
        
        print(valor,valor_anterior,_procesado)
        valor_anterior = valor
    return _procesado


#############################################################
#
# Ejecucion
#
#############################################################
print("Resultado ->",RomanoADecimal(texto_plano))
