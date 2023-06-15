# financewebservice

<h3 align="left"> Integrantes :</h3>    

- Caicedo Martinez Sebastian - 1841245  :imp:  
[sebastian.caicedo.martinez@correounivalle.edu.co](sebastian.caicedo.martinez@correounivalle.edu.co)
- Moyano Gonzalez Laura - 2023906   :penguin:  
[laura.moyano@correounivalle.edu.co ](laura.moyano@correounivalle.edu.co)  

 **Taller 01**   
Un web service que tiene las siguientes características:  
- Accesible por el método 'POST'
- El web service recibirá un tipo de dato JSON que permitirá conocer la acción por el cual se consulta, la fecha inicial y la fecha final desde la cual se consultará por el valor de la acción.
- El web service devolverá la respuesta al usuario en formato JSON 

 **Este repositorio contiene:**
 - Código fuente del web service

# ```Instrucciones de uso```
- Clonar el repositorio desde github
```
git clone https://github.com/rwxp/financewebservice.git
```
- Ejecutar el contenedor desde la imagen en el Dockerhub

```
docker container run --rm --name stock-market -p 5000:5000 sdrivert/stock-market:2.0
```


# ```Instrucciones para acceder al web service desde la línea de comandos usando el aplicativo 'curl'```

Una vez la aplicación se encuentra corriendo en su equipo ejecutando el siguiente comando puede acceder al web service: 

```
curl -X POST -H "Content-Type: application/json" -d '{"accion":"AAPL","fecha_inicial":"2023-01-01","fecha_final":"2023-06-01"}' http://localhost:5000/
```  
# ```Instrucciones para acceder al web service desde  Python```   

Una vez la aplicación se encuentra corriendo en su equipo ejecutando el siguiente comando puede acceder al web service desde python: 

```
python3 request.py
``` 
