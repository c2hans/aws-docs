---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/rest-api.html
---

# REST API

## REST API
<a name="rest-api.4ebd0208-8328-5d69-8c44-ec50939c0967"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/40a94040-9901-4fd3-9b89-66f7b4ece3bb.png)

## Data Flow - REST API
<a name="data-flow---rest-api.8778f211-927c-572d-a6d6-3f1fe3d6edd2"></a>

**Step 1 — DNS Resolution (REST API Client → Amazon Route 53):** The REST API Client resolves the API's custom domain name via Amazon Route 53, which serves as the DNS routing service. Route 53 returns the IP address associated with the API Gateway custom domain endpoint.

**Step 2 — HTTPS Connection (REST API Client → Amazon API Gateway):** The REST API Client establishes an HTTPS connection to Amazon API Gateway. The connection is secured using the SSL/TLS certificate managed by AWS Certificate Manager (ACM).

**Step 3 — Certificate Association (Amazon Route 53 → AWS Certificate Manager):** AWS Certificate Manager (ACM) provides the SSL/TLS certificate for the API Gateway's custom domain. This is a certificate association for HTTPS termination rather than a runtime API call — ACM ensures that all traffic between the client and API Gateway is encrypted in transit.

**Step 4 — Authentication (REST API Client → Identity Provider):** The REST API Client authenticates with the external Identity Provider (IdP) using an OIDC-compliant flow. For browser-based applications, this may involve a redirect-based authorization code flow. For machine-to-machine communication, this typically uses the client credentials grant. The IdP issues a JWT (JSON Web Token) / Bearer token upon successful authentication.

**Step 5 — Authenticated Request (REST API Client → Amazon API Gateway):** The REST API Client sends the API request to Amazon API Gateway with the JWT/Bearer token included in the `Authorization` header (e.g., `Authorization: Bearer <token>`). This is the primary API invocation carrying the business payload.

**Step 6 — Token Validation (Amazon API Gateway → JWT/OIDC Authorizer Lambda):** Amazon API Gateway invokes the Lambda authorizer (also known as a custom authorizer) to validate the JWT token. The Lambda authorizer is configured as a request-based or token-based authorizer that inspects the `Authorization` header.

**Step 7 — JWKS Key Retrieval (JWT/OIDC Authorizer Lambda → Identity Provider):** The JWT/OIDC Authorizer Lambda function calls the Identity Provider's `.well-known/openid-configuration` endpoint to retrieve the JSON Web Key Set (JWKS) containing the public keys. The authorizer uses these keys to verify the JWT token's signature, validate claims (issuer, audience, expiration), and generate an IAM policy that grants or denies access to the requested API resource.

**Step 8 — Business Logic Execution (Amazon API Gateway → Backend Lambda):** After the Lambda authorizer returns an "Allow" policy, Amazon API Gateway routes the request to the backend Lambda function. This Lambda function executes the REST API business logic serverlessly, processing the request and returning the response through API Gateway back to the client.

**Infrastructure Organization:** All AWS resources are deployed within a single AWS account. The Amazon API Gateway and both Lambda functions operate within a Virtual Private Cloud (VPC) for network isolation and security. The VPC boundary (blue border with padlock icon) encompasses the core compute components. Amazon Route 53 and AWS Certificate Manager operate at the account level. The Identity Provider (IdP) is external to the AWS Cloud boundary.

**Architecture Highlights:**
+ **Serverless Design:** Uses Lambda functions for scalable, event-driven compute with no infrastructure management
+ **Zero-Trust Security:** Every request is authenticated (IdP) and authorized (Lambda authorizer) before reaching business logic
+ **Certificate Management:** ACM automates SSL/TLS certificate provisioning and renewal for the custom domain
+ **Standards-Based Authentication:** Leverages OIDC/OAuth 2.0 and JWT for interoperable, industry-standard authentication
+ **Separation of Concerns:** Authentication (IdP), authorization (Lambda authorizer), and business logic (backend Lambda) are cleanly separated

[**Ontology Engineering REST API**](ontology-engineering.md)

[**Ontology Version Management REST API**](ontology-version-management.md)

[**Ontology Mapping Management (Source Schema → Ontology)**](ontology-mapping-management-source-schema-ontology.md)

[**Rules Management (SHACL \+ SPARQL)**](rules-management.md)

[**Semantic Metadata Management (Classes & Properties)**](semantic-metadata-management-classes-properties.md)

[**Semantic Search (Classes & Properties)**](semantic-search-classes-properties.md)

[**Metric Definition REST API**](metric-definition-rest-api.md)

### Supported MIME Types — Reference
<a name="supported-mime-types---reference.cec840d4-abe8-56eb-a949-18aa2a7618e9"></a>

|
|
| Format | MIME Type | Use Case |
| --- |--- |--- |
| Turtle | `text/turtle` | Default; human-readable, compact; preferred for ontology authoring and import/export |
| N-Quads | `application/n-quads` | Named graph support; recommended for versioned and provenance-aware exports |
| N-Triples | `application/n-triples` | Line-based, streaming-friendly; suited for large bulk exports |
| TriG | `application/trig` | Turtle \+ named graphs; natural fit for T-Box/A-Box separation in a single document |
| RDF/XML | `application/rdf+xml` | Legacy interoperability |
| JSON-LD | `application/ld+json` | Web/API-friendly; recommended for developer tooling and downstream API consumers |
| N3 | `text/n3` | Superset of Turtle; includes rules support |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.76746acc-9631-563a-a532-25daee7da7fe"></a>
+ **Content Negotiation:** All serialization endpoints support `Accept` (response format) and `Content-Type` (request body format) headers per the MIME type table above. Default response format is `text/turtle` for RDF resources and `application/json` for metadata/list endpoints. Returns `406 Not Acceptable` with a body listing supported types when an unsupported format is requested.
+ **Named Graph Recommendations:** Use `application/n-quads` or `application/trig` for exports requiring named graph provenance (e.g., versioned ontology snapshots, T-Box/A-Box separation).
+ **Authentication:** JWT/OIDC bearer token validated by API Gateway Lambda authorizer. Supports any OIDC-compliant identity provider including Amazon Cognito, Microsoft Entra ID, Okta, Auth0, Keycloak, and others. Required claims: `sub`, `groups`, `act`. Scope: `semantic-layer:access`.
+ **API Versioning:** All endpoints versioned via path prefix `/v1/`.
+ **Audit Logging:** All write operations emit structured events to CloudWatch Logs with `ontologyId`, `operation`, `principalId`, `contentType`, and `timestamp`.
+ **Observability:** OpenTelemetry traces propagated across all API calls; spans include ontology IRI, operation type, serialization format, and latency.
