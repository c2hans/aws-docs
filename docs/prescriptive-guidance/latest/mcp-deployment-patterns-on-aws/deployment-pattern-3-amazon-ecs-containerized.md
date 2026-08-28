---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-3-amazon-ecs-containerized.html
---

# Deployment Pattern 3 - Amazon ECS (Containerized)
<a name="deployment-pattern-3-amazon-ecs-containerized"></a>

Amazon Elastic Container Service (ECS) with API gateway orchestrates Docker containers running MCP server applications. ECS supports both AWS Fargate for serverless container execution and EC2 launch types for more control. The architecture diagram illustrates the "Public front door \+ private MCP runtime" pattern, where Amazon API Gateway is the only internet-facing endpoint, and enforces OAuth authorization. API Gateway then reaches into the VPC using VPC link v2 to call an internal Application Load Balancer. The private ALB forwards an ECS service running on the remote MCP server.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-ecs](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-ecs)

![Deployment Pattern of Amazon ECS (Containerized)](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/3e9f7765-04d2-4329-8586-eca256dcad75.png)

**Architecture Characteristics**
+ Pros: Backend stays private: ALB and ECS are not internet-exposed; only API Gateway is public. Centralized security controls at API Gateway, Centralized throttling, quotas, and logging management.
+ Limitations: API Gateway has default Timeouts and Payload limits. If any of the MCP tools are taking longer, then need to make the MCP tool async, or use Rest API and raise timeouts beyond 29s. If there are tools designed to run for a long time, then need to remove API Gateway and use public Application Load Balancer instead.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
