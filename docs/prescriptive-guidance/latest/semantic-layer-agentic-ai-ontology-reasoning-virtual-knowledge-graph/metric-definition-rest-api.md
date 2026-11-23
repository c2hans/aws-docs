---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/metric-definition-rest-api.html
---

# Metric Definition REST API

|
|
| Operation | Method | Endpoint | Request Content-Type | Response Accept | Notes |
| --- |--- |--- |--- |--- |--- |
| List Metrics | GET | /ontologies/{id}/versions/{versionId}/metrics | - | application/json | List all metric definitions for an ontology version |
| Get Metric | GET | /ontologies/{id}/versions/{versionId}/metrics/{metricId} | - | text/turtle |  |
| Create Metric | POST | /ontologies/{id}/versions/{versionId}/metrics | text/turtle | - | application/json |
| Update Metric | PUT | /ontologies/{id}/versions/{versionId}/metrics/{metricId} | text/turtle | - | application/json |
| Delete Metric | DELETE | /ontologies/{id}/versions/{versionId}/metrics/{metricId} | - | application/json | Soft-delete; governed by approval workflow |
| Validate Metric | POST | /ontologies/{id}/versions/{versionId}/metrics/{metricId}/validate | - | application/json | Test pre-compiled expression against sample data via VKG |
| Publish Metric | POST | /ontologies/{id}/versions/{versionId}/metrics/{metricId}/publish | - | application/json | Promote from draft to published |
