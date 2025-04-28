-- GAIA AIR Documentation System - Schema Ingestion Script
-- This script ingests the database schema definition into the documentation system itself
-- as a version-controlled document with doc_id = 00-00-SD-001, doc_type = SCHEMA

-- Start transaction
BEGIN;

-- Step 1: Check if SYSTEM 00-00 exists, create if not
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM SYSTEM WHERE system_id = '00-00') THEN
        -- Check if ATA chapter 00 exists, create if not
        IF NOT EXISTS (SELECT 1 FROM ATA_CHAPTER WHERE chapter_id = '00') THEN
            INSERT INTO ATA_CHAPTER (chapter_id, title, description)
            VALUES ('00', 'General', 'General documentation and system-wide information');
        END IF;
        
        -- Create SYSTEM record
        INSERT INTO SYSTEM (system_id, chapter_id, title, description)
        VALUES ('00-00', '00', 'Documentation System', 'GAIA AIR Documentation System');
    END IF;
END $$;

-- Step 2: Check if SUBSYSTEM 00-00-SD exists, create if not
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM SUBSYSTEM WHERE subsystem_id = '00-00-SD') THEN
        INSERT INTO SUBSYSTEM (subsystem_id, system_id, title, description)
        VALUES ('00-00-SD', '00-00', 'System Documentation', 'Documentation for the GAIA AIR Documentation System itself');
    END IF;
END $$;

-- Step 3: Check if DOCUMENT_TYPE SCHEMA exists, create if not
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM DOCUMENT_TYPE WHERE type_code = 'SCHEMA') THEN
        INSERT INTO DOCUMENT_TYPE (type_code, name, description)
        VALUES ('SCHEMA', 'Database Schema', 'SQL database schema definition');
    END IF;
END $$;

-- Step 4: Check if PROJECT record exists, create if not
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM PROJECT WHERE project_id = 'GAIA_DOCS') THEN
        INSERT INTO PROJECT (project_id, project_name, project_description, project_prefix)
        VALUES ('GAIA_DOCS', 'GAIA Documentation System', 'GAIA AIR Documentation System', 'GP-DOC');
    END IF;
END $$;

-- Step 5: Check if DOCUMENT 00-00-SD-001 exists
DO $$
DECLARE
    v_doc_exists BOOLEAN;
    v_schema_content TEXT;
BEGIN
    -- Check if document exists
    SELECT EXISTS(SELECT 1 FROM DOCUMENT WHERE doc_id = '00-00-SD-001') INTO v_doc_exists;
    
    -- Get the schema content (this is a placeholder - in a real implementation, 
    -- you would read this from a file or use a variable containing the schema)
    v_schema_content := (
        SELECT string_agg(line, E'\n')
        FROM (
            SELECT unnest(ARRAY[
                '-- GAIA AIR Documentation Database Schema',
                '-- This script creates a complete database schema for managing GAIA AIR aircraft documentation',
                '-- with proper relations and cross-references while preserving the established codification system.',
                '',
                '-- Enable UUID extension for unique identifiers',
                'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";',
                '',
                '-- Create PROJECT table to store project information',
                'CREATE TABLE PROJECT (',
                '    project_id VARCHAR(10) PRIMARY KEY,',
                '    project_name VARCHAR(50) NOT NULL,',
                '    project_description TEXT,',
                '    project_prefix VARCHAR(10) NOT NULL,',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create DOMAIN table to store domain information',
                'CREATE TABLE DOMAIN (',
                '    domain_code VARCHAR(10) PRIMARY KEY,',
                '    name VARCHAR(100) NOT NULL,',
                '    description TEXT,',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create DOCUMENT_TYPE table to store document type information',
                'CREATE TABLE DOCUMENT_TYPE (',
                '    type_code VARCHAR(10) PRIMARY KEY,',
                '    name VARCHAR(100) NOT NULL,',
                '    description TEXT,',
                '    template_path VARCHAR(255),',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create ATA_CHAPTER table to store ATA chapter information',
                'CREATE TABLE ATA_CHAPTER (',
                '    chapter_id VARCHAR(2) PRIMARY KEY CHECK (chapter_id ~ \'^[0-9]{2}$\'),',
                '    title VARCHAR(100) NOT NULL,',
                '    description TEXT,',
                '    domain_code VARCHAR(10) REFERENCES DOMAIN(domain_code),',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create SYSTEM table to store system information',
                'CREATE TABLE SYSTEM (',
                '    system_id VARCHAR(5) PRIMARY KEY CHECK (system_id ~ \'^[0-9]{2}-[0-9]{2}$\'),',
                '    chapter_id VARCHAR(2) NOT NULL REFERENCES ATA_CHAPTER(chapter_id),',
                '    title VARCHAR(100) NOT NULL,',
                '    description TEXT,',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create SUBSYSTEM table to store subsystem information',
                'CREATE TABLE SUBSYSTEM (',
                '    subsystem_id VARCHAR(8) PRIMARY KEY CHECK (subsystem_id ~ \'^[0-9]{2}-[0-9]{2}-[0-9]{2}$\'),',
                '    system_id VARCHAR(5) NOT NULL REFERENCES SYSTEM(system_id),',
                '    title VARCHAR(100) NOT NULL,',
                '    description TEXT,',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
                ');',
                '',
                '-- Create DOCUMENT table to store document information',
                'CREATE TABLE DOCUMENT (',
                '    doc_id VARCHAR(12) PRIMARY KEY CHECK (doc_id ~ \'^[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{3}$\'),',
                '    subsystem_id VARCHAR(8) NOT NULL REFERENCES SUBSYSTEM(subsystem_id),',
                '    project_id VARCHAR(10) NOT NULL REFERENCES PROJECT(project_id),',
                '    title VARCHAR(255) NOT NULL,',
                '    file_path VARCHAR(255) NOT NULL,',
                '    doc_type VARCHAR(10) NOT NULL REFERENCES DOCUMENT_TYPE(type_code),',
                '    revision CHAR(1) NOT NULL DEFAULT \'A\',',
                '    version VARCHAR(10) NOT NULL DEFAULT \'0100\',',
                '    status VARCHAR(20) NOT NULL DEFAULT \'DRAFT\' CHECK (status IN (\'DRAFT\', \'REVIEW\', \'APPROVED\', \'OBSOLETE\')),',
                '    author VARCHAR(100),',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    content TEXT,',
                '    metadata JSONB',
                ');',
                '',
                '-- Create DOCUMENT_HISTORY table to track document revisions',
                'CREATE TABLE DOCUMENT_HISTORY (',
                '    history_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),',
                '    doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),',
                '    revision CHAR(1) NOT NULL,',
                '    version VARCHAR(10) NOT NULL,',
                '    change_description TEXT,',
                '    changed_by VARCHAR(100),',
                '    changed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    previous_content TEXT,',
                '    previous_metadata JSONB',
                ');',
                '',
                '-- Create CROSS_REFERENCE table to store document relationships',
                'CREATE TABLE CROSS_REFERENCE (',
                '    reference_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),',
                '    source_doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),',
                '    target_doc_id VARCHAR(12) NOT NULL REFERENCES DOCUMENT(doc_id),',
                '    ref_type VARCHAR(20) NOT NULL CHECK (ref_type IN (\'DEPENDS_ON\', \'REFERENCES\', \'SUPERSEDES\', \'IMPLEMENTS\', \'VERIFIES\')),',
                '    description TEXT,',
                '    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,',
                '    CONSTRAINT different_docs CHECK (source_doc_id <> target_doc_id)',
                ');',
                '',
                '-- Function to generate file paths based on document metadata',
                'CREATE OR REPLACE FUNCTION generate_file_path(',
                '    p_project_prefix VARCHAR,',
                '    p_project_name VARCHAR,',
                '    p_version VARCHAR,',
                '    p_domain_code VARCHAR,',
                '    p_doc_id VARCHAR,',
                '    p_doc_type VARCHAR,',
                '    p_revision VARCHAR,',
                '    p_file_extension VARCHAR DEFAULT \'md\'',
                ') RETURNS VARCHAR AS $$',
                'BEGIN',
                '    RETURN p_project_prefix || \'-\' || p_project_name || \'-\' || p_version || \'-\' || ',
                '           p_domain_code || \'-\' || p_doc_id || \'-\' || p_doc_type || \'-\' || p_revision || \'.\' || p_file_extension;',
                'END;',
                '$$ LANGUAGE plpgsql;',
                '',
                '-- Function to update document revision and create history record',
                'CREATE OR REPLACE FUNCTION update_document_revision(',
                '    p_doc_id VARCHAR,',
                '    p_new_revision CHAR,',
                '    p_change_description TEXT,',
                '    p_changed_by VARCHAR',
                ') RETURNS VOID AS $$',
                'DECLARE',
                '    v_old_revision CHAR;',
                '    v_old_version VARCHAR;',
                '    v_old_content TEXT;',
                '    v_old_metadata JSONB;',
                'BEGIN',
                '    -- Get current document data',
                '    SELECT revision, version, content, metadata ',
                '    INTO v_old_revision, v_old_version, v_old_content, v_old_metadata',
                '    FROM DOCUMENT',
                '    WHERE doc_id = p_doc_id;',
                '    ',
                '    -- Create history record',
                '    INSERT INTO DOCUMENT_HISTORY (',
                '        doc_id, revision, version, change_description, ',
                '        changed_by, previous_content, previous_metadata',
                '    ) VALUES (',
                '        p_doc_id, v_old_revision, v_old_version, p_change_description,',
                '        p_changed_by, v_old_content, v_old_metadata',
                '    );',
                '    ',
                '    -- Update document with new revision',
                '    UPDATE DOCUMENT',
                '    SET revision = p_new_revision,',
                '        modified_date = CURRENT_TIMESTAMP',
                '    WHERE doc_id = p_doc_id;',
                'END;',
                '$$ LANGUAGE plpgsql;',
                '',
                '-- Function to extract ATA chapter, system, and subsystem IDs from document ID',
                'CREATE OR REPLACE FUNCTION extract_document_hierarchy(p_doc_id VARCHAR) ',
                'RETURNS TABLE (chapter_id VARCHAR, system_id VARCHAR, subsystem_id VARCHAR) AS $$',
                'BEGIN',
                '    RETURN QUERY',
                '    SELECT ',
                '        SUBSTRING(p_doc_id FROM 1 FOR 2),',
                '        SUBSTRING(p_doc_id FROM 1 FOR 5),',
                '        SUBSTRING(p_doc_id FROM 1 FOR 8);',
                'END;',
                '$$ LANGUAGE plpgsql;',
                '',
                '-- View to show document hierarchy',
                'CREATE OR REPLACE VIEW document_hierarchy AS',
                'SELECT ',
                '    d.doc_id,',
                '    d.title AS document_title,',
                '    d.doc_type,',
                '    d.revision,',
                '    d.status,',
                '    s.subsystem_id,',
                '    s.title AS subsystem_title,',
                '    sys.system_id,',
                '    sys.title AS system_title,',
                '    a.chapter_id,',
                '    a.title AS chapter_title,',
                '    p.project_id,',
                '    p.project_name,',
                '    dom.domain_code,',
                '    dom.name AS domain_name,',
                '    d.file_path,',
                '    d.created_date,',
                '    d.modified_date',
                'FROM ',
                '    DOCUMENT d',
                '    JOIN SUBSYSTEM s ON d.subsystem_id = s.subsystem_id',
                '    JOIN SYSTEM sys ON s.system_id = sys.system_id',
                '    JOIN ATA_CHAPTER a ON sys.chapter_id = a.chapter_id',
                '    JOIN PROJECT p ON d.project_id = p.project_id',
                '    LEFT JOIN DOMAIN dom ON a.domain_code = dom.domain_code;',
                '',
                '-- View to show document relationships',
                'CREATE OR REPLACE VIEW document_relationships AS',
                'SELECT ',
                '    cr.reference_id,',
                '    cr.ref_type,',
                '    src.doc_id AS source_doc_id,',
                '    src.title AS source_title,',
                '    src.doc_type AS source_type,',
                '    tgt.doc_id AS target_doc_id,',
                '    tgt.title AS target_title,',
                '    tgt.doc_type AS target_type,',
                '    cr.description,',
                '    cr.created_date',
                'FROM ',
                '    CROSS_REFERENCE cr',
                '    JOIN DOCUMENT src ON cr.source_doc_id = src.doc_id',
                '    JOIN DOCUMENT tgt ON cr.target_doc_id = tgt.doc_id;',
                '',
                '-- Function to search documents by content or metadata',
                'CREATE OR REPLACE FUNCTION search_documents(search_term TEXT)',
                'RETURNS TABLE (',
                '    doc_id VARCHAR,',
                '    title VARCHAR,',
                '    doc_type VARCHAR,',
                '    subsystem_id VARCHAR,',
                '    system_id VARCHAR,',
                '    chapter_id VARCHAR,',
                '    file_path VARCHAR,',
                '    relevance FLOAT',
                ') AS $$',
                'BEGIN',
                '    RETURN QUERY',
                '    SELECT ',
                '        d.doc_id,',
                '        d.title,',
                '        d.doc_type,',
                '        s.subsystem_id,',
                '        sys.system_id,',
                '        a.chapter_id,',
                '        d.file_path,',
                '        ts_rank_cd(',
                '            to_tsvector(\'english\', COALESCE(d.title, \'\') || \' \' || COALESCE(d.content, \'\')),',
                '            to_tsquery(\'english\', search_term)',
                '        ) AS relevance',
                '    FROM ',
                '        DOCUMENT d',
                '        JOIN SUBSYSTEM s ON d.subsystem_id = s.subsystem_id',
                '        JOIN SYSTEM sys ON s.system_id = sys.system_id',
                '        JOIN ATA_CHAPTER a ON sys.chapter_id = a.chapter_id',
                '    WHERE ',
                '        to_tsvector(\'english\', COALESCE(d.title, \'\') || \' \' || COALESCE(d.content, \'\')) @@ to_tsquery(\'english\', search_term)',
                '        OR d.metadata::TEXT ILIKE \'%\' || search_term || \'%\'',
                '    ORDER BY ',
                '        relevance DESC;',
                'END;',
                '$$ LANGUAGE plpgsql;',
                '',
                '-- Function to get all related documents',
                'CREATE OR REPLACE FUNCTION get_related_documents(p_doc_id VARCHAR)',
                'RETURNS TABLE (',
                '    related_doc_id VARCHAR,',
                '    related_title VARCHAR,',
                '    related_doc_type VARCHAR,',
                '    relationship_type VARCHAR,',
                '    relationship_direction VARCHAR',
                ') AS $$',
                'BEGIN',
                '    RETURN QUERY',
                '    -- Documents that the source references',
                '    SELECT ',
                '        d.doc_id AS related_doc_id,',
                '        d.title AS related_title,',
                '        d.doc_type AS related_doc_type,',
                '        cr.ref_type AS relationship_type,',
                '        \'OUTGOING\' AS relationship_direction',
                '    FROM ',
                '        CROSS_REFERENCE cr',
                '        JOIN DOCUMENT d ON cr.target_doc_id = d.doc_id',
                '    WHERE ',
                '        cr.source_doc_id = p_doc_id',
                '    ',
                '    UNION ALL',
                '    ',
                '    -- Documents that reference the source',
                '    SELECT ',
                '        d.doc_id AS related_doc_id,',
                '        d.title AS related_title,',
                '        d.doc_type AS related_doc_type,',
                '        cr.ref_type AS relationship_type,',
                '        \'INCOMING\' AS relationship_direction',
                '    FROM ',
                '        CROSS_REFERENCE cr',
                '        JOIN DOCUMENT d ON cr.source_doc_id = d.doc_id',
                '    WHERE ',
                '        cr.target_doc_id = p_doc_id',
                '    ',
                '    ORDER BY ',
                '        relationship_direction, ',
                '        relationship_type;',
                'END;',
                '$$ LANGUAGE plpgsql;',
                '',
                '-- Function to get document revision history',
                'CREATE OR REPLACE FUNCTION get_document_history(p_doc_id VARCHAR)',
                'RETURNS TABLE (',
                '    revision CHAR,',
                '    version VARCHAR,',
                '    changed_by VARCHAR,',
                '    changed_date TIMESTAMP,',
                '    change_description TEXT',
                ') AS $$',
                'BEGIN',
                '    RETURN QUERY',
                '    SELECT ',
                '        dh.revision,',
                '        dh.version,',
                '        dh.changed_by,',
                '        dh.changed_date,',
                '        dh.change_description',
                '    FROM ',
                '        DOCUMENT_HISTORY dh',
                '    WHERE ',
                '        dh.doc_id = p_doc_id',
                '    ORDER BY ',
                '        dh.changed_date DESC;',
                'END;',
                '$$ LANGUAGE plpgsql;'
            ]) AS line
        ) AS lines
    );
    
    IF NOT v_doc_exists THEN
        -- Insert new document
        INSERT INTO DOCUMENT (
            doc_id,
            subsystem_id,
            project_id,
            title,
            file_path,
            doc_type,
            revision,
            version,
            status,
            author,
            created_date,
            modified_date,
            content,
            metadata
        )
        VALUES (
            '00-00-SD-001',
            '00-00-SD',
            'GAIA_DOCS',
            'GAIA AIR Documentation System Database Schema',
            'GP-DOC-GAIA_DOCS-0100-00-00-00-SD-001-SCHEMA-A.sql',
            'SCHEMA',
            'A',
            '0100',
            'APPROVED',
            'System',
            CURRENT_TIMESTAMP,
            CURRENT_TIMESTAMP,
            v_schema_content,
            '{"description": "Database schema definition for the GAIA AIR Documentation System", "version": "1.0.0"}'::JSONB
        );
        
        -- Create initial history record
        INSERT INTO DOCUMENT_HISTORY (
            doc_id,
            revision,
            version,
            change_description,
            changed_by,
            changed_date,
            previous_content,
            previous_metadata
        )
        VALUES (
            '00-00-SD-001',
            'A',
            '0100',
            'Initial version of the GAIA AIR Documentation System Database Schema',
            'System',
            CURRENT_TIMESTAMP,
            NULL,
            NULL
        );
    ELSE
        -- Document already exists, update it using update_document_revision function
        -- First, get current revision
        DECLARE
            v_current_revision CHAR(1);
        BEGIN
            SELECT revision INTO v_current_revision FROM DOCUMENT WHERE doc_id = '00-00-SD-001';
            
            -- Calculate next revision (A->B, B->C, etc.)
            v_current_revision := CHR(ASCII(v_current_revision) + 1);
            
            -- Update document using the update_document_revision function
            PERFORM update_document_revision(
                '00-00-SD-001',
                v_current_revision,
                'Updated GAIA AIR Documentation System Database Schema',
                'System'
            );
            
            -- Update content separately (not handled by update_document_revision)
            UPDATE DOCUMENT
            SET content = v_schema_content,
                metadata = jsonb_set(metadata, '{version}', to_jsonb((metadata->>'version')::numeric + 0.1))
            WHERE doc_id = '00-00-SD-001';
        END;
    END IF;
END $$;

-- Commit transaction
COMMIT;

-- Verify the document was created/updated
SELECT doc_id, title, revision, status, created_date, modified_date
FROM DOCUMENT
WHERE doc_id = '00-00-SD-001';

-- Verify document history
SELECT doc_id, revision, version, change_description, changed_date
FROM DOCUMENT_HISTORY
WHERE doc_id = '00-00-SD-001'
ORDER BY changed_date DESC;
