def sample(signal, kernel_size):
    """
    Toma una signal de hasta 3 dimensiones y con el kernel size, modifica la cantidad de mediciones
    por ejemplo sample(Signal(333,3,8000), 8) -> NuevaSignal(333,3,1000) con datos promedidas
    """
    # definimos la forma de como saldra la data, la cantidad de mediciones las modifica
    mediciones = signal.shape[2]//kernel_size
    sampled = np.zeros((signal.shape[0], signal.shape[1], mediciones))
    for i in range(mediciones): # ejemplo para kernel size 100
        intervalo_inferior = kernel_size * i  # 0, 100, 200, 300, ...
        intervalo_superior = min(kernel_size * (i + 1), signal.shape[2]) # tomamos 100, 200, 300, ... maxData
        # aqui es la parte importante, cortamos la data entre intervalo inferior-superior
        # especificamos que en ese intervalo y axis queremos promediar np.mean(.., axis=2)
        # de esa manera sampled[:,:,i] recibe ese intervalo
        sampled[:, :, i] = np.mean(signal[:, :, intervalo_inferior:intervalo_superior], axis=2) 
    return sampled