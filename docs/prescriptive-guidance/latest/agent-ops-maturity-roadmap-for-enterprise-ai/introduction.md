---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/introduction.html
---

# Enterprise multi-account architecture for running agentic AI in production on AWS
<a name="introduction"></a>

*Vineet Singh, Cristian Balint, Natalia Cummings, Florian Gauter, and Mehdi Nemlaghi, Amazon Web Services*

Deploying AI agents into production introduces a class of infrastructure requirements that conventional workload patterns do not have. Agents require shared model gateways isolated from individual workloads, unified observability across agent reasoning and tool invocations, and platform-enforced cost controls for agentic AI consumption.

This guide provides an enterprise multi-account architecture for running agentic AI workloads in production on AWS. It defines the full account topology, from management root through security, observability, shared tooling, and per-environment workload and gateway accounts, with the governance, cost controls, and CI/CD automation that production deployments require. Use this guide to establish the account boundaries, governance controls, and operational foundations your organization needs to run agents in production at scale. A companion infrastructure-as-code repository accompanies this guide to accelerate deployment.

## Intended audience
<a name="intended-audience"></a>

This guide is written for the following roles:
+ **Cloud architects **designing multi-account strategies for AI and machine learning workloads.
+ **Platform engineers **building internal AI agent platforms for their organizations.
+ **Security and compliance teams **establishing governance frameworks for systems that include autonomous AI components.
+ **DevOps and MLOps engineers **implementing CI/CD pipelines for agent promotion across environments.

Readers should be familiar with AWS Organizations and AWS Control Tower, and with foundational landing zone concepts. Familiarity with AI or machine learning workloads is helpful but not required.

## Objectives
<a name="objectives"></a>

After reading this guide, you will be able to:
+ Select the appropriate account topology based on your organizational maturity and governance requirements.
+ Deploy a multi-account structure that provides workload isolation, centralized observability, and shared AI tooling while maintaining security boundaries between environments.
+ Integrate AI agent platform accounts into an existing AWS landing zone without duplicating management, security, or networking infrastructure.
+ Implement security controls and agent-specific governance appropriate for autonomous AI workloads.
+ Establish a CI/CD pipeline that enforces automated evaluation and manual approval gates before production promotion.
+ Establish platform-level cost controls that prevent token budget overruns from autonomous agent behavior.

## Business outcomes
<a name="business-outcomes"></a>

This architecture supports the following business outcomes:
+ Faster time-to-production for AI agent workloads through standardized account provisioning and CI/CD automation.
+ Cost predictability through platform-level token budget enforcement, preventing unexpected spend from autonomous agent behavior.
+ Regulatory confidence through environment isolation, audit trails, and data classification controls.
+ Reduced operational overhead by reusing existing landing zone infrastructure rather than building parallel governance.

## Prerequisites
<a name="prerequisites"></a>

Before implementing this architecture, ensure the following are in place:
+ An AWS account with permissions to create an AWS Organization, or an existing organization you can extend.
+ Familiarity with AWS Control Tower concepts, including organizational units, guardrails, and the Account Factory.
+ An understanding of your organization's existing landing zone topology, if one is in operation.
+ Defined requirements for your agentic AI workloads, including model providers, tooling integrations, data residency obligations, and compliance scope.

## Attachments
<a name="attachments-3ca5933d-b9b7-4be8-b507-ab406fad49ca"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
