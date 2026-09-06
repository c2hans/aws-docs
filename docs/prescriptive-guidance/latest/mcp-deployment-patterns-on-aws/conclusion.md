---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/conclusion.html
---

# Next steps
<a name="conclusion"></a>

Deploying MCP servers on AWS provides organizations with flexible, scalable, and secure infrastructure for AI-powered applications. This prescriptive guidance presented different deployment patterns, each optimized for different operational requirements, cost constraints, and scaling needs.

**Next Steps**

Organizations beginning MCP deployment on AWS should follow a structured approach. First, evaluate requirements by assessing traffic patterns, operational capabilities, and scaling needs against the pattern selection criteria. Consider current infrastructure and team expertise while selecting the MCP deployment pattern. Start small by beginning with Lambda for rapid prototyping or ECS for production-ready deployments that balance simplicity with flexibility.

Implement monitoring from day one by setting up CloudWatch dashboards, alarms, and log aggregation before production traffic begins. Follow AWS Well-Architected Framework security best practices including least-privilege IAM policies, VPC isolation, encryption at rest and in transit, and comprehensive audit logging. Gather metrics during initial operations and optimize based on actual usage patterns rather than assumptions. Consider hybrid approaches using multiple patterns for different MCP server types based on specific requirements such as Lambda for simple read-only servers and EKS for complex stateful servers.

**Reference Implementation**

The complete reference implementation with working code examples, deployment scripts, and detailed instructions for all four deployment patterns is available at: [https://github.com/aws-samples/sample-mcp-deployment-patterns/](https://github.com/aws-samples/sample-mcp-deployment-patterns/)
