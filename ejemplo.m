\name "test"
\theme "gruvbox"
title("titulo")
title3("titulo3")
text("hola mundo")
\n
link("google","https://google.com")
box(
	text("hola meli"),
	text("hola mundo"),
	row(text("text"), text("in row"))
)
\n
\n
row(
	box(
		text("hola"),
		text("mundo")
	),
	box(
		text("que"),
		text("tal")
	)
)
button("Boton", "alert(\"boton clickado\")")
image("./bitmap.png", "width: 100px")
