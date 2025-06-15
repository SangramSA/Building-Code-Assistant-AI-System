// Create constraints for unique identifiers
CREATE CONSTRAINT section_id IF NOT EXISTS 
ON (s:Section) ASSERT s.id IS UNIQUE;

CREATE CONSTRAINT chapter_id IF NOT EXISTS 
ON (c:Chapter) ASSERT c.id IS UNIQUE;

// Create indexes for common queries
CREATE INDEX section_content IF NOT EXISTS 
FOR (s:Section) ON (s.content);

CREATE INDEX section_title IF NOT EXISTS 
FOR (s:Section) ON (s.title);

// Initial node labels
CREATE (j:Jurisdiction {
    name: 'Philadelphia',
    code: 'PHL',
    updated: datetime()
});