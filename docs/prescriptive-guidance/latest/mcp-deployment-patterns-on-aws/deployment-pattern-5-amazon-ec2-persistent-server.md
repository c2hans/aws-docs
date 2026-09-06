---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-5-amazon-ec2-persistent-server.html
---

# Deployment Pattern 5 - Amazon EC2 (Persistent Server)
<a name="deployment-pattern-5-amazon-ec2-persistent-server"></a>

Amazon Elastic Compute Cloud (EC2) provides virtual server instances where MCP servers run traditional long-running processes. Organizations gain complete control over the operating system, installed software, and runtime environment. This pattern suits scenarios requiring persistent connections, custom runtime configurations, or migrations from on-premises infrastructure. The trade-off is higher operational overhead for managing instances, patching, and scaling.

**Architecture Characteristics**
+ Pros: Full OS and runtime control with no execution time limits, native WebSocket and SSE support without gateway timeout constraints, zero cold starts with predictable performance, cost-efficient at sustained high throughput with reserved Instances, familiar operational model for teams migrating from on-premises environments.
+ Limitations: Highest operational overhead — OS patching, AMI maintenance, and security hardening are fully self-managed. Scaling via Auto Scaling Groups is slower (2–5 min) compared to serverless patterns. Instances accrue costs 24/7 regardless of traffic. Multi-AZ high availability requires explicit configuration. Long-lived access keys on instances are a common security anti-pattern.
