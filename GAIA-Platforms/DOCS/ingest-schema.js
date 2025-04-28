import fs from 'fs/promises';
import path from 'path';
import { Pool } from 'pg';
import { fileURLToPath } from 'url';

// Configuration
const config = {
  db: {
    host: process.env.DB_HOST || 'localhost',
    port: process.env.DB_PORT || 5432,
    database: process.env.DB_NAME || 'gaia_air_docs',
    user: process.env.DB_USER || 'postgres',
    password: process.env.DB_PASSWORD || 'postgres',
  },
  schemaFilePath: process.env.SCHEMA_FILE_PATH || './gaia_air_documentation_schema.sql'
};

// Create PostgreSQL connection pool
const pool = new Pool(config.db);

/**
 * Ingest schema file into the documentation system
 * @param {string} schemaFilePath - Path to the schema file
 */
async function ingestSchemaFile(schemaFilePath) {
  const client = await pool.connect();
  
  try {
    await client.query('BEGIN');
    
    console.log(`Reading schema file: ${schemaFilePath}`);
    const schemaContent = await fs.readFile(schemaFilePath, 'utf8');
    
    // Step 1: Check if SYSTEM 00-00 exists, create if not
    const systemResult = await client.query(`
      SELECT 1 FROM SYSTEM WHERE system_id = '00-00'
    `);
    
    if (systemResult.rows.length === 0) {
      // Check if ATA chapter 00 exists, create if not
      const chapterResult = await client.query(`
        SELECT 1 FROM ATA_CHAPTER WHERE chapter_id = '00'
      `);
      
      if (chapterResult.rows.length === 0) {
        console.log('Creating ATA chapter 00');
        await client.query(`
          INSERT INTO ATA_CHAPTER (chapter_id, title, description)
          VALUES ('00', 'General', 'General documentation and system-wide information')
        `);
      }
      
      console.log('Creating SYSTEM 00-00');
      await client.query(`
        INSERT INTO SYSTEM (system_id, chapter_id, title, description)
        VALUES ('00-00', '00', 'Documentation System', 'GAIA AIR Documentation System')
      `);
    }
    
    // Step 2: Check if SUBSYSTEM 00-00-SD exists, create if not
    const subsystemResult = await client.query(`
      SELECT 1 FROM SUBSYSTEM WHERE subsystem_id = '00-00-SD'
    `);
    
    if (subsystemResult.rows.length === 0) {
      console.log('Creating SUBSYSTEM 00-00-SD');
      await client.query(`
        INSERT INTO SUBSYSTEM (subsystem_id, system_id, title, description)
        VALUES ('00-00-SD', '00-00', 'System Documentation', 'Documentation for the GAIA AIR Documentation System itself')
      `);
    }
    
    // Step 3: Check if DOCUMENT_TYPE SCHEMA exists, create if not
    const docTypeResult = await client.query(`
      SELECT 1 FROM DOCUMENT_TYPE WHERE type_code = 'SCHEMA'
    `);
    
    if (docTypeResult.rows.length === 0) {
      console.log('Creating DOCUMENT_TYPE SCHEMA');
      await client.query(`
        INSERT INTO DOCUMENT_TYPE (type_code, name, description)
        VALUES ('SCHEMA', 'Database Schema', 'SQL database schema definition')
      `);
    }
    
    // Step 4: Check if PROJECT record exists, create if not
    const projectResult = await client.query(`
      SELECT 1 FROM PROJECT WHERE project_id = 'GAIA_DOCS'
    `);
    
    if (projectResult.rows.length === 0) {
      console.log('Creating PROJECT GAIA_DOCS');
      await client.query(`
        INSERT INTO PROJECT (project_id, project_name, project_description, project_prefix)
        VALUES ('GAIA_DOCS', 'GAIA Documentation System', 'GAIA AIR Documentation System', 'GP-DOC')
      `);
    }
    
    // Step 5: Check if DOCUMENT 00-00-SD-001 exists
    const docResult = await client.query(`
      SELECT doc_id, revision FROM DOCUMENT WHERE doc_id = '00-00-SD-001'
    `);
    
    const fileName = 'GP-DOC-GAIA_DOCS-0100-00-00-00-SD-001-SCHEMA-A.sql';
    
    if (docResult.rows.length === 0) {
      // Document doesn't exist, create it
      console.log('Creating DOCUMENT 00-00-SD-001');
      await client.query(`
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
          $1,
          'SCHEMA',
          'A',
          '0100',
          'APPROVED',
          'System',
          CURRENT_TIMESTAMP,
          CURRENT_TIMESTAMP,
          $2,
          $3
        )
      `, [
        fileName,
        schemaContent,
        JSON.stringify({
          description: "Database schema definition for the GAIA AIR Documentation System",
          version: "1.0.0"
        })
      ]);
      
      // Create initial history record
      console.log('Creating initial history record');
      await client.query(`
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
        )
      `);
    } else {
      // Document exists, update it
      const currentRevision = docResult.rows[0].revision;
      const nextRevision = String.fromCharCode(currentRevision.charCodeAt(0) + 1);
      
      console.log(`Updating DOCUMENT 00-00-SD-001 from revision ${currentRevision} to ${nextRevision}`);
      
      // Get current document data
      const currentDocResult = await client.query(`
        SELECT revision, version, content, metadata
        FROM DOCUMENT
        WHERE doc_id = '00-00-SD-001'
      `);
      
      const currentDoc = currentDocResult.rows[0];
      
      // Create history record
      console.log('Creating history record for previous version');
      await client.query(`
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
          $1,
          $2,
          'Updated GAIA AIR Documentation System Database Schema',
          'System',
          CURRENT_TIMESTAMP,
          $3,
          $4
        )
      `, [
        currentDoc.revision,
        currentDoc.version,
        currentDoc.content,
        currentDoc.metadata
      ]);
      
      // Update document
      console.log('Updating document content and metadata');
      await client.query(`
        UPDATE DOCUMENT
        SET revision = $1,
            content = $2,
            metadata = jsonb_set(metadata, '{version}', to_jsonb((metadata->>'version')::numeric + 0.1)),
            modified_date = CURRENT_TIMESTAMP
        WHERE doc_id = '00-00-SD-001'
      `, [
        nextRevision,
        schemaContent
      ]);
    }
    
    // Save schema file to disk
    const outputDir = path.dirname(fileName);
    if (!await directoryExists(outputDir)) {
      await fs.mkdir(outputDir, { recursive: true });
    }
    
    console.log(`Saving schema file to ${fileName}`);
    await fs.writeFile(fileName, schemaContent);
    
    await client.query('COMMIT');
    
    console.log('Schema ingestion completed successfully');
    
    // Verify the document was created/updated
    const verifyResult = await client.query(`
      SELECT doc_id, title, revision, status, created_date, modified_date
      FROM DOCUMENT
      WHERE doc_id = '00-00-SD-001'
    `);
    
    console.log('Document details:');
    console.table(verifyResult.rows[0]);
    
    // Verify document history
    const historyResult = await client.query(`
      SELECT doc_id, revision, version, change_description, changed_date
      FROM DOCUMENT_HISTORY
      WHERE doc_id = '00-00-SD-001'
      ORDER BY changed_date DESC
    `);
    
    console.log('Document history:');
    console.table(historyResult.rows);
    
    return {
      success: true,
      document: verifyResult.rows[0],
      history: historyResult.rows
    };
  } catch (err) {
    await client.query('ROLLBACK');
    console.error('Error ingesting schema:', err);
    return {
      success: false,
      error: err.message
    };
  } finally {
    client.release();
  }
}

/**
 * Check if a directory exists
 * @param {string} dirPath - Path to the directory
 * @returns {Promise<boolean>} True if directory exists, false otherwise
 */
async function directoryExists(dirPath) {
  try {
    const stats = await fs.stat(dirPath);
    return stats.isDirectory();
  } catch (err) {
    return false;
  }
}

// Run the script if called directly
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const schemaFilePath = process.argv[2] || config.schemaFilePath;
  
  ingestSchemaFile(schemaFilePath)
    .then(result => {
      if (result.success) {
        console.log('Schema ingestion completed successfully');
        process.exit(0);
      } else {
        console.error('Schema ingestion failed:', result.error);
        process.exit(1);
      }
    })
    .catch(err => {
      console.error('Unhandled error:', err);
      process.exit(1);
    });
}

export { ingestSchemaFile };
