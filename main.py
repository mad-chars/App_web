# ======================================================================
# 1 Importaciones 
# ======================================================================
# asyncio permite manejar tiempos de espera sin congelar la app
import asyncio

# Importamos Flet
import flet as ft 


# ======================================================================
# 2 Función Principal
# ======================================================================
# Esta función recibe la página como parámetro.
# Todo lo que construyamos visualmente ocurre dentro de main().
def main(page: ft.Page):
    
    #
    # 3 Configuración general de la página
    #
    page.title = "¿Me perdonas?"  # Título de la ventana
    page.bgcolor = ft.Colors.RED_ACCENT_100 
    
    # Centramos contenido horizontal y verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    #
    # 4 Componentes Visuales
    #
    #
    # Texto principal
    label = ft.Text(
        "¿Me perdonas?",
        size=40,
        weight=ft.FontWeight.BOLD,
    )
    
    # Imagen inicial
    image = ft.Image(
        
    )