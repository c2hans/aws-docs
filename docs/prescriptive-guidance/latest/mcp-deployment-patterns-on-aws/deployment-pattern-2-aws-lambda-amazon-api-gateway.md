---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-2-aws-lambda-amazon-api-gateway.html
---

# Deployment Pattern 2 - AWS Lambda \+ Amazon API Gateway
<a name="deployment-pattern-2-aws-lambda-amazon-api-gateway"></a>

AWS Lambda with Amazon API Gateway represents the serverless approach where MCP server logic runs in ephemeral functions triggered by API requests. Lambda automatically manages the underlying compute resources, scaling from zero to thousands of concurrent executions without manual intervention. This pattern significantly reduces infrastructure management overhead, making it ideal for variable workloads and teams prioritizing rapid development over operational control.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-serverless](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-serverless)

The following diagram shows the baseline request and authentication flow for an MCP server deployed on AWS Lambda. Production implementations may also require durable application state, private VPC resource access, and managed credential retrieval, as shown in the expanded architecture that follows.

![Deployment Pattern of AWS Lambda + Amazon API Gateway](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/03fc7c1d-f5bd-4c0c-a202-1a2f85507458.png)

When the MCP server requires durable application state, store it outside the Lambda execution environment in Amazon DynamoDB or Amazon Aurora PostgreSQL. Configure the Lambda function for VPC access when it must connect to private resources, and use Amazon RDS Proxy for relational database connections. Retrieve database, internal-service, and API credentials from AWS Secrets Manager at runtime.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/be3c60b1-e957-442d-8db4-784fdebeab89.png)

**Architecture Characteristics**
+ Pros: Zero server management with automatic infrastructure scaling; pay-per-request pricing aligns costs with actual usage; and automatic scaling supports thousands of concurrent executions. Each Lambda execution environment processes one invocation at a time, providing concurrency isolation between simultaneous requests. Lambda also provides built-in multi-AZ availability, native integration with AWS services through IAM roles, fast deployment cycles, and no idle compute cost when using on-demand concurrency.
+ Limitations: Limitations include a 15-minute maximum execution time for synchronous invocations, cold-start latency for new execution environments, a 10 GB memory limit per function, the need to store durable application state externally, and limited runtime customization than container- or VM-based approaches. Each Lambda invocation processes one request, so these compute limits apply to that individual request. For GPU-backed processing or servers that share compute resources across concurrent requests, use Amazon ECS or Amazon EKS running on GPU-enabled EC2 instances.
