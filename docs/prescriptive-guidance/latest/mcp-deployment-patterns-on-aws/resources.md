---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/resources.html
---

# Why deploy MCP servers on AWS
<a name="resources"></a>

Organizations choose AWS for remote MCP server deployments due to its comprehensive range of services, proven scalability, and deep integration capabilities.
+ Flexible compute options: AWS provides multiple compute options ranging from serverless AWS Lambda functions to managed Kubernetes clusters on Amazon EKS, enabling organizations to select deployment patterns that match their operational maturity and scaling requirements with pay-per-use pricing that aligns costs with actual usage.
+ Native service integration: AWS SDK enables seamless access to S3, DynamoDB, RDS, Bedrock, and other AWS services. Managed services eliminate infrastructure management, allowing teams to focus on business logic.
+ Security and Compliance: Leverage existing AWS accounts, IAM roles, and security policies for consistent governance. Compliance certifications (SOC 2, ISO 27001, HIPAA, PCI DSS) support regulated industries.
+ Global Infrastructure: This supports deploying MCP servers close to users worldwide, reducing latency and improving user experience, enabling data residency compliance and geographic redundancy.
+ Operational Reliability: Operational maturity of AWS services provides production-grade reliability. Managed services like Application Load Balancer and ECS handle health checks, traffic routing, and rolling deployments. CloudWatch monitoring and alarms provide operational visibility and automated incident response.

## Prerequisites
<a name="prerequisites"></a>

This guidance assumes L200-300 AWS experience with familiarity across core AWS services. You should understand networking concepts including Amazon VPC, subnets, security groups, and network ACLs. container fundamentals and Docker basics are necessary for ECS and EKS patterns. Before implementing any MCP deployment pattern, ensure you have the necessary AWS account permissions, tools, and MCP client configured.

Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.
+ AWS Account and Permissions: You need an active AWS account with appropriate permissions to create AWS Lambda functions and execution roles for serverless deployments, Amazon EC2 instances and security groups for EC2 patterns, Amazon ECS clusters, task definitions, and services for containerized deployments, Amazon EKS clusters and node groups for Kubernetes patterns, Amazon API Gateway REST or HTTP APIs, Amazon CloudWatch Logs groups, and AWS Secrets Manager secrets for secure API key storage.
+ Tools and Software: Install and configure AWS CLI version 2 or later. For infrastructure as code (IaC), use the tool required by the selected deployment pattern, such as Terraform, AWS CloudFormation, AWS CDK, or AWS SAM. Install Docker for Amazon ECS and Amazon EKS patterns, kubectl for Amazon EKS patterns, and Git for version control.

  If you plan to develop or test the MCP server locally before deploying it to AWS install the official MCP SDK ([https://github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)) for your programming language, such as Python or Typescript SDK.
+ MCP Client Application: You need an AI application that supports MCP, such as Kiro, Quick, Claude Desktop, or a custom client. Understanding of MCP client configuration enables successful integration with deployed servers.

## Authentication options for remote MCP servers
<a name="authentication-options-for-remote-mcp-servers"></a>

The deployment platform and client authentication method are separate architectural decisions. An MCP server running on Lambda, ECS, EKS, or EC2 can use different authentication methods depending on its clients and security requirements.

This guidance focuses on two authentication options:
+ OAuth: Suitable for human users, web applications, third-party integrations, and general-purpose MCP clients that use bearer tokens.
+ IAM with SigV4: Suitable when an MCP client running on AWS uses an IAM role and temporary credentials to authenticate requests to an MCP server hosted on AWS. MCP clients without native SigV4 support require a signing proxy or adapter.

The deployment patterns illustrate selected combinations rather than platform requirements. Pattern 3 uses Amazon ECS with OAuth to demonstrate broad client compatibility. Pattern 4 uses Amazon EKS with IAM and SigV4 to demonstrate AWS-native service-to-service authentication. ECS can also use SigV4, and EKS can also use OAuth.

Choose the authentication option based on the client identity, credential model, identity-provider integration, and interoperability requirements.
