# ontology_server.py - Content negotiation for ontologies

from flask import Flask, request, Response, redirect, render_template
import os
import mimetypes
from rdflib import Graph
from domain_config import DomainConfig

app = Flask(__name__)

ONTOLOGY_DIR = "ontologies"

@app.route('/')
def index():
    """Landing page for the ontology server"""
    ontologies = []
    for filename in os.listdir(ONTOLOGY_DIR):
        if filename.endswith('.ttl'):
            ontology_name = filename[:-4]  # Remove .ttl extension
            ontologies.append({
                'name': ontology_name,
                'uri': f"{DomainConfig.ONTOLOGY_BASE}/{ontology_name}"
            })
    
    return render_template('index.html', ontologies=ontologies)

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
        return redirect(f"{DomainConfig.DOCS_ENDPOINT}/ontologies/{ontology_name}")
    
    elif 'application/rdf+xml' in accept:
        # Serve RDF/XML
        if os.path.exists(f"{base_path}.owl"):
            with open(f"{base_path}.owl", 'rb') as f:
                return Response(f.read(), mimetype='application/rdf+xml')
        else:
            # Convert Turtle to RDF/XML on the fly
            g = Graph()
            g.parse(f"{base_path}.ttl", format="turtle")
            return Response(g.serialize(format="xml"), mimetype='application/rdf+xml')
    
    elif 'application/n-triples' in accept:
        # Serve N-Triples
        if os.path.exists(f"{base_path}.nt"):
            with open(f"{base_path}.nt", 'rb') as f:
                return Response(f.read(), mimetype='application/n-triples')
        else:
            # Convert Turtle to N-Triples on the fly
            g = Graph()
            g.parse(f"{base_path}.ttl", format="turtle")
            return Response(g.serialize(format="nt"), mimetype='application/n-triples')
    
    elif 'application/ld+json' in accept:
        # Serve JSON-LD
        if os.path.exists(f"{base_path}.jsonld"):
            with open(f"{base_path}.jsonld", 'rb') as f:
                return Response(f.read(), mimetype='application/ld+json')
        else:
            # Convert Turtle to JSON-LD on the fly
            g = Graph()
            g.parse(f"{base_path}.ttl", format="turtle")
            return Response(g.serialize(format="json-ld"), mimetype='application/ld+json')
    
    else:
        # Default to Turtle
        with open(f"{base_path}.ttl", 'rb') as f:
            return Response(f.read(), mimetype='text/turtle')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
