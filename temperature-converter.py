from nicegui import ui

ui.colors(
      primary='#a30000',
      secondary='#ff9999',
      accent='#66b3ff',
      positive='#005c00',
      negative='#5c0000',
      info='#7b00f5',
      warning='#ffff33'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-xl font-semibold text-positive mt-4 mx-auto")
        # text-positive: sets text to positive color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-xl font-semibold text-negative mt-4 mx-auto")
        # text-negative: sets text to negative color

def convert_knob():
    try: 
        temp = float(knob.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-xl font-semibold text-positive mt-4 mx-auto")
        # text-positive: sets text to positive color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-xl font-semibold text-negative mt-4 mx-auto")
        # text-negative: sets text to negative color

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-secondary"):
        # w-100: Set element width to be fixed at 100
        # p-6: padding of value 6 on all sides of element
        # shadow-xl: adds extra large shadow emanating from element
        # mx-auto: centers content
        # mt-10: margin on top of element of 10
        # rounded-xl: extra large border radius
        ui.label("Temperature Converter").classes("text-2xl font-bold text-primary mb-4")
        # text-2xl: 2XL size text
        # font-bold: bolds the font
        # text-accent: sets the text to accent color
        # mb-4: sets bottom margin to 4
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: sets width to full extent of display
        # border: 1px border width
        # rounded: border radius of 1
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("font-semibold mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto")
        # text-white: sets text to white color
        # py-2: vertical padding of 2
        # px-4: horizontal padding of 4
        result_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-secondary"):
        ui.label("Temperature Converter").classes("text-2xl font-bold text-primary mb-4")
        knob = ui.knob(value=40, min=-300, max=300, step=1, show_value=True).classes('mx-auto')

        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("font-semibold mb-4") 
        convert_button = ui.button("Convert", on_click=convert_knob).classes("text-white font-bold py-2 px-4 rounded mx-auto")
        # text-white: sets text to white color
        # py-2: vertical padding of 2
        # px-4: horizontal padding of 4
        result_label = ui.label("").classes("text-lg mt-4")

ui.run()
