---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/ontology-version-management.html
---

# Ontology Version Management

## Ontology Version Management REST API
<a name="ontology-version-management-rest-api.c6e4ce06-91e9-5efe-8df4-f54785968266"></a>

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| List Versions | GET | `/ontologies/{id}/versions` | — | `application/json` | Returns version history with timestamps and authors |
| Get Version | GET | `/ontologies/{id}/versions/{versionId}` | — | `text/turtle`, `application/n-quads`, `application/trig` | Retrieve a specific version snapshot; N-Quads recommended for provenance-aware retrieval |
| Publish Version | POST | `/ontologies/{id}/versions/{versionId}/publish` | — | `application/json` | Publish ontology version |
| Diff Versions | GET | `/ontologies/{id}/versions/diff?from={v1}&to={v2}` | — | `application/json`, `text/turtle` | Returns added/removed/changed axioms |
| Rollback | POST | `/ontologies/{id}/versions/{versionId}/rollback` | — | `application/json` | Restore a prior version as active |
