def registar_habitos ():
    '''
    registrar_habitos
    registra cuales actividades hace el usuario

    Returns
    -------
    lista_act : list
        listra de actividades.

    '''
    opcion = "s"
    lista_act = []
    while opcion == "s":
        act = input("actividades: ")
        lista_act.append(act)
        opcion = input("desa seguir ingresadno actividades? (s/n): ")
    return lista_act

def analizar_habitos (lista):
    '''
    analizar habitos
    analiza los habitos del usuario desde una lista con sus habitos y devuelve un diccionario

    Parameters
    ----------
    lista : list
        lista con los habitos del usuario.

    Returns
    -------
    diccio_actividades : diccionario
        diccionarion cuyas claves son las distintas activisades y sus valores son cuantas veces aparecieron en la lista dada.

    '''
    diccio_actividades = {}
    for actividad in lista:
        if actividad not in diccio_actividades:
            diccio_actividades[actividad] = 1
        else:
<<<<<<< HEAD
            diccio_actividades[actividad] = +1 
=======
>>>>>>> 00d056940f6f0fe3512745693b480e518933a8c0
            diccio_actividades[actividad] += 1 
    return diccio_actividades


        
