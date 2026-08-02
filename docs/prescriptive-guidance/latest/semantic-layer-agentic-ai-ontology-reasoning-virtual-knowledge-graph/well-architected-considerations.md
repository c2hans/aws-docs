---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/well-architected-considerations.html
---

# Well-Architected Considerations
<a name="well-architected-considerations"></a>

The semantic layer architecture should be evaluated against the six pillars of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). The following guidance maps architectural decisions in this guide to each pillar.

## 1. Operational Excellence
<a name="1.-operational-excellence.fb00f981-f596-5919-8846-4f1ccb3acb45"></a>

**Design Principles Applied:**
+ **Perform operations as code**: Infrastructure components (Neptune clusters, OpenSearch domains, VPCs, Lambda functions, Step Functions workflows) are defined using AWS CloudFormation or CDK, enabling version-controlled, repeatable deployments.
+ **Make frequent, small, reversible changes**: Ontology evolution follows semantic versioning; changes to class hierarchies or property definitions are deployed incrementally with backward-compatible SPARQL queries.
+ **Anticipate failure**: The architecture uses Neptune's Multi-AZ deployment with automated failover and OpenSearch's managed availability to minimize single points of failure.

**Ontology Lifecycle Management:**
+ **Import and validation**: Support structured import of ontology artifacts (OWL, SHACL, SKOS) with automated validation using OWL reasoners (e.g., HermiT, Pellet, or ELK) to check consistency, satisfiability, and classification correctness before promotion to production graphs.
+ **Versioning and approval**: Maintain ontology versions in a source-controlled repository (e.g., CodeCommit, GitHub) and/or **S3 versioned buckets** (enabling object-level version history, rollback, and lifecycle policies for ontology artifacts serialized as Turtle, N-Triples, or JSON-LD) with a formal approval workflow — ontology changes should pass reasoner validation, SHACL constraint checks, and peer review before being loaded into Neptune.
+ **Ontology Induction from data catalogs**: Support automated or semi-automated ontology induction from existing business data catalogs (e.g., **Amazon SageMaker Catalog**) and technical data catalogs (e.g., **AWS Glue Data Catalog**). Induced ontologies extract entity types, relationships, and attribute schemas from catalog metadata (table schemas, column lineage, business glossaries) and propose them as candidate OWL classes and properties. These candidates must go through the same validation pipeline — reasoner checks for logical consistency, SHACL validation for constraint compliance, and a **Human-in-the-Loop (HITL)** review process where domain experts approve, refine, or reject induced ontology fragments before they are merged into the production semantic layer.

**Operational Recommendations:**
+ Use **Amazon CloudWatch** for monitoring Neptune query latency, SPARQL endpoint availability, and OpenSearch cluster health.
+ Implement **Neptune Streams** to capture graph mutations and trigger downstream processing (e.g., re-embedding changed entities into the vector store).
+ Use **AWS X-Ray** for distributed tracing across the agent orchestration layer (AgentCore Runtime → Lambda → Neptune → OpenSearch) to identify bottlenecks.
+ Establish **runbooks** for common operational tasks: ontology reload, graph snapshot/restore, embedding re-indexing.

## 2. Security
<a name="2.-security.5c9eb844-879e-5259-9f72-39a586bab702"></a>

**Design Principles Applied:**
+ **Implement a strong identity foundation**: Neptune access is controlled through **IAM authentication** (Signature Version 4) with least-privilege policies. AgentCore Runtime agents assume scoped IAM roles for graph queries.
+ **Enable traceability**: All SPARQL queries and graph mutations are logged via **Neptune Audit Logs** to CloudWatch Logs. API Gateway access logs capture agent-to-endpoint interactions.
+ **Apply security at all layers**: The architecture uses **VPC isolation** for Neptune (private subnets, no public endpoints), **VPC endpoints** for OpenSearch Serverless, and **AWS PrivateLink** for Bedrock and AgentCore.
+ **Protect data in transit and at rest**: Neptune encrypts storage at rest using AWS KMS; SPARQL endpoints use TLS. OpenSearch encrypts indexes at rest and enforces HTTPS.

**Security Recommendations:**
+ **Cedar policy language for authorization**: Use the **Cedar policy language** to define fine-grained, attribute-based access control (ABAC) policies for the semantic layer. Cedar can be deployed through [https://aws.amazon.com/verified-permissions/](https://aws.amazon.com/verified-permissions/) (fully managed) or as a **custom authorizer** using the open-source [Cedar SDK](https://www.cedarpolicy.com/) embedded in a Lambda function, Fargate service, or agent orchestration layer — the latter gives full control over policy storage, evaluation context, and integration patterns. Cedar policies can express rules such as: *"Agent X can query ontology classes in namespace *`finance:`* only if the requesting user belongs to the *`FinanceAnalysts`* group."* This provides a centralized, auditable authorization layer that is decoupled from application code and can enforce policies across Neptune SPARQL queries, OpenSearch indexes, and AgentCore tool invocations.
+ **RDF namespaces for multi-tenancy and access control**: Use **RDF named graphs and namespace prefixes** to logically partition ontology data by domain, team, business unit, or group (e.g., `finance:`, `engineering:`, `marketing:`). Each namespace maps to a distinct named graph in Neptune, enabling:
  + **Namespace-scoped access control**: Cedar policies and IAM conditions reference the namespace/named graph to grant or deny access — e.g., users in the `FinanceAnalysts` IdP group can query `finance:` graphs, while `EngineeringLeads` can query `engineering:` graphs.
  + **Ownership and delegation**: Namespace ownership is assigned to users or groups sourced from the organization's **Identity Provider (IdP)** via **OIDC** or **SAML** federation through IAM Identity Center. Group memberships from the IdP (e.g., Active Directory groups, Okta groups, Azure AD groups) are propagated as session tags or SAML attributes, which Cedar policies and IAM session policies evaluate at query time.
  + **Tenant isolation**: SPARQL queries are scoped to specific named graphs using `FROM` or `FROM NAMED` clauses, and the agent orchestration layer enforces that agents can only access graphs authorized for the delegating user's IdP groups. This prevents cross-tenant data leakage while allowing shared ontology base classes (e.g., a common `core:` namespace) to be accessible across all tenants.
  + **Hierarchical namespace structure**: Support nested namespace patterns (e.g., `org:finance:risk:`, `org:finance:compliance:`) for fine-grained scoping within large organizations, with inheritance rules defined in Cedar policies.
+ **Service accounts for agent identities**: AI agents (AgentCore Runtime agents, Lambda-based orchestrators) should operate using **dedicated IAM service accounts** (IAM roles) with tightly scoped permissions — not shared or overly broad roles. Each agent role should have:
  + Least-privilege access to specific Neptune graph endpoints and named graphs
  + Scoped OpenSearch index permissions (read-only vs. read-write)
  + Explicit deny policies preventing cross-tenant or cross-domain access
  + Session tags or context keys for Cedar policy evaluation
+ **User credential delegation for data access**: When agents act on behalf of human users, the architecture must ensure that **the user's own credentials and entitlements** govern data access — not the agent's service account alone. This is critical for maintaining data governance and audit compliance. **AgentCore Identity** provides the identity propagation framework for this pattern. Implementation patterns include:
  + **Identity propagation with IAM Identity Center and AgentCore Identity**: Pass the authenticated user's identity through the agent invocation chain using [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html) and AgentCore's identity resolution, so downstream services (Neptune, OpenSearch, S3) enforce access based on the user's IdP group memberships and attribute-based policies. AgentCore Identity resolves the calling user's identity context and makes it available to tool implementations and Cedar policy evaluation.
  + **Session policies**: Attach inline session policies when agents assume roles on behalf of users, constraining the agent's permissions to the intersection of the service account role and the user's entitlements.
  + **Cedar \+ user context**: Pass user attributes (department, role, clearance level) as Cedar context in authorization requests, so that even when the agent's service account makes the API call, the Cedar policy evaluates against the *user's* attributes to determine which ontology classes, named graphs, or search indexes are accessible.
  + **Audit trail**: Log both the agent service account identity *and* the delegating user's identity in CloudTrail and Neptune audit logs, ensuring full traceability of "who asked the agent to do what."
+ Use **SHACL constraints** in the ontology layer as a semantic-level validation mechanism — validate that agent-submitted graph mutations conform to the ontology schema before they are committed.
+ Implement **fine-grained access control** in OpenSearch for multi-tenant semantic layers (document-level security by ontology namespace), integrated with the Cedar authorization layer.
+ Encrypt sensitive entity attributes (PII in knowledge graphs) using **client-side encryption** before storing in Neptune.
+ Use custom classifiers or data scanning tools to audit ontology data for unintended PII exposure during bulk loads.

## 3. Reliability
<a name="3.-reliability.eaaa141a-4074-517c-907e-f68d5b184a35"></a>

**Design Principles Applied:**
+ **Automatically recover from failure**: Neptune Multi-AZ with automatic failover (typically 1–2 minutes for standard clusters); OpenSearch Serverless with built-in replication.
+ **Scale horizontally**: Neptune read replicas for query fan-out; OpenSearch auto-scaling for vector search throughput.
+ **Manage change in automation**: Ontology deployments through CI/CD pipelines with SHACL validation gates.

**Reliability Recommendations:**
+ Use **Neptune Global Database** for disaster recovery when the semantic layer is mission-critical (RPO < 1 second, RTO < 1 minute for read workloads).
+ Implement **circuit breakers** in the agent orchestration layer: if Neptune or OpenSearch becomes unavailable, agents should gracefully degrade (e.g., fall back to cached ontology subsets or simplified reasoning).
+ Design **idempotent** graph mutation operations — agents may retry failed writes, and the ontology update pipeline should handle duplicate triples gracefully.
+ Neptune cluster volume storage **scales automatically** in 10 GB segments (up to 128 TiB) as data grows — no configuration required. Monitor `VolumeBytesUsed` via CloudWatch to track ontology growth trends and plan for cost implications of expanding storage.
+ Test **failure modes** regularly: simulate AZ failure, Neptune failover, OpenSearch shard migration.

## 4. Performance Efficiency
<a name="4.-performance-efficiency.c410d573-3f8d-5ee7-95e8-10193f329589"></a>

**Design Principles Applied:**
+ **Use purpose-built databases**: Neptune for graph traversal and SPARQL querying, OpenSearch for vector similarity and hybrid search — each service optimized for its query pattern.
+ **Go global in minutes**: Neptune Global Database and OpenSearch cross-region replication enable low-latency access from any region.
+ **Experiment more often**: Neptune Serverless allows rapid prototyping of new ontology patterns without capacity provisioning.

**Performance Recommendations:**
+ **SPARQL query optimization**: Use `OPTIONAL` patterns sparingly; prefer bound variable patterns. Leverage Neptune's query plan explanations (`EXPLAIN`/`PROFILE`) to identify expensive operations.
+ **Caching layer**: Deploy **Amazon ElastiCache (Redis)** to cache frequently-accessed ontology subgraphs (e.g., class hierarchies, property domains/ranges) that rarely change — reducing Neptune query load during high-concurrency agent operations.
+ **Neptune Analytics** for bulk graph computations: offload expensive analytics (community detection, influence propagation, shortest path) to Neptune Analytics rather than running them on the transactional Neptune DB cluster.
+ **Vector index tuning**: In OpenSearch, configure HNSW parameters (`ef_construction`, `m`) based on the tradeoff between recall accuracy and query latency for the specific embedding dimensions used.
+ **Consider S3 Vectors** for cold/archival vector storage tiers where query latency tolerance is >500ms but cost optimization is paramount (up to 90% savings).

## 5. Cost Optimization
<a name="5.-cost-optimization.73893324-b344-5617-8f21-e755d9ba62ba"></a>

**Design Principles Applied:**
+ **Adopt a consumption model**: Neptune Serverless scales down to minimum configured NCUs (as low as 1.0 NCU) during idle periods; OpenSearch Serverless scales based on actual query volume.
+ **Measure overall efficiency**: Monitor cost-per-query metrics across the Neptune and OpenSearch tiers to right-size capacity.
+ **Stop spending money on undifferentiated heavy lifting**: Using managed services (Neptune, OpenSearch, Bedrock) eliminates operational overhead of running open-source graph databases.

**Cost Optimization Recommendations:**
+ **Right-size Neptune**: For development/staging, use Neptune Serverless with minimum NCUs; for production steady-state, evaluate provisioned instances (which can be 30-40% cheaper with Reserved Instances or Database Savings Plans).
+ **Database Savings Plans**: Neptune Analytics and OpenSearch Service are both eligible for Database Savings Plans (up to 35% savings for serverless deployments, up to 20% for provisioned instances, with 1-year commitment).
+ **Tiered vector storage**: Store the full embedding corpus in **S3 Vectors** (low cost) and maintain a hot subset in **OpenSearch** (low latency) — use one-click export from S3 Vectors to OpenSearch for seamless tiering.
+ **Neptune storage optimization**: Use `DROP GRAPH` or named graph isolation to manage ontology versions; archive deprecated versions to S3 as RDF exports rather than keeping them in live storage.
+ **Query cost tracking**: Use Neptune's `Query/Requests` and `Query/Time` CloudWatch metrics to identify and optimize expensive queries that drive compute costs.

## 6. Sustainability
<a name="6.-sustainability.c21c48dd-675d-5067-9739-9f0dfe4903c7"></a>

**Design Principles Applied:**
+ **Understand your impact**: Quantify the compute and storage footprint of the semantic layer components across Neptune, OpenSearch, and supporting services.
+ **Maximize utilization**: Neptune Serverless and OpenSearch Serverless automatically scale down during low-demand periods, reducing energy consumption.
+ **Use managed services**: AWS managed services run on shared, optimized infrastructure with better energy efficiency than self-managed deployments.

**Sustainability Recommendations:**
+ **Choose Graviton-based instances** (db.r8g Graviton4, db.r7g Graviton3, db.r6g Graviton2) for Neptune provisioned deployments — AWS Graviton-based instances use up to 60% less energy than comparable x86 instances (general Graviton claim across generations). R8g (Graviton4) is the latest generation available and offers significant price-performance improvements (up to 4.7x better write, 3.7x better read throughput over prior generations).
+ **Consolidate ontology namespaces**: Reduce redundant triples and ontology fragments to minimize storage and query processing overhead.
+ **Batch embedding operations**: When updating the vector store, batch entity embedding generation through Amazon Bedrock rather than making individual API calls — reduces compute cycles and network overhead.
+ **Data lifecycle policies**: Implement TTL or archival rules for temporal graph data (event entities, transient relationships) to prevent unbounded storage growth.
