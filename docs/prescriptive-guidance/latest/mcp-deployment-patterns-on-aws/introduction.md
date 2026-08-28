---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/introduction.html
---

# Model Context Protocol (MCP) Deployment Patterns on AWS
<a name="introduction"></a>

*Deepika Kumar and Lingling Cui, Amazon Web Services*

## Executive Summary
<a name="executive-summary.86f3998e-641b-51f8-8f6d-173632a5f6f4"></a>

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between AI applications and external data sources and tools. As organizations increasingly adopt AI-powered development tools like Kiro, Amazon Q Developer, Claude Code, and custom AI assistants, deploying MCP servers on AWS provides scalable, secure, and cost-effective infrastructure for contextual AI interactions.

This prescriptive guidance provides architecture patterns and implementation approaches for deploying MCP servers on AWS using AWS Lambda with Amazon API Gateway, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS) and others. Each pattern addresses different operational requirements, scaling needs, and management preferences.

The implementation examples and deployment scripts referenced in this guidance are available in the open-source repository at: [https://github.com/aws-samples/sample-mcp-deployment-patterns](https://github.com/aws-samples/sample-mcp-deployment-patterns)

### Intended audience
<a name="intended-audience.1a9f5601-3197-554f-86aa-842a9a3c4239"></a>

This guide is intended for cloud architects, DevOps engineers, platform engineers, and developers who want to deploy MCP servers on AWS infrastructure. It assumes L200-300 familiarity with core AWS services, networking concepts (Amazon VPC, subnets, security groups), and container fundamentals.

### Objectives
<a name="objectives.898ab2f8-88da-59c8-9008-e0553bc992ff"></a>

After reading this guide, you will be able to:
+ Understand the differences between local and remote MCP server deployment models
+ Evaluate five AWS deployment patterns (Amazon Bedrock AgentCore, Lambda \+ API Gateway, Amazon ECS, Amazon EKS, Amazon EC2) for hosting remote MCP servers
+ Select the appropriate deployment pattern based on your scaling, security, cost, and operational requirements
+ Apply best practices for production MCP deployments aligned with the AWS Well-Architected Framework

#### Attachments
<a name="attachments-596b5834-b415-44f3-9601-59b1ced57c6b"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
