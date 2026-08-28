---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-2-aws-lambda-amazon-api-gateway.html
---

# Deployment Pattern 2 - AWS Lambda \+ Amazon API Gateway
<a name="deployment-pattern-2-aws-lambda-amazon-api-gateway"></a>

AWS Lambda with Amazon API Gateway represents the serverless approach where MCP server logic runs in ephemeral functions triggered by API requests. Lambda automatically manages the underlying compute resources, scaling from zero to thousands of concurrent executions without manual intervention. This pattern significantly reduces infrastructure management overhead, making it ideal for variable workloads and teams prioritizing rapid development over operational control.

Sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-serverless](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-serverless)

![Deployment Pattern of AWS Lambda + Amazon API Gateway](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/03fc7c1d-f5bd-4c0c-a202-1a2f85507458.png)

**Architecture Characteristics**
+ Pros: Zero server management with automatic infrastructure scaling; pay-per-request pricing aligns costs with actual usage, instant scaling from zero to thousands of concurrent executions. Built-in multi-AZ high availability and fault tolerance, native integration with AWS services through IAM roles, fast deployment cycles with minimal operational overhead, no idle costs when not processing requests.
+ Limitations: 15-minute maximum execution time per request (synchronous), cold start latency of 0.5-3 seconds impacts first request performance, 10 GB memory limit per function, stateless architecture requires external storage for session management, WebSocket support requires API Gateway WebSocket APIs with additional configuration, limited runtime customization compared to container or VM approaches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
