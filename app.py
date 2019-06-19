from Application import Application

# config = {'height': 300, 'width': 300, 'title': "Ejemplo", 'maxheight': 800, 'maxwidth': 600}
config = {}

app = Application(**config)
# Muestra las posibles claves para configurar la aplicacion, por lo general el form principal.
# print(app.keys())
app.run()
