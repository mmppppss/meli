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

- Header (h1, h2, ..., hn)
    title("content")
    title2("header 2")
    title3("header 3")
    ...
    genera:
        <h1>content</h1>
        <h2>header 2</h2>
        <h3>header 3</h3>

- Link enlaces rutas
    link("nombre", "/ruta")
    link("google", "https://google.com")
    genera:
        <a href="/ruta">nombre</a>
        <a href="https://google.com">google</a>

- Imagen
    image("ruta/a/la/imagen", "css")
    genera:
        <img src="ruta/a/la/imagen" style="css">

- Botones:
    button("nombre", "accion")
    genera:
        <button onclick="accion">nombre</button>

- Inputs
    input("tipo", "placeholder")
    placeholder es opcional
    genera
        <input type="tipo" placeholder="placeholder">

- Listas
    list("elem1", "elem2", ..., elemN)

- Tablas:
    table(
        row("cadena", "Texto"),
        row("cadena", "Texto")
    )

## temas disponibles:
    normal
    cupertino
    gruvbox


## elementos
text("HOLA")
<span>HOLA</span>
 button("NOMBRE", accion)
 <button onclick="accion">NOMBRE</button>
