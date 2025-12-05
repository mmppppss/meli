\name "test"
\theme "gruvbox"
row(
	box#test(
		text("test1"),
		button("test1", "alert('test1 completo')")
	),
	box.test(
		text("test2"),
		input("password", "Contraseña")
	)
)
box(
	table(
		row#lineaUno.lin("hola", "mundo"),
		row#lineaDos("que", "tal"),
		row#lineaTre.lin("este", "es"),
		row#lineaCua("un", "test")
	),
	row.rowInBox(
		list("test", "de", "lista"),
			image#img("./bitmap.png", "width : 50%")
	)
)
link#link("ir a google","https://google.com")
text("hola")
box(
	text("hola")
)
