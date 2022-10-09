from PIL import Image
from pathlib import Path
import os


def main():

    inputFolder = input("Enter the input folder name: ")
    outputFolder = input("Enter the output folder name: ")
    get_folder = os.path.expanduser(f"~/Desktop/Projects/{inputFolder}")

    if not PathExists(os.path.expanduser(f"~/Desktop/Projects/{outputFolder}")):
        os.mkdir(os.path.expanduser(f"~/Desktop/Projects/{outputFolder}"))
    save_folder = os.path.expanduser(f"~/Desktop/Projects/{outputFolder}")
    if PathExists(get_folder):
        gif_name = input("Enter the name of the GIF file: ")
        images = []
        for filename in Path(get_folder).glob("*.png"):
            images.append(Image.open(filename))
        images[0].save(
            f"{save_folder}/{gif_name}.gif",
            save_all=True,
            append_images=images[1:],
            optimize=False,
            duration=1000,
            loop=0,
        )

    else:
        print("The path does not exist. Please try again.")


def PathExists(path):

    return Path(path).exists()


if __name__ == "__main__":
    main()
