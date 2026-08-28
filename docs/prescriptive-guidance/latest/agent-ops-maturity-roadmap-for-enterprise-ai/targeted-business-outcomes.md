---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/targeted-business-outcomes.html
---

# Architecture overview
<a name="targeted-business-outcomes"></a>

The guidance defines two primary deployment models. The single-account model is appropriate for proof-of-concept work and individual experimentation. The multi-account model is required for production workloads.

|
|
| Model | When to use | Trade-offs |
| --- |--- |--- |
| **Single account** | Proof-of-concept development, individual experimentation, internal demonstrations. | Fastest to set up with zero cross-account complexity. No workload isolation, environment separation, auditability, or production-grade governance. Cannot enforce environment-specific security boundaries or cost attribution at the account level. |
| **Multi-account** | Production workloads requiring workload isolation, environment separation, centralized observability, and shared AI tooling. | Full security isolation and governance. Increased management surface, as each account adds cross-account IAM configuration, networking, and operational overhead. |

Within the multi-account model, you adopt the accounts relevant to your current stage and expand incrementally as requirements grow. The architecture is designed so that teams with an existing landing zone add only the net-new accounts their Agentic AI platform requires, rather than re-creating governance infrastructure that already exists elsewhere.

## Architecture diagram
<a name="architecture-diagram.a03e23e8-0953-531c-ae16-0e93370625d4"></a>

The architecture diagram accompanying this guide illustrates the full multi-account topology, including the Agentic OU, the Gateway OU, CI/CD pipeline flow across the shared tooling account, and the relationship between workload accounts, gateway accounts, observability and data lake accounts. The numbered callouts on the diagram correspond to the descriptions below.

1. **Foundational accounts.** Management and security accounts enforce SCPs, audit trails, and encryption across all platform accounts.

1. **Source control.** Agentic engineers push code from their local IDE to the source repository in the shared tooling account, triggering the CI/CD Agent Promotion Pipeline.

1. **Build. **AWS CodeBuild compiles agent code, runs unit tests, and pushes the container image to the shared Amazon ECR registry.

1. **Deploy to dev and evaluate.** The pipeline deploys the image to the development account and runs AgentCore Evaluations.

1. **Promote to staging and production. **Manual approval gates require human review before each promotion. The same image digest is deployed to staging, then to production after a second approval.

1. **Agent runtime.** Workload accounts host AgentCore Runtime with Bedrock Models, memory, MCP gateway, identity, code interpreter, Bedrock Guardrails, and knowledge bases.

1. **Generative AI Gateway.** Per-environment gateway accounts route model invocations, enforce token budgets and rate limits, and host the AWS Agent Registry for agent version management.

1. **Data lake.** AWS Lake Formation governs data access. AWS Glue pipelines transform raw data into processed datasets available to agents via Bedrock Knowledge Base in the workload accounts.

1. **Observability account. **Amazon CloudWatch and AgentCore Observability aggregate agent traces, model metrics, token usage, and cost attribution from all workload and gateway accounts.

### Design principles
<a name="design-principles"></a>

The architecture aligns with the AWS Well-Architected Framework and is guided by five principles:
+ **Least-privilege isolation (Security Pillar). **Each account serves a single, well-defined purpose. Misconfigurations, cost overruns, and security incidents are contained to one functional domain rather than propagating across the platform.
+ **Observability as a first-class concern (Operational Excellence Pillar). **Agent traces, model metrics, token usage analytics, and cost attribution require dashboards that span all workload accounts. A dedicated observability account provides this capability without requiring access to workload account resources directly.
+ **Separation of generative AI gateways from workloads (Operational Excellence Pillar). **The model gateway and agent registry live in dedicated per-environment gateway accounts. This isolates model routing, rate limiting, and token budget enforcement from agent runtime logic, preventing any single team from bypassing platform-level cost controls.
+ **Progressive complexity (Operational Excellence Pillar). **Teams start with the simplest topology that meets their needs and add accounts as requirements grow. The data lake account and a full staging environment, for example, are introduced only when workload maturity justifies the operational overhead.
+ **Non-duplication with existing governance (Cost Optimization Pillar). **When an organization already operates a landing zone, the architecture overlays AI-specific accounts without recreating management, security, log archive, or networking infrastructure.

### Account structure
<a name="account-structure"></a>

This section describes each account in the architecture, its purpose, the services it hosts, and why it exists as a separate account. The single-account model is covered first for teams in early stages. Foundational accounts are covered first, followed by per-environment workload and gateway accounts, and finally the data lake account.

#### Single account
<a name="single-account.700896b7-294e-5aa0-ae9d-4bacccdda3ac"></a>

The single-account model consolidates all AI agent platform components into one AWS account. It is appropriate for proof-of-concept development, individual developer experimentation, and internal demonstrations.

|
|
| ImportantThe single-account model does not provide workload isolation, environment separation, or production-grade governance. Do not use it for production deployments, workloads that process sensitive data, or any environment where you require auditability of agent actions. |
| --- |

#### Multi-account
<a name="multi-account.9f98486e-6736-5615-9247-24b86b43806c"></a>

The multi-account topology introduces dedicated accounts for management, security, observability, shared tooling, generative AI gateways, workload environments, and data. The following sections describe each account, its purpose, the services it hosts, and the design decisions behind its placement.

##### agentic-ai-platform-management
<a name="agentic-ai-platform-management.b5b1302b-6bd1-50b1-88ee-cf9a64dae0e0"></a>

This account is the AWS Organizations root. It contains Service Control Policies that apply to the entire platform, billing consolidation, and the Control Tower landing zone configuration.

If your organization already operates a landing zone, this account already exists. Do not create a parallel management account. Enroll all new Agentic AI platform accounts through the existing Control Tower Account Factory and place them under the Agentic and Gateway organizational units within your existing OU hierarchy.

##### agentic-ai-platform-security
<a name="agentic-ai-platform-security.4d54dbe8-fc77-55b9-b424-99bb8b23bfe1"></a>

The security account provides centralized security monitoring, compliance reporting, and audit trails for all AI platform accounts. It hosts Amazon GuardDuty as the delegated administrator for the organization, AWS Security Hub for aggregated findings, AWS Config for configuration compliance, and AWS CloudTrail for the organization-level audit trail.

If your organization already has an audit or security account through its landing zone, reuse it. Do not create a parallel security structure for the Agentic AI platform accounts.

##### agentic-ai-platform-observability
<a name="agentic-ai-platform-observability.4c69c24a-6252-5c5b-bcb8-8c608c55722f"></a>

The observability account hosts AI-specific dashboards, agent execution traces, model performance metrics, token usage analytics, and cost attribution data aggregated from all platform accounts. It is configured as the monitoring account in a CloudWatch cross-account observability setup, with each workload account acting as a source account.

This account is deliberately separate from general infrastructure logging, which continues to route to the landing zone log archive account. The distinction matters: agent telemetry has different retention requirements, different access patterns, and different consumer audiences from infrastructure logs. Mixing them adds noise and complicates cost attribution.

Key services in this account include Amazon CloudWatch cross-account observability, AWS X-Ray for distributed tracing across agent execution steps, Amazon Managed Grafana for unified dashboards, and Amazon Managed Service for Prometheus for containerized workloads.

|
|
| NoteCertain CloudWatch widget types and custom metric configurations require additional cross-account IAM configuration to render correctly across account boundaries. Validate dashboard functionality during initial deployment before rolling out to production audiences. |
| --- |

##### agentic-ai-platform-shared-tooling
<a name="agentic-ai-platform-shared-tooling.1b50ff0b-6afa-566a-a587-24daba103efb"></a>

This account hosts the CI/CD pipeline and container registry that build, test, and promote agent artifacts across all environments. Amazon ECR stores container images built once and promoted by reference, not by rebuilding, guaranteeing that the artifact deployed to production is byte-for-byte identical to the artifact validated in staging. On-demand evaluations for agent benchmarking and regression testing run as part of the pipeline before promotion decisions are made.

##### agentic-ai-platform-dev
<a name="agentic-ai-platform-dev.0230f476-bd85-58ff-b317-135f965f2abe"></a>

The development account is where agentic engineers build, iterate, and test. It hosts the agent runtime, integration tests against the dev gateway account, MCP server development, and on-demand evaluation runs triggered by the CI/CD pipeline.

Services in this account include Amazon Bedrock for model access, AWS Lambda or Amazon ECS for agent runtime execution, and Amazon DynamoDB or Amazon Aurora for agent state persistence. The account is intentionally permissive relative to staging and production to support rapid iteration, but SCPs at the Agentic OU level enforce the boundaries that matter: region restrictions, service allowlisting, and prevention of privilege escalation.

##### agentic-ai-platform-gateway-dev
<a name="agentic-ai-platform-gateway-dev.065fe8c5-1204-51d5-b869-e17f88eaa5c9"></a>

The development gateway account hosts the Generative AI Gateway and AWS Agent Registry for the development environment. The gateway provides a unified interface to model providers with rate limiting, cost tracking, and failover routing. It enforces token budgets and prevents runaway costs from autonomous agent loops at the platform level rather than leaving budget enforcement as a per-team responsibility. The Agent Registry catalogs deployed agents, their versions, capabilities, and associated MCP server configurations. Budget thresholds in this environment are intentionally higher to support experimentation, but circuit breakers still prevent unbounded spending.

##### agentic-ai-platform-staging
<a name="agentic-ai-platform-staging.e8193cc3-a7a7-5c12-a749-18c8711c3f42"></a>

The staging account mirrors the production account configuration and serves as the final validation gate before any agent change reaches production users. Integration testing, load testing, and pre-deployment behavioral validation run here. Agents are deployed to this account through the same CI/CD pipeline used for production, with a manual approval gate between staging promotion and production promotion.

Introduce this account once you have a defined promotion workflow. Running staging on the same account as development produces false confidence because environmental differences between staging and production are invisible.

##### agentic-ai-platform-gateway-staging
<a name="agentic-ai-platform-gateway-staging.e6a38104-4b1f-5972-8403-1b8cdfe32b69"></a>

The staging gateway account mirrors the production Generative AI Gateway and AWS Agent Registry configuration. Routing rules, rate limits, tool access policies, and Agent Registry entries are identical to production. Integration testing validates that agents in the staging runtime account can discover and invoke tools through the gateway without configuration drift from production.

##### agentic-ai-platform-prod
<a name="agentic-ai-platform-prod.ec0596bf-f5fd-5bed-bc27-4e00104004f9"></a>

The production account hosts agents serving live users or business processes. It replicates the workload account pattern from the development and staging accounts but with production-grade configurations: multi-AZ deployments, auto-scaling policies, enhanced monitoring thresholds, and the most restrictive IAM policies of any account in the platform.

All production deployments must originate from the CI/CD pipeline. Manual console changes to this account should be prevented by SCP or IAM policy. AgentCore Evaluations Online runs continuously in this account to detect behavioral drift between releases.

##### agentic-ai-platform-gateway-prod
<a name="agentic-ai-platform-gateway-prod.d6e49ee9-7d31-57e0-97c2-01dbc9ba660c"></a>

The production gateway account hosts the Generative AI Gateway and Agent Registry serving live agent traffic. It enforces the most restrictive rate limits, tool access policies, and token budgets of any gateway environment. The Agent Registry in this account is the authoritative source of truth for what agents exist in production, their versions, and their MCP server configurations. All production gateway changes must originate from the CI/CD pipeline.

##### agentic-ai-platform-data-lake
<a name="agentic-ai-platform-data-lake.2cbbce6d-8db7-5b3a-a9b2-e3f1effcbaee"></a>

The data lake account centralizes AI-specific data storage and analytics. It hosts RAG knowledge bases for Retrieval Augmented Generation workloads, agent interaction logs for behavioral analysis and fine-tuning dataset construction, and reporting pipelines.

Key services include Amazon S3 as the primary storage layer, AWS Glue for data pipeline orchestration between raw and processed data zones, Amazon Athena for ad-hoc query access, and Amazon Bedrock Knowledge Bases for RAG integrations. AWS Lake Formation governs access to datasets, ensuring that only authorized accounts and IAM roles can query sensitive interaction data.

Introduce this account when AI-specific data storage and analytics requirements outgrow what workload accounts can manage inline. For early-stage deployments, interaction logs can live within workload accounts and be migrated to the data lake account later.

### Organizational unit structure
<a name="organizational-unit-structure"></a>

The architecture uses two organizational units within AWS Organizations to group AI agent platform accounts:
+ **Agentic OU. **Contains the development, staging, and production workload accounts. SCPs applied at this OU level enforce region restrictions, service allowlisting, and governance controls that apply uniformly across all agent runtime environments.
+ **Gateway OU. **Contains one gateway account per environment (development, staging, production). The gateway account hosts the Generative AI Gateway, which provides a managed, auditable entry point for agent interactions with external systems. Separating the gateway into its own OU enables targeted SCP application for outbound connectivity controls without affecting the agent runtime accounts.

The observability account, shared tooling account, and data lake account sit outside these two OUs. They are shared services accounts that do not belong to a single environment tier.

### Integrating with an existing landing zone
<a name="integrating-with-an-existing-landing-zone"></a>

When your organization already operates a landing zone through the Landing Zone Accelerator or a ProServe-deployed topology, you deploy only the net-new accounts the Agentic AI platform requires. Map existing accounts to AI platform functions as follows:

|
|
| AI platform capability | Maps to existing landing zone account |
| --- |--- |
| Security monitoring and compliance | Existing audit or security account |
| Centralized log aggregation | Existing log archive account |
| VPC connectivity and network routing | Existing networking account, via Transit Gateway or AWS RAM |
| Identity and access management | Existing shared services account, where applicable |

Create the Agentic and Gateway organizational units under your existing OU hierarchy. Enroll workload accounts (dev, staging, prod) in the Agentic OU and generative AI gateway accounts in the Gateway OU. This enables targeted SCP application and cost allocation tagging without affecting existing workload accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
