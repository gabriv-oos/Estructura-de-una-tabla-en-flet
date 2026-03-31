"""
ARCHIVO DE DIAGNÓSTICO - Ejecutar con: flet run test_card.py
Prueba 1: ¿Se ve la tarjeta con datos estáticos? (sin httpx, sin async)
"""
import flet as ft
from app.styles.estilos import Colors, Card, Textos_estilos

def main(page: ft.Page):
    page.title = "Test tarjeta"
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Tabla con datos estáticos
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nombre",   style=Textos_estilos.H4)),
            ft.DataColumn(label=ft.Text("Cantidad",  style=Textos_estilos.H4)),
            ft.DataColumn(label=ft.Text("Ingreso",   style=Textos_estilos.H4)),
            ft.DataColumn(label=ft.Text("Min",       style=Textos_estilos.H4)),
            ft.DataColumn(label=ft.Text("Max",       style=Textos_estilos.H4)),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Fanta")),
                ft.DataCell(ft.Text("5")),
                ft.DataCell(ft.Text("2026-02-11")),
                ft.DataCell(ft.Text("20")),
                ft.DataCell(ft.Text("30")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Coca-Cola")),
                ft.DataCell(ft.Text("48")),
                ft.DataCell(ft.Text("2026-03-01")),
                ft.DataCell(ft.Text("10")),
                ft.DataCell(ft.Text("60")),
            ]),
        ],
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48,
    )

    btn_nuevo = ft.Button("Nuevo producto", icon=ft.Icons.ADD)
    total_text = ft.Text("Total de productos: 2", style=Textos_estilos.H4)

    contenido = ft.Column(
        spacing=30,
        controls=[
            btn_nuevo,
            total_text,
            ft.Container(content=tabla)
        ]
    )
    tarjeta = ft.Container(content=contenido, **Card.tarjeta)

    page.add(tarjeta)

if __name__ == "__main__":
    ft.run(main)
