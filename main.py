# ================================================================
# 1️⃣ IMPORTACIONES
# ================================================================
# asyncio permite manejar tiempos de espera sin congelar la app
import asyncio

# Importamos Flet
import flet as ft


# ================================================================
# 2️⃣ FUNCIÓN PRINCIPAL
# ================================================================
# Esta función recibe la página como parámetro.
# Todo lo que construimos visualmente ocurre dentro de main().
def main(page: ft.Page):

    # ================================================================
    # 3️⃣ CONFIGURACIÓN GENERAL DE LA PÁGINA
    # ================================================================
    page.title = "¿Me perdonas? ❤️"
    page.bgcolor = ft.Colors.RED_ACCENT_100  # Color de fondo

    # Centramos contenido horizontal y verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # ================================================================
    # 4️⃣ COMPONENTES VISUALES
    # ================================================================

    # Texto principal
    label = ft.Text(
        "¿Me perdonas?",
        size=40,
        weight=ft.FontWeight.BOLD,
    )

    # Imagen inicial
    image = ft.Image(
        src="triste.png",
        width=200,
        height=200
    )

    # Función auxiliar para crear botones
    # Evita repetir código
    def crear_boton(texto: str, color_fondo):
        return ft.ElevatedButton(
            content=ft.Text(texto),
            width=100,
            height=50,
            style=ft.ButtonStyle(
                bgcolor=color_fondo,
                color=ft.Colors.WHITE,
            ),
        )

    # Creamos los tres botones
    button_yes = crear_boton("Sí", ft.Colors.GREEN)
    button_no = crear_boton("No", ft.Colors.RED)
    button_maybe = crear_boton("Quizás", ft.Colors.YELLOW)

    # ================================================================
    # 5️⃣ FUNCIONES DE EVENTOS (LÓGICA DEL PROGRAMA)
    # ================================================================

    # Función para reiniciar la aplicación
    def reset_app():
        image.src = "triste.png"
        button_yes.width = 100
        button_yes.height = 50
        page.update()

    # Evento cuando se presiona "No"
    # Hace que el botón "Sí" crezca
    def no_click(e: ft.Event):
        button_yes.width += 20
        button_yes.height += 10
        page.update()

    # Evento cuando se presiona "Sí"
    # Cambia la imagen a feliz
    def yes_click(e: ft.Event):
        image.src = "feliz.png"
        image.update()

    # Evento cuando se presiona "Quizás"
    # Cambia imagen y espera 2 segundos antes de reiniciar
    async def maybe_click(e: ft.Event):
        image.src = "quizas.png"
        image.update()

        await asyncio.sleep(2)
        reset_app()

    # ================================================================
    # 6️⃣ ASIGNACIÓN DE EVENTOS A LOS BOTONES
    # ================================================================
    button_no.on_click = no_click
    button_yes.on_click = yes_click
    button_maybe.on_click = maybe_click

    # ================================================================
    # 7️⃣ DISEÑO (LAYOUT)
    # ================================================================
    page.add(
        ft.Column(
            [
                label,
                image,
                ft.Row(
                    [
                        button_yes,
                        button_no,
                        button_maybe,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


# ================================================================
# 8️⃣ EJECUCIÓN DE LA APLICACIÓN
# ================================================================
# ft.run inicia la aplicación moderna de Flet
ft.run(main)