from nicegui import ui

with ui.row().classes('mx-auto'):
    with ui.card():
        ui.label('hello world').classes('text-xl')
        input_field = ui.input(on_change=lambda e: result.set_text(e.value.lower()çç))
        result = ui.label()
    with ui.card():
        ui.label('merely doubled over')



ui.run()
