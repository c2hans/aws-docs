---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/ontology-mapping-management-source-schema-ontology.html
---

# Ontology Mapping Management (Source Schema → Ontology)

## Ontology Mapping Management (Source Schema → Ontology)
<a name="ontology-mapping-management--source-schema---ontology-.4e86cf1a-1ac3-5936-8ca8-d44af2705afe"></a>

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| Create Mapping | POST | `/ontologies/{id}/mappings` | `text/turtle` (R2RML), `application/json` | `application/json` | Accepts R2RML (Turtle serialization) or custom mapping format |
| List Mappings | GET | `/ontologies/{id}/mappings` | — | `application/json` | Filter by source schema, target class |
| Get Mapping | GET | `/ontologies/{id}/mappings/{mappingId}` | — | `text/turtle`, `application/json` |  |
| Update Mapping | PUT | `/ontologies/{id}/mappings/{mappingId}` | `text/turtle`, `application/json` | `application/json` |  |
| Delete Mapping | DELETE | `/ontologies/{id}/mappings/{mappingId}` | — | — |  |
| Validate Mapping | POST | `/ontologies/{id}/mappings/{mappingId}/validate` | — | `application/json` | Dry-run against source schema |
