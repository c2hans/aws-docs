---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/prereqs.html
---

# Prerequisites and limitations
<a name="prereqs"></a>

## Prerequisites
<a name="prerequisites.d1dbd0ad-da1e-5c84-b917-6efbfd56a796"></a>

**AWS Services and Access:**
+ Active AWS account with appropriate IAM permissions for deploying and managing Amazon Neptune, Amazon Bedrock, Amazon ECS, AWS Glue Data Catalog, Amazon SageMaker Catalog, Amazon OpenSearch, Amazon S3, Amazon SNS/SQS, and AWS X-Ray
+ Amazon Bedrock model access enabled (e.g., Anthropic Claude Sonnet 4.0) through the Bedrock console
+ Amazon Bedrock AgentCore access (requires Python 3.10\+ for development with the starter toolkit)
+ VPC configuration with appropriate subnets, security groups, and network connectivity for ECS services and Neptune clusters

Note: some AWS services aren't available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.

**Technical Skills and Knowledge:**
+ Understanding of W3C Semantic Web standards (RDF, RDFS, OWL, SPARQL, SHACL, R2RML, SWRL)
+ Experience with ontology engineering and knowledge graph design
+ Familiarity with data catalog systems (AWS Glue Data Catalog, Amazon SageMaker Catalog/DataZone)
+ Knowledge of containerization and Amazon ECS deployment patterns
+ Understanding of event-driven architectures (SNS/SQS, Neptune DB Streams)
+ Experience with LLM integration and prompt engineering via Amazon Bedrock
+ Familiarity with observability tools (OpenTelemetry, AWS X-Ray, CloudWatch)

**Data and Infrastructure:**
+ Existing data sources (relational databases, data warehouses, data lakes, document repositories) with documented schemas
+ Business glossaries, data dictionaries, or domain expertise to inform ontology development
+ Network connectivity between data sources and the semantic layer infrastructure
+ S3 buckets for storing ontology versions, R2RML mappings, and document processing artifacts

**Open-Source Tools (Optional but Recommended):**
+ Ontop 5.5.0 or later for Virtual Knowledge Graph implementation
+ ELK, HermiT, or other OWL reasoners for inference and consistency checking
+ SHACL validators for constraint enforcement
+ unstructured.io for document processing (or equivalent document parsing capabilities)

**Organizational Readiness:**
+ Defined personas and responsibilities (Administrators, Data-Focused Practitioners, Business Analysts)
+ Governance processes for ontology approval, versioning, and lifecycle management
+ Human-in-the-loop workflows for semantic validation and domain expert review

## Limitations
<a name="limitations.6a0dd884-4555-5d1b-93a9-1fcdbd9b8818"></a>

**Amazon Neptune:**
+ Cluster volume size limited to **128 TiB per cluster** (up to 64 TiB in some regions)
+ Maximum of 15 read replicas per cluster
+ Query throughput scales to 100k\+ queries per second but depends on query complexity and instance types

**Amazon Bedrock AgentCore:**
+ Framework support via starter kit CLI limited to prominent frameworks (Strands, LangChain, CrewAI)
+ Session duration and memory persistence constraints depend on AgentCore service limits
+ Model access and token limits vary by foundation model provider (e.g., Anthropic Claude)

**Virtual Knowledge Graph (Ontop):**
+ Query performance depends on underlying data source capabilities and R2RML mapping complexity
+ SPARQL-to-SQL translation limited to OWL 2 QL profile for optimal query rewriting
+ Federated queries across heterogeneous sources may experience latency based on network and source system performance

**Reasoning Services:**
+ OWL reasoning complexity (ELK supports OWL 2 EL profile; HermiT supports OWL 2 DL but with higher computational cost)
+ Reasoning over large A-Box (instance data) may require materialization strategies or incremental reasoning approaches
+ SWRL rule execution performance depends on rule complexity and data volume

**Document Processing:**
+ File size limits for document ingestion (typically 50MB per file for unstructured.io and similar tools)
+ OCR accuracy for scanned documents depends on image quality and document structure
+ GraphRAG retrieval quality depends on embedding model selection and chunk size optimization

**General Constraints:**
+ Incremental adoption requires careful planning of ontology scope and R2RML mapping coverage to avoid incomplete virtualization
+ Cross-domain ontology queries may require multiple execution steps, impacting latency
+ Human-in-the-loop workflows introduce approval latency for ontology changes and entity resolution

## Product versions
<a name="product-versions.464ef7c5-68f1-5048-a092-e5340319e23b"></a>

**AWS Services:**
+ Amazon Neptune Database (1.4.7.0\+)
+ Amazon Bedrock (with AgentCore support, requires Python 3.10\+)
+ Amazon ECS (Fargate or EC2 launch types)
+ AWS Glue Data Catalog
+ Amazon SageMaker Catalog / Amazon DataZone
+ Amazon OpenSearch Service (3.5\+)
+ Amazon S3, SNS, SQS, X-Ray, CloudWatch

**Open-Source Components:**
+ **Ontop**: Version 5.5.0 (released February 14, 2026) or later
+ **ELK Reasoner**: Latest stable version compatible with OWL 2 EL
+ **HermiT Reasoner**: Latest stable version compatible with OWL 2 DL
+ **SHACL Validators**: Implementations compatible with W3C SHACL 1.1 or SHACL 1.2 specifications
+ **unstructured.io**: Latest stable version for document processing

**W3C Standards (Specifications):**
+ RDF 1.1 ([https://www.w3.org/RDF/](https://www.w3.org/RDF/))
+ RDFS 1.1 ([https://www.w3.org/TR/rdf-schema/](https://www.w3.org/RDF/))
+ OWL 2 ([https://www.w3.org/OWL/](https://www.w3.org/RDF/))
+ SPARQL 1.2 ([https://www.w3.org/TR/sparql12-query/](https://www.w3.org/RDF/))
+ SHACL 1.1 / 1.2 ([https://www.w3.org/TR/shacl/](https://www.w3.org/RDF/))
+ R2RML ([https://www.w3.org/TR/r2rml/](https://www.w3.org/RDF/))
+ SWRL (community-maintained specification)

**Note**
This architecture is designed to be version-agnostic where possible, leveraging AWS managed services that automatically update and open standards that ensure long-term compatibility. Specific version requirements apply primarily to development tooling (Python 3.10\+ for AgentCore) and open-source components (Ontop 5.5.0\+).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
