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