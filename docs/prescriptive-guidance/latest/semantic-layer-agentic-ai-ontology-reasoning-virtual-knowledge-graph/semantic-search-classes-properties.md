---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/semantic-search-classes-properties.html
---

# Semantic Search (Classes & Properties)

## Semantic Search (Classes & Properties)
<a name="semantic-search--classes-9999999999999999amp--properties-.eaa0e9cd-6d15-54c1-b0bd-98358ba1e431"></a>

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| Keyword Search | GET | `/ontologies/{id}/search?q={term}` | — | `application/json` | Matches `rdfs:label`, `skos:altLabel`, `rdfs:comment` |
| Semantic Similarity Search | POST | `/ontologies/{id}/search/semantic` | `application/json` | `application/json` | Vector-based search using embedding of class/property descriptions |
| Subclass Traversal Search | GET | `/ontologies/{id}/classes/{classIRI}/subclasses` | — | `application/json`, `text/turtle` | Returns full subclass hierarchy; `?depth=` param for bounded traversal |
| Combined Search | POST | `/ontologies/{id}/search/hybrid` | `application/json` | `application/json` | Combines subclass structure \+ semantic similarity; returns ranked results with `rdfs:subClassOf` path |
