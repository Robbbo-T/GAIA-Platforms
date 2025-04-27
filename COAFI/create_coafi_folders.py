import os

# Define the more detailed directory structure for COAFI as an active engine
# Paths are relative to the COAFI directory
coafi_dirs_to_create = [
    "Schema",                     # Para definir la estructura COAFI, metadatos, formato UTidS
    "Engine",                     # Lógica central del motor de orquestación COAFI
    "Engine/Orchestration_Core",  # Componentes principales del motor
    "Engine/Event_Handlers",      # Lógica para reaccionar a eventos (commits, API calls)
    "Generators",                 # Módulos para la generación de contenido
    "Generators/Document_Templates", # Plantillas para especificaciones, READMEs, etc.
    "Generators/Script_Generators",  # Lógica para generar scripts (ej. validación)
    "Workflows",                  # Definiciones de procesos de orquestación
    "Workflows/Process_Definitions", # Ej. flujo de actualización de documentos
    "Interfaces",                 # APIs y puntos de integración
    "Interfaces/API_Definitions",   # Especificaciones OpenAPI para servicios COAFI
    "Interfaces/Adapters",          # Conectores a otros sistemas (Git, BITT, AMEDEO)
    "Registries",                 # Punteros a artefactos gestionados (índices)
    "Registries/AERO",            # Índice específico del dominio AERO
    "Registries/SPACE",           # Índice específico del dominio SPACE
    "Registries/COM",             # Índice específico del dominio COM
    "Registries/GROUND",          # Índice específico del dominio GROUND
    "Registries/GREENTECH",       # Índice específico del dominio GREENTECH
    # Añadir otros dominios según sea necesario...
    "Policies",                   # Políticas de gobernanza sobre el uso y operación de COAFI
    "Tooling"                     # Scripts y utilidades de gestión/interacción con COAFI
]

# Function to create directories and placeholder READMEs within COAFI
def create_coafi_structure(base_coafi_path="COAFI"):
    """Creates the detailed directory structure within COAFI and adds placeholder README.md files."""
    print(f"Starting COAFI directory structure creation within: {base_coafi_path}")

    # Ensure the base COAFI directory exists
    if not os.path.exists(base_coafi_path):
        print(f"Error: Base directory '{base_coafi_path}' does not exist. Please create it first or run the main structure script.")
        return
    if not os.path.isdir(base_coafi_path):
        print(f"Error: '{base_coafi_path}' exists but is not a directory.")
        return

    # Create the base README if it doesn't exist
    base_readme_path = os.path.join(base_coafi_path, "README.md")
    if not os.path.exists(base_readme_path):
        with open(base_readme_path, 'w') as f:
            f.write(f"# COAFI - Canonical Orchestrated Architecture File Index\n\n")
            f.write("Overview of the COAFI system, acting as the central engine for content generation, information orchestration, and automated updates within GAIA Platforms.\n\n")
            f.write("*(Placeholder README - Contenido pendiente)*\n")
        print(f"  - Created placeholder README.md in {base_coafi_path}")

    # Create subdirectories and their READMEs
    for rel_path in coafi_dirs_to_create:
        # Construct the full path inside COAFI
        full_path = os.path.join(base_coafi_path, rel_path)

        try:
            # Create the directory, including any necessary parent directories
            os.makedirs(full_path, exist_ok=True)
            print(f"Created/Ensured directory: {full_path}")

            # Create a placeholder README.md file in the new directory
            readme_path = os.path.join(full_path, "README.md")
            if not os.path.exists(readme_path):
                # Extract the directory name for the title
                dir_name = os.path.basename(full_path)
                readme_title = dir_name.replace('_', ' ')
                with open(readme_path, 'w') as f:
                    # Write title in English, placeholder note in Spanish
                    f.write(f"# COAFI - {readme_title}\n\n")
                    f.write("*(Placeholder README - Contenido pendiente)*\n")
                print(f"  - Created placeholder README.md in {dir_name}")
            else:
                print(f"  - README.md already exists in {full_path}")

        except OSError as e:
            print(f"Error creating directory {full_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for path {full_path}: {e}")

    print("COAFI directory structure creation finished.")

# --- Main Execution ---
if __name__ == "__main__":
    # Assuming the script is run from the root of the GAIA-Platforms repository
    # It targets the existing COAFI directory
    create_coafi_structure(base_coafi_path="COAFI")
