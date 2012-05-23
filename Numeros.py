#####################################################################
#   
#   Conversion de numero romanos
#   
#    Romano   Decimal
#    I        1 
#    V        5 
#    X        10 
#    L        50 
#    C        100 
#    D        500 
#    M        1.000 
#  
#####################################################################



#####################################################################
#  
#  Defino Variables
texto_plano = ''
posicion = ''
_valores = [ (1000,"M"),
            (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), 
            (90,"XC"),  (50,"L"),  (40,"XL"),  (10,"X"), 
            (9,"IX"),   (5, "V"),  (4,"IV"),   (1,"I")  ]

#####################################################################
texto_plano = '2391' #input('Valor: ')

def Calcula_valor(valor_a_buscar):
    #############################################################
    #
    # Calcula el valor de la letra
    #
    #############################################################
    _resultado = ''
    
    while valor_a_buscar > 0:
        _bandera = True #lo uso para que no entre mas de una vez
        
        for decimal, romano in _valores:
            if (decimal <= valor_a_buscar) & _bandera:
                valor_a_buscar = valor_a_buscar - decimal
                _resultado = _resultado + romano
                _bandera = False
                
        print(valor_a_buscar,_resultado) # solo para ver como esta procesando
    return _resultado 

def DecimalARomano (texto):
    #############################################################
    #
    #   Convierte de numeros decimales a romanos
    #
    #############################################################
    _procesado = ''
    longitud = len(texto)-1 #determino el largo de la cadena
    
    print(longitud,texto)
    
    for posicion  in texto:
        _procesado = _procesado + Calcula_valor(int(posicion)*10**longitud) # envio el valor segun su posicion decimal
        longitud = longitud - 1

    return _procesado


#############################################################
#
#   Ejecucion
#
#############################################################
print("Resultado ->",DecimalARomano(texto_plano))

