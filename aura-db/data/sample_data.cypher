// Create sample movies
CREATE (m1:Movie {id: '1', title: 'The Matrix', year: 1999})
CREATE (m2:Movie {id: '2', title: 'Inception', year: 2010})

// Create sample people
CREATE (p1:Person {id: '1', name: 'Keanu Reeves', born: 1964})
CREATE (p2:Person {id: '2', name: 'Laurence Fishburne', born: 1961})
CREATE (p3:Person {id: '3', name: 'Leonardo DiCaprio', born: 1974})

// Create relationships
CREATE (p1)-[:ACTED_IN {role: 'Neo'}]->(m1)
CREATE (p2)-[:ACTED_IN {role: 'Morpheus'}]->(m1)
CREATE (p3)-[:ACTED_IN {role: 'Cobb'}]->(m2) 