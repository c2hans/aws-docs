---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-3-amazon-ecs-containerized.html
---

# Deployment Pattern 3 - Amazon ECS (Containerized)
<a name="deployment-pattern-3-amazon-ecs-containerized"></a>

Amazon ECS with API Gateway orchestrates Docker containers that run MCP server applications. Amazon ECS supports both AWS Fargate for serverless container execution and Amazon EC2 launch types for more control. The architecture diagram illustrates the "Public front door \+ private MCP runtime" pattern, where API Gateway is the only internet-facing endpoint and enforces OAuth authorization. API Gateway then reaches into the VPC by using VPC link v2 to call an internal Application Load Balancer. The private ALB forwards requests to an Amazon ECS service that runs the remote MCP server. This implementation uses OAuth authentication. OAuth provides broad MCP-client compatibility but isn't an Amazon ECS requirement. When the clients are AWS workloads, you can use IAM with SigV4.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-ecs](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-ecs)

![Deployment Pattern of Amazon ECS (Containerized)](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/3e9f7765-04d2-4329-8586-eca256dcad75.png)

**Architecture Characteristics**
+ Pros: The backend stays private. The ALB and Amazon ECS aren't exposed to the internet; only API Gateway is public. API Gateway provides centralized security controls, throttling, quotas, and logging management. API Gateway handles primary authentication through API keys, Amazon Cognito, or Lambda authorizers, while the ALB adds a second authentication layer through its native support for JWT/OIDC token validation.
+ Limitations: API Gateway has default timeout and payload limits. If any MCP tools take longer to run, make the MCP tool asynchronous, or use a REST API and raise timeouts beyond 29 seconds. If tools are designed to run for a long time, remove API Gateway and use a public Application Load Balancer instead.
