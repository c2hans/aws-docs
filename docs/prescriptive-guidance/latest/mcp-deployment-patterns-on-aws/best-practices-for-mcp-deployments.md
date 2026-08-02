---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/best-practices-for-mcp-deployments.html
---

# Best practices for MCP deployments
<a name="best-practices-for-mcp-deployments"></a>

The  [AWS Well-Architected Framework ](https://aws.amazon.com/architecture/well-architected/)provides a set of proven principles for building secure, reliable, and efficient cloud workloads. The following practices are most relevant when deploying MCP servers in production.
+ **Apply least-privilege access** - Every component — whether a function, container, or instance — should have only the permissions it needs for its specific task. Avoid wildcard resource permissions. Use short-lived credentials wherever possible and never store long-lived credentials on compute resources.
+ **Protect data at rest and in transit** -Encrypt all stored data using customer-managed or platform-managed keys depending on your compliance requirements. Enforce TLS 1.2 or higher for all network communication. Secrets should be stored in a managed secrets service with automatic rotation — never hardcoded or stored in environment variables unencrypted.
+ **Keep compute private **- Place all MCP servers behind a load balancer in private subnets. Only the load balancer or API entry point should be internet-facing. Use private endpoints for internal service-to-service traffic to avoid traversing the public internet.
+ **Design for failure** - Deploy across at least two availability zones. Implement circuit breakers and explicit timeouts on all downstream calls — never rely on platform defaults. Applications should degrade gracefully when a dependency is unavailable rather than failing entirely.
+ **Enable threat detection from day one** - Turn on audit logging for all API activities across your accounts. Use automated threat detection to analyze logs for anomalous behavior. Centralize security findings into a single dashboard and define incident response runbooks before an incident occurs.
+ **Right-size before you scale** - Start with a conservative allocation and tune based on observed metrics. Over-provisioned resources waste money and energy. Use automated recommendations after a period of baseline operation rather than guessing upfront.
+ **Define infrastructure as code** - Never create or modify production resources manually. All compute, networking, IAM, and monitoring resources should be version-controlled, peer-reviewed, and deployed through automated pipelines. This approach is designed to provide repeatability, auditability, and safe rollbacks.
+ **Design long-running operations asynchronously** - MCP tools that take more than a few seconds to complete should be decoupled from the synchronous request path. Accept the request, queue the work, return a job ID, and provide a polling or callback mechanism. This avoids gateway timeouts and improves user experience.
+ **Tag every resource** - Apply consistent tags — at minimum environment, application, team, and cost centre — to all resources. Enforce tagging policy through automated rules. Without tagging, cost attribution and compliance reporting become impractical at scale.
+ **Prefer managed services over self-managed infrastructure** - Managed and serverless compute eliminates idle resource consumption and reduce operational burden. When evaluating compute options, only choose self-managed infrastructure when there is a specific capability requirement that managed services cannot satisfy.
