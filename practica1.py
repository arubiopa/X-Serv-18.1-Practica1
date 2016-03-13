#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content
 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""
#importamos de webapp
import webapp

#webapp.webApp = para que no haya colision de nombres modulo.clase
class contentApp (webapp.webApp):
    """Simple web application for managing content.
    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    url1 = {}
    url2 = {}
    def formulario(self):
        return ('<form method="POST" action="">formulario urls'
                + '<input type="text" name="nombre" value=""/>'
                + '<input type="submit" value="enviar"/>'
                + '</form>'

    def parse(self, request):
        """Return the resource name (including /)"""
        #tendremos que diferenciar entre put y get
        metodo = request.split(' ', 2)[0]
        recurso = request.split(' ', 2)[1]
        if metodo == 'POST':
            cuerpo = request.split('\r\n\r\n ')[1]
        elif metodo == 'GET':
            cuerpo = ""

        return metodo, recurso, cuerpo

    def process(self, peticion):

        metodo, recurso, cuerpo = peticion
        if metodo == "GET":
            if recurso == '/':
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.formulario()
                    + "url almacenadas: </br>" + str(self.urls1)
                    + "</body></html>"
                return (httpCode, htmlBody)
            else:
                try:
                    url = self.url2[int(peticion[1][1:])]
                    httpCode = "300 Redirect"
                    htmlBody = "<html><head><meta http-equiv='refresh' content='0;url="+ url + "'></head></html>"
                    return (httpCode, htmlBody)
                except KeyError:
                    httpCode = "404 Not Found"
                    htmlBody = "<html><body>" + self.formulario()
                        +'<p>Recurso no encontrado</p>'
                        +'</body></html>'
                    return (httpCode, htmlBody)
                except IndexError:
                    httpCode = "404 Not Found"
                    htmlBody = "<html><body>" + self.formulario()
                        +'<p>Recurso no encontrado</p>'
                        +'</body></html>'
                    return (httpCode, htmlBody)
        elif metodo == "POST":
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "Todo ha ido bien"
        else:
            httpCode = "404 Not Found"
            htmlBody = "<html><body>" + self.formulario()
                +'<p>Metodo desconocido</p>'
                +'</body></html>'
            return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1235)
