# Propagacion de Errores
la Propagacion de errores es un tema que viene de tomar los errores sistematicos de los instrumentos y aplicar formulas de calculo multivariable; este es un repositorio pensado para hacer de shortcut a mucho del trabajo relacionado a laboratorios. Debe de notarse que distintos Laboratorios usan distintas convenciones para la propagacion de errores, por tanto consulta con tu instructor y el Readme de este proyecto para comparar.

### Error_Lab.nb
Es un Notebook de Mathematicas que usa arreglos que contienen los errores sistematicos y luego utiliza Calculo Multivariable para obtener el error sistematico final de la cantidad a medir. Se trata de Propagacion de errores.

### Build1.ipynb
Es la conversion de Mathematica a Python, se trata de un entorno de pruebas, la idea es finalmente crear una `main.py` con interfaz grafica, el cual deje en claro visualmente y sin explicacion el como utilizar el programa.

# Instalacion
requiere una version de sympy antigua, ya que la actual posee problemas con la diferenciacion simbolica que se incluye en este codigo
```
pip install sympy==1.5.1
```
