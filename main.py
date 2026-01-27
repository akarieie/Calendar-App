import flet as ft

def main(page: ft.Page):
    # Set the alignment of the app content to the center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Create a Text widget
    hello_text = ft.Text("hello", size=30, weight="bold", color="blue")
    text2 = ft.Text("world", size=30, weight="bold", color="red")
    
    # Add the widget to the page
    page.add(hello_text)
    page.add(text2)

# Run the app
ft.app(target=main)