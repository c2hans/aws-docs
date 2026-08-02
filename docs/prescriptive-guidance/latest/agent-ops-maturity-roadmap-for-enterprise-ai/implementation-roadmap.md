---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/implementation-roadmap.html
---

# Implementation roadmap
<a name="implementation-roadmap"></a>

The following phased roadmap reflects realistic timelines for a greenfield deployment. Organizations integrating with an existing landing zone should reduce Phase 1 to days, not weeks, because the management and security account infrastructure already exists.

## Phase 1: Foundation (Weeks 1 to 2)
<a name="phase-1--foundation--weeks-1-to-2-.c01ff3c0-8521-5a0f-92d6-b7c6b4acd3af"></a>

1. Deploy the management account or identify the existing one in a landing zone environment.

1. Create the Agentic and Gateway organizational units under the existing OU hierarchy.

1. Define and apply SCPs: region restrictions, service allowlisting, and privilege escalation prevention.

1. Deploy or map the security account and confirm organization-level CloudTrail is active.

## Phase 2: Shared Infrastructure (Weeks 2 to 4)
<a name="phase-2--shared-infrastructure--weeks-2-to-4-.c2533f18-a1fb-5f25-8c13-101065179d82"></a>

1. Deploy the shared tooling account.

1. Deploy the Amazon ECR shared registry and configure cross-account image pull permissions.

1. Establish cross-account IAM roles and AWS PrivateLink endpoints for workload account access.

1. Deploy the observability account and configure CloudWatch cross-account observability.

1. Deploy the development gateway account in the Gateway OU and configure the Generative AI Gateway with initial LLM provider integrations and token budget controls.

## Phase 3: Workload Environments (Weeks 4 to 6)
<a name="phase-3--workload-environments--weeks-4-to-6-.8bf62222-a9a0-5d84-a8f5-eaecc2097295"></a>

1. Deploy the development account with agent runtime infrastructure and MCP server integrations.

1. Establish the CI/CD pipeline in the shared tooling account with the build and dev evaluation stages.

1. Validate end-to-end agent execution with observability telemetry flowing to the observability account.

1. Deploy the staging gateway account in the Gateway OU.

## Phase 4: Production Readiness (Weeks 6 to 8)
<a name="phase-4--production-readiness--weeks-6-to-8-.7c05a995-2db8-565f-9d0e-3e0cbe162cb2"></a>

1. Deploy the staging and production accounts.

1. Extend the CI/CD pipeline with manual approval gates and the full promotion sequence.

1. Configure production-grade security controls, monitoring thresholds, and alerting runbooks.

1. Deploy the production gateway account.

1. Deploy the data lake account if RAG or analytics requirements warrant it. This account can be deferred until workload data volumes justify the operational overhead.

The infrastructure-as-code implementation for this architecture is available in the [companion GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-enterprise-agentic-ai-platform-on-aws). The repository demonstrates the multi-account structure, service placement across accounts, and the CI/CD pipeline for agent promotion between environments. It serves as the implementation companion for this guide.
