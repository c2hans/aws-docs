---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/introduction.html
---

# Model Context Protocol (MCP) Deployment Patterns on AWS
<a name="introduction"></a>

*Deepika Kumar and Lingling Cui, Amazon Web Services*

## Executive Summary
<a name="executive-summary.d3fd4ff6-dff9-5005-95da-da1037e4e556"></a>

The Model Context Protocol (MCP) is an open protocol that enables integration between AI applications and external data sources and tools. As organizations increasingly adopt AI-powered development tools like Kiro, Amazon Q Developer, Claude Code, and custom AI assistants, deploying MCP servers on AWS provides scalable infrastructure designed to help you build secure and cost-effective contextual AI interactions.

This prescriptive guidance provides architecture patterns and implementation approaches for deploying MCP servers on AWS using [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) with [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) (Amazon ECS), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) (Amazon EKS), and Amazon Elastic Compute Cloud (Amazon EC2). Each pattern addresses different operational requirements, scaling needs, and management preferences.

The implementation examples and deployment scripts referenced in this guidance are available in the open-source repository at: [https://github.com/aws-samples/sample-mcp-deployment-patterns](https://github.com/aws-samples/sample-mcp-deployment-patterns)

### Intended audience
<a name="intended-audience.3525b8b3-879b-52c5-8fb0-1c8f74f8b39f"></a>

This guide is intended for cloud architects, DevOps engineers, platform engineers, and developers who want to deploy MCP servers on AWS infrastructure. It assumes intermediate familiarity with core AWS services, networking concepts ([Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/), subnets, security groups), and container fundamentals.

### Objectives
<a name="objectives.f450f0cb-c470-5748-ac63-c215279dfab8"></a>

After reading this guide, you will be able to:
+ Understand the differences between local and remote MCP server deployment models
+ Evaluate five AWS deployment patterns (Amazon Bedrock AgentCore, AWS Lambda with Amazon API Gateway, [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/), [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)) for hosting remote MCP servers
+ Select the appropriate deployment pattern based on your scaling, security, cost, and operational requirements
+ Apply best practices for production MCP deployments aligned with the AWS Well-Architected Framework

#### Attachments
<a name="attachments-596b5834-b415-44f3-9601-59b1ced57c6b"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
