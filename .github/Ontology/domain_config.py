# domain_config.py - Configuration for domain-based services

class DomainConfig:
    """Configuration for domain-based services for AMEDEO Ontology Analyzer"""
    
    # Base domain
    BASE_DOMAIN = "gaiaair.org"
    
    # Ontology namespaces
    ONTOLOGY_BASE = f"http://www.{BASE_DOMAIN}/ontologies"
    AMEDEO_NS = f"{ONTOLOGY_BASE}/amedeo#"
    QAO_NS = f"{ONTOLOGY_BASE}/qao#"
    PET_NS = f"{ONTOLOGY_BASE}/pet-core#"
    AMPEL_NS = f"{ONTOLOGY_BASE}/ampel#"
    GAIA_CORE_NS = f"{ONTOLOGY_BASE}/gaia-core#"
    AMEDEO_SHAPES_NS = f"{ONTOLOGY_BASE}/amedeo/shapes#"
    
    # Service endpoints
    API_ENDPOINT = f"https://api.{BASE_DOMAIN}"
    VISUALIZATION_ENDPOINT = f"https://viz.{BASE_DOMAIN}"
    VALIDATION_ENDPOINT = f"https://validate.{BASE_DOMAIN}"
    ONTOLOGY_ENDPOINT = f"https://ontology.{BASE_DOMAIN}"
    
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
    
    @classmethod
    def get_namespace(cls, namespace_name):
        """Get a namespace by name"""
        from rdflib import Namespace
        namespaces = {
            "amedeo": Namespace(cls.AMEDEO_NS),
            "qao": Namespace(cls.QAO_NS),
            "pet": Namespace(cls.PET_NS),
            "ampel": Namespace(cls.AMPEL_NS),
            "gaia-core": Namespace(cls.GAIA_CORE_NS),
            "amedeo-shapes": Namespace(cls.AMEDEO_SHAPES_NS)
        }
        return namespaces.get(namespace_name)
