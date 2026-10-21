---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/next-steps.html
---

# Remote MCP Servers
<a name="next-steps"></a>

**Overview**

Remote MCP servers run on centralized cloud infrastructure and expose Streamable HTTP endpoints over HTTPS that multiple MCP clients can access over the network. This deployment model transforms MCP servers from personal development tools into production-grade services that support team collaboration, enterprise security requirements, and scalable AI applications.

The remote architecture separates the MCP client from the MCP server through network communication. Clients connect to remote server endpoints using Streamable HTTP over HTTPS. Each MCP message is sent in an HTTP POST, and the server returns either a JSON response or a request-scoped Server-Sent Events (SSE) stream. Load balancers distribute traffic across multiple server instances, providing horizontal scalability and fault tolerance. Cloud infrastructure enables automatic scaling based on demand, maintaining consistent performance during traffic spikes.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/69d254da-5dd8-41e2-8a0f-e39f4410da98.png)

Key architectural considerations while migrating from local to remote MCP deployment:
+ **Authentication and Security**: The MCP specification standardizes on [OAuth 2.1 for client authentication](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization). Amazon Bedrock AgentCore Gateway is the recommended approach, providing an OAuth authentication layer with fine-grained access control (FGAC) policies and guardrails out of the box.

  For self-managed deployments, AWS provides multiple authentication options: Application Load Balancer with native JWT authentication for OAuth-compliant token validation, Amazon Cognito for user-based authentication with JWT tokens and OAuth 2.0 flows, and API Gateway custom authorizers for enterprise identity provider integration. IAM with SigV4 request signing is most useful when an MCP client already has AWS credentials and needs to authenticate to an MCP server hosted on AWS. Because standard MCP clients typically expect OAuth, clients without native SigV4 support require a proxy or signing layer.

  An MCP server's permissions to access downstream AWS resources such as Amazon S3, DynamoDB, or Amazon Bedrock are a separate concern and are generally provided through the server's IAM execution role.
+ **Network latency and reliability**: API Gateway adds additional security layers including rate limiting, request throttling, API keys, and AWS WAF integration. Network security uses Amazon VPC for subnet isolation, security groups for traffic control, and TLS/SSL encryption. Organizations can deploy AWS PrivateLink or VPN connections for secure corporate network access without public internet exposure.
+ **Reliability and failure handling:** Remote MCP requests can fail because of transient network errors, throttling, service unavailability, or downstream dependency failures. Configure appropriate timeouts and retry only transient failures by using capped exponential backoff with jitter. Make retried operations idempotent, and do not retry validation or authorization failures. Use health checks, monitoring, and clear error responses to support detection and recovery.
+ **State management**: Prefer stateless Streamable HTTP for basic MCP servers because it simplifies horizontal scaling. Store shared application state in an external data store such as Amazon DynamoDB or Amazon ElastiCache. Use stateful Streamable HTTP when the server requires elicitation, sampling, or progress notifications. For more information, see: [Deploy MCP servers in AgentCore Runtime.](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)
+ **Well-Architected considerations:** Treat the MCP server and its supporting infrastructure as an application workload. Before production deployment, review the workload against [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), document identified risks, and create a remediation plan. Repeat the review after material changes to authentication, data access, scaling, or downstream dependencies.

The following sections explore specific deployment patterns on AWS including  AgentCore, Lambda with API Gateway for serverless deployments, ECS for containerized applications, and EKS for Kubernetes-based orchestration. Each pattern addresses different operational requirements, scaling needs, and team capabilities.
