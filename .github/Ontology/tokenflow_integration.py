# tokenflow_integration.py - Updated with gaiaair.org domain

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
from domain_config import DomainConfig

class TokenFlowIntegration:
    """Integration with TokenFlow pipeline for AMEDEO Ontology"""
    
    def __init__(self, graph=None, host='api.gaiaair.org', port=443):
        """Initialize with an optional RDFLib graph"""
        self.graph = graph if graph is not None else Graph()
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.server_thread = None
        self.running = False
        self.logger = logging.getLogger('TokenFlowIntegration')
        
        # Use domain config for namespaces
        self.amedeo = DomainConfig.get_namespace("amedeo")
        
        # Set up API routes
        self.setup_routes()
    
    # Rest of the class remains the same
    # ...
