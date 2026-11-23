---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/governance-security.html
---

# Governance / Security

## Governance / Security
<a name="governance---security.fa721167-b19d-5a4f-ac1d-881bd7f3770a"></a>

The Semantic Layer implements comprehensive governance and security controls across all components to ensure data protection, access control, compliance, and auditability for enterprise knowledge graph deployments.

### Access Control & Authentication
<a name="access-control-9999999999999999amp--authentication.eaca4879-e825-503c-a0da-facddddbb251"></a>
+ **Identity & Access Management** - AWS IAM roles and policies enforce least-privilege access for service-to-service communication (ECS tasks calling Neptune, Athena, Redshift, S3, Bedrock, Secrets Manager). Fine-grained permissions control who can read, write, or modify ontologies, mappings, and instance data, enforced through group-based authorization derived from JWT claims.
+ **Authentication Model** - The architecture implements a two-tier authentication model:

  *Interface Layer (external-facing)* - The AgentCore Gateway, MCP Server, and A2A endpoints accept JWT/OIDC bearer tokens from any OIDC-compliant identity provider, including Amazon Cognito, Microsoft Entra ID, Okta, Auth0, Keycloak, and others. For A2A interoperability, IAM SigV4 is also supported at the Interface Layer to accommodate AWS-native agent callers. The AgentCore Gateway validates inbound tokens and forwards authenticated requests to downstream services.

  *Internal services (VKG, Symbolic Reasoning, GraphRAG, Intent Classification, Query Planning, Ontology Induction, Information Extraction)* - JWT/OIDC only. The AgentCore Gateway propagates the validated JWT to each service, which extracts user identity and authorization context directly from the token. IAM execution roles for ECS tasks handle outbound calls to AWS services (Neptune, Athena, Redshift, S3, Bedrock) via SigV4, managed automatically by the AWS SDK.

  **Required JWT Claims** - All JWT tokens must include:
  + `sub` - unique user identifier (for row-level security, audit logging, and provenance tracking)
  + `groups` - authorization groups (for named graph restrictions, data masking, and role-based access control). Maps to roles such as `ontology-admin`, `knowledge-engineer`, `data-reader`, `agent-operator`
  + `act` - agent identity claim (RFC 8693), identifying the agent acting on behalf of the user (for audit logging, delegation chain tracking, and distinguishing which agent performed an action). Supports nested delegation for multi-agent workflows

  **Authorization Scope** - A single OAuth scope (`semantic-layer:access`) grants entry to the Semantic Layer. Fine-grained authorization is enforced through group-based policies derived from the `groups` JWT claim, not through multiple per-service scopes.

  **Row-Level Security** - The architecture implements row-level security through three complementary techniques based on the target data source:

  *Neptune (SPARQL Query Rewriting)* - For queries targeting the Semantic Layer Graph Database, the VKG Service extracts the authenticated user's identity and groups from the JWT, resolves authorization policies (via OPA, Lake Formation, or ontology-defined access rules), and injects FILTER clauses or named graph restrictions into the SPARQL query before execution. This approach also enables data masking and redaction of sensitive attributes (PII, PHI) based on user roles.

  *AWS Data Layer Sources (Trusted Identity Propagation)* - For queries targeting virtualized Data Layer sources (Athena, Redshift), the VKG Service leverages AWS Trusted Identity Propagation (TIP) via IAM Identity Center. The end-user's IdP identity is propagated through IAM Identity Center when establishing JDBC connections, enabling Lake Formation fine-grained access controls (for Athena) and native row-level security/column-level security (for Redshift) to enforce per-user data access policies at the source.

  *Non-AWS Data Layer Sources (OAuth/Session-Based)* - For non-AWS sources (Snowflake, Databricks), the VKG Service uses OAuth token propagation or per-user session establishment to enable native row access policies (Snowflake) and Unity Catalog permissions (Databricks). For sources that do not support identity propagation, the VKG Service falls back to SQL query rewriting, injecting WHERE clauses into the translated SQL based on the user's authorization context.

  **Agent Identity** - The `act` claim in the JWT identifies which agent is acting on behalf of the user. This is critical for provenance, audit logging, and distinguishing agent actions in multi-agent workflows. For A2A delegation chains, the `act` claim supports nesting (RFC 8693) to track the full delegation path. The emerging Agentic JWT (A-JWT) IETF draft extends this pattern with cryptographic agent fingerprinting for organizations requiring stronger agent identity guarantees.

### Data Protection & Encryption
<a name="data-protection-9999999999999999amp--encryption.72199376-7c15-54d7-8fbc-165fb2c2b2e2"></a>
+ **Encryption at Rest** — Neptune DB, OpenSearch, and S3 buckets enforce server-side encryption using AWS KMS with customer-managed keys (CMK) for sensitive ontologies and knowledge graphs.
+ **Encryption in Transit** — All communication between Semantic Layer components uses TLS 1.2\+ encryption. VPC endpoints ensure private connectivity without traversing the public internet.
+ **Data Masking & Redaction** — Sensitive attributes (PII, PHI) can be masked or redacted at query time based on user roles, using SPARQL query rewriting or post-processing filters in the VKG Service.

### Network Security & Isolation
<a name="network-security-9999999999999999amp--isolation.93e6eafc-0d8c-543b-90fd-be4f9db83d20"></a>
+ **VPC-Native Architecture** — Neptune DB, VKG Service (ECS), Symbolic Reasoning Service, and Lambda functions run within private subnets with no direct internet access. Security groups and NACLs restrict traffic to authorized sources.
+ **VPC Endpoints** — Private connectivity to AWS services (S3, Secrets Manager, CloudWatch) via VPC endpoints eliminates exposure to the public internet.
+ **API Gateway & WAF** — AgentCore Gateway fronts the VKG Service with AWS WAF rules to protect against SQL injection, SPARQL injection, and DDoS attacks.

### Ontology & Mapping Governance
<a name="ontology-9999999999999999amp--mapping-governance.2391d4af-59e9-5fc8-9a87-ab8d560a406d"></a>
+ **Version Control** — Ontologies (T-Box) and R2RML mappings are versioned using **S3 Versioned Buckets** or **Git repositories** (recommended implementations). S3 versioning provides automatic version history with rollback capabilities, while Git repositories enable collaborative development with branch-based workflows, pull requests, and approval gates. Neptune named graphs enable side-by-side deployment of ontology versions for A/B testing or gradual migration.
+ **Change Management** — Ontology modifications trigger automated validation workflows (ELK reasoner for consistency checking, SHACL for constraint validation) before deployment. Neptune DB Streams emit change events for audit logging and downstream notification. Changes are tested in non-production Neptune instances before promotion to production.
+ **Approval Workflows** — Critical ontology changes (class hierarchy modifications, property domain/range changes, breaking changes to R2RML mappings) require multi-party approval via internal workflow systems or third-party tools like ServiceNow. Approval policies are enforced through Git branch protection rules or S3 bucket policies that require signed approvals before deployment.
+ **Catalog Integration** — **AWS Glue Data Catalog** and **Amazon SageMaker Catalog** track lineage from source data (Data Layer) through R2RML mappings to Neptune entities, enabling impact analysis and compliance reporting. Open-source and third-party data catalog platforms including **DataHub** (LinkedIn's open-source metadata platform) and **Collibra** (enterprise data governance platform) can be integrated via APIs or OpenLineage-compatible connectors to provide unified metadata management, business glossary alignment, and cross-platform lineage tracking across hybrid and multicloud environments.

### Data Lineage & Provenance
<a name="data-lineage-9999999999999999amp--provenance.c2c3916d-d7e5-5166-8191-8ebcab423b1b"></a>
+ **Catalog Integration** — AWS Glue Data Catalog and Amazon SageMaker Catalog track lineage from source data (Data Layer) through R2RML mappings to Neptune entities, enabling impact analysis and compliance reporting.
+ **Provenance Metadata** — Every triple in Neptune includes provenance annotations (source system, extraction timestamp, confidence score, validation status) stored as reified statements or named graph metadata.
+ **Audit Logging** — All SPARQL queries, ontology modifications, and reasoning operations are logged to CloudWatch Logs with user identity, timestamp, and query details for compliance audits.

### Compliance & Regulatory Controls
<a name="compliance-9999999999999999amp--regulatory-controls.5a3dd9c3-6074-55ab-afe7-0caea4fb8965"></a>
+ **Data Residency** — Neptune DB and S3 buckets are deployed in specific AWS regions to meet data residency requirements (e.g., GDPR, HIPAA).
+ **Retention Policies** — S3 lifecycle policies and Neptune backup retention settings enforce data retention requirements. Automated deletion of expired knowledge graph data based on ontology-defined retention rules.
+ **Compliance Frameworks** — Architecture supports HIPAA, GDPR, SOC 2, and FedRAMP compliance through encryption, access controls, audit logging, and data residency controls.

### Reasoning & Validation Security
<a name="reasoning-9999999999999999amp--validation-security.0f9dea7f-d6de-514d-92fe-bcf6fdf02349"></a>
+ **Trusted Reasoning Engines** — Symbolic Reasoning Service (ELK, SHACL, SWRL) runs in isolated ECS tasks with read-only access to Neptune. Reasoning results are validated before being asserted into the knowledge graph.
+ **Constraint Enforcement** — SHACL shapes define data quality and security constraints (e.g., "PII fields must be encrypted", "Claims must have valid submitter"). Violations are flagged and prevented from entering the Semantic Layer Graph Database.
+ **Automated Reasoning Guardrails** — Amazon Bedrock Automated Reasoning validates critical inferences to prevent incorrect or malicious knowledge from being asserted.

### Monitoring & Incident Response
<a name="monitoring-9999999999999999amp--incident-response.0f87a6e5-0093-5eec-8428-fee0a9ed8545"></a>
+ **Observability** — OpenTelemetry traces, CloudWatch Logs, and X-Ray provide end-to-end visibility into query execution, reasoning workflows, and access patterns. Anomaly detection alerts on unusual query patterns or access attempts.
+ **Security Monitoring** — AWS GuardDuty and Security Hub monitor for threats. CloudTrail logs all API calls to Neptune, S3, and IAM for forensic analysis.
+ **Incident Response** — Automated runbooks (AWS Systems Manager) respond to security events (e.g., unauthorized access attempts, SPARQL injection detection) by isolating affected resources and notifying security teams.

This governance and security framework ensures that the Semantic Layer meets enterprise requirements for data protection, access control, compliance, and auditability — enabling trusted, production-grade knowledge graph deployments for agentic AI applications.
