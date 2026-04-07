# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Xavier Fernández

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Xavier Fernández Rodriguez

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `algebra/vectores.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.
<img width="384" height="606" alt="image" src="https://github.com/user-attachments/assets/aa2b67c6-738d-4faa-a2b3-0de7d57a1f79" />


#### Código desarrollado

Inserte a continuación el código de los métodos desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).

```python
"""
Módulo de álgebra de vectores.

Alumno: Xavier Fernández Rodriguez

Este módulo define la clase Vector y las operaciones algebraicas básicas
entre vectores y escalares, implementadas sin el uso de bibliotecas externas.

Pruebas unitarias (doctest):

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])

# Multiplicación por un escalar
>>> v1 * 2
Vector([2, 4, 6])

# Producto de Hadamard (elemento a elemento)
>>> v1 * v2
Vector([4, 10, 18])

# Producto escalar (matricial)
>>> v1 @ v2
32

# Descomposición de un vector (componentes tangencial y normal)
>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])

# Componente paralela (tangencial)
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

# Componente perpendicular (normal)
>>> v3 % v4
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Representa un vector matemático n-dimensional.
    """

    def __init__(self, componentes):
        """
        Inicializa un vector a partir de una secuencia de componentes.

        Argumentos:
            componentes (iterable): Una lista, tupla u otro iterable numérico.
        """
        self.componentes = list(componentes)

    def __repr__(self):
        """
        Devuelve la representación oficial del vector en formato cadena.

        Salida:
            str: Representación del vector, e.g., Vector([1, 2, 3]).
        """
        return f"Vector({self.componentes})"

    def __add__(self, otro):
        """
        Suma dos vectores elemento a elemento.

        Argumentos:
            otro (Vector): El vector a sumar.

        Salida:
            Vector: Un nuevo vector resultante de la suma.
        """
        if not isinstance(otro, Vector):
            return NotImplemented
        return Vector([a + b for a, b in zip(self.componentes, otro.componentes)])

    def __sub__(self, otro):
        """
        Resta dos vectores elemento a elemento.

        Argumentos:
            otro (Vector): El vector a restar.

        Salida:
            Vector: Un nuevo vector resultante de la resta.
        """
        if not isinstance(otro, Vector):
            return NotImplemented
        return Vector([a - b for a, b in zip(self.componentes, otro.componentes)])

    def __mul__(self, otro):
        """
        Implementa el producto de Hadamard o la multiplicación por un escalar.

        Argumentos:
            otro (Vector, int, float): El vector o escalar a multiplicar.

        Salida:
            Vector: Un nuevo vector con el resultado de la multiplicación.
        """
        if isinstance(otro, Vector):
            # Producto de Hadamard (elemento a elemento)
            return Vector([a * b for a, b in zip(self.componentes, otro.componentes)])
        elif isinstance(otro, (int, float)):
            # Multiplicación por escalar
            return Vector([a * otro for a in self.componentes])
        return NotImplemented

    def __rmul__(self, otro):
        """
        Implementa la multiplicación por la izquierda (escalar * Vector).
        """
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """
        Implementa el producto escalar de dos vectores.

        Argumentos:
            otro (Vector): El segundo vector.

        Salida:
            int/float: El resultado del producto escalar.
        """
        if not isinstance(otro, Vector):
            return NotImplemented
        return sum(a * b for a, b in zip(self.componentes, otro.componentes))

    def __rmatmul__(self, otro):
        """
        Implementa el producto escalar por la izquierda.
        """
        return self.__matmul__(otro)

    def __floordiv__(self, otro):
        """
        Calcula la componente paralela (tangencial) de este vector respecto a otro.

        Se calcula mediante la fórmula: v1_paralela = ((v1 @ v2) / (v2 @ v2)) * v2

        Argumentos:
            otro (Vector): El vector sobre el cual proyectar.

        Salida:
            Vector: La componente paralela.
        """
        if not isinstance(otro, Vector):
            return NotImplemented
        
        producto_escalar = self @ otro
        magnitud_otro_cuadrado = otro @ otro
        
        if magnitud_otro_cuadrado == 0:
            raise ValueError("No se puede proyectar sobre un vector nulo.")
            
        escalar_proyeccion = producto_escalar / magnitud_otro_cuadrado
        return otro * escalar_proyeccion

    def __rfloordiv__(self, otro):
        return NotImplemented

    def __mod__(self, otro):
        """
        Calcula la componente perpendicular (normal) de este vector respecto a otro.

        Se calcula como la diferencia entre el vector original y su componente paralela:
        v1_perpendicular = v1 - (v1 // v2)

        Argumentos:
            otro (Vector): El vector que define la dirección normal.

        Salida:
            Vector: La componente perpendicular.
        """
        if not isinstance(otro, Vector):
            return NotImplemented
        
        componente_paralela = self // otro
        return self - componente_paralela

    def __rmod__(self, otro):
        return NotImplemented


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```
#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
