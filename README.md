# 🧮 Calculadora Lógica en Python

> Mi primer programa en Python luego de terminar un curso de verano. Es una calculadora capaz de analizar ecuaciones en texto y respetar el orden de las operaciones.

## 📖 Sobre el proyecto
A diferencia de las calculadoras básicas que piden número por número, este programa permite al usuario escribir una ecuación fluida (ej. `2+2*5`) y utiliza un algoritmo propio para descomponer la cadena y calcular el resultado correcto.

## ⚙️ Características técnicas
- **Parsing manual:** Analiza la cadena de texto carácter por carácter.
- **Jerarquía de operaciones:** Detecta y ejecuta multiplicaciones/divisiones antes que sumas/restas.
- **Validación:** Verifica que no se introduzcan letras o caracteres inválidos.
- **Cero dependencias:** Lógica construida 100% con Python puro (sin librerías externas ni `eval()`).

## 🚀 Cómo usar
1. Ejecuta el archivo `CAL_21.py`.
2. Ingresa la operación completa cuando se te pida.
3. Finaliza la ecuación con un signo `=`.

Ejemplo:
```text
> Ingrese la operacion y finalize con "=": 10+5*2=
> El resultado es: 20
