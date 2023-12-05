from taipy.gui import Gui

img_path = "./starterFiles/placeholder.png"

content = ""

index = """
<|text-center|
<|{img_path}|image|>

<|{content}|file_selector|>
Select image from your file system
>
"""

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)