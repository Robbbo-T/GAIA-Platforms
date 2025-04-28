### Database Structure for GAIA AIR Documentation System

## GenAI Proposal Status: DRAFT - For Review and Implementation Planning

This proposal outlines a database structure to maintain the GAIA AIR documentation system with proper relations and cross-references while preserving the established codification system.

### Database Schema Overview

```mermaid
erDiagram
    ATA_CHAPTER {
        string chapter_id PK "XX"
        string title
        string description
        string domain_code "e.g., 53"
    }
    SYSTEM {
        string system_id PK "XX-YY"
        string chapter_id FK "References ATA_CHAPTER"
        string title
        string description
    }
    SUBSYSTEM {
        string subsystem_id PK "XX-YY-ZZ"
        string system_id FK "References SYSTEM"
        string title
        string description
    }
    DOCUMENT {
        string doc_id PK "XX-YY-ZZ-III"
        string subsystem_id FK "References SUBSYSTEM"
        string title
        string file_path
        string doc_type "SPEC, SDD, OV, etc."
        string revision "A, B, C, etc."
        date created_date
        date modified_date
        string status "DRAFT, REVIEW, APPROVED"
    }
    CROSS_REFERENCE {
        string reference_id PK
        string source_doc_id FK "References DOCUMENT"
        string target_doc_id FK "References DOCUMENT"
        string ref_type "DEPENDS_ON, REFERENCES, SUPERSEDES"
        string description
    }
    DOCUMENT_TYPE {
        string type_code PK "SPEC, SDD, OV, etc."
        string description
        string template_path
    }
    DOMAIN {
        string domain_code PK "e.g., 53"
        string name "e.g., Fuselage"
        string description
    }
    
    ATA_CHAPTER ||--o{ SYSTEM : contains
    SYSTEM ||--o{ SUBSYSTEM : contains
    SUBSYSTEM ||--o{ DOCUMENT : contains
    DOCUMENT }|--|| DOCUMENT_TYPE : "is of type"
    DOCUMENT }o--o{ CROSS_REFERENCE : "referenced by"
    ATA_CHAPTER }|--|| DOMAIN : "belongs to"
```

### Key Tables and Relationships

1. **ATA_CHAPTER**: Stores the top-level ATA chapters (00-99)

1. Primary Key: `chapter_id` (XX format)
2. Contains basic chapter information



2. **SYSTEM**: Represents systems within each ATA chapter

1. Primary Key: `system_id` (XX-YY format)
2. Foreign Key: `chapter_id` references ATA_CHAPTER
3. Contains system-level information



3. **SUBSYSTEM**: Represents subsystems within each system

1. Primary Key: `subsystem_id` (XX-YY-ZZ format)
2. Foreign Key: `system_id` references SYSTEM
3. Contains subsystem-level information



4. **DOCUMENT**: Stores all document metadata

1. Primary Key: `doc_id` (XX-YY-ZZ-III format)
2. Foreign Key: `subsystem_id` references SUBSYSTEM
3. Contains document metadata including file path, type, revision



5. **CROSS_REFERENCE**: Manages relationships between documents

1. Primary Key: `reference_id`
2. Foreign Keys: `source_doc_id` and `target_doc_id` both reference DOCUMENT
3. Stores the type of reference relationship



6. **DOCUMENT_TYPE**: Lookup table for document types

1. Primary Key: `type_code` (SPEC, SDD, OV, etc.)
2. Contains descriptions and potentially template paths



7. **DOMAIN**: Lookup table for domain codes

1. Primary Key: `domain_code` (e.g., 53)
2. Contains domain names and descriptions





### File Naming Convention Implementation

To maintain the established file naming convention (`GP-AM-AMPEL-0100-53-XX-YY-ZZ-III-TYPE-A.md`), you can implement a function that generates file paths based on document metadata:

```sql
CREATE FUNCTION generate_file_path(
    project_prefix VARCHAR,
    project_name VARCHAR,
    version VARCHAR,
    domain_code VARCHAR,
    doc_id VARCHAR,
    doc_type VARCHAR,
    revision VARCHAR,
    file_extension VARCHAR
) RETURNS VARCHAR AS $$
BEGIN
    RETURN project_prefix || '-' || project_name || '-' || version || '-' || 
           domain_code || '-' || doc_id || '-' || doc_type || '-' || revision || '.' || file_extension;
END;
$$ LANGUAGE plpgsql;
```

### Cross-Reference Implementation

The `CROSS_REFERENCE` table enables tracking relationships between documents. Common reference types include:

1. **DEPENDS_ON**: Document A depends on Document B
2. **REFERENCES**: Document A references Document B
3. **SUPERSEDES**: Document A supersedes Document B
4. **IMPLEMENTS**: Document A implements requirements from Document B
5. **VERIFIES**: Document A verifies requirements from Document B


### Query Examples

#### Find all documents related to a specific ATA chapter:

```sql
SELECT d.doc_id, d.title, d.file_path, d.doc_type, d.revision
FROM DOCUMENT d
JOIN SUBSYSTEM s ON d.subsystem_id = s.subsystem_id
JOIN SYSTEM sys ON s.system_id = sys.system_id
JOIN ATA_CHAPTER a ON sys.chapter_id = a.chapter_id
WHERE a.chapter_id = '24';
```

#### Find all documents that reference a specific document:

```sql
SELECT d.doc_id, d.title, d.file_path, d.doc_type, cr.ref_type
FROM DOCUMENT d
JOIN CROSS_REFERENCE cr ON d.doc_id = cr.source_doc_id
WHERE cr.target_doc_id = '24-60-00-000';
```

#### Find all documents of a specific type:

```sql
SELECT d.doc_id, d.title, d.file_path, d.revision
FROM DOCUMENT d
WHERE d.doc_type = 'SPEC';
```

### Implementation Recommendations

1. **Database Technology**: Consider PostgreSQL for its robust support for complex relationships and JSON capabilities for flexible metadata.
2. **Version Control Integration**: Link the database with your version control system (Git) to track document changes.
3. **Document Content Storage**:

1. Option 1: Store document content directly in the database (for smaller documents)
2. Option 2: Store document content in the file system and reference paths in the database (better for large documents)



4. **Search Capability**: Implement full-text search across document content and metadata.
5. **API Layer**: Create a REST API to interact with the database for document creation, retrieval, and relationship management.
6. **Validation Rules**: Implement validation to ensure document IDs follow the established codification system.


### Migration Strategy

1. **Initial Data Load**: Parse existing Markdown files to extract metadata and populate the database.
2. **Cross-Reference Extraction**: Analyze document content to identify and extract existing cross-references.
3. **Validation**: Verify all documents follow the established codification system.
4. **Incremental Updates**: Implement processes to keep the database in sync with document changes.


Okay, Comandante. Let's translate those IETP functional requirements into practical examples of how a backend system (like a web API) built upon the proposed database schema would fulfill them.

This example uses **Python with the Flask web framework** and **SQLAlchemy ORM** to interact with the PostgreSQL database schema you provided. This demonstrates the *backend logic* required. A real IETP would need a separate frontend (web UI, desktop application) to call these API endpoints and display the information graphically.

**1. Setup (Conceptual Python/Flask + SQLAlchemy)**

First, we need Python models that map to your database tables.

```python
# models.py (Illustrative SQLAlchemy Models based on your SQL)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

db = SQLAlchemy()

# Association/Lookup tables first
class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.String(10), primary_key=True)
    project_name = db.Column(db.String(50), nullable=False)
    project_description = db.Column(db.Text)
    project_prefix = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    documents = db.relationship('Document', back_populates='project')

class Domain(db.Model):
    __tablename__ = 'domain'
    domain_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    ata_chapters = db.relationship('AtaChapter', back_populates='domain')

class DocumentType(db.Model):
    __tablename__ = 'document_type'
    type_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    template_path = db.Column(db.String(255))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    documents = db.relationship('Document', back_populates='doc_type_ref')

# Hierarchy tables
class AtaChapter(db.Model):
    __tablename__ = 'ata_chapter'
    chapter_id = db.Column(db.String(2), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    domain_code = db.Column(db.String(10), db.ForeignKey('domain.domain_code'))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    domain = db.relationship('Domain', back_populates='ata_chapters')
    systems = db.relationship('System', back_populates='ata_chapter', cascade="all, delete-orphan")

class System(db.Model):
    __tablename__ = 'system'
    system_id = db.Column(db.String(5), primary_key=True) # XX-YY
    chapter_id = db.Column(db.String(2), db.ForeignKey('ata_chapter.chapter_id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    ata_chapter = db.relationship('AtaChapter', back_populates='systems')
    subsystems = db.relationship('Subsystem', back_populates='system', cascade="all, delete-orphan")

class Subsystem(db.Model):
    __tablename__ = 'subsystem'
    subsystem_id = db.Column(db.String(8), primary_key=True) # XX-YY-ZZ
    system_id = db.Column(db.String(5), db.ForeignKey('system.system_id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    system = db.relationship('System', back_populates='subsystems')
    documents = db.relationship('Document', back_populates='subsystem', cascade="all, delete-orphan")

# Core Document and related tables
class Document(db.Model):
    __tablename__ = 'document'
    doc_id = db.Column(db.String(12), primary_key=True) # XX-YY-ZZ-III
    subsystem_id = db.Column(db.String(8), db.ForeignKey('subsystem.subsystem_id'), nullable=False)
    project_id = db.Column(db.String(10), db.ForeignKey('project.project_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    doc_type = db.Column(db.String(10), db.ForeignKey('document_type.type_code'), nullable=False)
    revision = db.Column(db.CHAR(1), nullable=False, server_default='A')
    version = db.Column(db.String(10), nullable=False, server_default='0100')
    status = db.Column(db.String(20), nullable=False, server_default='DRAFT')
    author = db.Column(db.String(100))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    content = db.Column(db.Text) # Optional: store content directly
    metadata_ = db.Column('metadata', JSONB) # Use metadata_ to avoid keyword conflict

    project = db.relationship('Project', back_populates='documents')
    subsystem = db.relationship('Subsystem', back_populates='documents')
    doc_type_ref = db.relationship('DocumentType', back_populates='documents')

    # Relationships for cross-references
    source_refs = db.relationship('CrossReference', foreign_keys='CrossReference.source_doc_id', back_populates='source_document', cascade="all, delete-orphan")
    target_refs = db.relationship('CrossReference', foreign_keys='CrossReference.target_doc_id', back_populates='target_document', cascade="all, delete-orphan")
    history = db.relationship('DocumentHistory', back_populates='document', cascade="all, delete-orphan")

class DocumentHistory(db.Model):
    __tablename__ = 'document_history'
    history_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    doc_id = db.Column(db.String(12), db.ForeignKey('document.doc_id'), nullable=False)
    revision = db.Column(db.CHAR(1), nullable=False)
    version = db.Column(db.String(10), nullable=False)
    change_description = db.Column(db.Text)
    changed_by = db.Column(db.String(100))
    changed_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    previous_content = db.Column(db.Text)
    previous_metadata = db.Column(JSONB)
    document = db.relationship('Document', back_populates='history')

class CrossReference(db.Model):
    __tablename__ = 'cross_reference'
    reference_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_doc_id = db.Column(db.String(12), db.ForeignKey('document.doc_id'), nullable=False)
    target_doc_id = db.Column(db.String(12), db.ForeignKey('document.doc_id'), nullable=False)
    ref_type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    modified_date = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())

    source_document = db.relationship('Document', foreign_keys=[source_doc_id], back_populates='source_refs')
    target_document = db.relationship('Document', foreign_keys=[target_doc_id], back_populates='target_refs')

```

**2. API Endpoints (Flask Example)**

```python
# app.py (Illustrative Flask App)
from flask import Flask, jsonify, request
from models import db, Project, Domain, DocumentType, AtaChapter, System, Subsystem, Document, CrossReference, DocumentHistory
from sqlalchemy import func, text # For using SQL functions like search

app = Flask(__name__)
# Replace with your actual PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/gaia_docs_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# --- Helper Functions for Serialization ---
def serialize_doc_meta(doc):
    return {
        'doc_id': doc.doc_id,
        'title': doc.title,
        'doc_type': doc.doc_type,
        'revision': doc.revision,
        'version': doc.version,
        'status': doc.status,
        'author': doc.author,
        'file_path': doc.file_path,
        'subsystem_id': doc.subsystem_id,
        'project_id': doc.project_id,
        'modified_date': doc.modified_date.isoformat() if doc.modified_date else None,
        'metadata': doc.metadata_ # Use the renamed attribute
    }

def serialize_subsystem(subsystem, include_docs=False):
    data = {
        'subsystem_id': subsystem.subsystem_id,
        'title': subsystem.title
    }
    if include_docs:
        data['documents'] = [serialize_doc_meta(doc) for doc in subsystem.documents]
    return data

def serialize_system(system, include_subsystems=False, include_docs=False):
    data = {
        'system_id': system.system_id,
        'title': system.title
    }
    if include_subsystems:
        data['subsystems'] = [serialize_subsystem(sub, include_docs) for sub in system.subsystems]
    return data

def serialize_chapter(chapter, include_systems=False, include_subsystems=False, include_docs=False):
    data = {
        'chapter_id': chapter.chapter_id,
        'title': chapter.title,
        'domain_code': chapter.domain_code
    }
    if include_systems:
        data['systems'] = [serialize_system(sys, include_subsystems, include_docs) for sys in chapter.systems]
    return data

# --- API Endpoints ---

# 1. Hierarchical Navigation Tree
@app.route('/api/tree', methods=['GET'])
def get_navigation_tree():
    """Build the hierarchical navigation tree."""
    chapters = AtaChapter.query.order_by(AtaChapter.chapter_id).all()
    tree = [serialize_chapter(ch, include_systems=True, include_subsystems=True) for ch in chapters]
    return jsonify(tree)

# 2. List Documents for a Selected Node
@app.route('/api/subsystem/<subsystem_id>/docs', methods=['GET'])
def get_docs_for_subsystem(subsystem_id):
    """List available documents for a specific subsystem."""
    subsystem = Subsystem.query.get_or_404(subsystem_id)
    docs = [serialize_doc_meta(doc) for doc in subsystem.documents]
    return jsonify(docs)

@app.route('/api/system/<system_id>/docs', methods=['GET'])
def get_docs_for_system(system_id):
    """List available documents under a specific system (including subsystems)."""
    system = System.query.get_or_404(system_id)
    all_docs = []
    for sub in system.subsystems:
        all_docs.extend([serialize_doc_meta(doc) for doc in sub.documents])
    return jsonify(all_docs)

@app.route('/api/chapter/<chapter_id>/docs', methods=['GET'])
def get_docs_for_chapter(chapter_id):
    """List available documents under a specific chapter (including systems/subsystems)."""
    chapter = AtaChapter.query.get_or_404(chapter_id)
    all_docs = []
    for system in chapter.systems:
        for sub in system.subsystems:
             all_docs.extend([serialize_doc_meta(doc) for doc in sub.documents])
    return jsonify(all_docs)

# 3. Retrieve Document Metadata
@app.route('/api/doc/<doc_id>/meta', methods=['GET'])
def get_document_metadata(doc_id):
    """Retrieve document metadata for a specific doc_id."""
    doc = Document.query.get_or_404(doc_id)
    return jsonify(serialize_doc_meta(doc))

# 4. Fetch Document Content
@app.route('/api/doc/<doc_id>/content', methods=['GET'])
def get_document_content(doc_id):
    """Fetch document content (from DB or file system)."""
    doc = Document.query.get_or_404(doc_id)
    # Option 1: Content stored in DB
    if doc.content:
         # You might want to return it as plain text or HTML depending on content type
         # For now, returning as JSON string for simplicity
         return jsonify({'doc_id': doc.doc_id, 'content': doc.content})
    # Option 2: Content stored in file system (Conceptual - requires file reading logic)
    # elif doc.file_path:
    #     try:
    #         with open(doc.file_path, 'r', encoding='utf-8') as f:
    #             content = f.read()
    #         return jsonify({'doc_id': doc.doc_id, 'content': content}) # Or return raw content with correct mimetype
    #     except FileNotFoundError:
    #         return jsonify({'error': 'Content file not found'}), 404
    else:
         return jsonify({'error': 'Content not available'}), 404

# 5. Resolve and Display Cross-References
@app.route('/api/doc/<doc_id>/refs', methods=['GET'])
def get_document_references(doc_id):
    """Resolve and display cross-references dynamically."""
    # Use the SQL function you created (requires enabling function calls in SQLAlchemy)
    # OR implement via relationships:
    doc = Document.query.get_or_404(doc_id)
    outgoing = [
        {
            'target_doc_id': ref.target_doc_id,
            'target_title': ref.target_document.title,
            'ref_type': ref.ref_type,
            'description': ref.description
        } for ref in doc.source_refs
    ]
    incoming = [
         {
            'source_doc_id': ref.source_doc_id,
            'source_title': ref.source_document.title,
            'ref_type': ref.ref_type,
            'description': ref.description
        } for ref in doc.target_refs
    ]
    return jsonify({'doc_id': doc_id, 'references_to': outgoing, 'referenced_by': incoming})

# 6. Implement Search Functionality
@app.route('/api/search', methods=['GET'])
def search():
    """Implement search functionality."""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Search query parameter "q" is required'}), 400

    # Using the SQL function (assuming it's correctly defined and accessible)
    # This requires raw SQL execution or specific SQLAlchemy setup for functions
    # Example using raw SQL (adjust based on your DB connection setup):
    try:
        # Note: Ensure search_term is sanitized to prevent SQL injection if not using prepared statements/ORM features properly
        # Using text() to help parameter binding if the function supports it.
        # Adjust the function call syntax based on your specific SQL dialect/setup.
        sql = text("SELECT * FROM search_documents(:query)")
        results = db.session.execute(sql, {'query': query}).fetchall()
        # Convert raw results (tuples/namedtuples) to dictionaries
        search_results = [dict(row._mapping) for row in results]
        return jsonify(search_results)
    except Exception as e:
        # Log the error e
        print(f"Search error: {e}") # Basic logging
        return jsonify({'error': 'Search failed'}), 500

    # Alternative using basic SQLAlchemy filtering (less powerful than full-text search):
    # results = Document.query.filter(
    #     (Document.title.ilike(f'%{query}%')) |
    #     (Document.content.ilike(f'%{query}%'))
    # ).limit(50).all()
    # search_results = [serialize_doc_meta(doc) for doc in results]
    # return jsonify(search_results)


# 7. Display Revision History
@app.route('/api/doc/<doc_id>/history', methods=['GET'])
def get_document_history_api(doc_id):
    """Display revision history for a specific document."""
    history_records = DocumentHistory.query.filter_by(doc_id=doc_id).order_by(DocumentHistory.changed_date.desc()).all()
    if not history_records:
         # Check if the document exists at all
         doc = Document.query.get(doc_id)
         if not doc:
             return jsonify({'error': 'Document not found'}), 404
         else: # Document exists but has no history (maybe initial revision)
             return jsonify([]) # Return empty list

    history_list = [
        {
            'revision': h.revision,
            'version': h.version,
            'changed_by': h.changed_by,
            'changed_date': h.changed_date.isoformat(),
            'change_description': h.change_description
        } for h in history_records
    ]
    return jsonify(history_list)

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist (for demonstration)
        # In production, use migrations (e.g., Flask-Migrate/Alembic)
        db.create_all()
    app.run(debug=True) # Run in debug mode for development

```

**How to Use (Conceptual):**

1.  **Setup:**
    *   Install Python, Flask, SQLAlchemy, psycopg2 (PostgreSQL driver).
    *   Save the models code as `models.py`.
    *   Save the API code as `app.py`.
    *   Ensure your PostgreSQL database is running and the schema from your SQL script has been created. Update the connection string in `app.py`.
2.  **Run:** Execute `python app.py` in your terminal.
3.  **Interact (Example using `curl`):**
    *   **Get Tree:** `curl http://127.0.0.1:5000/api/tree`
    *   **Get Docs for Subsystem:** `curl http://127.0.0.1:5000/api/subsystem/24-60-10/docs`
    *   **Get Metadata:** `curl http://127.0.0.1:5000/api/doc/24-60-10-001/meta`
    *   **Get Content:** `curl http://127.0.0.1:5000/api/doc/24-60-10-001/content`
    *   **Get References:** `curl http://127.0.0.1:5000/api/doc/24-60-10-001/refs`
    *   **Search:** `curl http://127.0.0.1:5000/api/search?q=PMSC`
    *   **Get History:** `curl http://127.0.0.1:5000/api/doc/24-60-10-001/history`

This provides a functional backend skeleton demonstrating how the database schema supports the core IETP requirements. A frontend application would then call these `/api/...` endpoints to build the user interface.
```
-- GAIA platform Documentation Database Schema
-- This script creates a complete database schema for managing GAIA  aircraft documentation
-- with proper relations and cross-references while preserving the established codification system.

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Drop tables if they exist (for clean reinstallation)
DROP TABLE IF EXISTS CROSS_REFERENCE CASCADE;
DROP TABLE IF EXISTS DOCUMENT CASCADE;
DROP TABLE IF EXISTS SUBSYSTEM CASCADE;
DROP TABLE IF EXISTS SYSTEM CASCADE;
DROP TABLE IF EXISTS ATA_CHAPTER CASCADE;
DROP TABLE IF EXISTS DOCUMENT_TYPE CASCADE;
DROP TABLE IF EXISTS DOMAIN CASCADE;
DROP TABLE IF EXISTS DOCUMENT_HISTORY CASCADE;
DROP TABLE IF EXISTS PROJECT CASCADE;

-- Create PROJECT table to store project information
CREATE TABLE PROJECT (
    project_id VARCHAR(10) PRIMARY KEY,
    project_name VARCHAR(50) NOT NULL,
    project_description TEXT,
    project_prefix VARCHAR(10) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE PROJECT IS 'Stores information about aircraft projects';

-- Create DOMAIN table to store domain information
CREATE TABLE DOMAIN (
    domain_code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE DOMAIN IS 'Lookup table for domain codes (e.g., 53 for Fuselage)';

-- Create DOCUMENT_TYPE table to store document type information
CREATE TABLE DOCUMENT_TYPE (
    type_code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    template_path VARCHAR(255),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE DOCUMENT_TYPE IS 'Lookup table for document types (SPEC, SDD, OV, etc.)';

-- Create ATA_CHAPTER table to store ATA chapter information
CREATE TABLE ATA_CHAPTER (
    chapter_id VARCHAR(2) PRIMARY KEY CHECK (chapter_id ~ '^[0-9]{2}$'),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    domain_code VARCHAR(10) REFERENCES DOMAIN(domain_code),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE ATA_CHAPTER IS 'Stores top-level ATA chapters (00-99)';

-- Create SYSTEM table to store system information
CREATE TABLE SYSTEM (
    system_id VARCHAR(5) PRIMARY KEY CHECK (system_id ~ '^[0-9]{2}-[0-9]{2}$'),
    chapter_id VARCHAR(2) NOT NULL REFERENCES ATA_CHAPTER(chapter_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE SYSTEM IS 'Stores systems within each ATA chapter (XX-YY format)';

-- Create SUBSYSTEM table to store subsystem information
CREATE TABLE SUBSYSTEM (
    subsystem_id VARCHAR(8) PRIMARY KEY CHECK (subsystem_id ~ '^[0-9]{2}-[0-9]{2}-[0-9]{2}$'),
    system_id VARCHAR(5) NOT NULL REFERENCES SYSTEM(system_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE SUBSYSTEM IS 'Stores subsystems within each system (XX-YY-ZZ format)';

-- Create DOCUMENT table to store document information
CREATE TABLE DOCUMENT (
    doc_id VARCHAR(12) PRIMARY KEY CHECK (doc_id ~ '^[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{3}$'),
    subsystem_id VARCHAR(8) NOT NULL REFERENCES SUBSYSTEM(subsystem_id),
    project_id VARCHAR(10) NOT NULL REFERENCES PROJECT(project_id),
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    doc_type VARCHAR(10) NOT NULL REFERENCES DOCUMENT_TYPE(type_code),
    revision CHAR(1) NOT NULL DEFAULT 'A',
    version VARCHAR(10) NOT NULL DEFAULT '0100',
    status VARCHAR(20) NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT', 'REVIEW', 'APPROVED', 'OBSOLETE')),
    author VARCHAR(100),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT,
    metadata JSONB
);

COMMENT ON TABLE DOCUMENT IS 'Stores document metadata and content';

-- Create index on document status for faster filtering
CREATE INDEX idx_document_status ON DOCUMENT(status);
-- Create index on document type for faster filtering
CREATE INDEX idx_document_type ON DOCUMENT(doc_type);
-- Create index on subsystem for faster querying
CREATE INDEX idx_document_subsystem ON DOCUMENT(subsystem_id);

-- Create DOCUMENT_HISTORY table to track document revisions
CREATE TABLE DOCUMENT_HISTORY (
    history_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),
    revision CHAR(1) NOT NULL,
    version VARCHAR(10) NOT NULL,
    change_description TEXT,
    changed_by VARCHAR(100),
    changed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    previous_content TEXT,
    previous_metadata JSONB
);

COMMENT ON TABLE DOCUMENT_HISTORY IS 'Tracks revision history of documents';

-- Create CROSS_REFERENCE table to store document relationships
CREATE TABLE CROSS_REFERENCE (
    reference_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),
    target_doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),
    ref_type VARCHAR(20) NOT NULL CHECK (ref_type IN ('DEPENDS_ON', 'REFERENCES', 'SUPERSEDES', 'IMPLEMENTS', 'VERIFIES')),
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT different_docs CHECK (source_doc_id <> target_doc_id)
);

COMMENT ON TABLE CROSS_REFERENCE IS 'Stores relationships between documents';

-- Create indexes for faster cross-reference lookups
CREATE INDEX idx_cross_ref_source ON CROSS_REFERENCE(source_doc_id);
CREATE INDEX idx_cross_ref_target ON CROSS_REFERENCE(target_doc_id);
CREATE INDEX idx_cross_ref_type ON CROSS_REFERENCE(ref_type);

-- Function to generate file paths based on document metadata
CREATE OR REPLACE FUNCTION generate_file_path(
    p_project_prefix VARCHAR,
    p_project_name VARCHAR,
    p_version VARCHAR,
    p_domain_code VARCHAR,
    p_doc_id VARCHAR,
    p_doc_type VARCHAR,
    p_revision VARCHAR,
    p_file_extension VARCHAR DEFAULT 'md'
) RETURNS VARCHAR AS $$
BEGIN
    RETURN p_project_prefix || '-' || p_project_name || '-' || p_version || '-' || 
           p_domain_code || '-' || p_doc_id || '-' || p_doc_type || '-' || p_revision || '.' || p_file_extension;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION generate_file_path IS 'Generates standardized file paths based on document metadata';

-- Function to update document revision and create history record
CREATE OR REPLACE FUNCTION update_document_revision(
    p_doc_id VARCHAR,
    p_new_revision CHAR,
    p_change_description TEXT,
    p_changed_by VARCHAR
) RETURNS VOID AS $$
DECLARE
    v_old_revision CHAR;
    v_old_version VARCHAR;
    v_old_content TEXT;
    v_old_metadata JSONB;
BEGIN
    -- Get current document data
    SELECT revision, version, content, metadata 
    INTO v_old_revision, v_old_version, v_old_content, v_old_metadata
    FROM DOCUMENT
    WHERE doc_id = p_doc_id;
    
    -- Create history record
    INSERT INTO DOCUMENT_HISTORY (
        doc_id, revision, version, change_description, 
        changed_by, previous_content, previous_metadata
    ) VALUES (
        p_doc_id, v_old_revision, v_old_version, p_change_description,
        p_changed_by, v_old_content, v_old_metadata
    );
    
    -- Update document with new revision
    UPDATE DOCUMENT
    SET revision = p_new_revision,
        modified_date = CURRENT_TIMESTAMP
    WHERE doc_id = p_doc_id;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION update_document_revision IS 'Updates document revision and creates history record';

-- Function to extract ATA chapter, system, and subsystem IDs from document ID
CREATE OR REPLACE FUNCTION extract_document_hierarchy(p_doc_id VARCHAR) 
RETURNS TABLE (chapter_id VARCHAR, system_id VARCHAR, subsystem_id VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        SUBSTRING(p_doc_id FROM 1 FOR 2),
        SUBSTRING(p_doc_id FROM 1 FOR 5),
        SUBSTRING(p_doc_id FROM 1 FOR 8);
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION extract_document_hierarchy IS 'Extracts hierarchy IDs from a document ID';

-- View to show document hierarchy
CREATE OR REPLACE VIEW document_hierarchy AS
SELECT 
    d.doc_id,
    d.title AS document_title,
    d.doc_type,
    d.revision,
    d.status,
    s.subsystem_id,
    s.title AS subsystem_title,
    sys.system_id,
    sys.title AS system_title,
    a.chapter_id,
    a.title AS chapter_title,
    p.project_id,
    p.project_name,
    dom.domain_code,
    dom.name AS domain_name,
    d.file_path,
    d.created_date,
    d.modified_date
FROM 
    DOCUMENT d
    JOIN SUBSYSTEM s ON d.subsystem_id = s.subsystem_id
    JOIN SYSTEM sys ON s.system_id = sys.system_id
    JOIN ATA_CHAPTER a ON sys.chapter_id = a.chapter_id
    JOIN PROJECT p ON d.project_id = p.project_id
    LEFT JOIN DOMAIN dom ON a.domain_code = dom.domain_code;

COMMENT ON VIEW document_hierarchy IS 'Provides a hierarchical view of all documents';

-- View to show document relationships
CREATE OR REPLACE VIEW document_relationships AS
SELECT 
    cr.reference_id,
    cr.ref_type,
    src.doc_id AS source_doc_id,
    src.title AS source_title,
    src.doc_type AS source_type,
    tgt.doc_id AS target_doc_id,
    tgt.title AS target_title,
    tgt.doc_type AS target_type,
    cr.description,
    cr.created_date
FROM 
    CROSS_REFERENCE cr
    JOIN DOCUMENT src ON cr.source_doc_id = src.doc_id
    JOIN DOCUMENT tgt ON cr.target_doc_id = tgt.doc_id;

COMMENT ON VIEW document_relationships IS 'Shows all document relationships';

-- Trigger to update modified_date when a record is updated
CREATE OR REPLACE FUNCTION update_modified_date()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified_date = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with modified_date
CREATE TRIGGER update_project_modified_date
BEFORE UPDATE ON PROJECT
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_domain_modified_date
BEFORE UPDATE ON DOMAIN
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_document_type_modified_date
BEFORE UPDATE ON DOCUMENT_TYPE
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_ata_chapter_modified_date
BEFORE UPDATE ON ATA_CHAPTER
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_system_modified_date
BEFORE UPDATE ON SYSTEM
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_subsystem_modified_date
BEFORE UPDATE ON SUBSYSTEM
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_document_modified_date
BEFORE UPDATE ON DOCUMENT
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

CREATE TRIGGER update_cross_reference_modified_date
BEFORE UPDATE ON CROSS_REFERENCE
FOR EACH ROW EXECUTE FUNCTION update_modified_date();

-- Insert sample data for testing

-- Insert project data
INSERT INTO PROJECT (project_id, project_name, project_description, project_prefix)
VALUES ('AMPEL360X', 'AMPEL360XWLRGA', 'Advanced Multi-Purpose Electric Light Aircraft', 'GP-AM');

-- Insert domain data
INSERT INTO DOMAIN (domain_code, name, description)
VALUES 
('53', 'Fuselage', 'Aircraft fuselage structure and components'),
('24', 'Electrical Power', 'Aircraft electrical power systems'),
('21', 'Air Conditioning', 'Environmental control systems');

-- Insert document types
INSERT INTO DOCUMENT_TYPE (type_code, name, description)
VALUES 
('SPEC', 'Specification', 'Technical specifications document'),
('SDD', 'Software Design Document', 'Software design and architecture document'),
('OV', 'Overview', 'System overview document'),
('ICD', 'Interface Control Document', 'Interface specifications document'),
('UM', 'User Manual', 'End-user documentation'),
('TM', 'Technical Manual', 'Technical maintenance documentation'),
('TR', 'Test Report', 'Test results and analysis');

-- Insert ATA chapters
INSERT INTO ATA_CHAPTER (chapter_id, title, description, domain_code)
VALUES 
('21', 'Air Conditioning', 'Environmental control system', '21'),
('24', 'Electrical Power', 'Aircraft electrical power generation and distribution', '24'),
('53', 'Fuselage', 'Main aircraft body structure', '53');

-- Insert systems
INSERT INTO SYSTEM (system_id, chapter_id, title, description)
VALUES 
('21-00', '21', 'Air Conditioning - General', 'General information about air conditioning systems'),
('21-20', '21', 'Distribution', 'Air distribution system'),
('24-00', '24', 'Electrical Power - General', 'General information about electrical power systems'),
('24-30', '24', 'DC Generation', 'DC power generation system'),
('24-40', '24', 'External Power', 'External power connection system'),
('24-60', '24', 'AC Generation', 'AC power generation system'),
('53-10', '53', 'Fuselage Main', 'Main fuselage structure');

-- Insert subsystems
INSERT INTO SUBSYSTEM (subsystem_id, system_id, title, description)
VALUES 
('21-00-00', '21-00', 'Air Conditioning - General', 'General information about air conditioning systems'),
('21-20-00', '21-20', 'Distribution - General', 'General information about air distribution'),
('24-00-00', '24-00', 'Electrical Power - General', 'General information about electrical power systems'),
('24-30-00', '24-30', 'DC Generation - General', 'General information about DC generation'),
('24-40-00', '24-40', 'External Power - General', 'General information about external power connections'),
('24-60-00', '24-60', 'AC Generation - General', 'General information about AC generation'),
('24-60-10', '24-60', 'AC Generation - PMSC', 'Power Management System Controller'),
('53-10-00', '53-10', 'Fuselage Main - General', 'General information about main fuselage structure');

-- Insert documents
INSERT INTO DOCUMENT (doc_id, subsystem_id, project_id, title, file_path, doc_type, revision, version, status, author)
VALUES 
('21-00-00-000', '21-00-00', 'AMPEL360X', 'Air Conditioning System Overview', 
 'GP-AM-AMPEL-0100-21-21-00-00-000-OV-A.md', 'OV', 'A', '0100', 'APPROVED', 'John Smith'),
 
('21-20-00-001', '21-20-00', 'AMPEL360X', 'Air Distribution System Specification', 
 'GP-AM-AMPEL-0100-21-21-20-00-001-SPEC-A.md', 'SPEC', 'A', '0100', 'APPROVED', 'Jane Doe'),
 
('24-00-00-000', '24-00-00', 'AMPEL360X', 'Electrical Power System Overview', 
 'GP-AM-AMPEL-0100-24-24-00-00-000-OV-A.md', 'OV', 'A', '0100', 'APPROVED', 'Robert Johnson'),
 
('24-30-00-001', '24-30-00', 'AMPEL360X', 'DC Generation System Specification', 
 'GP-AM-AMPEL-0100-24-24-30-00-001-SPEC-A.md', 'SPEC', 'A', '0100', 'APPROVED', 'Sarah Williams'),
 
('24-60-00-000', '24-60-00', 'AMPEL360X', 'AC Generation System Overview', 
 'GP-AM-AMPEL-0100-24-24-60-00-000-OV-A.md', 'OV', 'A', '0100', 'APPROVED', 'Michael Brown'),
 
('24-60-10-001', '24-60-10', 'AMPEL360X', 'Power Management System Controller Specification', 
 'GP-AM-AMPEL-0100-24-24-60-10-001-SPEC-A.md', 'SPEC', 'A', '0100', 'APPROVED', 'Emily Davis'),
 
('24-60-10-002', '24-60-10', 'AMPEL360X', 'Power Management System Controller Software Design', 
 'GP-AM-AMPEL-0100-24-24-60-10-002-SDD-A.md', 'SDD', 'A', '0100', 'REVIEW', 'David Wilson'),
 
('53-10-00-000', '53-10-00', 'AMPEL360X', 'Fuselage Main Structure Overview', 
 'GP-AM-AMPEL-0100-53-53-10-00-000-OV-A.md', 'OV', 'A', '0100', 'APPROVED', 'Lisa Martinez');

-- Insert cross-references
INSERT INTO CROSS_REFERENCE (source_doc_id, target_doc_id, ref_type, description)
VALUES 
('24-60-10-002', '24-60-10-001', 'IMPLEMENTS', 'Software design implements the PMSC specification'),
('24-60-10-001', '24-60-00-000', 'REFERENCES', 'PMSC specification references the AC Generation System Overview'),
('24-60-00-000', '24-00-00-000', 'REFERENCES', 'AC Generation references the Electrical Power System Overview'),
('21-20-00-001', '21-00-00-000', 'REFERENCES', 'Air Distribution System references the Air Conditioning System Overview'),
('24-30-00-001', '24-00-00-000', 'REFERENCES', 'DC Generation System references the Electrical Power System Overview');

-- Create a function to search documents by content or metadata
CREATE OR REPLACE FUNCTION search_documents(search_term TEXT)
RETURNS TABLE (
    doc_id VARCHAR,
    title VARCHAR,
    doc_type VARCHAR,
    subsystem_id VARCHAR,
    system_id VARCHAR,
    chapter_id VARCHAR,
    file_path VARCHAR,
    relevance FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        d.doc_id,
        d.title,
        d.doc_type,
        s.subsystem_id,
        sys.system_id,
        a.chapter_id,
        d.file_path,
        ts_rank_cd(
            to_tsvector('english', COALESCE(d.title, '') || ' ' || COALESCE(d.content, '')),
            to_tsquery('english', search_term)
        ) AS relevance
    FROM 
        DOCUMENT d
        JOIN SUBSYSTEM s ON d.subsystem_id = s.subsystem_id
        JOIN SYSTEM sys ON s.system_id = sys.system_id
        JOIN ATA_CHAPTER a ON sys.chapter_id = a.chapter_id
    WHERE 
        to_tsvector('english', COALESCE(d.title, '') || ' ' || COALESCE(d.content, '')) @@ to_tsquery('english', search_term)
        OR d.metadata::TEXT ILIKE '%' || search_term || '%'
    ORDER BY 
        relevance DESC;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION search_documents IS 'Searches documents by content or metadata';

-- Create a function to get all related documents
CREATE OR REPLACE FUNCTION get_related_documents(p_doc_id VARCHAR)
RETURNS TABLE (
    related_doc_id VARCHAR,
    related_title VARCHAR,
    related_doc_type VARCHAR,
    relationship_type VARCHAR,
    relationship_direction VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    -- Documents that the source references
    SELECT 
        d.doc_id AS related_doc_id,
        d.title AS related_title,
        d.doc_type AS related_doc_type,
        cr.ref_type AS relationship_type,
        'OUTGOING' AS relationship_direction
    FROM 
        CROSS_REFERENCE cr
        JOIN DOCUMENT d ON cr.target_doc_id = d.doc_id
    WHERE 
        cr.source_doc_id = p_doc_id
    
    UNION ALL
    
    -- Documents that reference the source
    SELECT 
        d.doc_id AS related_doc_id,
        d.title AS related_title,
        d.doc_type AS related_doc_type,
        cr.ref_type AS relationship_type,
        'INCOMING' AS relationship_direction
    FROM 
        CROSS_REFERENCE cr
        JOIN DOCUMENT d ON cr.source_doc_id = d.doc_id
    WHERE 
        cr.target_doc_id = p_doc_id
    
    ORDER BY 
        relationship_direction, 
        relationship_type;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION get_related_documents IS 'Gets all documents related to a specific document';

-- Create a function to get document revision history
CREATE OR REPLACE FUNCTION get_document_history(p_doc_id VARCHAR)
RETURNS TABLE (
    revision CHAR,
    version VARCHAR,
    changed_by VARCHAR,
    changed_date TIMESTAMP,
    change_description TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        dh.revision,
        dh.version,
        dh.changed_by,
        dh.changed_date,
        dh.change_description
    FROM 
        DOCUMENT_HISTORY dh
    WHERE 
        dh.doc_id = p_doc_id
    ORDER BY 
        dh.changed_date DESC;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION get_document_history IS 'Gets revision history for a specific document';
