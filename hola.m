\theme "cupertino"
\name "Holaaa"

box(
	row(
		text("hola"),
		text("mundo")
	),
	button("Botoncito", "alert('hola')"),
	box(
		row(
			text("Otro"),
			image("./bitmap.png", "width: 100px"),
			link("Google", "https://google.com")
		)
	)
)

