def analyze_living_loops(self):
    """Analyze Living Loops in the ontology"""
    loops = []
    
    # Find all Living Loop instances
    for s, p, o in self.graph.triples((None, RDF.type, self.ll.LivingLoop)):
        loop = {
            "uri": s,
            "label": self._get_label_or_id(s),
            "nodes": [],
            "cycles": [],
            "pathways": [],
            "domain": None
        }
        
        # Get implementation domain
        for s2, p2, o2 in self.graph.triples((s, self.ll.implementedIn, None)):
            loop["domain"] = {
                "uri": o2,
                "label": self._get_label_or_id(o2)
            }
        
        # Find nodes in this loop
        for s2, p2, o2 in self.graph.triples((s, self.ll.hasNode, None)):
            node = {
                "uri": o2,
                "label": self._get_label_or_id(o2),
                "type": None,
                "connections": []
            }
            
            # Get node type
            for s3, p3, o3 in self.graph.triples((o2, RDF.type, None)):
                if o3 in [self.ll.EnergyNode, self.ll.EnvironmentalNode, 
                          self.ll.KnowledgeNode, self.ll.SolidarityNode,
                          self.ll.RegenerationNode, self.ll.AdaptiveNode]:
                    node["type"] = o3
            
            # Get node connections
            for s3, p3, o3 in self.graph.triples((o2, self.ll.connectsTo, None)):
                connection = {
                    "target": o3,
                    "type": p3
                }
                node["connections"].append(connection)
            
            loop["nodes"].append(node)
        
        # Find cycles in this loop
        for s2, p2, o2 in self.graph.triples((s, self.ll.hasCycle, None)):
            cycle = {
                "uri": o2,
                "label": self._get_label_or_id(o2),
                "type": None,
                "efficiency": None
            }
            
            # Get cycle type
            for s3, p3, o3 in self.graph.triples((o2, RDF.type, None)):
                if o3 in [self.ll.EnergyCycle, self.ll.KnowledgeCycle, 
                          self.ll.SolidarityCycle, self.ll.RegenerationCycle]:
                    cycle["type"] = o3
            
            # Get cycle efficiency
            for s3, p3, o3 in self.graph.triples((o2, self.ll.cycleEfficiency, None)):
                cycle["efficiency"] = float(o3)
            
            loop["cycles"].append(cycle)
        
        # Find pathways in this loop
        for s2, p2, o2 in self.graph.triples((s, self.ll.hasPathway, None)):
            pathway = {
                "uri": o2,
                "label": self._get_label_or_id(o2),
                "density": None
            }
            
            # Get pathway density
            for s3, p3, o3 in self.graph.triples((o2, self.ll.pathwayDensity, None)):
                pathway["density"] = float(o3)
            
            loop["pathways"].append(pathway)
        
        loops.append(loop)
    
    return loops

def _get_label_or_id(self, uri):
    """Get the label of a resource or its ID if no label exists"""
    for s, p, o in self.graph.triples((uri, RDFS.label, None)):
        return str(o)
    
    # If no label, return the last part of the URI
    if "#" in uri:
        return uri.split("#")[-1]
    return uri.split("/")[-1]

def visualize_living_loops(self):
    """Create a NetworkX graph of Living Loops and their connected nodes"""
    G = nx.DiGraph()
    
    # Add all Living Loops as nodes
    for s, p, o in self.graph.triples((None, RDF.type, self.ll.LivingLoop)):
        G.add_node(self._get_label_or_id(s), type="LivingLoop")
    
    # Add all nodes in Living Loops
    for s, p, o in self.graph.triples((None, self.ll.hasNode, None)):
        loop_name = self._get_label_or_id(s)
        node_name = self._get_label_or_id(o)
        
        # Get node type
        node_type = "Node"
        for s2, p2, o2 in self.graph.triples((o, RDF.type, None)):
            if o2 in [self.ll.EnergyNode, self.ll.EnvironmentalNode, 
                      self.ll.KnowledgeNode, self.ll.SolidarityNode,
                      self.ll.RegenerationNode, self.ll.AdaptiveNode]:
                node_type = self._get_label_or_id(o2)
        
        G.add_node(node_name, type=node_type)
        G.add_edge(loop_name, node_name, relation="hasNode")
    
    # Add connections between nodes
    for s, p, o in self.graph.triples((None, self.ll.connectsTo, None)):
        source_name = self._get_label_or_id(s)
        target_name = self._get_label_or_id(o)
        
        # Get connection type
        conn_type = "connectsTo"
        if p in [self.ll.transfersEnergy, self.ll.sharesKnowledge, 
                 self.ll.providesSupportTo, self.ll.regeneratesEnvironmentFor]:
            conn_type = self._get_label_or_id(p)
        
        G.add_edge(source_name, target_name, relation=conn_type)
    
    return G
