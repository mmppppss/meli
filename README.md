MELI: Modern Easy Lean Interfaces

Programa para hacer intefaces modernas

## Documentacion
- EJECUCION:
    `python main.py -i *codigoFuente* -o "archivoSalida"`

- Poner Texto:
    `text("contenido")`
    genera:
        <span>contenido</span>

- Salto de linea
    `\n`
    genera:
        <br>

- Poner titulo a la pagina:
    `\name "Titulo"`
    Estable title :
        <title>Titulo</title>

- Establecer tema:
    `\theme "tema"`
    Estable el tema:
        <link rel="stylesheet" href="tema.css">

- Contenedor vertical
    `box( elem1, elem2, ..., elemN)`
    admite cualquier elemento dentro de si

- Contenedor horizontal
    `row(elem1, elem2, ..., elemN)`
    admite cualquier elemento dentro de si










## elementos
text("HOLA")
<span>HOLA</span>
 button("NOMBRE", accion)
 <button onclick="accion">NOMBRE</button>
