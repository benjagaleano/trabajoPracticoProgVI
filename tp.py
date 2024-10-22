import flet as ft
class Task(ft.Row):
    def __init__(self, text, on_delete):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.icons.SAVE, on_click=self.save
        )
        self.delete_button = ft.IconButton(
            icon=ft.icons.DELETE, on_click=lambda e: on_delete(self)
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(page):
    # Definir ancho y alto de la ventana
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista de Compras"

    tasks = []

    def add_clicked(e):
        if new_task.value.strip():  # No agregar tareas vacías
            task = Task(new_task.value, on_delete=delete_task)
            tasks.append(task)
            task_list.controls.append(task)
            task_list.update()
            new_task.value = ""
            new_task.focus()

    def delete_task(task):
        tasks.remove(task)
        task_list.controls.remove(task)
        task_list.update()

    # Cabecera con logo
    logo = ft.Image(src="./logo.png", width=150, height=150)
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)

    # Organizar cabecera en una columna
    header = ft.Column([logo, header_text], alignment="center")

    # Entrada de nueva tarea
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    # Lista de tareas
    task_list = ft.Column()

    # Añadir elementos a la aplicación
    page.add(
        header,
        ft.Divider(height=20),
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)]),
        task_list  # Mostrar la lista de tareas
    )

ft.app(main, assets_dir="logo")
