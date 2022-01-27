from pickletools import optimize
import drawerFunctions as df
import PySimpleGUI as sg
from pathlib import Path
import os

ROOT = Path(__file__).parent


def savePNG(png, directory, filename):

    png.save(str(directory + "\\" + (filename + ".png")), optimize=True)


def drawPack(images, W, H):
    canvasB = df.backgroundPNG(W, H)[0]
    coordinates = [
        (W * 0.25, H * 0.25),
        (W * 0.75, H * 0.25),
        (W * 0.5, H * 0.5),
        (W * 0.25, H * 0.75),
        (W * 0.75, H * 0.75),
    ]

    for i in range(len(images)):
        image = df.openImage(images[i])[0].convert("RGBA")
        image = df.cropToRealSize(image)
        image, _ = df.resizeToFit(image, W//3 - W//10)
        x, y = coordinates[i]
        x -= image.width // 2
        y -= image.height // 2
        canvasB = df.pasteItem(canvasB, image, int(x), int(y))

    return canvasB


layout = [
    [
        sg.Column(
            [
                [
                    sg.Text("Images"),
                ],
                [
                    sg.Text("Width"),
                ],
                [
                    sg.Text("Height"),
                ],
                [
                    sg.Text("Save Folder"),
                ],
                [
                    sg.Text("Name"),
                ],
            ]
        ),
        sg.Column(
            [
                [sg.Input(key="IMAGES"), sg.FilesBrowse("Browse", target="IMAGES")],
                [sg.Input("8000", key="W")],
                [sg.Input("8000", key="H")],
                [
                    sg.Input(str(Path(__file__).parent), key="FOLDER"),
                    sg.FolderBrowse(
                        "Browse", target="FOLDER", initial_folder=Path(__file__).parent
                    ),
                ],
                [sg.Input("1.png", key="FILENAME")],
            ]
        ),
    ],
    [sg.Push(), sg.Button("Generate", p=((0, 0), (20, 0)))],
]

window = sg.Window("Sticker pack maker", layout=layout)

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if len(values["IMAGES"].split(";")) != 5 or not os.path.isdir(values['FOLDER'].strip('\n')):
        sg.Popup("Images: " + str(len(values["IMAGES"].split(";"))) +". Must be 5")
        lock = True
    else:
        lock = False

    if event == "Generate" and not lock:
        sticker_pack = drawPack(
            values["IMAGES"].split(";"), int(values["W"]), int(values["H"])
        )

        savePNG(
            sticker_pack, values["FOLDER"].strip("\n"), values["FILENAME"].strip("\n")
        )

window.close()
