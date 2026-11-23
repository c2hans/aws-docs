---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/rules-management.html
---

# Rules Management

## Rules Management (SHACL \+ SPARQL)
<a name="rules-management--shacl---sparql-.140facfa-0462-5d91-a43d-a90b080bc1e5"></a>

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| Import Rules | POST | `/ontologies/{id}/rules` | `text/turtle` (SHACL Shapes Graph), `application/n-quads` | `application/json` | Accepts SHACL Shapes Graph (Turtle) or SPARQL CONSTRUCT/SPIN |
| Export Rules | GET | `/ontologies/{id}/rules/export` | — | `text/turtle` (default), `application/n-quads` | Turtle for SHACL Shapes Graph; N-Quads for rule provenance with named graph context |
| List Rules | GET | `/ontologies/{id}/rules` | — | `application/json` | Filter by type: `shacl`, `sparql`, `swrl` |
| Get Rule | GET | `/ontologies/{id}/rules/{ruleId}` | — | `text/turtle`, `application/json` |  |
| Update Rule | PUT | `/ontologies/{id}/rules/{ruleId}` | `text/turtle`, `application/json` | `application/json` |  |
| Delete Rule | DELETE | `/ontologies/{id}/rules/{ruleId}` | — | — |  |
| Validate Rules | POST | `/ontologies/{id}/rules/validate` | — | `application/json` | Run SHACL validation against a named graph; returns violation report |
