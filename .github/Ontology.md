## GenAI Proposal Status Disclaimer

*This document is a GenAI-generated proposal and has not been validated by domain experts. The implementation details are theoretical and would need formal review and validation by specialists in ontological engineering and semantic web technologies.*

# AMEDEO Ontology Analyzer

## Overview

The AMEDEO Ontology Analyzer is a Python-based tool for parsing, analyzing, and visualizing the AMEDEO Ontology - the ethical-semantic foundation for Federated Intelligent Systems in the GAIA AIR ecosystem. This tool supports multiple serialization formats (Turtle, OWL/XML, JSON-LD) and provides comprehensive analysis capabilities for ontology validation, ethical principle extraction, and federation anchor detection.

## Project Information

- **Filename**: GP-FD-ONTOLOGY-AMEDEO-ANALYZER-001-PROC-A.py
- **Version**: 0.9
- **InfoCode**: PROC (Procedure)
- **Status**: Draft
- **Extensions**: RDFLIB, NETWORKX, MATPLOTLIB, JSON-LD, TTL, OWL2-DL, CFSI-Conformant

## Features

- **Multi-format Parsing**: Support for Turtle, OWL/XML, and JSON-LD serializations
- **Comprehensive Extraction**: Classes, properties, individuals, and their relationships
- **Federation Analysis**: Detection and analysis of federation anchors (QAO, PET-CORE, AMPEL)
- **Ethical Framework**: Identification and extraction of ethical principles and constraints
- **Visualization**: Graph-based visualization of class hierarchies and relationships
- **Metrics Generation**: Statistical analysis of ontology structure and complexity

## Requirements

- Python 3.7+
- rdflib
- networkx
- matplotlib
- json

## Installation

```bash
# Clone the repository
git clone https://github.com/gaiaair/ontology-tools.git
cd ontology-tools

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer

# Create analyzer instance
analyzer = AmedeoOntologyAnalyzer()

# Parse ontology data (choose one format)
analyzer.parse_turtle("path/to/amedeo.ttl")  # From file
analyzer.parse_xml(xml_data_string)          # From string
analyzer.parse_jsonld(json_data_dict)        # From dictionary

# Analyze the ontology
results = analyzer.analyze_ontology()
print(f"Total triples: {results['total_triples']}")
print(f"Classes: {results['classes']}")
```

### Visualization

```python
# Generate class hierarchy graph
G = analyzer.visualize_class_hierarchy()

# Visualize using matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1500, arrows=True, font_size=10)
plt.title("AMEDEO Ontology Class Hierarchy")
plt.savefig("amedeo_hierarchy.png")
plt.show()
```

### Extracting Ethical Principles

```python
# Get all ethical principles
principles = analyzer.get_ethical_principles()

# Print principles
for principle in principles:
    print(f"Principle: {principle['label']}")
    print(f"Description: {principle['description']}")
    print("---")
```

### Federation Analysis

```python
# Get federation anchors
anchors = analyzer.get_federation_anchors()

# Print federation connections
for anchor in anchors:
    print(f"Anchor: {anchor['anchor']}")
    print("Equivalent classes:")
    for eq_class in anchor['equivalent_classes']:
        print(f"  - {eq_class}")
    print("---")
```

## Integration with GAIA AIR Ecosystem

The AMEDEO Ontology Analyzer is designed to integrate seamlessly with other components of the GAIA AIR ecosystem:

- **TokenFlow Pipeline**: Provides ontological validation for the TokenFlow processing pipeline
- **Ethical Certification**: Supports automated ethical certification of AI systems
- **Federation Management**: Enables cross-ontology mapping and federation
- **Audit Trail Generation**: Facilitates the creation of audit trails for AI decision processes


## Extension Points

The analyzer can be extended in several ways:

1. **SWRL Rule Processing**: Add support for parsing and analyzing SWRL rules
2. **Reasoning Capabilities**: Integrate with OWL reasoners for inference
3. **Validation Rules**: Implement custom validation rules for AMEDEO compliance
4. **Interactive Visualization**: Create interactive web-based visualizations
5. **Blockchain Integration**: Add support for anchoring ontology versions to blockchain


## License

GAIA AIR License v1.0

## Contact

GAIA AIR Ontology Team[ontology@gaiaair.org](mailto:ontology@gaiaair.org)



## Sample amedeo.owl for Testing

Here's a simplified but functional amedeo.owl file that can be used for testing the analyzer:

```xml
<?xml version="1.0"?>
<Ontology xmlns="http://www.gaiaair.org/ontologies/amedeo#"
     xml:base="http://www.gaiaair.org/ontologies/amedeo"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     ontologyIRI="http://www.gaiaair.org/ontologies/amedeo">

    <!-- Ontology Metadata -->
    <owl:Ontology rdf:about="http://www.gaiaair.org/ontologies/amedeo">
        <rdfs:comment>AMEDEO Ontology: Ethical and Semantic Foundation for Federated Intelligent Systems</rdfs:comment>
        <rdfs:label>AMEDEO Ontology</rdfs:label>
        <owl:versionInfo>1.0</owl:versionInfo>
    </owl:Ontology>

    <!-- Core Classes -->
    <owl:Class rdf:about="#Concept"/>
    <owl:Class rdf:about="#Relationship"/>
    <owl:Class rdf:about="#EthicalAssertion"/>
    <owl:Class rdf:about="#FederatedEntity"/>
    <owl:Class rdf:about="#SemanticValidation"/>

    <!-- Expanded Classes -->
    <owl:Class rdf:about="#EthicalPrinciple">
        <rdfs:subClassOf rdf:resource="#EthicalAssertion"/>
        <rdfs:comment>Fundamental ethical principles that guide system behavior</rdfs:comment>
    </owl:Class>

    <owl:Class rdf:about="#OperationalConstraint">
        <rdfs:subClassOf rdf:resource="#FederatedEntity"/>
        <rdfs:comment>Constraints on system operation to ensure ethical compliance</rdfs:comment>
    </owl:Class>

    <owl:Class rdf:about="#CertificationLevel">
        <rdfs:comment>Levels of certification for validated entities</rdfs:comment>
    </owl:Class>

    <owl:Class rdf:about="#FederationAnchor">
        <rdfs:comment>Connection points to external ontologies and frameworks</rdfs:comment>
    </owl:Class>

    <owl:Class rdf:about="#QAOAnchor">
        <rdfs:subClassOf rdf:resource="#FederationAnchor"/>
        <rdfs:comment>Connection to Quality Assurance Ontology</rdfs:comment>
    </owl:Class>

    <!-- Core Properties -->
    <owl:ObjectProperty rdf:about="#relatesTo">
        <rdfs:domain rdf:resource="#Concept"/>
        <rdfs:range rdf:resource="#Concept"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="#governs">
        <rdfs:domain rdf:resource="#EthicalAssertion"/>
        <rdfs:range rdf:resource="#FederatedEntity"/>
    </owl:ObjectProperty>

    <owl:DatatypeProperty rdf:about="#hasDescription">
        <rdfs:domain rdf:resource="#Concept"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- Individuals -->
    <owl:NamedIndividual rdf:about="#EthicalPrinciple-EP-001">
        <rdf:type rdf:resource="#EthicalPrinciple"/>
        <rdfs:label>Safety First Principle</rdfs:label>
        <hasDescription>System must prioritize human safety above all other considerations</hasDescription>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="#EthicalPrinciple-EP-002">
        <rdf:type rdf:resource="#EthicalPrinciple"/>
        <rdfs:label>Transparency Principle</rdfs:label>
        <hasDescription>System decisions must be explainable and transparent to users</hasDescription>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="#CertificationLevel-CL-001">
        <rdf:type rdf:resource="#CertificationLevel"/>
        <rdfs:label>Level 1 - Basic</rdfs:label>
        <hasDescription>Basic certification for non-critical systems</hasDescription>
    </owl:NamedIndividual>
</Ontology>
```

## Dashboard GUI Proposal

For the dashboard GUI, I recommend using Streamlit for its simplicity and rapid development capabilities. Here's a basic implementation:

```python
# streamlit_amedeo_dashboard.py
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer

st.set_page_config(page_title="AMEDEO Ontology Analyzer", layout="wide")

st.title("AMEDEO Ontology Analyzer Dashboard")
st.markdown("Analyze and visualize the AMEDEO Ontology for Federated Intelligent Systems")

# File upload
st.sidebar.header("Upload Ontology File")
file_format = st.sidebar.selectbox("Select Format", ["Turtle (.ttl)", "OWL/XML (.owl, .xml)", "JSON-LD (.jsonld)"])
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["ttl", "owl", "xml", "jsonld"])

# Initialize analyzer
analyzer = AmedeoOntologyAnalyzer()

if uploaded_file is not None:
    # Parse the uploaded file
    file_content = uploaded_file.read()
    
    try:
        if file_format == "Turtle (.ttl)":
            analyzer.parse_turtle(file_content.decode("utf-8"))
        elif file_format == "OWL/XML (.owl, .xml)":
            analyzer.parse_xml(file_content.decode("utf-8"))
        elif file_format == "JSON-LD (.jsonld)":
            import json
            analyzer.parse_jsonld(json.loads(file_content.decode("utf-8")))
        
        # Analyze the ontology
        analysis = analyzer.analyze_ontology()
        
        # Display metrics
        st.header("Ontology Metrics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Triples", analysis["total_triples"])
        col2.metric("Classes", analysis["classes"])
        col3.metric("Object Properties", analysis["object_properties"])
        col4.metric("Individuals", analysis["individuals"])
        
        # Display class hierarchy
        st.header("Class Hierarchy")
        G = analyzer.visualize_class_hierarchy()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, arrows=True, font_size=10, ax=ax)
        st.pyplot(fig)
        
        # Display ethical principles
        st.header("Ethical Principles")
        principles = analysis["ethical_principles"]
        if principles:
            principles_df = pd.DataFrame([
                {"Label": p["label"], "Description": p["description"]} 
                for p in principles if p["label"] is not None
            ])
            st.table(principles_df)
        else:
            st.info("No ethical principles found in the ontology.")
        
        # Display federation anchors
        st.header("Federation Anchors")
        anchors = analysis["federation_anchors"]
        if anchors:
            for i, anchor in enumerate(anchors):
                st.subheader(f"Anchor {i+1}: {anchor['anchor']}")
                st.write("Equivalent classes:")
                for eq_class in anchor["equivalent_classes"]:
                    st.write(f"- {eq_class}")
        else:
            st.info("No federation anchors found in the ontology.")
            
    except Exception as e:
        st.error(f"Error parsing the ontology file: {str(e)}")
else:
    st.info("Please upload an ontology file to begin analysis.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**GAIA AIR Ontology Tools**")
st.sidebar.markdown("Version 0.9")
st.sidebar.markdown("[Documentation](https://gaiaair.org/docs)")
```

To run this dashboard:

1. Save the code above as `streamlit_amedeo_dashboard.py`
2. Install Streamlit: `pip install streamlit pandas`
3. Run the dashboard: `streamlit run streamlit_amedeo_dashboard.py`

## GenAI Proposal Status Disclaimer

*This document is a GenAI-generated proposal and has not been validated by domain experts. The implementation details are theoretical and would need formal review and validation by specialists in ontological engineering and semantic web technologies.*

# AMEDEO Ontology Analyzer: Advanced Extensions

Based on your detailed information, I've developed a comprehensive implementation plan for extending the AMEDEO Ontology Analyzer with visualization capabilities, validation tools, cross-ontology mapping support, federation anchor management, and TokenFlow pipeline integration.

## 1. Ontology Visualization Extension

```python
# visualization_extension.py - Visualization capabilities for AMEDEO Ontology Analyzer

import networkx as nx
from pyvis.network import Network
import json
import os
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL

class OntologyVisualizer:
    """Visualization tools for AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.nodes_data = []
        self.edges_data = []
        
    def set_graph(self, graph):
        """Set the RDFLib graph to visualize"""
        self.graph = graph
        
    def prepare_visualization_data(self, include_individuals=True, include_literals=False, 
                                  include_datatypes=False, max_nodes=1000):
        """Extract nodes and edges from the ontology graph for visualization"""
        self.nodes_data = []
        self.edges_data = []
        
        # Track processed nodes to avoid duplicates
        processed_nodes = set()
        
        # Helper function to get a short name for display
        def get_short_name(uri):
            if isinstance(uri, URIRef):
                if "#" in uri:
                    return uri.split("#")[-1]
                return uri.split("/")[-1]
            return str(uri)
        
        # Helper function to get node type
        def get_node_type(node):
            if isinstance(node, Literal):
                return "Literal"
            elif isinstance(node, BNode):
                return "BlankNode"
            
            # Check if it's a class
            if (node, RDF.type, OWL.Class) in self.graph:
                return "Class"
            # Check if it's an individual
            elif (node, RDF.type, OWL.NamedIndividual) in self.graph:
                return "Individual"
            # Check if it's an object property
            elif (node, RDF.type, OWL.ObjectProperty) in self.graph:
                return "ObjectProperty"
            # Check if it's a datatype property
            elif (node, RDF.type, OWL.DatatypeProperty) in self.graph:
                return "DatatypeProperty"
            # Check if it's an annotation property
            elif (node, RDF.type, OWL.AnnotationProperty) in self.graph:
                return "AnnotationProperty"
            # Check if it's a datatype
            elif (node, RDF.type, RDFS.Datatype) in self.graph:
                return "Datatype"
            
            # Default
            return "Entity"
        
        # Add classes
        for s in self.graph.subjects(RDF.type, OWL.Class):
            if isinstance(s, URIRef) and s not in processed_nodes:
                node_id = str(s)
                label = get_short_name(s)
                
                # Get description if available
                description = None
                for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                    description = str(comment)
                    break
                
                self.nodes_data.append({
                    'id': node_id,
                    'label': label,
                    'type': 'Class',
                    'description': description
                })
                processed_nodes.add(s)
        
        # Add properties
        for prop_type in [OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty]:
            for s in self.graph.subjects(RDF.type, prop_type):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    # Get description if available
                    description = None
                    for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                        description = str(comment)
                        break
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': get_node_type(s),
                        'description': description
                    })
                    processed_nodes.add(s)
        
        # Add individuals if requested
        if include_individuals:
            for s in self.graph.subjects(RDF.type, OWL.NamedIndividual):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    # Get description if available
                    description = None
                    for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                        description = str(comment)
                        break
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Individual',
                        'description': description
                    })
                    processed_nodes.add(s)
        
        # Add datatypes if requested
        if include_datatypes:
            for s in self.graph.subjects(RDF.type, RDFS.Datatype):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Datatype',
                        'description': None
                    })
                    processed_nodes.add(s)
        
        # Add literals if requested (usually not recommended for large ontologies)
        if include_literals:
            for s, p, o in self.graph:
                if isinstance(o, Literal) and o not in processed_nodes:
                    node_id = f"lit_{len(processed_nodes)}"  # Generate unique ID
                    label = str(o)[:20] + "..." if len(str(o)) > 20 else str(o)
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Literal',
                        'description': None
                    })
                    processed_nodes.add(o)
        
        # Limit nodes if necessary
        if len(self.nodes_data) > max_nodes:
            self.nodes_data = self.nodes_data[:max_nodes]
            processed_nodes = {node['id'] for node in self.nodes_data}
        
        # Add edges
        edge_id = 0
        
        # Add subclass relationships
        for s, p, o in self.graph.triples((None, RDFS.subClassOf, None)):
            if (isinstance(s, URIRef) and isinstance(o, URIRef) and 
                str(s) in processed_nodes and str(o) in processed_nodes):
                self.edges_data.append({
                    'id': f"edge_{edge_id}",
                    'source': str(s),
                    'target': str(o),
                    'label': 'subClassOf',
                    'type': 'SubClassRelation'
                })
                edge_id += 1
        
        # Add type relationships for individuals
        if include_individuals:
            for s, p, o in self.graph.triples((None, RDF.type, None)):
                if (isinstance(s, URIRef) and isinstance(o, URIRef) and 
                    str(s) in processed_nodes and str(o) in processed_nodes and
                    o != OWL.Class and o != OWL.ObjectProperty and 
                    o != OWL.DatatypeProperty and o != OWL.NamedIndividual):
                    self.edges_data.append({
                        'id': f"edge_{edge_id}",
                        'source': str(s),
                        'target': str(o),
                        'label': 'type',
                        'type': 'TypeRelation'
                    })
                    edge_id += 1
        
        # Add property relationships
        for s, p, o in self.graph:
            if (isinstance(p, URIRef) and p != RDF.type and p != RDFS.subClassOf and
                str(s) in processed_nodes and 
                (isinstance(o, URIRef) and str(o) in processed_nodes)):
                self.edges_data.append({
                    'id': f"edge_{edge_id}",
                    'source': str(s),
                    'target': str(o),
                    'label': get_short_name(p),
                    'type': 'PropertyRelation'
                })
                edge_id += 1
        
        return self.nodes_data, self.edges_data
    
    def visualize_with_pyvis(self, output_file="ontology_graph.html", height="750px", width="100%",
                           physics=True, show_buttons=True):
        """Generate an interactive visualization using Pyvis"""
        if not self.nodes_data:
            self.prepare_visualization_data()
        
        # Create network
        net = Network(notebook=False, height=height, width=width, heading="AMEDEO Ontology Graph")
        
        # Define node colors based on type
        color_map = {
            'Class': '#4CAF50',  # Green
            'ObjectProperty': '#2196F3',  # Blue
            'DatatypeProperty': '#03A9F4',  # Light Blue
            'AnnotationProperty': '#00BCD4',  # Cyan
            'Individual': '#FFC107',  # Amber
            'Datatype': '#9C27B0',  # Purple
            'Literal': '#E91E63',  # Pink
            'Entity': '#607D8B'  # Blue Grey
        }
        
        # Add nodes
        for node in self.nodes_data:
            color = color_map.get(node['type'], '#607D8B')
            shape = 'box' if node['type'] == 'Class' else 'dot'
            
            title = f"Type: {node['type']}"
            if node['description']:
                title += f"\nDescription: {node['description']}"
            
            net.add_node(
                node['id'],
                label=node['label'],
                title=title,
                color=color,
                shape=shape,
                group=node['type']
            )
        
        # Add edges
        for edge in self.edges_data:
            net.add_edge(
                edge['source'],
                edge['target'],
                title=edge['label'],
                label=edge['label'] if edge['type'] == 'PropertyRelation' else '',
                arrows='to'
            )
        
        # Configure options
        net.toggle_physics(physics)
        if show_buttons:
            net.show_buttons(filter_=['physics', 'nodes', 'edges'])
        
        # Set other options
        net.set_options("""
        var options = {
            "nodes": {
                "font": {
                    "size": 12
                }
            },
            "edges": {
                "color": {
                    "inherit": true
                },
                "smooth": {
                    "enabled": false
                }
            },
            "physics": {
                "hierarchicalRepulsion": {
                    "centralGravity": 0.5,
                    "springLength": 150,
                    "springConstant": 0.01,
                    "nodeDistance": 120,
                    "damping": 0.09
                },
                "solver": "hierarchicalRepulsion"
            }
        }
        """)
        
        # Save to file
        net.save_graph(output_file)
        return output_file
    
    def export_for_d3(self, output_file="ontology_d3.json"):
        """Export the graph data for use with D3.js"""
        if not self.nodes_data:
            self.prepare_visualization_data()
        
        # Create the data structure expected by D3
        d3_data = {
            "nodes": self.nodes_data,
            "links": [{
                "source": edge["source"],
                "target": edge["target"],
                "label": edge["label"],
                "type": edge["type"]
            } for edge in self.edges_data]
        }
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(d3_data, f, indent=2)
        
        return output_file
    
    def create_d3_visualization(self, output_dir="d3_visualization"):
        """Create a complete D3.js visualization package"""
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Export data
        data_file = os.path.join(output_dir, "ontology_data.json")
        self.export_for_d3(data_file)
        
        # Create HTML file
        html_file = os.path.join(output_dir, "index.html")
        with open(html_file, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMEDEO Ontology Visualization</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        #controls {
            padding: 10px;
            background-color: #f0f0f0;
            border-bottom: 1px solid #ccc;
        }
        #search-container {
            margin-bottom: 10px;
        }
        #search {
            padding: 5px;
            width: 300px;
        }
        #filters {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .filter-group {
            margin-right: 15px;
        }
        #graph {
            flex-grow: 1;
            border-top: 1px solid #ccc;
            overflow: hidden;
        }
        .node {
            cursor: pointer;
        }
        .node text {
            font-size: 10px;
        }
        .link {
            stroke: #999;
            stroke-opacity: 0.6;
        }
        #tooltip {
            position: absolute;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            display: none;
            z-index: 1000;
            max-width: 300px;
        }
        #info-panel {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 300px;
            max-height: 80%;
            overflow-y: auto;
            z-index: 900;
        }
    </style>
</head>
<body>
    <div id="controls">
        <div id="search-container">
            <input type="text" id="search" placeholder="Search nodes...">
            <button id="search-btn">Search</button>
        </div>
        <div id="filters">
            <div class="filter-group">
                <b>Node Types:</b>
                <div>
                    <input type="checkbox" id="filter-class" checked>
                    <label for="filter-class">Classes</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-property" checked>
                    <label for="filter-property">Properties</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-individual" checked>
                    <label for="filter-individual">Individuals</label>
                </div>
            </div>
            <div class="filter-group">
                <b>Edge Types:</b>
                <div>
                    <input type="checkbox" id="filter-subclass" checked>
                    <label for="filter-subclass">SubClass</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-type" checked>
                    <label for="filter-type">Type</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-property-rel" checked>
                    <label for="filter-property-rel">Property</label>
                </div>
            </div>
            <div class="filter-group">
                <b>Layout:</b>
                <div>
                    <input type="radio" id="layout-force" name="layout" checked>
                    <label for="layout-force">Force</label>
                </div>
                <div>
                    <input type="radio" id="layout-radial" name="layout">
                    <label for="layout-radial">Radial</label>
                </div>
            </div>
        </div>
    </div>
    
    <div id="graph"></div>
    <div id="tooltip"></div>
    <div id="info-panel" style="display: none;">
        <h3 id="info-title">Node Information</h3>
        <div id="info-content"></div>
    </div>

    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script>
        // Load data
        d3.json("ontology_data.json").then(function(data) {
            // Create a map for faster node lookup
            const nodeMap = new Map();
            data.nodes.forEach(node => nodeMap.set(node.id, node));
            
            // Set up the SVG
            const width = document.getElementById('graph').clientWidth;
            const height = document.getElementById('graph').clientHeight;
            
            const svg = d3.select("#graph")
                .append("svg")
                .attr("width", width)
                .attr("height", height);
            
            // Create a group for the graph
            const g = svg.append("g");
            
            // Set up zoom behavior
            const zoom = d3.zoom()
                .scaleExtent([0.1, 10])
                .on("zoom", (event) => {
                    g.attr("transform", event.transform);
                });
            
            svg.call(zoom);
            
            // Define node colors
            const colorMap = {
                'Class': '#4CAF50',
                'ObjectProperty': '#2196F3',
                'DatatypeProperty': '#03A9F4',
                'AnnotationProperty': '#00BCD4',
                'Individual': '#FFC107',
                'Datatype': '#9C27B0',
                'Literal': '#E91E63',
                'Entity': '#607D8B'
            };
            
            // Create the force simulation
            const simulation = d3.forceSimulation(data.nodes)
                .force("link", d3.forceLink(data.links)
                    .id(d => d.id)
                    .distance(100))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.1))
                .force("y", d3.forceY(height / 2).strength(0.1));
            
            // Create the links
            const link = g.append("g")
                .attr("class", "links")
                .selectAll("line")
                .data(data.links)
                .enter()
                .append("line")
                .attr("class", d => `link ${d.type}`)
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .attr("stroke-width", 1.5);
            
            // Create the link labels
            const linkLabel = g.append("g")
                .attr("class", "link-labels")
                .selectAll("text")
                .data(data.links.filter(d => d.label && d.type === 'PropertyRelation'))
                .enter()
                .append("text")
                .attr("class", "link-label")
                .attr("font-size", "8px")
                .attr("text-anchor", "middle")
                .text(d => d.label);
            
            // Create the nodes
            const node = g.append("g")
                .attr("class", "nodes")
                .selectAll("circle")
                .data(data.nodes)
                .enter()
                .append("circle")
                .attr("class", d => `node ${d.type}`)
                .attr("r", d => d.type === 'Class' ? 8 : 5)
                .attr("fill", d => colorMap[d.type] || colorMap['Entity'])
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5)
                .on("mouseover", showTooltip)
                .on("mouseout", hideTooltip)
                .on("click", showInfoPanel)
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));
            
            // Create the node labels
            const nodeLabel = g.append("g")
                .attr("class", "node-labels")
                .selectAll("text")
                .data(data.nodes)
                .enter()
                .append("text")
                .attr("class", "node-label")
                .attr("font-size", "10px")
                .attr("text-anchor", "middle")
                .attr("dy", "0.35em")
                .text(d => d.label);
            
            // Set up the simulation tick
            simulation.on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);
                
                linkLabel
                    .attr("x", d => (d.source.x + d.target.x) / 2)
                    .attr("y", d => (d.source.y + d.target.y) / 2);
                
                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);
                
                nodeLabel
                    .attr("x", d => d.x)
                    .attr("y", d => d.y + 15);
            });
            
            // Tooltip functions
            function showTooltip(event, d) {
                const tooltip = d3.select("#tooltip");
                tooltip.style("display", "block")
                    .html(`<strong>${d.label}</strong><br>Type: ${d.type}${d.description ? '<br>Description: ' + d.description : ''}`)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY + 10) + "px");
            }
            
            function hideTooltip() {
                d3.select("#tooltip").style("display", "none");
            }
            
            // Info panel function
            function showInfoPanel(event, d) {
                const infoPanel = d3.select("#info-panel");
                const infoTitle = d3.select("#info-title");
                const infoContent = d3.select("#info-content");
                
                infoTitle.text(d.label);
                
                let content = `<p><strong>Type:</strong> ${d.type}</p>`;
                content += `<p><strong>ID:</strong> ${d.id}</p>`;
                
                if (d.description) {
                    content += `<p><strong>Description:</strong> ${d.description}</p>`;
                }
                
                // Find related nodes
                const relatedLinks = data.links.filter(link => 
                    link.source.id === d.id || link.target.id === d.id);
                
                if (relatedLinks.length > 0) {
                    content += `<p><strong>Relationships:</strong></p><ul>`;
                    
                    relatedLinks.forEach(link => {
                        const isSource = link.source.id === d.id;
                        const otherNode = isSource ? link.target : link.source;
                        const direction = isSource ? "→" : "←";
                        
                        content += `<li>${isSource ? '' : otherNode.label + ' '}${link.label}${direction}${isSource ? ' ' + otherNode.label : ''}</li>`;
                    });
                    
                    content += `</ul>`;
                }
                
                infoContent.html(content);
                infoPanel.style("display", "block");
            }
            
            // Drag functions
            function dragstarted(event, d) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }
            
            function dragged(event, d) {
                d.fx = event.x;
                d.fy = event.y;
            }
            
            function dragended(event, d) {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
            
            // Search functionality
            document.getElementById("search-btn").addEventListener("click", performSearch);
            document.getElementById("search").addEventListener("keyup", function(event) {
                if (event.key === "Enter") {
                    performSearch();
                }
            });
            
            function performSearch() {
                const searchTerm = document.getElementById("search").value.toLowerCase();
                
                if (!searchTerm) {
                    // Reset all nodes and links
                    node.attr("opacity", 1);
                    link.attr("opacity", 0.6);
                    nodeLabel.attr("opacity", 1);
                    linkLabel.attr("opacity", 1);
                    return;
                }
                
                // Find matching nodes
                const matchingNodes = data.nodes.filter(n => 
                    n.label.toLowerCase().includes(searchTerm) || 
                    (n.description && n.description.toLowerCase().includes(searchTerm)));
                
                const matchingNodeIds = new Set(matchingNodes.map(n => n.id));
                
                // Highlight matching nodes and their connections
                node.attr("opacity", d => matchingNodeIds.has(d.id) ? 1 : 0.1);
                nodeLabel.attr("opacity", d => matchingNodeIds.has(d.id) ? 1 : 0.1);
                
                link.attr("opacity", d => 
                    matchingNodeIds.has(d.source.id) || matchingNodeIds.has(d.target.id) ? 0.6 : 0.1);
                
                linkLabel.attr("opacity", d => 
                    matchingNodeIds.has(d.source.id) || matchingNodeIds.has(d.target.id) ? 1 : 0.1);
                
                // If there's exactly one match, center on it
                if (matchingNodes.length === 1) {
                    const d = matchingNodes[0];
                    const transform = d3.zoomIdentity
                        .translate(width/2, height/2)
                        .scale(2)
                        .translate(-d.x, -d.y);
                    
                    svg.transition().duration(750).call(zoom.transform, transform);
                }
            }
            
            // Filter functionality
            document.getElementById("filter-class").addEventListener("change", applyFilters);
            document.getElementById("filter-property").addEventListener("change", applyFilters);
            document.getElementById("filter-individual").addEventListener("change", applyFilters);
            document.getElementById("filter-subclass").addEventListener("change", applyFilters);
            document.getElementById("filter-type").addEventListener("change", applyFilters);
            document.getElementById("filter-property-rel").addEventListener("change", applyFilters);
            
            function applyFilters() {
                const showClass = document.getElementById("filter-class").checked;
                const showProperty = document.getElementById("filter-property").checked;
                const showIndividual = document.getElementById("filter-individual").checked;
                
                const showSubclass = document.getElementById("filter-subclass").checked;
                const showType = document.getElementById("filter-type").checked;
                const showPropertyRel = document.getElementById("filter-property-rel").checked;
                
                // Filter nodes
                node.attr("display", d => {
                    if (d.type === 'Class' && !showClass) return "none";
                    if ((d.type === 'ObjectProperty' || d.type === 'DatatypeProperty' || 
                         d.type === 'AnnotationProperty') && !showProperty) return "none";
                    if (d.type === 'Individual' && !showIndividual) return "none";
                    return "inline";
                });
                
                nodeLabel.attr("display", d => {
                    if (d.type === 'Class' && !showClass) return "none";
                    if ((d.type === 'ObjectProperty' || d.type === 'DatatypeProperty' || 
                         d.type === 'AnnotationProperty') && !showProperty) return "none";
                    if (d.type === 'Individual' && !showIndividual) return "none";
                    return "inline";
                });
                
                // Filter links
                link.attr("display", d => {
                    if (d.type === 'SubClassRelation' && !showSubclass) return "none";
                    if (d.type === 'TypeRelation' && !showType) return "none";
                    if (d.type === 'PropertyRelation' && !showPropertyRel) return "none";
                    return "inline";
                });
                
                linkLabel.attr("display", d => {
                    if (d.type === 'PropertyRelation' && !showPropertyRel) return "none";
                    return "inline";
                });
                
                // Restart simulation to adjust layout
                simulation.alpha(0.3).restart();
            }
            
            // Layout switching
            document.getElementById("layout-force").addEventListener("change", switchLayout);
            document.getElementById("layout-radial").addEventListener("change", switchLayout);
            
            function switchLayout() {
                const useForce = document.getElementById("layout-force").checked;
                const useRadial = document.getElementById("layout-radial").checked;
                
                if (useForce) {
                    simulation
                        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                        .force("charge", d3.forceManyBody().strength(-300))
                        .force("center", d3.forceCenter(width / 2, height / 2))
                        .force("x", d3.forceX(width / 2).strength(0.1))
                        .force("y", d3.forceY(height / 2).strength(0.1))
                        .alpha(1)
                        .restart();
                } else if (useRadial) {
                    // Group nodes by type for radial layout
                    const nodeTypes = [...new Set(data.nodes.map(d => d.type))];
                    const typeGroups = {};
                    nodeTypes.forEach((type, i) => {
                        typeGroups[type] = i;
                    });
                    
                    simulation
                        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                        .force("charge", d3.forceManyBody().strength(-100))
                        .force("r", d3.forceRadial(d => {
                            // Different radius based on node type
                            return 100 + typeGroups[d.type] * 100;
                        }, width / 2, height / 2).strength(1))
                        .force("center", d3.forceCenter(width / 2, height / 2))
                        .alpha(1)
                        .restart();
                }
            }
            
            // Close info panel when clicking elsewhere
            svg.on("click", function(event) {
                if (event.target === this) {
                    d3.select("#info-panel").style("display", "none");
                }
            });
        });
    </script>
</body>
</html>
""")
        
        return output_dir

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with visualization support"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.visualizer = OntologyVisualizer()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def visualize_ontology(self, output_file="ontology_graph.html", use_pyvis=True):
        """Visualize the ontology"""
        if use_pyvis:
            return self.visualizer.visualize_with_pyvis(output_file)
        else:
            return self.visualizer.create_d3_visualization()
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 2. OWL 2 DL Validation Extension

```python
# validation_extension.py - OWL 2 DL validation for AMEDEO Ontology Analyzer

import subprocess
import tempfile
import os
import json
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL
import re
import datetime

class OWL2DLValidator:
    """OWL 2 DL Validator for AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.validation_results = None
        
        # Path to external tools (adjust as needed)
        self.hermit_path = "HermiT.jar"  # Path to HermiT reasoner JAR
        self.owl_api_path = "owlapi.jar"  # Path to OWL API JAR
        
    def set_graph(self, graph):
        """Set the RDFLib graph to validate"""
        self.graph = graph
        
    def _check_type_separation(self):
        """Check for type separation violations (same IRI used for different entity types)"""
        violations = []
        
        # Get all entities by type
        classes = set(self.graph.subjects(RDF.type, OWL.Class))
        individuals = set(self.graph.subjects(RDF.type, OWL.NamedIndividual))
        obj_properties = set(self.graph.subjects(RDF.type, OWL.ObjectProperty))
        data_properties = set(self.graph.subjects(RDF.type, OWL.DatatypeProperty))
        
        # Check for overlaps
        class_individual_overlap = classes.intersection(individuals)
        for entity in class_individual_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both a Class and an Individual",
                    'recommendation': f"Rename either the Class or Individual using IRI {entity}"
                })
        
        class_property_overlap = classes.intersection(obj_properties.union(data_properties))
        for entity in class_property_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both a Class and a Property",
                    'recommendation': f"Rename either the Class or Property using IRI {entity}"
                })
        
        obj_data_property_overlap = obj_properties.intersection(data_properties)
        for entity in obj_data_property_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both an ObjectProperty and a DatatypeProperty",
                    'recommendation': f"Decide whether {entity} should be an ObjectProperty or DatatypeProperty and remove the incorrect type"
                })
        
        return violations
    
    def _check_property_characteristics(self):
        """Check for illegal property characteristic combinations"""
        violations = []
        
        # Get transitive properties
        transitive_props = set(self.graph.subjects(RDF.type, OWL.TransitiveProperty))
        
        # Check for transitive properties used with cardinality restrictions
        for prop in transitive_props:
            # Find all cardinality restrictions using this property
            for s, p, o in self.graph.triples((None, None, None)):
                if isinstance(o, BNode):
                    # Check if this is a cardinality restriction on the transitive property
                    if (o, RDF.type, OWL.Restriction) in self.graph and \
                       (o, OWL.onProperty, prop) in self.graph:
                        # Check for any cardinality restriction
                        for card_type in [OWL.maxCardinality, OWL.cardinality, OWL.maxQualifiedCardinality]:
                            for _, _, card_value in self.graph.triples((o, card_type, None)):
                                try:
                                    if int(card_value) > 0:
                                        violations.append({
                                            'type': 'IllegalPropertyCharacteristic',
                                            'severity': 'Error',
                                            'entity': str(prop),
                                            'message': f"Transitive property {prop} is used with cardinality restriction > 0",
                                            'recommendation': f"Either remove the transitivity characteristic from {prop} or remove the cardinality restriction"
                                        })
                                except (ValueError, TypeError):
                                    pass
        
        return violations
    
    def _check_datatype_restrictions(self):
        """Check for illegal datatype restrictions"""
        violations = []
        
        # This is a simplified check - a complete implementation would need to check
        # for all illegal datatype facet combinations in OWL 2 DL
        
        # Example: Check for custom datatypes with illegal facet combinations
        for s, p, o in self.graph.triples((None, RDF.type, RDFS.Datatype)):
            if isinstance(s, BNode):
                # This is a datatype definition, check for potential issues
                # In a real implementation, we would check for specific illegal facet combinations
                violations.append({
                    'type': 'PotentialDatatypeIssue',
                    'severity': 'Warning',
                    'entity': str(s),
                    'message': f"Custom datatype definition found. Verify it complies with OWL 2 DL restrictions.",
                    'recommendation': "Ensure the datatype definition only uses allowed facet combinations in OWL 2 DL"
                })
        
        return violations
    
    def validate_with_reasoner(self):
        """Validate the ontology using an external OWL reasoner"""
        violations = []
        
        # Save the ontology to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.owl', delete=False) as tmp:
            tmp_path = tmp.name
            self.graph.serialize(destination=tmp_path, format='xml')
        
        try:
            # Run HermiT reasoner via command line
            cmd = [
                'java', '-jar', self.hermit_path,
                '-o', tmp_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Parse the output for inconsistencies or errors
            if "Inconsistent ontology" in result.stdout or "Inconsistent ontology" in result.stderr:
                violations.append({
                    'type': 'InconsistentOntology',
                    'severity': 'Error',
                    'entity': 'Ontology',
                    'message': "The ontology is logically inconsistent",
                    'recommendation': "Check for contradictory axioms or unsatisfiable classes"
                })
            
            # Look for unsatisfiable classes
            unsatisfiable_pattern = r"Class\s+<([^>]+)>\s+is unsatisfiable"
            for match in re.finditer(unsatisfiable_pattern, result.stdout + result.stderr):
                class_iri = match.group(1)
                violations.append({
                    'type': 'UnsatisfiableClass',
                    'severity': 'Error',
                    'entity': class_iri,
                    'message': f"Class {class_iri} is unsatisfiable",
                    'recommendation': f"Check the axioms involving {class_iri} for contradictions"
                })
            
            # Look for other errors
            error_pattern = r"Error:\s+(.+)"
            for match in re.finditer(error_pattern, result.stdout + result.stderr):
                error_msg = match.group(1)
                violations.append({
                    'type': 'ReasonerError',
                    'severity': 'Error',
                    'entity': 'Unknown',
                    'message': error_msg,
                    'recommendation': "Review the error message and fix the related axioms"
                })
            
        except Exception as e:
            violations.append({
                'type': 'ValidationError',
                'severity': 'Error',
                'entity': 'Validator',
                'message': f"Error running reasoner: {str(e)}",
                'recommendation': "Ensure the reasoner is properly installed and accessible"
            })
        finally:
            # Clean up the temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        
        return violations
    
    def validate_owl2_dl(self):
        """Perform comprehensive OWL 2 DL validation"""
        # Collect violations from different checks
        violations = []
        
        # Basic structural checks
        violations.extend(self._check_type_separation())
        violations.extend(self._check_property_characteristics())
        violations.extend(self._check_datatype_restrictions())
        
        # Try reasoner-based validation if external tools are available
        if os.path.exists(self.hermit_path):
            violations.extend(self.validate_with_reasoner())
        
        # Store the results
        self.validation_results = {
            'timestamp': datetime.datetime.now().isoformat(),
            'ontology_iri': self._get_ontology_iri(),
            'total_violations': len(violations),
            'violations': violations,
            'is_compliant': len(violations) == 0
        }
        
        return self.validation_results
    
    def _get_ontology_iri(self):
        """Get the ontology IRI if available"""
        for s, p, o in self.graph.triples((None, RDF.type, OWL.Ontology)):
            return str(s)
        return "Unknown"
    
    def generate_validation_report(self, format='markdown'):
        """Generate a formatted validation report"""
        if not self.validation_results:
            self.validate_owl2_dl()
        
        if format == 'json':
            return json.dumps(self.validation_results, indent=2)
        
        elif format == 'markdown':
            report = []
            
            # Header
            report.append("# OWL 2 DL Compliance Report\n")
            report.append(f"**Ontology:** `{self.validation_results['ontology_iri']}`")
            report.append(f"**Date:** {self.validation_results['timestamp']}")
            report.append(f"**Validator:** AMEDEO OWL 2 DL Validator")
            
            # Status
            if self.validation_results['is_compliant']:
                report.append(f"**Status:** <span style=\"color:green; font-weight:bold;\">COMPLIANT</span>")
            else:
                report.append(f"**Status:** <span style=\"color:red; font-weight:bold;\">NOT COMPLIANT</span>")
            
            report.append(f"**Total Issues:** {self.validation_results['total_violations']}\n")
            report.append("---\n")
            
            # Violations
            if self.validation_results['violations']:
                report.append("### Violations Found:\n")
                
                for i, violation in enumerate(self.validation_results['violations']):
                    report.append(f"**{i+1}. {violation['severity']}: {violation['type']}**")
                    report.append(f"   - **Violation Type:** {violation['type']}")
                    report.append(f"   - **Violating Entity:** `{violation['entity']}`")
                    report.append(f"   - **Message:** {violation['message']}")
                    report.append(f"   - **Recommendation:** {violation['recommendation']}\n")
            else:
                report.append("### No Violations Found\n")
                report.append("The ontology is fully compliant with OWL 2 DL restrictions.\n")
            
            report.append("---\n")
            report.append("*Generated by AMEDEO OWL 2 DL Validator*")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format: {format}")

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with OWL 2 DL validation"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.validator = OWL2DLValidator()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def validate_owl2_dl(self):
        """Validate the ontology against OWL 2 DL restrictions"""
        return self.validator.validate_owl2_dl()
    
    def generate_validation_report(self, format='markdown'):
        """Generate a validation report"""
        return self.validator.generate_validation_report(format)
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 3. Cross-Ontology Mapping Extension

```python
# mapping_extension.py - Cross-ontology mapping support for AMEDEO Ontology Analyzer

import csv
import yaml
import json
import os
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL, SKOS
import pandas as pd
from collections import defaultdict

class OntologyMappingManager:
    """Manager for cross-ontology mappings using SSSOM format"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.mappings = []
        
        # Define common mapping predicates
        self.mapping_predicates = {
            'exactMatch': SKOS.exactMatch,
            'closeMatch': SKOS.closeMatch,
            'relatedMatch': SKOS.relatedMatch,
            'broadMatch': SKOS.broadMatch,
            'narrowMatch': SKOS.narrowMatch,
            'equivalentClass': OWL.equivalentClass,
            'equivalentProperty': OWL.equivalentProperty,
            'sameAs': OWL.sameAs,
            'subClassOf': RDFS.subClassOf,
            'subPropertyOf': RDFS.subPropertyOf
        }
    
    def set_graph(self, graph):
        """Set the RDFLib graph"""
        self.graph = graph
    
    def extract_mappings_from_graph(self):
        """Extract existing mappings from the ontology graph"""
        self.mappings = []
        
        # Extract mappings for each predicate type
        for pred_name, pred_uri in self.mapping_predicates.items():
            for s, p, o in self.graph.triples((None, pred_uri, None)):
                if isinstance(s, URIRef) and isinstance(o, URIRef):
                    # Get labels if available
                    s_label = self._get_entity_label(s)
                    o_label = self._get_entity_label(o)
                    
                    # Determine entity types
                    s_type = self._get_entity_type(s)
                    o_type = self._get_entity_type(o)
                    
                    # Extract source and target ontology IRIs
                    s_ontology = self._extract_ontology_iri(s)
                    o_ontology = self._extract_ontology_iri(o)
                    
                    mapping = {
                        'subject_id': str(s),
                        'subject_label': s_label,
                        'subject_category': s_type,
                        'subject_source': s_ontology,
                        'predicate_id': str(pred_uri),
                        'predicate_label': pred_name,
                        'object_id': str(o),
                        'object_label': o_label,
                        'object_category': o_type,
                        'object_source': o_ontology,
                        'mapping_provider': 'AMEDEO Ontology Analyzer',
                        'confidence': 1.0,  # Default confidence for explicit mappings
                        'comment': None
                    }
                    
                    self.mappings.append(mapping)
        
        return self.mappings
    
    def _get_entity_label(self, entity):
        """Get the label for an entity"""
        for _, _, label in self.graph.triples((entity, RDFS.label, None)):
            return str(label)
        return None
    
    def _get_entity_type(self, entity):
        """Determine the type of an entity"""
        if (entity, RDF.type, OWL.Class) in self.graph:
            return 'Class'
        elif (entity, RDF.type, OWL.ObjectProperty) in self.graph:
            return 'ObjectProperty'
        elif (entity, RDF.type, OWL.DatatypeProperty) in self.graph:
            return 'DatatypeProperty'
        elif (entity, RDF.type, OWL.NamedIndividual) in self.graph:
            return 'Individual'
        return 'Entity'
    
    def _extract_ontology_iri(self, entity_iri):
        """Extract the ontology IRI from an entity IRI"""
        iri = str(entity_iri)
        
        # Try to extract namespace
        if '#' in iri:
            return iri.split('#')[0]
        
        # If no fragment identifier, use the last directory
        parts = iri.split('/')
        if len(parts) > 3:  # At least http://domain/path
            return '/'.join(parts[:-1])
        
        return iri
    
    def import_sssom_mappings(self, file_path):
        """Import mappings from an SSSOM file (TSV format)"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"SSSOM file not found: {file_path}")
        
        # Determine file format based on extension
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.tsv':
            # Read TSV file
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    self.mappings.append(row)
        
        elif ext == '.yaml' or ext == '.yml':
            # Read YAML file
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
                if 'mappings' in data:
                    self.mappings.extend(data['mappings'])
                else:
                    self.mappings.extend(data)
        
        elif ext == '.json':
            # Read JSON file
            with open(file_path, 'r') as f:
                data = json.load(f)
                if 'mappings' in data:
                    self.mappings.extend(data['mappings'])
                else:
                    self.mappings.extend(data)
        
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        
        return self.mappings
    
    def export_sssom_mappings(self, file_path, format='tsv'):
        """Export mappings to an SSSOM file"""
        if not self.mappings:
            self.extract_mappings_from_graph()
        
        if format == 'tsv':
            # Write TSV file
            with open(file_path, 'w', newline='') as f:
                fieldnames = [
                    'subject_id', 'subject_label', 'subject_category', 'subject_source',
                    'predicate_id', 'predicate_label',
                    'object_id', 'object_label', 'object_category', 'object_source',
                    'mapping_provider', 'confidence', 'comment'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                for mapping in self.mappings:
                    writer.writerow(mapping)
        
        elif format == 'yaml':
            # Write YAML file
            with open(file_path, 'w') as f:
                yaml.dump({'mappings': self.mappings}, f)
        
        elif format == 'json':
            # Write JSON file
            with open(file_path, 'w') as f:
                json.dump({'mappings': self.mappings}, f, indent=2)
        
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        return file_path
    
    def add_mapping(self, subject_id, object_id, predicate='exactMatch', confidence=1.0, comment=None):
        """Add a new mapping between two entities"""
        # Convert string predicate to URI if needed
        if isinstance(predicate, str) and predicate in self.mapping_predicates:
            predicate_uri = self.mapping_predicates[predicate]
            predicate_label = predicate
        else:
            predicate_uri = predicate
            predicate_label = str(predicate).split('#')[-1] if '#' in str(predicate) else str(predicate).split('/')[-1]
        
        # Convert string IDs to URIRefs if needed
        subject = URIRef(subject_id) if isinstance(subject_id, str) else subject_id
        object = URIRef(object_id) if isinstance(object_id, str) else object_id
        
        # Get entity information
        subject_label = self._get_entity_label(subject)
        object_label = self._get_entity_label(object)
        subject_type = self._get_entity_type(subject)
        object_type = self._get_entity_type(object)
        subject_source = self._extract_ontology_iri(subject)
        object_source = self._extract_ontology_iri(object)
        
        # Create the mapping
        mapping = {
            'subject_id': str(subject),
            'subject_label': subject_label,
            'subject_category': subject_type,
            'subject_source': subject_source,
            'predicate_id': str(predicate_uri),
            'predicate_label': predicate_label,
            'object_id': str(object),
            'object_label': object_label,
            'object_category': object_type,
            'object_source': object_source,
            'mapping_provider': 'AMEDEO Ontology Analyzer',
            'confidence': confidence,
            'comment': comment
        }
        
        # Add to mappings list
        self.mappings.append(mapping)
        
        # Add to graph if available
        if self.graph:
            self.graph.add((subject, predicate_uri, object))
        
        return mapping
    
    def remove_mapping(self, subject_id, object_id, predicate=None):
        """Remove a mapping between two entities"""
        subject = URIRef(subject_id) if isinstance(subject_id, str) else subject_id
        object = URIRef(object_id) if isinstance(object_id, str) else object_id
        
        # Remove from graph if available
        if self.graph:
            if predicate:
                predicate_uri = self.mapping_predicates.get(predicate, predicate)
                self.graph.remove((subject, predicate_uri, object))
            else:
                # Remove all predicates between subject and object
                for s, p, o in self.graph.triples((subject, None, object)):
                    if p in self.mapping_predicates.values():
                        self.graph.remove((s, p, o))
        
        # Remove from mappings list
        self.mappings = [m for m in self.mappings if not (
            m['subject_id'] == str(subject) and 
            m['object_id'] == str(object) and 
            (predicate is None or m['predicate_label'] == predicate)
        )]
        
        return True
    
    def get_mappings_by_entity(self, entity_id):
        """Get all mappings involving a specific entity"""
        entity_str = str(entity_id)
        return [m for m in self.mappings if m['subject_id'] == entity_str or m['object_id'] == entity_str]
    
    def get_mappings_by_ontology(self, ontology_iri):
        """Get all mappings involving a specific ontology"""
        return [m for m in self.mappings if m['subject_source'] == ontology_iri or m['object_source'] == ontology_iri]
    
    def get_mappings_by_predicate(self, predicate):
        """Get all mappings using a specific predicate"""
        if isinstance(predicate, str) and predicate in self.mapping_predicates:
            predicate_uri = str(self.mapping_predicates[predicate])
        else:
            predicate_uri = str(predicate)
        
        return [m for m in self.mappings if m['predicate_id'] == predicate_uri]
    
    def analyze_mappings(self):
        """Analyze the mappings to generate statistics and insights"""
        if not self.mappings:
            return {"error": "No mappings available"}
        
        analysis = {
            'total_mappings': len(self.mappings),
            'ontologies_involved': set(),
            'predicate_counts': defaultdict(int),
            'entity_type_pairs': defaultdict(int),
            'confidence_distribution': defaultdict(int),
            'most_connected_entities': []
        }
        
        # Entity connection counts
        entity_connections = defaultdict(int)
        
        for mapping in self.mappings:
            # Count ontologies
            analysis['ontologies_involved'].add(mapping['subject_source'])
            analysis['ontologies_involved'].add(mapping['object_source'])
            
            # Count predicates
            analysis['predicate_counts'][mapping['predicate_label']] += 1
            
            # Count entity type pairs
            type_pair = f"{mapping['subject_category']}-{mapping['object_category']}"
            analysis['entity_type_pairs'][type_pair] += 1
            
            # Count confidence distribution (rounded to nearest 0.1)
            if 'confidence' in mapping and mapping['confidence'] is not None:
                conf = round(float(mapping['confidence']) * 10) / 10
                analysis['confidence_distribution'][conf] += 1
            
            # Count entity connections
            entity_connections[mapping['subject_id']] += 1
            entity_connections[mapping['object_id']] += 1
        
        # Convert sets to lists for JSON serialization
        analysis['ontologies_involved'] = list(analysis['ontologies_involved'])## GenAI Proposal Status Disclaimer

*This document is a GenAI-generated proposal and has not been validated by domain experts. The implementation details are theoretical and would need formal review and validation by specialists in ontological engineering and semantic web technologies.*

# AMEDEO Ontology Analyzer: Advanced Extensions

Based on your detailed information, I've developed a comprehensive implementation plan for extending the AMEDEO Ontology Analyzer with visualization capabilities, validation tools, cross-ontology mapping support, federation anchor management, and TokenFlow pipeline integration.

## 1. Ontology Visualization Extension

```python
# visualization_extension.py - Visualization capabilities for AMEDEO Ontology Analyzer

import networkx as nx
from pyvis.network import Network
import json
import os
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL

class OntologyVisualizer:
    """Visualization tools for AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.nodes_data = []
        self.edges_data = []
        
    def set_graph(self, graph):
        """Set the RDFLib graph to visualize"""
        self.graph = graph
        
    def prepare_visualization_data(self, include_individuals=True, include_literals=False, 
                                  include_datatypes=False, max_nodes=1000):
        """Extract nodes and edges from the ontology graph for visualization"""
        self.nodes_data = []
        self.edges_data = []
        
        # Track processed nodes to avoid duplicates
        processed_nodes = set()
        
        # Helper function to get a short name for display
        def get_short_name(uri):
            if isinstance(uri, URIRef):
                if "#" in uri:
                    return uri.split("#")[-1]
                return uri.split("/")[-1]
            return str(uri)
        
        # Helper function to get node type
        def get_node_type(node):
            if isinstance(node, Literal):
                return "Literal"
            elif isinstance(node, BNode):
                return "BlankNode"
            
            # Check if it's a class
            if (node, RDF.type, OWL.Class) in self.graph:
                return "Class"
            # Check if it's an individual
            elif (node, RDF.type, OWL.NamedIndividual) in self.graph:
                return "Individual"
            # Check if it's an object property
            elif (node, RDF.type, OWL.ObjectProperty) in self.graph:
                return "ObjectProperty"
            # Check if it's a datatype property
            elif (node, RDF.type, OWL.DatatypeProperty) in self.graph:
                return "DatatypeProperty"
            # Check if it's an annotation property
            elif (node, RDF.type, OWL.AnnotationProperty) in self.graph:
                return "AnnotationProperty"
            # Check if it's a datatype
            elif (node, RDF.type, RDFS.Datatype) in self.graph:
                return "Datatype"
            
            # Default
            return "Entity"
        
        # Add classes
        for s in self.graph.subjects(RDF.type, OWL.Class):
            if isinstance(s, URIRef) and s not in processed_nodes:
                node_id = str(s)
                label = get_short_name(s)
                
                # Get description if available
                description = None
                for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                    description = str(comment)
                    break
                
                self.nodes_data.append({
                    'id': node_id,
                    'label': label,
                    'type': 'Class',
                    'description': description
                })
                processed_nodes.add(s)
        
        # Add properties
        for prop_type in [OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty]:
            for s in self.graph.subjects(RDF.type, prop_type):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    # Get description if available
                    description = None
                    for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                        description = str(comment)
                        break
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': get_node_type(s),
                        'description': description
                    })
                    processed_nodes.add(s)
        
        # Add individuals if requested
        if include_individuals:
            for s in self.graph.subjects(RDF.type, OWL.NamedIndividual):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    # Get description if available
                    description = None
                    for _, _, comment in self.graph.triples((s, RDFS.comment, None)):
                        description = str(comment)
                        break
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Individual',
                        'description': description
                    })
                    processed_nodes.add(s)
        
        # Add datatypes if requested
        if include_datatypes:
            for s in self.graph.subjects(RDF.type, RDFS.Datatype):
                if isinstance(s, URIRef) and s not in processed_nodes:
                    node_id = str(s)
                    label = get_short_name(s)
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Datatype',
                        'description': None
                    })
                    processed_nodes.add(s)
        
        # Add literals if requested (usually not recommended for large ontologies)
        if include_literals:
            for s, p, o in self.graph:
                if isinstance(o, Literal) and o not in processed_nodes:
                    node_id = f"lit_{len(processed_nodes)}"  # Generate unique ID
                    label = str(o)[:20] + "..." if len(str(o)) > 20 else str(o)
                    
                    self.nodes_data.append({
                        'id': node_id,
                        'label': label,
                        'type': 'Literal',
                        'description': None
                    })
                    processed_nodes.add(o)
        
        # Limit nodes if necessary
        if len(self.nodes_data) > max_nodes:
            self.nodes_data = self.nodes_data[:max_nodes]
            processed_nodes = {node['id'] for node in self.nodes_data}
        
        # Add edges
        edge_id = 0
        
        # Add subclass relationships
        for s, p, o in self.graph.triples((None, RDFS.subClassOf, None)):
            if (isinstance(s, URIRef) and isinstance(o, URIRef) and 
                str(s) in processed_nodes and str(o) in processed_nodes):
                self.edges_data.append({
                    'id': f"edge_{edge_id}",
                    'source': str(s),
                    'target': str(o),
                    'label': 'subClassOf',
                    'type': 'SubClassRelation'
                })
                edge_id += 1
        
        # Add type relationships for individuals
        if include_individuals:
            for s, p, o in self.graph.triples((None, RDF.type, None)):
                if (isinstance(s, URIRef) and isinstance(o, URIRef) and 
                    str(s) in processed_nodes and str(o) in processed_nodes and
                    o != OWL.Class and o != OWL.ObjectProperty and 
                    o != OWL.DatatypeProperty and o != OWL.NamedIndividual):
                    self.edges_data.append({
                        'id': f"edge_{edge_id}",
                        'source': str(s),
                        'target': str(o),
                        'label': 'type',
                        'type': 'TypeRelation'
                    })
                    edge_id += 1
        
        # Add property relationships
        for s, p, o in self.graph:
            if (isinstance(p, URIRef) and p != RDF.type and p != RDFS.subClassOf and
                str(s) in processed_nodes and 
                (isinstance(o, URIRef) and str(o) in processed_nodes)):
                self.edges_data.append({
                    'id': f"edge_{edge_id}",
                    'source': str(s),
                    'target': str(o),
                    'label': get_short_name(p),
                    'type': 'PropertyRelation'
                })
                edge_id += 1
        
        return self.nodes_data, self.edges_data
    
    def visualize_with_pyvis(self, output_file="ontology_graph.html", height="750px", width="100%",
                           physics=True, show_buttons=True):
        """Generate an interactive visualization using Pyvis"""
        if not self.nodes_data:
            self.prepare_visualization_data()
        
        # Create network
        net = Network(notebook=False, height=height, width=width, heading="AMEDEO Ontology Graph")
        
        # Define node colors based on type
        color_map = {
            'Class': '#4CAF50',  # Green
            'ObjectProperty': '#2196F3',  # Blue
            'DatatypeProperty': '#03A9F4',  # Light Blue
            'AnnotationProperty': '#00BCD4',  # Cyan
            'Individual': '#FFC107',  # Amber
            'Datatype': '#9C27B0',  # Purple
            'Literal': '#E91E63',  # Pink
            'Entity': '#607D8B'  # Blue Grey
        }
        
        # Add nodes
        for node in self.nodes_data:
            color = color_map.get(node['type'], '#607D8B')
            shape = 'box' if node['type'] == 'Class' else 'dot'
            
            title = f"Type: {node['type']}"
            if node['description']:
                title += f"\nDescription: {node['description']}"
            
            net.add_node(
                node['id'],
                label=node['label'],
                title=title,
                color=color,
                shape=shape,
                group=node['type']
            )
        
        # Add edges
        for edge in self.edges_data:
            net.add_edge(
                edge['source'],
                edge['target'],
                title=edge['label'],
                label=edge['label'] if edge['type'] == 'PropertyRelation' else '',
                arrows='to'
            )
        
        # Configure options
        net.toggle_physics(physics)
        if show_buttons:
            net.show_buttons(filter_=['physics', 'nodes', 'edges'])
        
        # Set other options
        net.set_options("""
        var options = {
            "nodes": {
                "font": {
                    "size": 12
                }
            },
            "edges": {
                "color": {
                    "inherit": true
                },
                "smooth": {
                    "enabled": false
                }
            },
            "physics": {
                "hierarchicalRepulsion": {
                    "centralGravity": 0.5,
                    "springLength": 150,
                    "springConstant": 0.01,
                    "nodeDistance": 120,
                    "damping": 0.09
                },
                "solver": "hierarchicalRepulsion"
            }
        }
        """)
        
        # Save to file
        net.save_graph(output_file)
        return output_file
    
    def export_for_d3(self, output_file="ontology_d3.json"):
        """Export the graph data for use with D3.js"""
        if not self.nodes_data:
            self.prepare_visualization_data()
        
        # Create the data structure expected by D3
        d3_data = {
            "nodes": self.nodes_data,
            "links": [{
                "source": edge["source"],
                "target": edge["target"],
                "label": edge["label"],
                "type": edge["type"]
            } for edge in self.edges_data]
        }
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(d3_data, f, indent=2)
        
        return output_file
    
    def create_d3_visualization(self, output_dir="d3_visualization"):
        """Create a complete D3.js visualization package"""
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Export data
        data_file = os.path.join(output_dir, "ontology_data.json")
        self.export_for_d3(data_file)
        
        # Create HTML file
        html_file = os.path.join(output_dir, "index.html")
        with open(html_file, 'w') as f:
            f.write("""&lt;!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMEDEO Ontology Visualization</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        #controls {
            padding: 10px;
            background-color: #f0f0f0;
            border-bottom: 1px solid #ccc;
        }
        #search-container {
            margin-bottom: 10px;
        }
        #search {
            padding: 5px;
            width: 300px;
        }
        #filters {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .filter-group {
            margin-right: 15px;
        }
        #graph {
            flex-grow: 1;
            border-top: 1px solid #ccc;
            overflow: hidden;
        }
        .node {
            cursor: pointer;
        }
        .node text {
            font-size: 10px;
        }
        .link {
            stroke: #999;
            stroke-opacity: 0.6;
        }
        #tooltip {
            position: absolute;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            display: none;
            z-index: 1000;
            max-width: 300px;
        }
        #info-panel {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 300px;
            max-height: 80%;
            overflow-y: auto;
            z-index: 900;
        }
    </style>
</head>
<body>
    <div id="controls">
        <div id="search-container">
            <input type="text" id="search" placeholder="Search nodes...">
            <button id="search-btn">Search</button>
        </div>
        <div id="filters">
            <div class="filter-group">
                <b>Node Types:</b>
                <div>
                    <input type="checkbox" id="filter-class" checked>
                    <label for="filter-class">Classes</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-property" checked>
                    <label for="filter-property">Properties</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-individual" checked>
                    <label for="filter-individual">Individuals</label>
                </div>
            </div>
            <div class="filter-group">
                <b>Edge Types:</b>
                <div>
                    <input type="checkbox" id="filter-subclass" checked>
                    <label for="filter-subclass">SubClass</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-type" checked>
                    <label for="filter-type">Type</label>
                </div>
                <div>
                    <input type="checkbox" id="filter-property-rel" checked>
                    <label for="filter-property-rel">Property</label>
                </div>
            </div>
            <div class="filter-group">
                <b>Layout:</b>
                <div>
                    <input type="radio" id="layout-force" name="layout" checked>
                    <label for="layout-force">Force</label>
                </div>
                <div>
                    <input type="radio" id="layout-radial" name="layout">
                    <label for="layout-radial">Radial</label>
                </div>
            </div>
        </div>
    </div>
    
    <div id="graph"></div>
    <div id="tooltip"></div>
    <div id="info-panel" style="display: none;">
        <h3 id="info-title">Node Information</h3>
        <div id="info-content"></div>
    </div>

    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script>
        // Load data
        d3.json("ontology_data.json").then(function(data) {
            // Create a map for faster node lookup
            const nodeMap = new Map();
            data.nodes.forEach(node => nodeMap.set(node.id, node));
            
            // Set up the SVG
            const width = document.getElementById('graph').clientWidth;
            const height = document.getElementById('graph').clientHeight;
            
            const svg = d3.select("#graph")
                .append("svg")
                .attr("width", width)
                .attr("height", height);
            
            // Create a group for the graph
            const g = svg.append("g");
            
            // Set up zoom behavior
            const zoom = d3.zoom()
                .scaleExtent([0.1, 10])
                .on("zoom", (event) => {
                    g.attr("transform", event.transform);
                });
            
            svg.call(zoom);
            
            // Define node colors
            const colorMap = {
                'Class': '#4CAF50',
                'ObjectProperty': '#2196F3',
                'DatatypeProperty': '#03A9F4',
                'AnnotationProperty': '#00BCD4',
                'Individual': '#FFC107',
                'Datatype': '#9C27B0',
                'Literal': '#E91E63',
                'Entity': '#607D8B'
            };
            
            // Create the force simulation
            const simulation = d3.forceSimulation(data.nodes)
                .force("link", d3.forceLink(data.links)
                    .id(d => d.id)
                    .distance(100))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.1))
                .force("y", d3.forceY(height / 2).strength(0.1));
            
            // Create the links
            const link = g.append("g")
                .attr("class", "links")
                .selectAll("line")
                .data(data.links)
                .enter()
                .append("line")
                .attr("class", d => `link ${d.type}`)
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .attr("stroke-width", 1.5);
            
            // Create the link labels
            const linkLabel = g.append("g")
                .attr("class", "link-labels")
                .selectAll("text")
                .data(data.links.filter(d => d.label && d.type === 'PropertyRelation'))
                .enter()
                .append("text")
                .attr("class", "link-label")
                .attr("font-size", "8px")
                .attr("text-anchor", "middle")
                .text(d => d.label);
            
            // Create the nodes
            const node = g.append("g")
                .attr("class", "nodes")
                .selectAll("circle")
                .data(data.nodes)
                .enter()
                .append("circle")
                .attr("class", d => `node ${d.type}`)
                .attr("r", d => d.type === 'Class' ? 8 : 5)
                .attr("fill", d => colorMap[d.type] || colorMap['Entity'])
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5)
                .on("mouseover", showTooltip)
                .on("mouseout", hideTooltip)
                .on("click", showInfoPanel)
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));
            
            // Create the node labels
            const nodeLabel = g.append("g")
                .attr("class", "node-labels")
                .selectAll("text")
                .data(data.nodes)
                .enter()
                .append("text")
                .attr("class", "node-label")
                .attr("font-size", "10px")
                .attr("text-anchor", "middle")
                .attr("dy", "0.35em")
                .text(d => d.label);
            
            // Set up the simulation tick
            simulation.on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);
                
                linkLabel
                    .attr("x", d => (d.source.x + d.target.x) / 2)
                    .attr("y", d => (d.source.y + d.target.y) / 2);
                
                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);
                
                nodeLabel
                    .attr("x", d => d.x)
                    .attr("y", d => d.y + 15);
            });
            
            // Tooltip functions
            function showTooltip(event, d) {
                const tooltip = d3.select("#tooltip");
                tooltip.style("display", "block")
                    .html(`<strong>${d.label}</strong><br>Type: ${d.type}${d.description ? '<br>Description: ' + d.description : ''}`)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY + 10) + "px");
            }
            
            function hideTooltip() {
                d3.select("#tooltip").style("display", "none");
            }
            
            // Info panel function
            function showInfoPanel(event, d) {
                const infoPanel = d3.select("#info-panel");
                const infoTitle = d3.select("#info-title");
                const infoContent = d3.select("#info-content");
                
                infoTitle.text(d.label);
                
                let content = `<p><strong>Type:</strong> ${d.type}</p>`;
                content += `<p><strong>ID:</strong> ${d.id}</p>`;
                
                if (d.description) {
                    content += `<p><strong>Description:</strong> ${d.description}</p>`;
                }
                
                // Find related nodes
                const relatedLinks = data.links.filter(link => 
                    link.source.id === d.id || link.target.id === d.id);
                
                if (relatedLinks.length > 0) {
                    content += `<p><strong>Relationships:</strong></p><ul>`;
                    
                    relatedLinks.forEach(link => {
                        const isSource = link.source.id === d.id;
                        const otherNode = isSource ? link.target : link.source;
                        const direction = isSource ? "→" : "←";
                        
                        content += `<li>${isSource ? '' : otherNode.label + ' '}${link.label}${direction}${isSource ? ' ' + otherNode.label : ''}</li>`;
                    });
                    
                    content += `</ul>`;
                }
                
                infoContent.html(content);
                infoPanel.style("display", "block");
            }
            
            // Drag functions
            function dragstarted(event, d) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }
            
            function dragged(event, d) {
                d.fx = event.x;
                d.fy = event.y;
            }
            
            function dragended(event, d) {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
            
            // Search functionality
            document.getElementById("search-btn").addEventListener("click", performSearch);
            document.getElementById("search").addEventListener("keyup", function(event) {
                if (event.key === "Enter") {
                    performSearch();
                }
            });
            
            function performSearch() {
                const searchTerm = document.getElementById("search").value.toLowerCase();
                
                if (!searchTerm) {
                    // Reset all nodes and links
                    node.attr("opacity", 1);
                    link.attr("opacity", 0.6);
                    nodeLabel.attr("opacity", 1);
                    linkLabel.attr("opacity", 1);
                    return;
                }
                
                // Find matching nodes
                const matchingNodes = data.nodes.filter(n => 
                    n.label.toLowerCase().includes(searchTerm) || 
                    (n.description && n.description.toLowerCase().includes(searchTerm)));
                
                const matchingNodeIds = new Set(matchingNodes.map(n => n.id));
                
                // Highlight matching nodes and their connections
                node.attr("opacity", d => matchingNodeIds.has(d.id) ? 1 : 0.1);
                nodeLabel.attr("opacity", d => matchingNodeIds.has(d.id) ? 1 : 0.1);
                
                link.attr("opacity", d => 
                    matchingNodeIds.has(d.source.id) || matchingNodeIds.has(d.target.id) ? 0.6 : 0.1);
                
                linkLabel.attr("opacity", d => 
                    matchingNodeIds.has(d.source.id) || matchingNodeIds.has(d.target.id) ? 1 : 0.1);
                
                // If there's exactly one match, center on it
                if (matchingNodes.length === 1) {
                    const d = matchingNodes[0];
                    const transform = d3.zoomIdentity
                        .translate(width/2, height/2)
                        .scale(2)
                        .translate(-d.x, -d.y);
                    
                    svg.transition().duration(750).call(zoom.transform, transform);
                }
            }
            
            // Filter functionality
            document.getElementById("filter-class").addEventListener("change", applyFilters);
            document.getElementById("filter-property").addEventListener("change", applyFilters);
            document.getElementById("filter-individual").addEventListener("change", applyFilters);
            document.getElementById("filter-subclass").addEventListener("change", applyFilters);
            document.getElementById("filter-type").addEventListener("change", applyFilters);
            document.getElementById("filter-property-rel").addEventListener("change", applyFilters);
            
            function applyFilters() {
                const showClass = document.getElementById("filter-class").checked;
                const showProperty = document.getElementById("filter-property").checked;
                const showIndividual = document.getElementById("filter-individual").checked;
                
                const showSubclass = document.getElementById("filter-subclass").checked;
                const showType = document.getElementById("filter-type").checked;
                const showPropertyRel = document.getElementById("filter-property-rel").checked;
                
                // Filter nodes
                node.attr("display", d => {
                    if (d.type === 'Class' && !showClass) return "none";
                    if ((d.type === 'ObjectProperty' || d.type === 'DatatypeProperty' || 
                         d.type === 'AnnotationProperty') && !showProperty) return "none";
                    if (d.type === 'Individual' && !showIndividual) return "none";
                    return "inline";
                });
                
                nodeLabel.attr("display", d => {
                    if (d.type === 'Class' && !showClass) return "none";
                    if ((d.type === 'ObjectProperty' || d.type === 'DatatypeProperty' || 
                         d.type === 'AnnotationProperty') && !showProperty) return "none";
                    if (d.type === 'Individual' && !showIndividual) return "none";
                    return "inline";
                });
                
                // Filter links
                link.attr("display", d => {
                    if (d.type === 'SubClassRelation' && !showSubclass) return "none";
                    if (d.type === 'TypeRelation' && !showType) return "none";
                    if (d.type === 'PropertyRelation' && !showPropertyRel) return "none";
                    return "inline";
                });
                
                linkLabel.attr("display", d => {
                    if (d.type === 'PropertyRelation' && !showPropertyRel) return "none";
                    return "inline";
                });
                
                // Restart simulation to adjust layout
                simulation.alpha(0.3).restart();
            }
            
            // Layout switching
            document.getElementById("layout-force").addEventListener("change", switchLayout);
            document.getElementById("layout-radial").addEventListener("change", switchLayout);
            
            function switchLayout() {
                const useForce = document.getElementById("layout-force").checked;
                const useRadial = document.getElementById("layout-radial").checked;
                
                if (useForce) {
                    simulation
                        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                        .force("charge", d3.forceManyBody().strength(-300))
                        .force("center", d3.forceCenter(width / 2, height / 2))
                        .force("x", d3.forceX(width / 2).strength(0.1))
                        .force("y", d3.forceY(height / 2).strength(0.1))
                        .alpha(1)
                        .restart();
                } else if (useRadial) {
                    // Group nodes by type for radial layout
                    const nodeTypes = [...new Set(data.nodes.map(d => d.type))];
                    const typeGroups = {};
                    nodeTypes.forEach((type, i) => {
                        typeGroups[type] = i;
                    });
                    
                    simulation
                        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                        .force("charge", d3.forceManyBody().strength(-100))
                        .force("r", d3.forceRadial(d => {
                            // Different radius based on node type
                            return 100 + typeGroups[d.type] * 100;
                        }, width / 2, height / 2).strength(1))
                        .force("center", d3.forceCenter(width / 2, height / 2))
                        .alpha(1)
                        .restart();
                }
            }
            
            // Close info panel when clicking elsewhere
            svg.on("click", function(event) {
                if (event.target === this) {
                    d3.select("#info-panel").style("display", "none");
                }
            });
        });
    </script>
</body>
</html>
""")
        
        return output_dir

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with visualization support"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.visualizer = OntologyVisualizer()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.visualizer.set_graph(self.base_analyzer.graph)
    
    def visualize_ontology(self, output_file="ontology_graph.html", use_pyvis=True):
        """Visualize the ontology"""
        if use_pyvis:
            return self.visualizer.visualize_with_pyvis(output_file)
        else:
            return self.visualizer.create_d3_visualization()
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 2. OWL 2 DL Validation Extension

```python
# validation_extension.py - OWL 2 DL validation for AMEDEO Ontology Analyzer

import subprocess
import tempfile
import os
import json
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL
import re
import datetime

class OWL2DLValidator:
    """OWL 2 DL Validator for AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.validation_results = None
        
        # Path to external tools (adjust as needed)
        self.hermit_path = "HermiT.jar"  # Path to HermiT reasoner JAR
        self.owl_api_path = "owlapi.jar"  # Path to OWL API JAR
        
    def set_graph(self, graph):
        """Set the RDFLib graph to validate"""
        self.graph = graph
        
    def _check_type_separation(self):
        """Check for type separation violations (same IRI used for different entity types)"""
        violations = []
        
        # Get all entities by type
        classes = set(self.graph.subjects(RDF.type, OWL.Class))
        individuals = set(self.graph.subjects(RDF.type, OWL.NamedIndividual))
        obj_properties = set(self.graph.subjects(RDF.type, OWL.ObjectProperty))
        data_properties = set(self.graph.subjects(RDF.type, OWL.DatatypeProperty))
        
        # Check for overlaps
        class_individual_overlap = classes.intersection(individuals)
        for entity in class_individual_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both a Class and an Individual",
                    'recommendation': f"Rename either the Class or Individual using IRI {entity}"
                })
        
        class_property_overlap = classes.intersection(obj_properties.union(data_properties))
        for entity in class_property_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both a Class and a Property",
                    'recommendation': f"Rename either the Class or Property using IRI {entity}"
                })
        
        obj_data_property_overlap = obj_properties.intersection(data_properties)
        for entity in obj_data_property_overlap:
            if isinstance(entity, URIRef):
                violations.append({
                    'type': 'TypeSeparationViolation',
                    'severity': 'Error',
                    'entity': str(entity),
                    'message': f"Entity {entity} is used as both an ObjectProperty and a DatatypeProperty",
                    'recommendation': f"Decide whether {entity} should be an ObjectProperty or DatatypeProperty and remove the incorrect type"
                })
        
        return violations
    
    def _check_property_characteristics(self):
        """Check for illegal property characteristic combinations"""
        violations = []
        
        # Get transitive properties
        transitive_props = set(self.graph.subjects(RDF.type, OWL.TransitiveProperty))
        
        # Check for transitive properties used with cardinality restrictions
        for prop in transitive_props:
            # Find all cardinality restrictions using this property
            for s, p, o in self.graph.triples((None, None, None)):
                if isinstance(o, BNode):
                    # Check if this is a cardinality restriction on the transitive property
                    if (o, RDF.type, OWL.Restriction) in self.graph and \
                       (o, OWL.onProperty, prop) in self.graph:
                        # Check for any cardinality restriction
                        for card_type in [OWL.maxCardinality, OWL.cardinality, OWL.maxQualifiedCardinality]:
                            for _, _, card_value in self.graph.triples((o, card_type, None)):
                                try:
                                    if int(card_value) > 0:
                                        violations.append({
                                            'type': 'IllegalPropertyCharacteristic',
                                            'severity': 'Error',
                                            'entity': str(prop),
                                            'message': f"Transitive property {prop} is used with cardinality restriction > 0",
                                            'recommendation': f"Either remove the transitivity characteristic from {prop} or remove the cardinality restriction"
                                        })
                                except (ValueError, TypeError):
                                    pass
        
        return violations
    
    def _check_datatype_restrictions(self):
        """Check for illegal datatype restrictions"""
        violations = []
        
        # This is a simplified check - a complete implementation would need to check
        # for all illegal datatype facet combinations in OWL 2 DL
        
        # Example: Check for custom datatypes with illegal facet combinations
        for s, p, o in self.graph.triples((None, RDF.type, RDFS.Datatype)):
            if isinstance(s, BNode):
                # This is a datatype definition, check for potential issues
                # In a real implementation, we would check for specific illegal facet combinations
                violations.append({
                    'type': 'PotentialDatatypeIssue',
                    'severity': 'Warning',
                    'entity': str(s),
                    'message': f"Custom datatype definition found. Verify it complies with OWL 2 DL restrictions.",
                    'recommendation': "Ensure the datatype definition only uses allowed facet combinations in OWL 2 DL"
                })
        
        return violations
    
    def validate_with_reasoner(self):
        """Validate the ontology using an external OWL reasoner"""
        violations = []
        
        # Save the ontology to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.owl', delete=False) as tmp:
            tmp_path = tmp.name
            self.graph.serialize(destination=tmp_path, format='xml')
        
        try:
            # Run HermiT reasoner via command line
            cmd = [
                'java', '-jar', self.hermit_path,
                '-o', tmp_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Parse the output for inconsistencies or errors
            if "Inconsistent ontology" in result.stdout or "Inconsistent ontology" in result.stderr:
                violations.append({
                    'type': 'InconsistentOntology',
                    'severity': 'Error',
                    'entity': 'Ontology',
                    'message': "The ontology is logically inconsistent",
                    'recommendation': "Check for contradictory axioms or unsatisfiable classes"
                })
            
            # Look for unsatisfiable classes
            unsatisfiable_pattern = r"Class\s+<([^>]+)>\s+is unsatisfiable"
            for match in re.finditer(unsatisfiable_pattern, result.stdout + result.stderr):
                class_iri = match.group(1)
                violations.append({
                    'type': 'UnsatisfiableClass',
                    'severity': 'Error',
                    'entity': class_iri,
                    'message': f"Class {class_iri} is unsatisfiable",
                    'recommendation': f"Check the axioms involving {class_iri} for contradictions"
                })
            
            # Look for other errors
            error_pattern = r"Error:\s+(.+)"
            for match in re.finditer(error_pattern, result.stdout + result.stderr):
                error_msg = match.group(1)
                violations.append({
                    'type': 'ReasonerError',
                    'severity': 'Error',
                    'entity': 'Unknown',
                    'message': error_msg,
                    'recommendation': "Review the error message and fix the related axioms"
                })
            
        except Exception as e:
            violations.append({
                'type': 'ValidationError',
                'severity': 'Error',
                'entity': 'Validator',
                'message': f"Error running reasoner: {str(e)}",
                'recommendation': "Ensure the reasoner is properly installed and accessible"
            })
        finally:
            # Clean up the temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        
        return violations
    
    def validate_owl2_dl(self):
        """Perform comprehensive OWL 2 DL validation"""
        # Collect violations from different checks
        violations = []
        
        # Basic structural checks
        violations.extend(self._check_type_separation())
        violations.extend(self._check_property_characteristics())
        violations.extend(self._check_datatype_restrictions())
        
        # Try reasoner-based validation if external tools are available
        if os.path.exists(self.hermit_path):
            violations.extend(self.validate_with_reasoner())
        
        # Store the results
        self.validation_results = {
            'timestamp': datetime.datetime.now().isoformat(),
            'ontology_iri': self._get_ontology_iri(),
            'total_violations': len(violations),
            'violations': violations,
            'is_compliant': len(violations) == 0
        }
        
        return self.validation_results
    
    def _get_ontology_iri(self):
        """Get the ontology IRI if available"""
        for s, p, o in self.graph.triples((None, RDF.type, OWL.Ontology)):
            return str(s)
        return "Unknown"
    
    def generate_validation_report(self, format='markdown'):
        """Generate a formatted validation report"""
        if not self.validation_results:
            self.validate_owl2_dl()
        
        if format == 'json':
            return json.dumps(self.validation_results, indent=2)
        
        elif format == 'markdown':
            report = []
            
            # Header
            report.append("# OWL 2 DL Compliance Report\n")
            report.append(f"**Ontology:** `{self.validation_results['ontology_iri']}`")
            report.append(f"**Date:** {self.validation_results['timestamp']}")
            report.append(f"**Validator:** AMEDEO OWL 2 DL Validator")
            
            # Status
            if self.validation_results['is_compliant']:
                report.append(f"**Status:** <span style=\"color:green; font-weight:bold;\">COMPLIANT</span>")
            else:
                report.append(f"**Status:** <span style=\"color:red; font-weight:bold;\">NOT COMPLIANT</span>")
            
            report.append(f"**Total Issues:** {self.validation_results['total_violations']}\n")
            report.append("---\n")
            
            # Violations
            if self.validation_results['violations']:
                report.append("### Violations Found:\n")
                
                for i, violation in enumerate(self.validation_results['violations']):
                    report.append(f"**{i+1}. {violation['severity']}: {violation['type']}**")
                    report.append(f"   - **Violation Type:** {violation['type']}")
                    report.append(f"   - **Violating Entity:** `{violation['entity']}`")
                    report.append(f"   - **Message:** {violation['message']}")
                    report.append(f"   - **Recommendation:** {violation['recommendation']}\n")
            else:
                report.append("### No Violations Found\n")
                report.append("The ontology is fully compliant with OWL 2 DL restrictions.\n")
            
            report.append("---\n")
            report.append("*Generated by AMEDEO OWL 2 DL Validator*")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format: {format}")

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with OWL 2 DL validation"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.validator = OWL2DLValidator()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.validator.set_graph(self.base_analyzer.graph)
    
    def validate_owl2_dl(self):
        """Validate the ontology against OWL 2 DL restrictions"""
        return self.validator.validate_owl2_dl()
    
    def generate_validation_report(self, format='markdown'):
        """Generate a validation report"""
        return self.validator.generate_validation_report(format)
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 3. Cross-Ontology Mapping Extension

```python
# mapping_extension.py - Cross-ontology mapping support for AMEDEO Ontology Analyzer

import csv
import yaml
import json
import os
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL, SKOS
import pandas as pd
from collections import defaultdict

class OntologyMappingManager:
    """Manager for cross-ontology mappings using SSSOM format"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.mappings = []
        
        # Define common mapping predicates
        self.mapping_predicates = {
            'exactMatch': SKOS.exactMatch,
            'closeMatch': SKOS.closeMatch,
            'relatedMatch': SKOS.relatedMatch,
            'broadMatch': SKOS.broadMatch,
            'narrowMatch': SKOS.narrowMatch,
            'equivalentClass': OWL.equivalentClass,
            'equivalentProperty': OWL.equivalentProperty,
            'sameAs': OWL.sameAs,
            'subClassOf': RDFS.subClassOf,
            'subPropertyOf': RDFS.subPropertyOf
        }
    
    def set_graph(self, graph):
        """Set the RDFLib graph"""
        self.graph = graph
    
    def extract_mappings_from_graph(self):
        """Extract existing mappings from the ontology graph"""
        self.mappings = []
        
        # Extract mappings for each predicate type
        for pred_name, pred_uri in self.mapping_predicates.items():
            for s, p, o in self.graph.triples((None, pred_uri, None)):
                if isinstance(s, URIRef) and isinstance(o, URIRef):
                    # Get labels if available
                    s_label = self._get_entity_label(s)
                    o_label = self._get_entity_label(o)
                    
                    # Determine entity types
                    s_type = self._get_entity_type(s)
                    o_type = self._get_entity_type(o)
                    
                    # Extract source and target ontology IRIs
                    s_ontology = self._extract_ontology_iri(s)
                    o_ontology = self._extract_ontology_iri(o)
                    
                    mapping = {
                        'subject_id': str(s),
                        'subject_label': s_label,
                        'subject_category': s_type,
                        'subject_source': s_ontology,
                        'predicate_id': str(pred_uri),
                        'predicate_label': pred_name,
                        'object_id': str(o),
                        'object_label': o_label,
                        'object_category': o_type,
                        'object_source': o_ontology,
                        'mapping_provider': 'AMEDEO Ontology Analyzer',
                        'confidence': 1.0,  # Default confidence for explicit mappings
                        'comment': None
                    }
                    
                    self.mappings.append(mapping)
        
        return self.mappings
    
    def _get_entity_label(self, entity):
        """Get the label for an entity"""
        for _, _, label in self.graph.triples((entity, RDFS.label, None)):
            return str(label)
        return None
    
    def _get_entity_type(self, entity):
        """Determine the type of an entity"""
        if (entity, RDF.type, OWL.Class) in self.graph:
            return 'Class'
        elif (entity, RDF.type, OWL.ObjectProperty) in self.graph:
            return 'ObjectProperty'
        elif (entity, RDF.type, OWL.DatatypeProperty) in self.graph:
            return 'DatatypeProperty'
        elif (entity, RDF.type, OWL.NamedIndividual) in self.graph:
            return 'Individual'
        return 'Entity'
    
    def _extract_ontology_iri(self, entity_iri):
        """Extract the ontology IRI from an entity IRI"""
        iri = str(entity_iri)
        
        # Try to extract namespace
        if '#' in iri:
            return iri.split('#')[0]
        
        # If no fragment identifier, use the last directory
        parts = iri.split('/')
        if len(parts) > 3:  # At least http://domain/path
            return '/'.join(parts[:-1])
        
        return iri
    
    def import_sssom_mappings(self, file_path):
        """Import mappings from an SSSOM file (TSV format)"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"SSSOM file not found: {file_path}")
        
        # Determine file format based on extension
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.tsv':
            # Read TSV file
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    self.mappings.append(row)
        
        elif ext == '.yaml' or ext == '.yml':
            # Read YAML file
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
                if 'mappings' in data:
                    self.mappings.extend(data['mappings'])
                else:
                    self.mappings.extend(data)
        
        elif ext == '.json':
            # Read JSON file
            with open(file_path, 'r') as f:
                data = json.load(f)
                if 'mappings' in data:
                    self.mappings.extend(data['mappings'])
                else:
                    self.mappings.extend(data)
        
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        
        return self.mappings
    
    def export_sssom_mappings(self, file_path, format='tsv'):
        """Export mappings to an SSSOM file"""
        if not self.mappings:
            self.extract_mappings_from_graph()
        
        if format == 'tsv':
            # Write TSV file
            with open(file_path, 'w', newline='') as f:
                fieldnames = [
                    'subject_id', 'subject_label', 'subject_category', 'subject_source',
                    'predicate_id', 'predicate_label',
                    'object_id', 'object_label', 'object_category', 'object_source',
                    'mapping_provider', 'confidence', 'comment'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                for mapping in self.mappings:
                    writer.writerow(mapping)
        
        elif format == 'yaml':
            # Write YAML file
            with open(file_path, 'w') as f:
                yaml.dump({'mappings': self.mappings}, f)
        
        elif format == 'json':
            # Write JSON file
            with open(file_path, 'w') as f:
                json.dump({'mappings': self.mappings}, f, indent=2)
        
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        return file_path
    
    def add_mapping(self, subject_id, object_id, predicate='exactMatch', confidence=1.0, comment=None):
        """Add a new mapping between two entities"""
        # Convert string predicate to URI if needed
        if isinstance(predicate, str) and predicate in self.mapping_predicates:
            predicate_uri = self.mapping_predicates[predicate]
            predicate_label = predicate
        else:
            predicate_uri = predicate
            predicate_label = str(predicate).split('#')[-1] if '#' in str(predicate) else str(predicate).split('/')[-1]
        
        # Convert string IDs to URIRefs if needed
        subject = URIRef(subject_id) if isinstance(subject_id, str) else subject_id
        object = URIRef(object_id) if isinstance(object_id, str) else object_id
        
        # Get entity information
        subject_label = self._get_entity_label(subject)
        object_label = self._get_entity_label(object)
        subject_type = self._get_entity_type(subject)
        object_type = self._get_entity_type(object)
        subject_source = self._extract_ontology_iri(subject)
        object_source = self._extract_ontology_iri(object)
        
        # Create the mapping
        mapping = {
            'subject_id': str(subject),
            'subject_label': subject_label,
            'subject_category': subject_type,
            'subject_source': subject_source,
            'predicate_id': str(predicate_uri),
            'predicate_label': predicate_label,
            'object_id': str(object),
            'object_label': object_label,
            'object_category': object_type,
            'object_source': object_source,
            'mapping_provider': 'AMEDEO Ontology Analyzer',
            'confidence': confidence,
            'comment': comment
        }
        
        # Add to mappings list
        self.mappings.append(mapping)
        
        # Add to graph if available
        if self.graph:
            self.graph.add((subject, predicate_uri, object))
        
        return mapping
    
    def remove_mapping(self, subject_id, object_id, predicate=None):
        """Remove a mapping between two entities"""
        subject = URIRef(subject_id) if isinstance(subject_id, str) else subject_id
        object = URIRef(object_id) if isinstance(object_id, str) else object_id
        
        # Remove from graph if available
        if self.graph:
            if predicate:
                predicate_uri = self.mapping_predicates.get(predicate, predicate)
                self.graph.remove((subject, predicate_uri, object))
            else:
                # Remove all predicates between subject and object
                for s, p, o in self.graph.triples((subject, None, object)):
                    if p in self.mapping_predicates.values():
                        self.graph.remove((s, p, o))
        
        # Remove from mappings list
        self.mappings = [m for m in self.mappings if not (
            m['subject_id'] == str(subject) and 
            m['object_id'] == str(object) and 
            (predicate is None or m['predicate_label'] == predicate)
        )]
        
        return True
    
    def get_mappings_by_entity(self, entity_id):
        """Get all mappings involving a specific entity"""
        entity_str = str(entity_id)
        return [m for m in self.mappings if m['subject_id'] == entity_str or m['object_id'] == entity_str]
    
    def get_mappings_by_ontology(self, ontology_iri):
        """Get all mappings involving a specific ontology"""
        return [m for m in self.mappings if m['subject_source'] == ontology_iri or m['object_source'] == ontology_iri]
    
    def get_mappings_by_predicate(self, predicate):
        """Get all mappings using a specific predicate"""
        if isinstance(predicate, str) and predicate in self.mapping_predicates:
            predicate_uri = str(self.mapping_predicates[predicate])
        else:
            predicate_uri = str(predicate)
        
        return [m for m in self.mappings if m['predicate_id'] == predicate_uri]
    
    def analyze_mappings(self):
        """Analyze the mappings to generate statistics and insights"""
        if not self.mappings:
            return {"error": "No mappings available"}
        
        analysis = {
            'total_mappings': len(self.mappings),
            'ontologies_involved': set(),
            'predicate_counts': defaultdict(int),
            'entity_type_pairs': defaultdict(int),
            'confidence_distribution': defaultdict(int),
            'most_connected_entities': []
        }
        
        # Entity connection counts
        entity_connections = defaultdict(int)
        
        for mapping in self.mappings:
            # Count ontologies
            analysis['ontologies_involved'].add(mapping['subject_source'])
            analysis['ontologies_involved'].add(mapping['object_source'])
            
            # Count predicates
            analysis['predicate_counts'][mapping['predicate_label']] += 1
            
            # Count entity type pairs
            type_pair = f"{mapping['subject_category']}-{mapping['object_category']}"
            analysis['entity_type_pairs'][type_pair] += 1
            
            # Count confidence distribution (rounded to nearest 0.1)
            if 'confidence' in mapping and mapping['confidence'] is not None:
                conf = round(float(mapping['confidence']) * 10) / 10
                analysis['confidence_distribution'][conf] += 1
            
            # Count entity connections
            entity_connections[mapping['subject_id']] += 1
            entity_connections[mapping['object_id']] += 1
        
        # Convert sets to lists for JSON serialization
        analysis['ontologies_involved'] = list(analysis['ontologies_involved'])
        
        # Get most connected entities
        most_connected = sorted(entity_connections.items(), key=lambda x: x[1], reverse=True)[:10]
        for entity_id, count in most_connected:
            entity_info = {
                'id': entity_id,
                'connection_count': count,
                'label': next((m['subject_label'] for m in self.mappings if m['subject_id'] == entity_id), None) or
                         next((m['object_label'] for m in self.mappings if m['object_id'] == entity_id), None)
            }
            analysis['most_connected_entities'].append(entity_info)
        
        return analysis
    
    def visualize_mapping_network(self, output_file="mapping_network.html"):
        """Visualize the mapping network using Pyvis"""
        try:
            from pyvis.network import Network
        except ImportError:
            return "Pyvis not installed. Install with: pip install pyvis"
        
        if not self.mappings:
            return "No mappings available to visualize"
        
        # Create network
        net = Network(notebook=False, height="750px", width="100%", heading="Ontology Mapping Network")
        
        # Track added nodes to avoid duplicates
        added_nodes = set()
        
        # Define node colors based on ontology source
        ontology_colors = {}
        for mapping in self.mappings:
            if mapping['subject_source'] not in ontology_colors:
                # Generate a color based on hash of ontology IRI
                h = hash(mapping['subject_source']) % 360
                ontology_colors[mapping['subject_source']] = f"hsl({h}, 70%, 60%)"
            
            if mapping['object_source'] not in ontology_colors:
                h = hash(mapping['object_source']) % 360
                ontology_colors[mapping['object_source']] = f"hsl({h}, 70%, 60%)"
        
        # Add nodes
        for mapping in self.mappings:
            # Add subject node if not already added
            if mapping['subject_id'] not in added_nodes:
                label = mapping['subject_label'] or mapping['subject_id'].split('/')[-1].split('#')[-1]
                net.add_node(
                    mapping['subject_id'],
                    label=label,
                    title=f"ID: {mapping['subject_id']}\nType: {mapping['subject_category']}\nOntology: {mapping['subject_source']}",
                    color=ontology_colors.get(mapping['subject_source'], "#CCCCCC")
                )
                added_nodes.add(mapping['subject_id'])
            
            # Add object node if not already added
            if mapping['object_id'] not in added_nodes:
                label = mapping['object_label'] or mapping['object_id'].split('/')[-1].split('#')[-1]
                net.add_node(
                    mapping['object_id'],
                    label=label,
                    title=f"ID: {mapping['object_id']}\nType: {mapping['object_category']}\nOntology: {mapping['object_source']}",
                    color=ontology_colors.get(mapping['object_source'], "#CCCCCC")
                )
                added_nodes.add(mapping['object_id'])
        
        # Add edges
        for mapping in self.mappings:
            # Determine edge color based on predicate
            if 'exact' in mapping['predicate_label'].lower():
                edge_color = "#00AA00"  # Green for exact matches
            elif 'equivalent' in mapping['predicate_label'].lower():
                edge_color = "#00AA00"  # Green for equivalence
            elif 'close' in mapping['predicate_label'].lower():
                edge_color = "#0088FF"  # Blue for close matches
            elif 'related' in mapping['predicate_label'].lower():
                edge_color = "#AAAAAA"  # Gray for related matches
            elif 'sub' in mapping['predicate_label'].lower():
                edge_color = "#FF8800"  # Orange for subclass/subproperty
            else:
                edge_color = "#000000"  # Black for other predicates
            
            # Determine edge width based on confidence
            confidence = float(mapping.get('confidence', 1.0))
            edge_width = 1 + 3 * confidence  # Width between 1 and 4
            
            net.add_edge(
                mapping['subject_id'],
                mapping['object_id'],
                title=mapping['predicate_label'],
                label=mapping['predicate_label'],
                color=edge_color,
                width=edge_width
            )
        
        # Configure options
        net.toggle_physics(True)
        net.show_buttons(filter_=['physics', 'nodes', 'edges'])
        
        # Set other options
        net.set_options("""
        var options = {
            "nodes": {
                "font": {
                    "size": 12
                },
                "shape": "dot",
                "size": 20
            },
            "edges": {
                "font": {
                    "size": 10,
                    "align": "middle"
                },
                "smooth": {
                    "enabled": true,
                    "type": "continuous"
                },
                "arrows": {
                    "to": {
                        "enabled": true,
                        "scaleFactor": 0.5
                    }
                }
            },
            "physics": {
                "forceAtlas2Based": {
                    "gravitationalConstant": -50,
                    "centralGravity": 0.01,
                    "springLength": 100,
                    "springConstant": 0.08
                },
                "solver": "forceAtlas2Based",
                "stabilization": {
                    "iterations": 100
                }
            }
        }
        """)
        
        # Save to file
        net.save_graph(output_file)
        return output_file
    
    def generate_mapping_report(self, format='markdown'):
        """Generate a report of the mappings"""
        if not self.mappings:
            self.extract_mappings_from_graph()
        
        analysis = self.analyze_mappings()
        
        if format == 'json':
            report = {
                'analysis': analysis,
                'mappings': self.mappings
            }
            return json.dumps(report, indent=2)
        
        elif format == 'markdown':
            report = []
            
            # Header
            report.append("# Ontology Mapping Report\n")
            report.append(f"**Total Mappings:** {analysis['total_mappings']}")
            report.append(f"**Ontologies Involved:** {len(analysis['ontologies_involved'])}\n")
            
            # Predicate statistics
            report.append("## Mapping Predicates\n")
            report.append("| Predicate | Count | Percentage |")
            report.append("| --- | --- | --- |")
            
            for pred, count in sorted(analysis['predicate_counts'].items(), key=lambda x: x[1], reverse=True):
                percentage = (count / analysis['total_mappings']) * 100
                report.append(f"| {pred} | {count} | {percentage:.1f}% |")
            
            report.append("\n## Entity Type Pairs\n")
            report.append("| Source Type | Target Type | Count | Percentage |")
            report.append("| --- | --- | --- | --- |")
            
            for type_pair, count in sorted(analysis['entity_type_pairs'].items(), key=lambda x: x[1], reverse=True):
                source_type, target_type = type_pair.split('-')
                percentage = (count / analysis['total_mappings']) * 100
                report.append(f"| {source_type} | {target_type} | {count} | {percentage:.1f}% |")
            
            # Most connected entities
            report.append("\n## Most Connected Entities\n")
            report.append("| Entity | Label | Connections |")
            report.append("| --- | --- | --- |")
            
            for entity in analysis['most_connected_entities']:
                entity_short = entity['id'].split('/')[-1].split('#')[-1]
                report.append(f"| {entity_short} | {entity['label'] or 'N/A'} | {entity['connection_count']} |")
            
            # Ontologies involved
            report.append("\n## Ontologies Involved\n")
            for ontology in sorted(analysis['ontologies_involved']):
                report.append(f"- {ontology}")
            
            # Sample mappings
            report.append("\n## Sample Mappings\n")
            
            sample_size = min(10, len(self.mappings))
            for i, mapping in enumerate(self.mappings[:sample_size]):
                subject_label = mapping['subject_label'] or mapping['subject_id'].split('/')[-1].split('#')[-1]
                object_label = mapping['object_label'] or mapping['object_id'].split('/')[-1].split('#')[-1]
                
                report.append(f"### Mapping {i+1}\n")
                report.append(f"- **Subject:** {subject_label} ({mapping['subject_category']})")
                report.append(f"- **Subject ID:** `{mapping['subject_id']}`")
                report.append(f"- **Subject Ontology:** {mapping['subject_source']}")
                report.append(f"- **Predicate:** {mapping['predicate_label']}")
                report.append(f"- **Object:** {object_label} ({mapping['object_category']})")
                report.append(f"- **Object ID:** `{mapping['object_id']}`")
                report.append(f"- **Object Ontology:** {mapping['object_source']}")
                
                if mapping.get('confidence'):
                    report.append(f"- **Confidence:** {float(mapping['confidence']):.2f}")
                
                if mapping.get('comment'):
                    report.append(f"- **Comment:** {mapping['comment']}")
                
                report.append("")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format: {format}")

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with cross-ontology mapping support"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.mapping_manager = OntologyMappingManager()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.mapping_manager.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.mapping_manager.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.mapping_manager.set_graph(self.base_analyzer.graph)
    
    def extract_mappings(self):
        """Extract mappings from the ontology"""
        return self.mapping_manager.extract_mappings_from_graph()
    
    def import_mappings(self, file_path):
        """Import mappings from an SSSOM file"""
        return self.mapping_manager.import_sssom_mappings(file_path)
    
    def export_mappings(self, file_path, format='tsv'):
        """Export mappings to an SSSOM file"""
        return self.mapping_manager.export_sssom_mappings(file_path, format)
    
    def add_mapping(self, subject_id, object_id, predicate='exactMatch', confidence=1.0, comment=None):
        """Add a new mapping"""
        return self.mapping_manager.add_mapping(subject_id, object_id, predicate, confidence, comment)
    
    def visualize_mappings(self, output_file="mapping_network.html"):
        """Visualize the mapping network"""
        return self.mapping_manager.visualize_mapping_network(output_file)
    
    def generate_mapping_report(self, format='markdown'):
        """Generate a mapping report"""
        return self.mapping_manager.generate_mapping_report(format)
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 4. Federation Anchor Support

```python
# federation_extension.py - Federation anchor support for AMEDEO Ontology Analyzer

import json
import os
import tempfile
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, RDFS, OWL
import re
from collections import defaultdict

class FederationAnchorManager:
    """Manager for federation anchors in AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.amedeo = Namespace("http://www.gaiaair.org/ontologies/amedeo#")
        self.federation_anchors = []
        
    def set_graph(self, graph):
        """Set the RDFLib graph"""
        self.graph = graph
    
    def identify_federation_anchors(self):
        """Identify federation anchors in the ontology"""
        self.federation_anchors = []
        
        # Look for classes that are explicitly marked as federation anchors
        for s in self.graph.subjects(RDF.type, self.amedeo.FederationAnchor):
            self._add_federation_anchor(s)
        
        # Look for subclasses of FederationAnchor
        for s in self.graph.subjects(RDFS.subClassOf, self.amedeo.FederationAnchor):
            self._add_federation_anchor(s)
        
        # Look for classes with owl:equivalentClass to external ontologies
        for s, p, o in self.graph.triples((None, OWL.equivalentClass, None)):
            if isinstance(s, URIRef) and isinstance(o, URIRef):
                # Check if they are from different ontologies
                s_ontology = self._extract_ontology_iri(s)
                o_ontology = self._extract_ontology_iri(o)
                
                if s_ontology != o_ontology:
                    self._add_federation_anchor(s)
        
        return self.federation_anchors
    
    def _add_federation_anchor(self, entity):
        """Add an entity as a federation anchor"""
        if not isinstance(entity, URIRef):
            return
        
        # Check if already added
        if any(a['uri'] == str(entity) for a in self.federation_anchors):
            return
        
        # Get label and description
        label = None
        for _, _, l in self.graph.triples((entity, RDFS.label, None)):
            label = str(l)
            break
        
        description = None
        for _, _, d in self.graph.triples((entity, RDFS.comment, None)):
            description = str(d)
            break
        
        # Get equivalent classes
        equivalent_classes = []
        for _, _, eq in self.graph.triples((entity, OWL.equivalentClass, None)):
            if isinstance(eq, URIRef):
                eq_label = None
                for _, _, l in self.graph.triples((eq, RDFS.label, None)):
                    eq_label = str(l)
                    break
                
                equivalent_classes.append({
                    'uri': str(eq),
                    'label': eq_label,
                    'ontology': self._extract_ontology_iri(eq)
                })
        
        # Get subclasses
        subclasses = []
        for sub in self.graph.subjects(RDFS.subClassOf, entity):
            if isinstance(sub, URIRef):
                sub_label = None
                for _, _, l in self.graph.triples((sub, RDFS.label, None)):
                    sub_label = str(l)
                    break
                
                subclasses.append({
                    'uri': str(sub),
                    'label': sub_label,
                    'ontology': self._extract_ontology_iri(sub)
                })
        
        # Add to federation anchors
        self.federation_anchors.append({
            'uri': str(entity),
            'label': label,
            'description': description,
            'ontology': self._extract_ontology_iri(entity),
            'equivalent_classes': equivalent_classes,
            'subclasses': subclasses
        })
    
    def _extract_ontology_iri(self, entity_iri):
        """Extract the ontology IRI from an entity IRI"""
        iri = str(entity_iri)
        
        # Try to extract namespace
        if '#' in iri:
            return iri.split('#')[0]
        
        # If no fragment identifier, use the last directory
        parts = iri.split('/')
        if len(parts) > 3:  # At least http://domain/path
            return '/'.join(parts[:-1])
        
        return iri
    
    def create_federation_anchor(self, class_uri, label, description=None):
        """Create a new federation anchor"""
        class_uri = URIRef(class_uri) if isinstance(class_uri, str) else class_uri
        
        # Add to graph
        self.graph.add((class_uri, RDF.type, OWL.Class))
        self.graph.add((class_uri, RDF.type, self.amedeo.FederationAnchor))
        
        if label:
            self.graph.add((class_uri, RDFS.label, Literal(label)))
        
        if description:
            self.graph.add((class_uri, RDFS.comment, Literal(description)))
        
        # Add to federation anchors
        self._add_federation_anchor(class_uri)
        
        return next((a for a in self.federation_anchors if a['uri'] == str(class_uri)), None)
    
    def add_equivalent_class(self, anchor_uri, equivalent_uri, equivalent_label=None):
        """Add an equivalent class to a federation anchor"""
        anchor_uri = URIRef(anchor_uri) if isinstance(anchor_uri, str) else anchor_uri
        equivalent_uri = URIRef(equivalent_uri) if isinstance(equivalent_uri, str) else equivalent_uri
        
        # Add to graph
        self.graph.add((anchor_uri, OWL.equivalentClass, equivalent_uri))
        self.graph.add((equivalent_uri, OWL.equivalentClass, anchor_uri))
        
        if equivalent_label:
            self.graph.add((equivalent_uri, RDFS.label, Literal(equivalent_label)))
        
        # Update federation anchors
        self.identify_federation_anchors()
        
        return next((a for a in self.federation_anchors if a['uri'] == str(anchor_uri)), None)
    
    def validate_federation_anchors(self):
        """Validate federation anchors for consistency and completeness"""
        if not self.federation_anchors:
            self.identify_federation_anchors()
        
        validation_results = {
            'valid': True,
            'issues': []
        }
        
        for anchor in self.federation_anchors:
            # Check if anchor has a label
            if not anchor['label']:
                validation_results['valid'] = False
                validation_results['issues'].append({
                    'severity': 'Warning',
                    'type': 'MissingLabel',
                    'entity': anchor['uri'],
                    'message': f"Federation anchor {anchor['uri']} is missing a label",
                    'recommendation': f"Add rdfs:label to {anchor['uri']}"
                })
            
            # Check if anchor has a description
            if not anchor['description']:
                validation_results['valid'] = False
                validation_results['issues'].append({
                    'severity': 'Warning',
                    'type': 'MissingDescription',
                    'entity': anchor['uri'],
                    'message': f"Federation anchor {anchor['uri']} is missing a description",
                    'recommendation': f"Add rdfs:comment to {anchor['uri']}"
                })
            
            # Check if anchor has at least one equivalent class
            if not anchor['equivalent_classes']:
                validation_results['valid'] = False
                validation_results['issues'].append({
                    'severity': 'Warning',
                    'type': 'NoEquivalentClasses',
                    'entity': anchor['uri'],
                    'message': f"Federation anchor {anchor['uri']} has no equivalent classes",
                    'recommendation': f"Add owl:equivalentClass relationships to {anchor['uri']}"
                })
            
            # Check for equivalent classes without labels
            for eq_class in anchor['equivalent_classes']:
                if not eq_class['label']:
                    validation_results['valid'] = False
                    validation_results['issues'].append({
                        'severity': 'Warning',
                        'type': 'MissingEquivalentClassLabel',
                        'entity': eq_class['uri'],
                        'message': f"Equivalent class {eq_class['uri']} is missing a label",
                        'recommendation': f"Add rdfs:label to {eq_class['uri']}"
                    })
        
        return validation_results
    
    def generate_shacl_shapes(self, output_file=None):
        """Generate SHACL shapes for validating federation anchors"""
        shacl_graph = Graph()
        
        # Define namespaces
        sh = Namespace("http://www.w3.org/ns/shacl#")
        shacl_graph.bind("sh", sh)
        shacl_graph.bind("owl", OWL)
        shacl_graph.bind("rdfs", RDFS)
        shacl_graph.bind("amedeo", self.amedeo)
        
        # Create shape for FederationAnchor
        anchor_shape = URIRef("http://www.gaiaair.org/ontologies/amedeo/shapes#FederationAnchorShape")
        shacl_graph.add((anchor_shape, RDF.type, sh.NodeShape))
        shacl_graph.add((anchor_shape, sh.targetClass, self.amedeo.FederationAnchor))
        shacl_graph.add((anchor_shape, RDFS.label, Literal("Federation Anchor Shape")))
        shacl_graph.add((anchor_shape, RDFS.comment, Literal("Constraints for Federation Anchors")))
        
        # Require rdfs:label
        label_constraint = BNode()
        shacl_graph.add((anchor_shape, sh.property, label_constraint))
        shacl_graph.add((label_constraint, sh.path, RDFS.label))
        shacl_graph.add((label_constraint, sh.minCount, Literal(1)))
        shacl_graph.add((label_constraint, sh.message, Literal("Federation anchors must have at least one rdfs:label")))
        
        # Require rdfs:comment
        comment_constraint = BNode()
        shacl_graph.add((anchor_shape, sh.property, comment_constraint))
        shacl_graph.add((comment_constraint, sh.path, RDFS.comment))
        shacl_graph.add((comment_constraint, sh.minCount, Literal(1)))
        shacl_graph.add((comment_constraint, sh.message, Literal("Federation anchors should have at least one rdfs:comment")))
        
        # Recommend at least one owl:equivalentClass
        eq_class_constraint = BNode()
        shacl_graph.add((anchor_shape, sh.property, eq_class_constraint))
        shacl_graph.add((eq_class_constraint, sh.path, OWL.equivalentClass))
        shacl_graph.add((eq_class_constraint, sh.minCount, Literal(1)))
        shacl_graph.add((eq_class_constraint, sh.severity, sh.Warning))
        shacl_graph.add((eq_class_constraint, sh.message, Literal("Federation anchors should have at least one owl:equivalentClass")))
        
        # Write to file if specified
        if output_file:
            shacl_graph.serialize(destination=output_file, format="turtle")
            return output_file
        
        # Otherwise return as string
        return shacl_graph.serialize(format="turtle")
    
    def analyze_federation_coverage(self):
        """Analyze the coverage of federation anchors across ontologies"""
        if not self.federation_anchors:
            self.identify_federation_anchors()
        
        # Collect ontologies and their anchors
        ontology_anchors = defaultdict(list)
        ontology_equivalents = defaultdict(list)
        
        for anchor in self.federation_anchors:
            ontology_anchors[anchor['ontology']].append(anchor)
            
            for eq_class in anchor['equivalent_classes']:
                ontology_equivalents[eq_class['ontology']].append({
                    'anchor': anchor,
                    'equivalent': eq_class
                })
        
        # Analyze connections between ontologies
        ontology_connections = defaultdict(set)
        
        for anchor in self.federation_anchors:
            for eq_class in anchor['equivalent_classes']:
                source_ont = anchor['ontology']
                target_ont = eq_class['ontology']
                
                if source_ont != target_ont:
                    ontology_connections[source_ont].add(target_ont)
                    ontology_connections[target_ont].add(source_ont)
        
        # Convert sets to lists for JSON serialization
        for ont in ontology_connections:
            ontology_connections[ont] = list(ontology_connections[ont])
        
        # Prepare analysis results
        analysis = {
            'total_anchors': len(self.federation_anchors),
            'ontologies': {
                'total': len(set(ont for ont in ontology_anchors.keys()).union(set(ont for ont in ontology_equivalents.keys()))),
                'with_anchors': len(ontology_anchors),
                'with_equivalents': len(ontology_equivalents),
                'details': []
            },
            'connections': {
                'total': sum(len(conns) for conns in ontology_connections.values()) // 2,  # Divide by 2 to avoid counting both directions
                'details': dict(ontology_connections)
            }
        }
        
        # Add details for each ontology
        for ont in sorted(set(ont for ont in ontology_anchors.keys()).union(set(ont for ont in ontology_equivalents.keys()))):
            ont_details = {
                'ontology': ont,
                'anchors': len(ontology_anchors.get(ont, [])),
                'equivalents': len(ontology_equivalents.get(ont, [])),
                'connected_to': len(ontology_connections.get(ont, []))
            }
            analysis['ontologies']['details'].append(ont_details)
        
        return analysis
    
    def generate_federation_report(self, format='markdown'):
        """Generate a report on federation anchors"""
        if not self.federation_anchors:
            self.identify_federation_anchors()
        
        validation = self.validate_federation_anchors()
        coverage = self.analyze_federation_coverage()
        
        if format == 'json':
            report = {
                'federation_anchors': self.federation_anchors,
                'validation': validation,
                'coverage': coverage
            }
            return json.dumps(report, indent=2)
        
        elif format == 'markdown':
            report = []
            
            # Header
            report.append("# Federation Anchor Report\n")
            report.append(f"**Total Federation Anchors:** {len(self.federation_anchors)}")
            report.append(f"**Ontologies Involved:** {coverage['ontologies']['total']}")
            report.append(f"**Validation Status:** {'Valid' if validation['valid'] else 'Invalid - See Issues Below'}\n")
            
            # Coverage summary
            report.append("## Coverage Summary\n")
            report.append(f"- **Ontologies with Anchors:** {coverage['ontologies']['with_anchors']}")
            report.append(f"- **Ontologies with Equivalent Classes:** {coverage['ontologies']['with_equivalents']}")
            report.append(f"- **Total Connections Between Ontologies:** {coverage['connections']['total']}\n")
            
            # Ontology details
            report.append("## Ontology Details\n")
            report.append("| Ontology | Anchors | Equivalents | Connected To |")
            report.append("| --- | --- | --- | --- |")
            
            for ont in coverage['ontologies']['details']:
                report.append(f"| {ont['ontology']} | {ont['anchors']} | {ont['equivalents']} | {ont['connected_to']} |")
            
            # Federation anchors
            report.append("\n## Federation Anchors\n")
            
            for i, anchor in enumerate(self.federation_anchors):
                report.append(f"### {i+1}. {anchor['label'] or 'Unnamed Anchor'}\n")
                report.append(f"- **URI:** `{anchor['uri']}`")
                report.append(f"- **Ontology:** {anchor['ontology']}")
                
                if anchor['description']:
                    report.append(f"- **Description:** {anchor['description']}")
                
                if anchor['equivalent_classes']:
                    report.append("\n**Equivalent Classes:**")
                    for eq in anchor['equivalent_classes']:
                        report.append(f"- {eq['label'] or 'Unnamed'} (`{eq['uri']}`) from {eq['ontology']}")
                
                if anchor['subclasses']:
                    report.append("\n**Subclasses:**")
                    for sub in anchor['subclasses']:
                        report.append(f"- {sub['label'] or 'Unnamed'} (`{sub['uri']}`) from {sub['ontology']}")
                
                report.append("")
            
            # Validation issues
            if validation['issues']:
                report.append("## Validation Issues\n")
                
                for i, issue in enumerate(validation['issues']):
                    report.append(f"### Issue {i+1}: {issue['type']}\n")
                    report.append(f"- **Severity:** {issue['severity']}")
                    report.append(f"- **Entity:** `{issue['entity']}`")
                    report.append(f"- **Message:** {issue['message']}")
                    report.append(f"- **Recommendation:** {issue['recommendation']}\n")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format: {format}")

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with federation anchor support"""
    
    def __init__(self):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.federation_manager = FederationAnchorManager()
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.federation_manager.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.federation_manager.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.federation_manager.set_graph(self.base_analyzer.graph)
    
    def identify_federation_anchors(self):
        """Identify federation anchors in the ontology"""
        return self.federation_manager.identify_federation_anchors()
    
    def create_federation_anchor(self, class_uri, label, description=None):
        """Create a new federation anchor"""
        return self.federation_manager.create_federation_anchor(class_uri, label, description)
    
    def validate_federation_anchors(self):
        """Validate federation anchors"""
        return self.federation_manager.validate_federation_anchors()
    
    def generate_federation_report(self, format='markdown'):
        """Generate a federation anchor report"""
        return self.federation_manager.generate_federation_report(format)
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 5. TokenFlow Pipeline Integration

```python
# tokenflow_extension.py - TokenFlow pipeline integration for AMEDEO Ontology Analyzer

import json
import os
import tempfile
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, RDFS, OWL
import requests
from flask import Flask, request, jsonify
import threading
import time
import logging

class TokenFlowIntegration:
    """Integration with TokenFlow pipeline for AMEDEO Ontology"""
    
    def __init__(self, graph=None, host='localhost', port=5000):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.server_thread = None
        self.running = False
        self.logger = logging.getLogger('TokenFlowIntegration')
        
        # Set up API routes
        self.setup_routes()
    
    def set_graph(self, graph):
        """Set the RDFLib graph"""
        self.graph = graph
    
    def setup_routes(self):
        """Set up API routes for TokenFlow integration"""
        
        @self.app.route('/api/health', methods=['GET'])
        def health_check():
            return jsonify({'status': 'ok', 'message': 'AMEDEO Ontology API is running'})
        
        @self.app.route('/api/validate/instance', methods=['POST'])
        def validate_instance():
            """Validate an instance against class definitions"""
            data = request.json
            
            if not data or 'type' not in data or 'properties' not in data:
                return jsonify({
                    'valid': False,
                    'error': 'Invalid request format. Requires type and properties.'
                }), 400
            
            try:
                result = self.validate_instance_data(data['type'], data['properties'])
                return jsonify(result)
            except Exception as e:
                self.logger.error(f"Error validating instance: {str(e)}")
                return jsonify({
                    'valid': False,
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/validate/triple', methods=['POST'])
        def validate_triple():
            """Validate a subject-predicate-object triple"""
            data = request.json
            
            if not data or 'subject' not in data or 'predicate' not in data or 'object' not in data:
                return jsonify({
                    'valid': False,
                    'error': 'Invalid request format. Requires subject, predicate, and object.'
                }), 400
            
            try:
                result = self.validate_triple_data(data['subject'], data['predicate'], data['object'])
                return jsonify(result)
            except Exception as e:
                self.logger.error(f"Error validating triple: {str(e)}")
                return jsonify({
                    'valid': False,
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/validate/shacl', methods=['POST'])
        def validate_shacl():
            """Validate data against SHACL shapes"""
            data = request.json
            
            if not data or 'data' not in data:
                return jsonify({
                    'valid': False,
                    'error': 'Invalid request format. Requires data to validate.'
                }), 400
            
            try:
                shapes_graph = None
                if 'shapes' in data:
                    shapes_graph = data['shapes']
                
                result = self.validate_with_shacl(data['data'], shapes_graph)
                return jsonify(result)
            except Exception as e:
                self.logger.error(f"Error validating with SHACL: {str(e)}")
                return jsonify({
                    'valid': False,
                    'error': str(e)
                }), 500
        
        @self.app.route('/api/query', methods=['POST'])
        def query_ontology():
            """Query the ontology with SPARQL"""
            data = request.json
            
            if not data or 'query' not in data:
                return jsonify({
                    'error': 'Invalid request format. Requires query.'
                }), 400
            
            try:
                result = self.query_sparql(data['query'])
                return jsonify(result)
            except Exception as e:
                self.logger.error(f"Error querying ontology: {str(e)}")
                return jsonify({
                    'error': str(e)
                }), 500
    
    def start_server(self, debug=False):
        """Start the API server in a separate thread"""
        if self.running:
            return False
        
        def run_server():
            self.app.run(host=self.host, port=self.port, debug=debug, use_reloader=False)
        
        self.server_thread = threading.Thread(target=run_server)
        self.server_thread.daemon = True
        self.server_thread.start()
        self.running = True
        
        # Wait for server to start
        time.sleep(1)
        
        return True
    
    def stop_server(self):
        """Stop the API server"""
        if not self.running:
            return False
        
        # This is a simple implementation - in production, you would use a more robust shutdown mechanism
        self.running = False
        # The thread will terminate when the main program exits
        
        return True
    
    def validate_instance_data(self, type_uri, properties):
        """Validate instance data against class definitions"""
        # Create a temporary graph for validation
        temp_graph = Graph()
        temp_graph += self.graph  # Copy the ontology graph
        
        # Create a new instance with the given properties
        instance_uri = URIRef(f"http://validation.example.org/instance_{int(time.time())}")
        type_uri = URIRef(type_uri) if isinstance(type_uri, str) else type_uri
        
        # Add type assertion
        temp_graph.add((instance_uri, RDF.type, type_uri))
        
        # Add properties
        for prop, values in properties.items():
            prop_uri = URIRef(prop) if isinstance(prop, str) else prop
            
            if not isinstance(values, list):
                values = [values]
            
            for value in values:
                if isinstance(value, dict) and 'uri' in value:
                    # Object property
                    obj_uri = URIRef(value['uri'])
                    temp_graph.add((instance_uri, prop_uri, obj_uri))
                elif isinstance(value, dict) and 'value' in value and 'datatype' in value:
                    # Datatype property with explicit datatype
                    lit_value = Literal(value['value'], datatype=URIRef(value['datatype']))
                    temp_graph.add((instance_uri, prop_uri, lit_value))
                else:
                    # Simple literal
                    temp_graph.add((instance_uri, prop_uri, Literal(value)))
        
        # Validate using SHACL if available
        try:
            import pyshacl
            conforms, results_graph, results_text = pyshacl.validate(
                temp_graph,
                shacl_graph=None,  # Use the ontology itself for validation
                ont_graph=self.graph,
                inference='rdfs',
                abort_on_error=False
            )
            
            if conforms:
                return {
                    'valid': True,
                    'message': 'Instance is valid'
                }
            else:
                # Extract validation results
                violations = []
                for result in results_graph.subjects(RDF.type, URIRef("http://www.w3.org/ns/shacl#ValidationResult")):
                    message = None
                    for _, _, msg in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#resultMessage"), None)):
                        message = str(msg)
                    
                    path = None
                    for _, _, p in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#resultPath"), None)):
                        path = str(p)
                    
                    violations.append({
                        'message': message,
                        'path': path
                    })
                
                return {
                    'valid': False,
                    'message': 'Instance is invalid',
                    'violations': violations
                }
        
        except ImportError:
            # Fall back to basic validation if SHACL is not available
            # Check domain/range constraints
            issues = []
            
            for prop, values in properties.items():
                prop_uri = URIRef(prop) if isinstance(prop, str) else prop
                
                # Check if property exists
                if (prop_uri, RDF.type, None) not in temp_graph:
                    issues.append({
                        'property': prop,
                        'message': f"Property {prop} is not defined in the ontology"
                    })
                    continue
                
                # Check domain constraints
                domains = []
                for _, _, domain in temp_graph.triples((prop_uri, RDFS.domain, None)):
                    domains.append(domain)
                
                if domains and not any((type_uri, RDFS.subClassOf, domain) in temp_graph or type_uri == domain for domain in domains):
                    issues.append({
                        'property': prop,
                        'message': f"Property {prop} has domain constraints that are not satisfied by type {type_uri}"
                    })
                
                # Check range constraints for each value
                if not isinstance(values, list):
                    values = [values]
                
                ranges = []
                for _, _, range_val in temp_graph.triples((prop_uri, RDFS.range, None)):
                    ranges.append(range_val)
                
                for value in values:
                    if isinstance(value, dict) and 'uri' in value:
                        # Object property - check if value type is compatible with range
                        obj_uri = URIRef(value['uri'])
                        obj_types = list(temp_graph.objects(obj_uri, RDF.type))
                        
                        if ranges and not any(any((obj_type, RDFS.subClassOf, range_val) in temp_graph or obj_type == range_val for obj_type in obj_types) for range_val in ranges):
                            issues.append({
                                'property': prop,
                                'value': value['uri'],
                                'message': f"Value {value['uri']} for property {prop} does not satisfy range constraints"
                            })
            
            if issues:
                return {
                    'valid': False,
                    'message': 'Instance has validation issues',
                    'issues': issues
                }
            else:
                return {
                    'valid': True,
                    'message': 'Instance appears valid (basic validation only)'
                }
    
    def validate_triple_data(self, subject, predicate, object_value):
        """Validate a subject-predicate-object triple"""
        subject_uri = URIRef(subject) if isinstance(subject, str) else subject
        predicate_uri = URIRef(predicate) if isinstance(predicate, str) else predicate
        
        # Determine if object is a URI or literal
        if isinstance(object_value, dict) and 'uri' in object_value:
            object_uri = URIRef(object_value['uri'])
            is_literal = False
        elif isinstance(object_value, dict) and 'value' in object_value:
            if 'datatype' in object_value:
                object_uri = Literal(object_value['value'], datatype=URIRef(object_value['datatype']))
            elif 'language' in object_value:
                object_uri = Literal(object_value['value'], lang=object_value['language'])
            else:
                object_uri = Literal(object_value['value'])
            is_literal = True
        else:
            object_uri = Literal(object_value)
            is_literal = True
        
        # Check if subject exists in the ontology
        if (subject_uri, None, None) not in self.graph and (None, None, subject_uri) not in self.graph:
            return {
                'valid': False,
                'message': f"Subject {subject} does not exist in the ontology"
            }
        
        # Check if predicate is defined in the ontology
        if (predicate_uri, RDF.type, None) not in self.graph:
            return {
                'valid': False,
                'message': f"Predicate {predicate} is not defined in the ontology"
            }
        
        # If object is a URI, check if it exists in the ontology
        if not is_literal and (object_uri, None, None) not in self.graph and (None, None, object_uri) not in self.graph:
            return {
                'valid': False,
                'message': f"Object {object_value['uri']} does not exist in the ontology"
            }
        
        # Check domain constraints
        subject_types = list(self.graph.objects(subject_uri, RDF.type))
        domains = list(self.graph.objects(predicate_uri, RDFS.domain))
        
        if domains:
            domain_satisfied = False
            for domain in domains:
                for s_type in subject_types:
                    if (s_type, RDFS.subClassOf, domain) in self.graph or s_type == domain:
                        domain_satisfied = True
                        break
                if domain_satisfied:
                    break
            
            if not domain_satisfied:
                return {
                    'valid': False,
                    'message': f"Subject {subject} does not satisfy domain constraints for predicate {predicate}"
                }
        
        # Check range constraints
        ranges = list(self.graph.objects(predicate_uri, RDFS.range))
        
        if ranges and not is_literal:
            object_types = list(self.graph.objects(object_uri, RDF.type))
            range_satisfied = False
            
            for range_val in ranges:
                for o_type in object_types:
                    if (o_type, RDFS.subClassOf, range_val) in self.graph or o_type == range_val:
                        range_satisfied = True
                        break
                if range_satisfied:
                    break
            
            if not range_satisfied:
                return {
                    'valid': False,
                    'message': f"Object {object_value['uri']} does not satisfy range constraints for predicate {predicate}"
                }
        
        # If we got here, the triple is valid
        return {
            'valid': True,
            'message': 'Triple is valid'
        }
    
    def validate_with_shacl(self, data, shapes=None):
        """Validate data against SHACL shapes"""
        try:
            import pyshacl
        except ImportError:
            return {
                'valid': False,
                'error': 'SHACL validation requires pyshacl package'
            }
        
        # Parse data into a graph
        data_graph = Graph()
        if isinstance(data, str):
            # Assume it's Turtle format
            data_graph.parse(data=data, format='turtle')
        elif isinstance(data, dict):
            # Assume it's JSON-LD
            data_graph.parse(data=json.dumps(data), format='json-ld')
        else:
            return {
                'valid': False,
                'error': 'Unsupported data format'
            }
        
        # Parse shapes if provided
        shapes_graph = None
        if shapes:
            shapes_graph = Graph()
            if isinstance(shapes, str):
                # Assume it's Turtle format
                shapes_graph.parse(data=shapes, format='turtle')
            elif isinstance(shapes, dict):
                # Assume it's JSON-LD
                shapes_graph.parse(data=json.dumps(shapes), format='json-ld')
            else:
                return {
                    'valid': False,
                    'error': 'Unsupported shapes format'
                }
        
        # Validate
        conforms, results_graph, results_text = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            ont_graph=self.graph,
            inference='rdfs',
            abort_on_error=False
        )
        
        if conforms:
            return {
                'valid': True,
                'message': 'Data conforms to SHACL shapes'
            }
        else:
            # Extract validation results
            violations = []
            for result in results_graph.subjects(RDF.type, URIRef("http://www.w3.org/ns/shacl#ValidationResult")):
                violation = {}
                
                # Get message
                for _, _, msg in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#resultMessage"), None)):
                    violation['message'] = str(msg)
                
                # Get focus node
                for _, _, focus in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#focusNode"), None)):
                    violation['focusNode'] = str(focus)
                
                # Get path
                for _, _, path in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#resultPath"), None)):
                    violation['path'] = str(path)
                
                # Get severity
                for _, _, severity in results_graph.triples((result, URIRef("http://www.w3.org/ns/shacl#resultSeverity"), None)):
                    violation['severity'] = str(severity).split('#')[-1]
                
                violations.append(violation)
            
            return {
                'valid': False,
                'message': 'Data does not conform to SHACL shapes',
                'violations': violations
            }
    
    def query_sparql(self, query_string):
        """Query the ontology with SPARQL"""
        try:
            results = self.graph.query(query_string)
            
            # Convert results to a more JSON-friendly format
            if results.type == 'SELECT':
                bindings = []
                for row in results:
                    binding = {}
                    for var in results.vars:
                        value = row[var]
                        if value:
                            if isinstance(value, URIRef):
                                binding[var] = {'type': 'uri', 'value': str(value)}
                            elif isinstance(value, Literal):
                                binding[var] = {
                                    'type': 'literal',
                                    'value': str(value),
                                    'datatype': str(value.datatype) if value.datatype else None,
                                    'language': value.language if value.language else None
                                }
                            elif isinstance(value, BNode):
                                binding[var] = {'type': 'bnode', 'value': str(value)}
                            else:
                                binding[var] = {'type': 'unknown', 'value': str(value)}
                    bindings.append(binding)
                
                return {
                    'head': {'vars': [str(var) for var in results.vars]},
                    'results': {'bindings': bindings}
                }
            
            elif results.type == 'ASK':
                return {'boolean': results.askAnswer}
            
            elif results.type == 'CONSTRUCT' or results.type == 'DESCRIBE':
                # Return as Turtle
                return {'turtle': results.serialize(format='turtle')}
            
            else:
                return {'error': f'Unsupported query type: {results.type}'}
        
        except Exception as e:
            return {'error': str(e)}
    
    def create_client(self):
        """Create a client for the TokenFlow API"""
        return TokenFlowClient(f"http://{self.host}:{self.port}")

class TokenFlowClient:
    """Client for interacting with the TokenFlow API"""
    
    def __init__(self, base_url):
        """Initialize with the base URL of the API"""
        self.base_url = base_url
    
    def health_check(self):
        """Check if the API is running"""
        try:
            response = requests.get(f"{self.base_url}/api/health")
            return response.json()
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def validate_instance(self, type_uri, properties):
        """Validate an instance against class definitions"""
        try:
            response = requests.post(
                f"{self.base_url}/api/validate/instance",
                json={'type': type_uri, 'properties': properties}
            )
            return response.json()
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def validate_triple(self, subject, predicate, object_value):
        """Validate a subject-predicate-object triple"""
        try:
            response = requests.post(
                f"{self.base_url}/api/validate/triple",
                json={'subject': subject, 'predicate': predicate, 'object': object_value}
            )
            return response.json()
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def validate_with_shacl(self, data, shapes=None):
        """Validate data against SHACL shapes"""
        payload = {'data': data}
        if shapes:
            payload['shapes'] = shapes
        
        try:
            response = requests.post(
                f"{self.base_url}/api/validate/shacl",
                json=payload
            )
            return response.json()
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def query_ontology(self, query_string):
        """Query the ontology with SPARQL"""
        try:
            response = requests.post(
                f"{self.base_url}/api/query",
                json={'query': query_string}
            )
            return response.json()
        except Exception as e:
            return {'error': str(e)}

# Integration with AmedeoOntologyAnalyzer
class EnhancedAmedeoOntologyAnalyzer:
    """Enhanced AMEDEO Ontology Analyzer with TokenFlow integration"""
    
    def __init__(self, host='localhost', port=5000):
        """Initialize the analyzer"""
        from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer
        
        self.base_analyzer = AmedeoOntologyAnalyzer()
        self.tokenflow_integration = TokenFlowIntegration(host=host, port=port)
    
    def parse_turtle(self, ttl_data):
        """Parse Turtle data into the graph"""
        self.base_analyzer.parse_turtle(ttl_data)
        self.tokenflow_integration.set_graph(self.base_analyzer.graph)
    
    def parse_xml(self, xml_data):
        """Parse OWL/XML data into the graph"""
        self.base_analyzer.parse_xml(xml_data)
        self.tokenflow_integration.set_graph(self.base_analyzer.graph)
    
    def parse_jsonld(self, jsonld_data):
        """Parse JSON-LD data into the graph"""
        self.base_analyzer.parse_jsonld(jsonld_data)
        self.tokenflow_integration.set_graph(self.base_analyzer.graph)
    
    def start_api_server(self, debug=False):
        """Start the API server for TokenFlow integration"""
        return self.tokenflow_integration.start_server(debug)
    
    def stop_api_server(self):
        """Stop the API server"""
        return self.tokenflow_integration.stop_server()
    
    def create_tokenflow_client(self):
        """Create a client for the TokenFlow API"""
        return self.tokenflow_integration.create_client()
    
    # Forward other methods to base_analyzer
    def __getattr__(self, name):
        return getattr(self.base_analyzer, name)
```

## 6. Complete Integration Example

```python
# amedeo_ontology_analyzer_extended.py - Complete integration of all extensions

import os
import sys
import argparse
import json
import logging
from rdflib import Graph

# Import base analyzer
from amedeo_ontology_analyzer import AmedeoOntologyAnalyzer

# Import extensions
from visualization_extension import OntologyVisualizer
from validation_extension import OWL2DLValidator
from mapping_extension import OntologyMappingManager
from federation_extension import FederationAnchorManager
from tokenflow_extension import TokenFlowIntegration, TokenFlowClient

class AmedeoOntologyAnalyzerExtended:
    """Extended AMEDEO Ontology Analyzer with all extensions"""
    
    def __init__(self, api_host='localhost', api_port=5000):
        """Initialize the extended analyzer"""
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('AmedeoOntologyAnalyzerExtended')
        
        # Initialize base analyzer
        self.base_analyzer = AmedeoOntologyAnalyzer()
        
        # Initialize extensions
        self.visualizer = OntologyVisualizer()
        self.validator = OWL2DLValidator()
        self.mapping_manager = OntologyMappingManager()
        self.federation_manager = FederationAnchorManager()
        self.tokenflow_integration = TokenFlowIntegration(host=api_host, port=api_port)
        
        # Set graph reference for all components
        self.graph = self.base_analyzer.graph
    
    def parse_ontology(self, file_path=None, data=None, format='turtle'):
        """Parse an ontology from a file or data string"""
        try:
            if file_path:
                self.logger.info(f"Loading ontology from file: {file_path}")
                self.graph.parse(file_path, format=format)
            elif data:
                self.logger.info(f"Loading ontology from data string")
                self.graph.parse(data=data, format=format)
            else:
                raise ValueError("Either file_path or data must be provided")
            
            # Update graph reference in all components
            self.visualizer.set_graph(self.graph)
            self.validator.set_graph(self.graph)
            self.mapping_manager.set_graph(self.graph)
            self.federation_manager.set_graph(self.graph)
            self.tokenflow_integration.set_graph(self.graph)
            
            self.logger.info(f"Loaded {len(self.graph)} triples")
            return True
        
        except Exception as e:
            self.logger.error(f"Error parsing ontology: {str(e)}")
            return False
    
    def analyze_ontology(self):
        """Perform comprehensive analysis of the ontology"""
        self.logger.info("Analyzing ontology...")
        
        # Basic analysis from base analyzer
        base_analysis = self.base_analyzer.analyze_ontology()
        
        # OWL 2 DL validation
        validation = self.validator.validate_owl2_dl()
        
        # Extract mappings
        mappings = self.mapping_manager.extract_mappings_from_graph()
        mapping_analysis = self.mapping_manager.analyze_mappings()
        
        # Identify federation anchors
        federation_anchors = self.federation_manager.identify_federation_anchors()
        federation_analysis = self.federation_manager.analyze_federation_coverage()
        
        # Combine all analyses
        analysis = {
            'base_analysis': base_analysis,
            'validation': validation,
            'mapping_analysis': mapping_analysis,
            'federation_analysis': federation_analysis
        }
        
        self.logger.info("Analysis complete")
        return analysis
    
    def visualize_ontology(self, output_file="ontology_graph.html", use_pyvis=True):
        """Visualize the ontology"""
        self.logger.info(f"Visualizing ontology with {'Pyvis' if use_pyvis else 'D3.js'}")
        
        if use_pyvis:
            return self.visualizer.visualize_with_pyvis(output_file)
        else:
            return self.visualizer.create_d3_visualization()
    
    def generate_reports(self, output_dir="reports", format='markdown'):
        """Generate all reports"""
        self.logger.info(f"Generating reports in {format} format")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate validation report
        validation_report = self.validator.generate_validation_report(format)
        validation_file = os.path.join(output_dir, f"validation_report.{format}")
        with open(validation_file, 'w') as f:
            f.write(validation_report)
        
        # Generate mapping report
        mapping_report = self.mapping_manager.generate_mapping_report(format)
        mapping_file = os.path.join(output_dir, f"mapping_report.{format}")
        with open(mapping_file, 'w') as f:
            f.write(mapping_report)
        
        # Generate federation report
        federation_report = self.federation_manager.generate_federation_report(format)
        federation_file = os.path.join(output_dir, f"federation_report.{format}")
        with open(federation_file, 'w') as f:
            f.write(federation_report)
        
        # Generate SHACL shapes for federation anchors
        shacl_shapes = self.federation_manager.generate_shacl_shapes()
        shacl_file = os.path.join(output_dir, "federation_shapes.ttl")
        with open(shacl_file, 'w') as f:
            f.write(shacl_shapes)
        
        self.logger.info(f"Reports generated in {output_dir}")
        return {
            'validation_report': validation_file,
            'mapping_report': mapping_file,
            'federation_report': federation_file,
            'shacl_shapes': shacl_file
        }
    
    def start_api_server(self, debug=False):
        """Start the API server for TokenFlow integration"""
        self.logger.info(f"Starting API server on {self.tokenflow_integration.host}:{self.tokenflow_integration.port}")

```

## GenAI Proposal Status Disclaimer

*This document is a GenAI-generated proposal and has not been validated by domain experts. The implementation details are theoretical and would need formal review and validation by specialists in ontological engineering and semantic web technologies.*

# Domain Integration for AMEDEO Ontology Analyzer

Great! Purchasing the domain `gaiaair.org` is an excellent step for establishing a proper namespace for your ontologies and services. This domain will help create persistent, professional URIs for your ontology components and provide a hosting location for the analyzer services.

## Integrating the Domain with AMEDEO Ontology Analyzer

Here's how we can update the AMEDEO Ontology Analyzer to use your new domain:

### 1. Update Namespace URIs

```python
# Update the namespace definitions in the analyzer to use your domain
from rdflib import Namespace

# Replace existing namespaces with your domain-based ones
AMEDEO = Namespace("http://www.gaiaair.org/ontologies/amedeo#")
QAO = Namespace("http://www.gaiaair.org/ontologies/qao#")
PET = Namespace("http://www.gaiaair.org/ontologies/pet-core#")
AMPEL = Namespace("http://www.gaiaair.org/ontologies/ampel#")

# Add new namespaces for federation anchors and shapes
AMEDEO_SHAPES = Namespace("http://www.gaiaair.org/ontologies/amedeo/shapes#")
GAIA_CORE = Namespace("http://www.gaiaair.org/ontologies/gaia-core#")
```

### 2. Configure TokenFlow Integration to Use the Domain

```python
# Update the TokenFlow integration to use your domain
class TokenFlowIntegration:
    def __init__(self, graph=None, host='api.gaiaair.org', port=443):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.server_thread = None
        self.running = False
        self.logger = logging.getLogger('TokenFlowIntegration')
        
        # Set up API routes
        self.setup_routes()
```

### 3. Create a Domain Configuration Module

```python
# domain_config.py - Configuration for domain-based services

class DomainConfig:
    """Configuration for domain-based services"""
    
    # Base domain
    BASE_DOMAIN = "gaiaair.org"
    
    # Ontology namespaces
    ONTOLOGY_BASE = f"http://www.{BASE_DOMAIN}/ontologies"
    AMEDEO_NS = f"{ONTOLOGY_BASE}/amedeo#"
    QAO_NS = f"{ONTOLOGY_BASE}/qao#"
    PET_NS = f"{ONTOLOGY_BASE}/pet-core#"
    AMPEL_NS = f"{ONTOLOGY_BASE}/ampel#"
    GAIA_CORE_NS = f"{ONTOLOGY_BASE}/gaia-core#"
    
    # Service endpoints
    API_ENDPOINT = f"https://api.{BASE_DOMAIN}"
    VISUALIZATION_ENDPOINT = f"https://viz.{BASE_DOMAIN}"
    VALIDATION_ENDPOINT = f"https://validate.{BASE_DOMAIN}"
    
    # Documentation
    DOCS_ENDPOINT = f"https://docs.{BASE_DOMAIN}"
    
    @classmethod
    def get_ontology_uri(cls, ontology_name):
        """Get the URI for a specific ontology"""
        return f"{cls.ONTOLOGY_BASE}/{ontology_name}"
    
    @classmethod
    def get_federation_anchor_uri(cls, anchor_id):
        """Get the URI for a federation anchor"""
        return f"{cls.GAIA_CORE_NS}FederationAnchor-{anchor_id}"
```

### 4. Update Federation Anchor Manager to Use Domain

```python
# Update the Federation Anchor Manager to use your domain
class FederationAnchorManager:
    """Manager for federation anchors in AMEDEO Ontology"""
    
    def __init__(self, graph=None):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.amedeo = Namespace("http://www.gaiaair.org/ontologies/amedeo#")
        self.gaia_core = Namespace("http://www.gaiaair.org/ontologies/gaia-core#")
        self.federation_anchors = []
        
    def generate_shacl_shapes(self, output_file=None):
        """Generate SHACL shapes for validating federation anchors"""
        shacl_graph = Graph()
        
        # Define namespaces
        sh = Namespace("http://www.w3.org/ns/shacl#")
        shacl_graph.bind("sh", sh)
        shacl_graph.bind("owl", OWL)
        shacl_graph.bind("rdfs", RDFS)
        shacl_graph.bind("amedeo", self.amedeo)
        shacl_graph.bind("gaia-core", self.gaia_core)
        
        # Create shape for FederationAnchor
        anchor_shape = URIRef("http://www.gaiaair.org/ontologies/amedeo/shapes#FederationAnchorShape")
        # ... rest of the method
```

## Deployment Recommendations for Your Domain

Now that you have the domain, here are some recommendations for deploying the AMEDEO Ontology Analyzer:

1. **Set up subdomain DNS records**:

1. `api.gaiaair.org` - For the TokenFlow API endpoints
2. `viz.gaiaair.org` - For visualization interfaces
3. `docs.gaiaair.org` - For documentation
4. `ontology.gaiaair.org` - For serving ontology files



2. **Configure SSL certificates**:

1. Use Vercel's automatic SSL certificate provisioning
2. Ensure all endpoints use HTTPS



3. **Deploy the analyzer as a web service**:

1. Package the analyzer as a Docker container
2. Deploy to Vercel or another cloud provider
3. Configure the API endpoints to use your domain



4. **Create a persistent ontology repository**:

1. Set up content negotiation for ontology URIs
2. Ensure ontology URIs resolve to human-readable documentation and machine-readable formats





## Example Implementation for Domain-Based Ontology Serving

```python
# ontology_server.py - Server for ontology content negotiation

from flask import Flask, request, Response, redirect
import os
import mimetypes

app = Flask(__name__)

ONTOLOGY_DIR = "ontologies"

@app.route('/ontologies/<ontology_name>')
def serve_ontology(ontology_name):
    """Serve ontology files with content negotiation"""
    # Check if ontology exists
    base_path = os.path.join(ONTOLOGY_DIR, ontology_name)
    
    if not os.path.exists(f"{base_path}.ttl"):
        return "Ontology not found", 404
    
    # Content negotiation
    accept = request.headers.get('Accept', '')
    
    if 'text/html' in accept or 'application/xhtml+xml' in accept:
        # Redirect to HTML documentation
        return redirect(f"/docs/ontologies/{ontology_name}")
    
    elif 'application/rdf+xml' in accept:
        # Serve RDF/XML
        with open(f"{base_path}.owl", 'rb') as f:
            return Response(f.read(), mimetype='application/rdf+xml')
    
    elif 'application/n-triples' in accept:
        # Serve N-Triples
        with open(f"{base_path}.nt", 'rb') as f:
            return Response(f.read(), mimetype='application/n-triples')
    
    elif 'application/ld+json' in accept:
        # Serve JSON-LD
        with open(f"{base_path}.jsonld", 'rb') as f:
            return Response(f.read(), mimetype='application/ld+json')
    
    else:
        # Default to Turtle
        with open(f"{base_path}.ttl", 'rb') as f:
            return Response(f.read(), mimetype='text/turtle')

if __name__ == '__main__':
    app.run(debug=True)
```

## Next Steps

1. **Update all namespace URIs** in your ontologies to use the new domain
2. **Configure DNS settings** in Vercel for your subdomains
3. **Set up SSL certificates** for secure access
4. **Deploy the analyzer** as a web service using your domain
5. **Create a landing page** at `www.gaiaair.org` explaining the project
6. **Implement content negotiation** for ontology URIs


Having your own domain will significantly enhance the professionalism and persistence of your ontology ecosystem, making it more reliable for others to reference and integrate with.
