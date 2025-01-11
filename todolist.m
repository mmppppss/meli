\theme "gruvbox"
\name "App Lista De Tareas"

title("App Lista De Tareas")
title3("Agrege aqui sus Tareas")

box(
	box(
		list(
			"tarea1",
			"tarea2",
			"tarea3"
		)
	),

	row(
		input("text", "Agregar nueva:"),
		button("Agregar", "alert('agregada')")
	)

)
text("frontend")

