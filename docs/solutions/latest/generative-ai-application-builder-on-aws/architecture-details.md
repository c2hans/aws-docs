---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  **Core**. This service provides the REST APIs for the Deployment dashboard and the WebSocket API for the use case. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core**. This solution is distributed as a CloudFormation template, and CloudFormation deploys the AWS resources for the solution. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core**. CloudFront serves the web content hosted in Amazon S3. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core**. This service handles user management and authentication for the API. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core**. DynamoDB stores deployment information and configuration details for the Deployment dashboard. It stores chat history and conversation IDs in the Text use case to enable conversation history and query disambiguation. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core**. The solution uses Lambda functions to:<br />\* Back the REST and WebSocket API endpoints \* Handle the core logic of each use case orchestrator \* Implement custom resources during CloudFormation deployment |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core**. Amazon S3 hosts the static web content. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting**. This solution publishes logs from solution resources to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), and publishes metrics to [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html). The solution also creates a [CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) to view this data. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting**. Systems Manager provides application-level resource monitoring and visualization of resource operations and cost data. Also used to store configuration data in Parameter Store. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Supporting.** AWS WAF is deployed in front of the API Gateway deployment to protect it. |
|  [Amazon Bedrock](https://aws.amazon.com/bedrock/)  |  **Optional**. The solution leverages Amazon Bedrock to access foundation or customized models, Amazon Bedrock Agents, Amazon Bedrock Knowledge Bases. Amazon Bedrock is the recommended integration to keep your data from leaving the AWS network. |
|  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)  |  **Optional** The solution leveraages Amazon Bedrock AgentCore to run and support MCP Server connections as well as Agent Builder and Workflow Use Cases. |
|  [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/)  |  **Optional**. For Agent Builder deployments, ECR stores and distributes agent container images. The solution uses ECR Pull-Through Cache to automatically retrieve pre-built agent images from the GAAB team’s public ECR repository. |
|  [AWS Distro for OpenTelemetry (ADOT)](https://aws.amazon.com/otel/)  |  **Optional**. For Agent Builder deployments, ADOT provides automatic instrumentation for agent observability, enabling distributed tracing and structured logging for agent operations. |
|  [Amazon Kendra](https://aws.amazon.com/kendra/)  |  **Optional**. In the Text use case, admin users can optionally decide to connect an Amazon Kendra index to use as a knowledge base for the conversation with the LLM. This can be used to inject new information into the LLM giving it the ability to use that information in its responses. |
|  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)  |  **Optional**. The solution can integrate with an Amazon SageMaker AI inference endpoint to access FMs that are hosted within your AWS account and Region and is a preferred integration to keep your data from leaving the AWS network. You must deploy the solution in the same Region where the inference endpoint is available.  |
|  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)  |  **Optional**. The solution provides the option to deploy components with a VPC-enabled configuration. While deploying the solution with a VPC-enabled configuration, you have the option to let the solution create a VPC for you, or use an existing VPC that exists in the same account and Region where the solution will be deployed (Bring Your Own VPC). If the solution creates the VPC, it creates the necessary network components that includes, subnets, security groups and its rules, route tables, network ACLs, NAT Gateways, Internet Gateways, VPC endpoints, and its policies. |
