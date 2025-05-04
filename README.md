# Converter Minecraft in-game maps to PNG

This application converts `.dat` files of in-game Minecraft maps into PNG image files.  
It also supports combining multiple maps into a single image by arranging them in a grid. Duplicate maps are allowed and handled correctly.

## Features

- Convert individual `.dat` map files to `.png`
- Merge multiple map images into a single composite PNG
- Supports duplicate maps in the output
- GUI interface built with PyQt6

## Requirements

- Python 3.8+
- PyQt6
- PIL (Pillow)
- PyNBT

You can install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

You can run the application in two ways:

1. Through Python (running main.py):
Run the application using Python:

```bash
python main.py
```

2. Using the Executable File (from Release):
Alternatively, you can download the executable from the Releases section of repository.
Once downloaded, you can run the application by simply opening the executable file (no need to install Python or dependencies).

## How to Use the Application

1. Launch the Application

    Start the program using Python or the executable as described above.

2. Add Map Files

    * Click the "Add maps" button.

    * In the file dialog, select one or more `.dat` files containing Minecraft map data.

    * Click "Open" to load them into the application.

3. Configure the Grid

    * Use the arrow buttons next to "Column count" and "Row count" to set the desired grid dimensions.

    * Use drag-and-drop to place each loaded map into the desired grid cell.

4. Preview the Layout (Optional)

    * Double-check the grid layout and reposition maps if necessary.

5. Export to PNG

    * Click the "Save as image" button.

    * Choose a file name and destination folder in the dialog.

    * Click "Save" to generate the PNG image.

    * Note: Empty grid cells will appear as solid black squares in the output image.

## License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file for details.