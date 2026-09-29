---
source_url: https://docs.aws.amazon.com/solutions/agentic-network-firewall-automation-on-aws/index.html
---

---
title: 'Guidance for Agentic Network Firewall Automation on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-network-firewall-automation-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Agentic Network Firewall Automation on AWS

## Overview

This Guidance demonstrates how to automate the complete Network Firewall change lifecycle using Amazon Bedrock AgentCore as an orchestration layer, integrating ServiceNow, OpenSearch, DynamoDB, and Azure DevOps into a unified CI/CD pipeline. By reducing manual intervention to a single approval step, organizations achieve faster deployment cycles, eliminate configuration errors caused by manual rule creation, and ensure full auditability across all firewall changes. The solution frees network and security engineers from repetitive, error-prone tasks, allowing them to focus on strategic security initiatives while maintaining consistent, reliable firewall management at scale with significantly reduced operational overhead.

## Benefits

### Accelerate firewall rule deployment

Reduce the time needed to create, validate, and deploy AWS Network Firewall rules by submitting requests in plain language instead of writing complex Suricata syntax manually. A multi-agent system handles IP validation, change management, and Git-based approval workflows automatically, so your security team can respond to threats faster.

### Strengthen security governance at scale

Help verify that every firewall rule change passes IPAM validation, receives a ServiceNow change request, and goes through a GitSecOps pull request review before reaching production. This automated audit trail, supported by Amazon CloudWatch and AWS Identity and Access Management, helps your organization meet internal compliance requirements without slowing down operations.

### Reduce operational burden on security teams

Empower network and security engineers to manage firewall policies without deep expertise in rule syntax or manual coordination across multiple tools. By connecting your existing ServiceNow, Azure DevOps, and identity workflows through a single conversational interface, your teams can focus on higher-value security priorities.

## How it works

This architecture diagram illustrates how a multi-agent system automates AWS Network Firewall rule management through natural language commands, integrating IPAM validation, GitSecOps workflows, and change management to streamline security operations. [Download the architecture diagram](downloads/agentic-network-firewall-automation-on-aws.pdf)

![Architecture diagram for Agentic Network Firewall Automation on AWS](/images/solutions/agentic-network-firewall-automation-on-aws/images/agentic-network-firewall-automation-on-aws-1.png)

1. **Step 1**: A user submits a natural-language request to the web application, served by Amazon Elastic Container Service on AWS Fargate behind an Elastic Load Balancing (ALB).
1. **Step 2**: Amazon Cognito authenticates the user, federated with Azure Active Directory (Azure AD) for enterprise single sign-on.
1. **Step 3**: The web app streams chat with Amazon Bedrock AgentCore via the InvokeAgentRuntime API; the supervisor agent runs on the Strands Agents SDK with Amazon Bedrock (Claude Sonnet 4) and AgentCore Memory.
1. **Step 4**: The supervisor delegates to five specialist agents (Account Details, Firewall Logs, GitSecOps, IPAM, and ServiceNow).
1. **Step 5**: Agents query Amazon DynamoDB for account metadata and Amazon OpenSearch Service for firewall alert, flow, and TLS logs.
1. **Step 6**: Agents integrate with third-party systems: ServiceNow (change requests), Azure DevOps (Git commit and pull request), and EfficientIP IPAM (IP/CIDR validation).
1. **Step 7**: Amazon Elastic Container Registry stores the agent and web-app container images; AWS Secrets Manager holds the integration credentials read by AgentCore.
1. **Step 8**: Validated Suricata rules are staged via Git pull request and change request and, after approval, applied to AWS Network Firewall; responses stream to the user over Server-Sent Events (SSE).
[Read usage guidelines](/solutions/guidance-disclaimers/)
