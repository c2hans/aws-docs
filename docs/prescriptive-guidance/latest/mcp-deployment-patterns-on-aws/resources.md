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
+ Tools and Software: Install and configure AWS CLI version 2 or later, AWS CDK, CloudFormation or AWS SAM for optional IaaC, Docker for ECS and EKS patterns, kubectl for EKS pattern implementation, and Git for version control. Install the official [MCP SDK](https://github.com/modelcontextprotocol) for your programming language, such as @modelcontextprotocol/sdk for Node.js or other.
+ MCP Client Application: You need an AI application that supports MCP, such as Amazon Q Developer, Claude Desktop, or a custom client. Understanding of MCP client configuration enables successful integration with deployed servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
