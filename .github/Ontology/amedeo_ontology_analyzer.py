# amedeo_ontology_analyzer.py - Updated with gaiaair.org domain

import rdflib
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD
import io
import json
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

class AmedeoOntologyAnalyzer:
    def __init__(self):
        self.graph = Graph()
        # Updated namespaces with gaiaair.org domain
        self.amedeo = Namespace("http://www.gaiaair.org/ontologies/amedeo#")
        self.qao = Namespace("http://www.gaiaair.org/ontologies/qao#")
        self.pet = Namespace("http://www.gaiaair.org/ontologies/pet-core#")
        self.ampel = Namespace("http://www.gaiaair.org/ontologies/ampel#")
        self.gaia_core = Namespace("http://www.gaiaair.org/ontologies/gaia-core#")
        self.amedeo_shapes = Namespace("http://www.gaiaair.org/ontologies/amedeo/shapes#")
        
        # Bind namespaces
        self.graph.bind("amedeo", self.amedeo)
        self.graph.bind("qao", self.qao)
        self.graph.bind("pet", self.pet)
        self.graph.bind("ampel", self.ampel)
        self.graph.bind("gaia-core", self.gaia_core)
        self.graph.bind("amedeo-shapes", self.amedeo_shapes)
        self.graph.bind("owl", OWL)
        self.graph.bind("rdfs", RDFS)
    
    # Rest of the class remains the same
    # ...
