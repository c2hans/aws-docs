---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/next-steps.html
---

# Remote MCP Servers
<a name="next-steps"></a>

**Overview**

Remote MCP servers deploy on centralized cloud infrastructure, providing HTTP/HTTPS or WebSocket endpoints that multiple MCP clients access over the network. This deployment model transforms MCP servers from personal development tools into production-grade services that support team collaboration, enterprise security requirements, and scalable AI applications.

The remote architecture separates the MCP client from the MCP server through network communication. Clients connect to server endpoints using HTTPS for request-response patterns or WebSocket protocols for persistent bidirectional communication. Load balancers distribute traffic across multiple server instances, providing horizontal scalability and fault tolerance. Cloud infrastructure enables automatic scaling based on demand, maintaining consistent performance during traffic spikes.

![Architecture diagram showing remote MCP server deployment with clients connecting via HTTPS to load balancer](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/8ff1290a-e005-4633-9a63-b0e10c5c341b.png)

Key architectural considerations while migrating from local to remote MCP deployment:
+ **Authentication and Security**: Remote MCP servers require robust authentication and authorization mechanisms. AWS provides multiple authentication options: IAM with SigV4 request signing for service-to-service authentication using temporary credentials, Amazon Cognito for user-based authentication with JWT tokens, and OAuth 2.0 flows for enterprise identity provider integration. API Gateway adds security layers including rate limiting, request throttling, API keys, and AWS WAF integration. Network security uses Amazon VPC for subnet isolation, security groups for traffic control, and TLS/SSL encryption. Organizations can deploy AWS PrivateLink or VPN connections for secure corporate network access without public internet exposure.
+ **Network latency and reliability**: Communication crosses internet or corporate networks rather than remaining local. Mitigate through geographic proximity, caching strategies, efficient API design, retry logic with exponential backoff, and clear error messaging.
+ **State management:** Stateless designs enable horizontal scaling but require external storage like Redis or DynamoDB for shared state. Stateful WebSocket patterns maintain context but complicate load balancing and failover.
+ **Cost Management:** Balance performance against infrastructure costs through appropriate sizing, usage tracking, cost allocation, and reserved capacity for predictable workloads.

The following sections explore specific deployment patterns on AWS including Lambda with API Gateway for serverless deployments, ECS for containerized applications, and EKS for Kubernetes-based orchestration. Each pattern addresses different operational requirements, scaling needs, and team capabilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
