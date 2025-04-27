import os

# Define the directory structure based on the proposal
# Using a list of paths relative to the script's location (repo root)
dirs_to_create = [
    "COAFI",
    "DOCS",
    "Domains",
    "Domains/AERO",
    "Domains/AERO/CIVIL",
    "Domains/AERO/CIVIL/COMMERCIAL",
    "Domains/AERO/CIVIL/COMMERCIAL/IMG",
    "Domains/AERO/CIVIL/PRIVATE_JETS",
    "Domains/AERO/SECURE_AERO",
    "Domains/AERO/SECURE_AERO/Cyber_Defence",
    "Domains/AERO/SECURE_AERO/Post_Quantum_Security",
    "Domains/AERO/SECURE_AERO/Cryptography",
    "Domains/AERO/SECURE_AERO/Defensive_Systems_Tech",
    "Domains/AERO/INTERFACE",
    "Domains/AERO/INTERFACE/Aeronautical-Interfaces",
    "Domains/AERO/INTERFACE/Ground-Aerospace-Interfaces",
    "Domains/AERO/INTERFACE/Data-Control-Interfaces",
    "Domains/COM",
    "Domains/COM/InaC",
    "Domains/COM/InaC/Computing-Communications",
    "Domains/COM/InaC/Computing-Communications/HPC",
    "Domains/COM/InaC/Computing-Communications/Cloud",
    "Domains/COM/InaC/Computing-Communications/Digital",
    "Domains/COM/InaC/Computing-Communications/Quantum",
    "Domains/COM/InaC/Computing-Communications/AI-ML-AGI",
    "Domains/COM/InaC/Computing-Communications/Robotics-Braining",
    "Domains/COM/InaC/Computing-Communications/CoT-IoT",
    "Domains/COM/InaC/Fintech",
    "Domains/COM/InaC/DevOps",
    "Domains/COM/InaC/Industrial-Intelligence",
    "Domains/COM/InaC/Sectorial-Intelligence",
    "Domains/COM/InaC/Data-Compliance-Policy",
    "Domains/COM/InaC/Cybersecurity",
    "Domains/COM/BITT",
    "Domains/COM/Ethics",
    "Domains/COM/Federation",
    "Domains/COM/Security",
    "Domains/COM/Services",
    "Domains/DRONES",
    "Domains/GREENTECH",
    "Domains/GROUND",
    "Domains/GROUND/Data_Centers", # Added
    "Domains/GROUND/Tower_Control", # Added
    "Domains/GROUND/Airports", # Added
    "Domains/GROUND/Launch_Systems_Support", # Added (Clarified name)
    "Domains/GROUND/Space_Research_Centers", # Added
    "Domains/GROUND/Assembly_Lines", # Added (Intelligent & Green)
    "Domains/RESEARCH-INNOVATION",
    "Domains/SPACE",
    "Domains/SPACE/INTERPLANETARY",
    "Domains/SPACE/INTERPLANETARY/PROPULSION",
    "Domains/SPACE/ORBITAL_SERVICES",
    "Domains/SPACE/ORBITAL_SERVICES/SATELLITES",
    "Domains/SPACE/LAUNCH_SYSTEMS", # Kept here for space vehicle specifics
    "Domains/SPACE/HABITAT_SYSTEMS",
    "Domains/SPACE/ROBOTICS",
    "Domains/SPACE/INTERFACE",
    "Domains/SPACE/INTERFACE/Orbital-Interfaces",
    "Domains/SUPPLY",
    "Domains/URBAN-MOBILITY",
    "GAIA-AIR",
    "GAIA-GREENTECH",
    "GAIA-SPACE",
    "WorldWideWinner",
    "DOCS/COAFI-TOC-0001-OV-A",
    "DOCS/COAFI-FOUND-0001-OV-A",
    "DOCS/COAFI-FOUND-0002-PRINC-A",
    "DOCS/COAFI-FOUND-0003-FED-A",
    "Engine/Event_Handlers",
    "Engine/Orchestration_Core",
    "Schema",
    "Registries",
    "Registries/AERO",
    "Registries/SPACE",
    "Registries/COM",
    "Registries/GROUND",
    "Registries/GREENTECH",
    "Workflows/Process_Definitions",
    "Policies",
    "Interfaces/API_Definitions",
    "Interfaces/Adapters",
    "Tooling/Document_Templates",
    "Tooling/Script_Generators",
    "Tooling"
]

# Function to create directories and placeholder READMEs
def create_structure(base_path="."):
    """Creates the directory structure and adds placeholder README.md files."""
    print("Starting directory structure creation...")
    for rel_path in dirs_to_create:
        # Construct the full path
        full_path = os.path.join(base_path, rel_path)

        try:
            # Create the directory, including any necessary parent directories
            # exist_ok=True prevents an error if the directory already exists
            os.makedirs(full_path, exist_ok=True)
            print(f"Created/Ensured directory: {full_path}")

            # Create a placeholder README.md file in the new directory
            readme_path = os.path.join(full_path, "README.md")
            if not os.path.exists(readme_path):
                # Extract the directory name for the title
                dir_name = os.path.basename(full_path)
                # Replace underscores with spaces for a cleaner title
                readme_title = dir_name.replace('_', ' ')
                with open(readme_path, 'w') as f:
                    f.write(f"# {readme_title}\n\n")
                    f.write("*(Placeholder README)*\n")
                print(f"  - Created placeholder README.md in {dir_name}")
            else:
                print(f"  - README.md already exists in {full_path}")

        except OSError as e:
            print(f"Error creating directory {full_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for path {full_path}: {e}")

    print("Directory structure creation finished.")

# --- Main Execution ---
if __name__ == "__main__":
    # Assuming the script is run from the root of the GAIA-Platforms repository
    create_structure()
