# TA_Scripts
🚀 A collection of scripts and tools for Technical Art, focusing on automation in Maya and (eventually) Unreal Engine.

📂 Repository Structure

TA_Scripts/
```
│── Python/

│   ├── Maya/

│   │   ├── random_object_generator.py  # Script generates random number of cubes and spheres, positions them randomly in 3D space,
                                        applies random scales, and renames them based on their size (large or small).

│   │   ├── Forest_generator.py         #Procedural tree generation in Maya using Python. This script creates "trees" with random
                                        trunk and leaf positions, rotation, and scaling. It also generates a forest of trees at
                                        random positions, suitable for creating dynamic environments for 3D scenes or animation
                                        projects.Plug and play custom models.

│   │   ├── Maya_JSON_Importer.py       #Python script that uses Maya's file opener and reads a JSON file to create and position
                                        3D objects. It supports predefined object types (trees and rocks, but easily editable),
                                        creates and assign colors to shaders based on names or RGB values, and applies
                                        transformations like scaling and positioning.
```
│   ├── Unreal/  (future scripts)

│── C++/ (future Unreal Engine tools)

│── README.md  

🛠 Features

Maya Automation: Tools for optimizing workflows, including object manipulation, naming conventions, and retopology helpers.
Unreal Integration (Soon): Planned tools for automating workflows in UE.

📌 Getting Started

Clone the repo:

git clone https://github.com/daphfodils/TA_Scripts.git
Open Maya and load a script via the Script Editor or MEL command:
exec(open("path/to/script.py").read())
Modify and use freely!

💡 Future Plans

✅ Expand Python automation for Maya

✅ Add C++ tools for Unreal

✅ Create UI-based scripts for better usability


