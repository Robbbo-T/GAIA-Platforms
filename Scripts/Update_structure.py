#!/usr/bin/env python3
"""
GAIA PLATFORMS Structure Maintenance Script
------------------------------------------
This script validates and updates the GAIA PLATFORMS directory structure
to ensure COAFI compliance and implement all required enhancements.
"""

import os
import sys
import json
import yaml
import logging
import datetime
from pathlib import Path
from git import Repo

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('gaia-structure')

# Root directory of the repository
REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# InfoCode subdirectories to ensure in each component directory
INFOCODE_DIRS = [
    'OV',    # Overview documents
    'SDD',   # System Design Descriptions
    'SPEC',  # Specifications
    'TEST',  # Testing Plans
    'PROC',  # Procedures
    'PLAN',  # Program Management Plans
    'IDX',   # Indexes and Cross-References
    'NEXUS', # Interconnection Points (Federated)
]

# Major divisions to process
MAJOR_DIVISIONS = [
    'GAIA-AIRs',
    'GAIA-SPACEs',
    'GAIA-GREEN-TECHNOLOGIES',
]

# Shared services to process
SHARED_SERVICES = [
    'GP-COM',
    'GP-RAME',
    'GP-SUPL',
]

# Special directories to track
SPECIAL_DIRS = []

def ensure_directory(path):
    """Ensure directory exists, create if not."""
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True)
        logger.info(f"Created directory: {path}")
    return path

def create_gitkeep(path):
    """Create .gitkeep file if directory is empty."""
    path = Path(path)
    if path.is_dir() and not any(path.iterdir()):
        gitkeep = path / '.gitkeep'
        if not gitkeep.exists():
            gitkeep.touch()
            logger.info(f"Created .gitkeep in: {path}")

def find_component_dirs(root_dir):
    """Find all component directories that should have InfoCode subdirectories."""
    component_dirs = []
    
    # Process GAIA-AIRs structure
    if (REPO_ROOT / 'GAIA-AIRs' / 'GP-AM' / 'AMPEL').exists():
        for ata_dir in (REPO_ROOT / 'GAIA-AIRs' / 'GP-AM' / 'AMPEL').glob('ATA-*'):
            if ata_dir.is_dir():
                component_dirs.append(ata_dir)
                # Track special directories
                if 'SPECIAL' in ata_dir.name:
                    SPECIAL_DIRS.append(ata_dir)
    
    # Process GAIA-SPACEs structure
    if (REPO_ROOT / 'GAIA-SPACEs' / 'GP-AS' / 'AMPELPLUS').exists():
        for as_dir in (REPO_ROOT / 'GAIA-SPACEs' / 'GP-AS' / 'AMPELPLUS').glob('AS-*'):
            if as_dir.is_dir():
                component_dirs.append(as_dir)
                # Track special directories
                if 'SPECIAL' in as_dir.name:
                    SPECIAL_DIRS.append(as_dir)
    
    # Process SharedServices structure
    for service in SHARED_SERVICES:
        service_path = REPO_ROOT / 'SharedServices' / service
        if service_path.exists():
            for ch_dir in service_path.glob('*/CH-*'):
                if ch_dir.is_dir():
                    component_dirs.append(ch_dir)
                    # Track special directories
                    if 'SPECIAL' in ch_dir.name or 'CH-99' in ch_dir.name:
                        SPECIAL_DIRS.append(ch_dir)
    
    return component_dirs

def ensure_infocode_structure(component_dirs):
    """Ensure InfoCode subdirectories exist in all component directories."""
    for component_dir in component_dirs:
        logger.info(f"Processing component directory: {component_dir}")
        for infocode_dir in INFOCODE_DIRS:
            dir_path = ensure_directory(component_dir / infocode_dir)
            create_gitkeep(dir_path)

def create_special_hub():
    """Create or update the GP-SPECIAL hub."""
    special_hub = ensure_directory(REPO_ROOT / 'SharedServices' / 'GP-SPECIAL')
    
    # Create README.md
    readme_path = special_hub / 'README.md'
    if not readme_path.exists():
        with open(readme_path, 'w') as f:
            f.write("# GP-SPECIAL Hub\n\n")
            f.write("This centralized index tracks all Special/Emerging Technologies across GAIA PLATFORMS domains.\n\n")
            f.write("See [index.md](./index.md) for a complete cross-reference of all special technology directories.\n")
    
    # Create index.md with dynamic links to all SPECIAL directories
    index_path = special_hub / 'index.md'
    with open(index_path, 'w') as f:
        f.write("# GP-SPECIAL Hub - Emerging Technologies Index\n\n")
        f.write("Last updated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
        
        f.write("| Domain | Path | Description | Status |\n")
        f.write("|--------|------|-------------|--------|\n")
        
        for special_dir in SPECIAL_DIRS:
            rel_path = os.path.relpath(special_dir, special_hub)
            domain = special_dir.parts[1] if len(special_dir.parts) > 1 else "Unknown"
            description = f"{domain} Special/Emerging Tech"
            f.write(f"| {domain} | [{special_dir.name}]({rel_path}) | {description} | Active |\n")
    
    # Create domains directory structure
    domains_dir = ensure_directory(special_hub / 'domains')
    for division in MAJOR_DIVISIONS:
        division_short = division.split('-')[1].lower()
        domain_dir = ensure_directory(domains_dir / division_short)
        domain_index = domain_dir / 'index.md'
        if not domain_index.exists():
            with open(domain_index, 'w') as f:
                f.write(f"# {division} Special Technologies\n\n")
                f.write("This index tracks special and emerging technologies specific to this domain.\n")

def update_version_files():
    """Update VERSION.md files in major divisions."""
    if os.environ.get('UPDATE_VERSION', 'false').lower() != 'true':
        logger.info("Skipping VERSION.md updates (set UPDATE_VERSION=true to enable)")
        return
        
    for division in MAJOR_DIVISIONS:
        division_path = REPO_ROOT / division
        if not division_path.exists():
            continue
            
        version_path = division_path / 'VERSION.md'
        
        # If VERSION.md doesn't exist, create it
        if not version_path.exists():
            with open(version_path, 'w') as f:
                f.write(f"# {division} – Version Record\n\n")
                f.write("## Current Version\n")
                f.write("- v0.1.0 (Initial Structure)\n\n")
                f.write("## Major Milestones\n")
                f.write(f"- v0.1.0 – Initial structure creation based on AToC.md COAFI standard ({datetime.date.today()})\n")
                f.write("- v0.2.0 – [Future Milestone] (Planned)\n\n")
                f.write("## Component Version Matrix\n\n")
                f.write("| Component | Version | Last Updated | Status | Dependencies |\n")
                f.write("|-----------|---------|--------------|--------|-------------|\n")
                
                # Add components based on directory structure
                for component_dir in division_path.glob('*'):
                    if component_dir.is_dir() and not component_dir.name.startswith('.'):
                        f.write(f"| {component_dir.name} | v0.1.0 | {datetime.date.today()} | Planning | - |\n")
        else:
            # Update existing VERSION.md (more complex, would need to parse and modify)
            logger.info(f"VERSION.md already exists for {division}, skipping update")

def ensure_ampide_readiness():
    """Ensure AMPIDE readiness files exist in docs directories."""
    for division in MAJOR_DIVISIONS:
        division_path = REPO_ROOT / division
        if not division_path.exists():
            continue
            
        # Find all docs directories
        for docs_dir in division_path.glob('**/docs'):
            if docs_dir.is_dir():
                # Create semantic-map.yaml if it doesn't exist
                semantic_map = docs_dir / 'semantic-map.yaml'
                if not semantic_map.exists():
                    component_path = docs_dir.parent
                    component_name = component_path.name
                    
                    with open(semantic_map, 'w') as f:
                        f.write(f"# semantic-map.yaml\n")
                        f.write(f"# GAIA PLATFORMS - {component_name} Semantic Map\n")
                        f.write("# This file defines the semantic relationships between components for AMPIDE integration\n\n")
                        f.write("version: \"1.0\"\n")
                        f.write(f"component_id: \"{component_name}\"\n")
                        f.write(f"component_name: \"{component_name}\"\n")
                        f.write(f"domain: \"{division}\"\n")
                        f.write(f"coafi_path: \"{os.path.relpath(component_path, REPO_ROOT)}\"\n\n")
                        f.write("# Semantic Relationships\n")
                        f.write("relationships: []\n\n")
                        f.write("# Semantic Tags\n")
                        f.write("tags: []\n\n")
                        f.write("# Ontology References\n")
                        f.write("ontology_references: []\n\n")
                        f.write("# Data Flows\n")
                        f.write("data_flows: []\n")
                
                # Create datamodel-schema.json if it doesn't exist
                datamodel_schema = docs_dir / 'datamodel-schema.json'
                if not datamodel_schema.exists():
                    component_path = docs_dir.parent
                    component_name = component_path.name
                    
                    schema = {
                        "$schema": "http://json-schema.org/draft-07/schema#",
                        "title": f"{component_name} Data Model",
                        "description": f"Data model schema for {component_name} in GAIA PLATFORMS",
                        "type": "object",
                       
