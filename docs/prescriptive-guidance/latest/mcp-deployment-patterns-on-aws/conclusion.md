---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/conclusion.html
---

# Next steps
<a name="conclusion"></a>

Deploying MCP servers on AWS provides organizations with flexible, scalable, and secure infrastructure for AI-powered applications. This prescriptive guidance presents several deployment patterns, each designed for specific operational requirements, cost constraints, and scaling needs.

**Next Steps**

Organizations beginning MCP deployment on AWS should first determine whether they can expose the required business capability through Amazon Bedrock AgentCore Gateway as a Lambda function, OpenAPI, or Smithy target. This is the preferred starting point because it avoids operating a standalone MCP server while centralizing authentication, authorization, credential management, and observability. Consider AWS Lambda, Amazon ECS, Amazon EKS, or Amazon EC2 when their execution model, networking options, container orchestration, portability, hardware support, or operating-system control fit the workload better. These patterns provide implementation flexibility but, depending on the selected service, might require you to take on more responsibility for deployment, scaling, resilience, security configuration, observability, and infrastructure maintenance compared with managed AgentCore services.

Implement monitoring from the start by setting up CloudWatch dashboards, alarms, and log aggregation before production traffic begins. Follow AWS Well-Architected Framework security best practices, including least-privilege IAM policies, VPC isolation, encryption at rest and in transit, and audit logging. Gather metrics during initial operations and optimize based on actual usage patterns rather than assumptions. Consider hybrid approaches that use multiple patterns for different MCP server types based on specific requirements, such as Lambda for simple read-only servers and Amazon EKS for complex stateful servers.

**Reference Implementation**

The complete reference implementation with working code examples, deployment scripts, and detailed instructions for all four deployment patterns is available at: [https://github.com/aws-samples/sample-mcp-deployment-patterns/](https://github.com/aws-samples/sample-mcp-deployment-patterns/)
