---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/semantic-metadata-management-classes-properties.html
---

# Semantic Metadata Management (Classes & Properties)

## Semantic Metadata Management (Classes & Properties)
<a name="semantic-metadata-management--classes-9999999999999999amp--properties-.aaa30887-b69f-5c53-b87b-271cde410ff0"></a>

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| Update Class Metadata | PATCH | `/ontologies/{id}/classes/{classIRI}` | `application/json`, `text/turtle` | `application/json` | Set `rdfs:comment`, `rdfs:label`, `skos:altLabel`, `skos:definition` |
| Update Property Metadata | PATCH | `/ontologies/{id}/properties/{propertyIRI}` | `application/json`, `text/turtle` | `application/json` | Same metadata vocabulary as class metadata |
| Get Class | GET | `/ontologies/{id}/classes/{classIRI}` | — | `text/turtle`, `application/ld+json`, `application/json` | Returns full axiom set \+ metadata |
| List Classes | GET | `/ontologies/{id}/classes` | — | `application/json` | Filter by namespace, superclass |
| List Properties | GET | `/ontologies/{id}/properties` | — | `application/json` | Filter by domain, range, type (`owl:ObjectProperty`, `owl:DatatypeProperty`) |
