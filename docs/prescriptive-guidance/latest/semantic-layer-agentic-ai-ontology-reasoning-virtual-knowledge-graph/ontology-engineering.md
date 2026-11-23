---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/ontology-engineering.html
---

# Ontology Engineering

## Ontology Engineering REST API
<a name="ontology-engineering-rest-api.5a123d1b-d784-58fa-9394-861e709c1c91"></a>

The following API surface defines the contract for Ontology Management & Knowledge Engineering UIs, services, and agents to interact with the Semantic Layer.

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| Import Ontology | POST | `/ontologies` | `text/turtle`, `application/n-quads`, `application/n-triples`, `application/trig`, `application/rdf+xml`, `application/ld+json` | — | Multipart or body; format auto-detected from Content-Type |
| Export Ontology | GET | `/ontologies/{id}/export` | — | `text/turtle` (default), `application/n-quads`, `application/n-triples`, `application/trig`, `application/rdf+xml`, `application/ld+json` | Returns `406 Not Acceptable` for unsupported types |
| Get Ontology | GET | `/ontologies/{id}` | — | `text/turtle`, `application/ld+json` | Returns ontology metadata \+ IRI |
| List Ontologies | GET | `/ontologies` | — | `application/json` | Supports pagination, filter by namespace/domain |
| Delete Ontology | DELETE | `/ontologies/{id}` | — | — | Soft-delete with version retention |
