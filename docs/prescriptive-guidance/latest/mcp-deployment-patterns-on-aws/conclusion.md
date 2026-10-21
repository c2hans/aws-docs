---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/conclusion.html
---

# Next steps
<a name="conclusion"></a>

Deploying MCP servers on AWS provides organizations with flexible, scalable, and secure infrastructure for AI-powered applications. This prescriptive guidance presented different deployment patterns, each optimized for different operational requirements, cost constraints, and scaling needs.

**Next Steps**

Organizations beginning MCP deployment on AWS should first determine whether the required business capability can be exposed through Amazon Bedrock AgentCore Gateway as a Lambda, OpenAPI, or Smithy target. This is the preferred starting point because it avoids operating a standalone MCP server while centralizing authentication, authorization, credential management, and observability. Consider AWS Lambda, Amazon ECS, Amazon EKS, or Amazon EC2 when their execution model, networking options, container orchestration, portability, hardware support, or operating-system control better fits the workload. These patterns provide implementation flexibility but, depending on the selected service, may require additional responsibility for deployment, scaling, resilience, security configuration, observability, and infrastructure maintenance compared with managed AgentCore services.

Implement monitoring from day one by setting up CloudWatch dashboards, alarms, and log aggregation before production traffic begins. Follow AWS Well-Architected Framework security best practices including least-privilege IAM policies, VPC isolation, encryption at rest and in transit, and comprehensive audit logging. Gather metrics during initial operations and optimize based on actual usage patterns rather than assumptions. Consider hybrid approaches using multiple patterns for different MCP server types based on specific requirements such as Lambda for simple read-only servers and EKS for complex stateful servers.

**Reference Implementation**

The complete reference implementation with working code examples, deployment scripts, and detailed instructions for all four deployment patterns is available at: [https://github.com/aws-samples/sample-mcp-deployment-patterns/](https://github.com/aws-samples/sample-mcp-deployment-patterns/)
