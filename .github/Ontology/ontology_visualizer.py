# ontology_visualizer.py - Updated with gaiaair.org domain

import networkx as nx
from pyvis.network import Network
import json
import os
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL
from domain_config import DomainConfig

class OntologyVisualizer:
    """Visualization tools for AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.nodes_data = []
        self.edges_data = []
        
        # Use domain config for namespaces
        self.amedeo = DomainConfig.get_namespace("amedeo")
        
    # Rest of the class remains the same
    # ...
    
    def create_d3_visualization(self, output_dir="d3_visualization"):
        """Create a complete D3.js visualization package"""
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Export data
        data_file = os.path.join(output_dir, "ontology_data.json")
        self.export_for_d3(data_file)
        
        # Create HTML file with updated title and branding
        html_file = os.path.join(output_dir, "index.html")
        with open(html_file, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMEDEO Ontology Visualization - GAIA AIR</title>
    <link rel="icon" href="https://www.gaiaair.org/favicon.ico">
    <!-- Rest of the HTML remains the same -->
    <!-- ... -->
</head>
<body>
    <header>
        <h1>AMEDEO Ontology Visualization</h1>
        <p>Powered by <a href="https://www.gaiaair.org">GAIA AIR</a></p>
    </header>
    <!-- Rest of the HTML remains the same -->
    <!-- ... -->
    <footer>
        <p>&copy; 2025 GAIA AIR - <a href="https://www.gaiaair.org">gaiaair.org</a></p>
    </footer>
</body>
</html>""")
        
        return output_dir
