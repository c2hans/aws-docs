---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/resources.html
---

# Why deploy MCP servers on AWS
<a name="resources"></a>

Organizations choose AWS for remote MCP server deployments due to its comprehensive range of services, proven scalability, and deep integration capabilities.
+ Flexible compute options: AWS provides multiple compute options, from serverless AWS Lambda functions to managed Kubernetes clusters on Amazon EKS. You can select deployment patterns that match your operational maturity and scaling requirements. Pay-per-use pricing aligns costs with actual usage.
+ Native service integration: AWS SDKs provide access to Amazon S3, Amazon DynamoDB, [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), Amazon Bedrock, and other AWS services. Managed services reduce infrastructure management, so your teams can focus on business logic.
+ Security and compliance: Use your existing AWS accounts, IAM roles, and security policies for consistent governance. Many AWS services are in scope for assurance programs such as SOC, ISO 27001, and PCI DSS, and many are HIPAA Eligible Services, which can help you support regulated workloads.
+ Global infrastructure: You can deploy MCP servers close to users worldwide to reduce latency and improve user experience. AWS Regions also help you address data residency requirements and build geographic redundancy.
+ Operational reliability: Managed services such as Application Load Balancer and Amazon ECS handle health checks, traffic routing, and rolling deployments. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) monitoring and alarms provide operational visibility and can initiate automated incident response.

## Prerequisites
<a name="prerequisites"></a>

This guidance assumes intermediate to advanced (level 200–300) AWS experience with familiarity across core AWS services. You should understand networking concepts including Amazon VPC, subnets, security groups, and network ACLs. Container fundamentals and Docker basics are required for Amazon ECS and Amazon EKS patterns. Before you implement any MCP deployment pattern, make sure that you have the required AWS account permissions and tools, and that you have configured your MCP client.

Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.
+ AWS Account and Permissions: You need an active AWS account with AWS Identity and Access Management (IAM) permissions to create AWS Lambda functions and execution roles for serverless deployments, Amazon EC2 instances and security groups for EC2 patterns, Amazon ECS clusters, task definitions, and services for containerized deployments, Amazon EKS clusters and node groups for Kubernetes patterns, Amazon API Gateway REST or HTTP APIs, Amazon CloudWatch Logs groups, and [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) secrets for API key storage.
+ Tools and Software: Install and configure AWS CLI version 2 or later. For infrastructure as code (IaC), use the tool required by the selected deployment pattern, such as Terraform, AWS CloudFormation, AWS CDK, or AWS SAM. Install Docker for Amazon ECS and Amazon EKS patterns, kubectl for Amazon EKS patterns, and Git for version control.

  If you plan to develop or test the MCP server locally before you deploy it to AWS, install the official [MCP SDK](https://github.com/modelcontextprotocol) for your programming language, such as the Python SDK or TypeScript SDK.
+ MCP Client Application: You need an AI application that supports MCP, such as Kiro, Quick, Claude Desktop, or a custom client. Familiarity with MCP client configuration helps you connect to your deployed servers.

## Authentication options for remote MCP servers
<a name="authentication-options-for-remote-mcp-servers"></a>

The compute service and client authentication method are separate architectural decisions. A Model Context Protocol (MCP) server running on Lambda, ECS, EKS, or EC2 can use different authentication methods depending on its clients and security requirements.

This guidance focuses on two authentication options:
+ OAuth: Suitable for human users, web applications, third-party integrations, and general-purpose MCP clients that use bearer tokens.
+ IAM with Signature Version 4 (SigV4): Suitable when an MCP client running on AWS uses an IAM role and temporary credentials to authenticate requests to an MCP server hosted on AWS. MCP clients without native SigV4 support require a signing proxy or adapter.

The deployment patterns illustrate selected combinations rather than compute service requirements. Pattern 3 uses Amazon ECS with OAuth to demonstrate broad client compatibility. Pattern 4 uses Amazon EKS with IAM and SigV4 to demonstrate AWS-native service-to-service authentication. ECS can also use SigV4, and EKS can also use OAuth.

Choose the authentication option based on the client identity, credential model, identity-provider integration, and interoperability requirements.
