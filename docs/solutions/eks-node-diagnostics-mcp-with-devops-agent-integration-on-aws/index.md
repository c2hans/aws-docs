---
source_url: https://docs.aws.amazon.com/solutions/eks-node-diagnostics-mcp-with-devops-agent-integration-on-aws/index.html
---

---
title: 'Guidance for EKS Node Diagnostics MCP with DevOps Agent Integration on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/eks-node-diagnostics-mcp-with-devops-agent-integration-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for EKS Node Diagnostics MCP with DevOps Agent Integration on AWS

## Overview

This Guidance helps customers diagnose EKS worker node issues—such as NotReady states, pod failures, and networking problems—by automating the collection and analysis of OS-level logs that are not accessible through standard Kubernetes APIs. When an EKS node experiences problems, AI agents use SSM Automation to gather diagnostic bundles from over 20 log sources including kubelet, containerd, CNI configuration, and system logs. The system pre-indexes errors with severity classification, correlates events across multiple sources, and follows structured runbooks to guide remediation—all through a conversational workflow that eliminates manual SSH access and multi-step troubleshooting. You can resolve node-level issues faster without needing to manually SSH into nodes or piece together logs from multiple locations.

## Benefits

### Automate EKS node troubleshooting

Eliminate manual log collection and analysis across 20+ sources by enabling an AI-powered DevOps agent to autonomously investigate and identify root causes on your EKS worker nodes.

### Accelerate incident resolution with tool chaining

Reduce mean time to resolution by letting the agent sequentially collect, correlate, and summarize diagnostic findings without human intervention, turning hours of investigation into minutes.

### Secure diagnostics with serverless architecture

Run comprehensive node diagnostics through a fully serverless pipeline secured by OAuth 2.0 authentication and AWS KMS encryption, requiring no persistent infrastructure to manage.

## How it works

This architecture diagram illustrates how to effectively support EKS Node Diagnostics MCP with DevOps Integration on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram](downloads/eks-node-diagnostics-mcp-with-devops-integration-on-aws.pdf)

![Architecture diagram for EKS Node Diagnostics MCP with DevOps Integration on AWS](/images/solutions/eks-node-diagnostics-mcp-with-devops-agent-integration-on-aws/images/eks-node-diagnostics-mcp-with-devops-integration-on-aws.png)

1. **Step 1**: AWS DevOps Agent calls a collect tool with an instance ID. The agent connects to the MCP server through Amazon Bedrock AgentCore Gateway over MCP/HTTPS.
1. **Step 2**: AgentCore Gateway authenticates the request using an OAuth 2.0 token from Amazon Cognito (client credentials flow) and routes the tool invocation to the registered AWS Lambda function.
1. **Step 3**: The Lambda function (MCP Handler) dispatches an AWS Systems Manager Automation execution to the target node, running the AWSSupport-CollectEKSInstanceLogs runbook.
1. **Step 4**: The SSM Automation runbook collects 20+ log sources on the EKS worker node — kubelet, containerd, iptables, CNI config, route tables, dmesg, sysctl, ENI metadata, IPAMD logs, and more — packages them into an archive and uploads it to Amazon S3 with AWS KMS encryption.
1. **Step 5**: A processing pipeline extracts the archive, pre-indexes errors with severity classification and stable finding IDs, and provides the structured results back through additional MCP tools.
1. **Step 6**: AWS DevOps Agent chains tools together (collect → status → errors → search → correlate → summarize) to autonomously investigate and identify root causes without human intervention.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-eks-node-diagnostics-mcp)

[Read usage guidelines](/solutions/guidance-disclaimers/)
