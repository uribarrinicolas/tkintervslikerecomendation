from tkinter import *

_defaultConfig = {'height': 600, 'width': 800, 'title': "Application"}


class Application:
    def __init__(self, **config):
        self.root = Tk()
        oldschoolconfig = self._applynonnativeconfig(**_defaultConfig)
        self.root.configure(oldschoolconfig)
        # override default configuration
        oldschoolconfig = self._applynonnativeconfig(**config)
        self.root.configure(**oldschoolconfig)
        self._initializecomponents()

    def run(self):
        self.root.mainloop()
        return 0

    # Aca se definen los componentes, sus estilos y su comportamiento
    # Esta funcion deberia ser la unica que importa en el diseño y deberia crecer
    #   de forma procedural
    # De ser posible deberia separarse en grupos por funcionalidad:
    # - Definicion de controladores
    # - Configuracion de estilos de controladores
    # - Configuracion de comportamiento de controladores
    # - Renderizado de controladores
    # Es complicado porque el renderizado esta mezclado con la configuracion de estilos
    #   en muchos casos. Es solo una recomendacion.
    def _initializecomponents(self):

        self.boton1 = Button(self.root)
        self.boton1.config(command=funcionejemplo)

    # Hasta aca la zona editable de la clase

    # A partir de aca se agregan las configuraciones adicionales
    # Por cada key agregada hay que agregar a la lista _addedkeys ademas del comportamiento
    #   en _applynonnativeconfig
    _addedkeys = ["title", "maxheight", "maxwidth", "minheight", "minwidth"]

    def _applynonnativeconfig(self, **config):
        result = config.copy()

        s = "title"
        if s in result:
            self.root.title(result[s])
            result.pop(s)

        s = "maxheight"
        p = "maxwidth"
        if s and p in result:
            self.root.maxsize(height=result[s], width=result[p])
        if s in result:
            result.pop(s)
        if p in result:
            result.pop(p)

        s = "minheight"
        p = "minwidth"
        if s and p in result:
            self.root.minsize(height=result[s], width=result[p])
        if s in result:
            result.pop(s)
        if p in result:
            result.pop(p)

        return result

    def keys(self):
        result = self._addedkeys
        result += self.root.keys()
        return result
    # Hasta aca las configuraciones adicionales


# Funcion ejemplo relacionada con el ejemplo inicial de _initializecomponents.
# De no usarse puede borrarse.
def funcionejemplo():
    pass