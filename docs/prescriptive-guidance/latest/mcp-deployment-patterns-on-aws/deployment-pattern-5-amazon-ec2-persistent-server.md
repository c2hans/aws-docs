---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-5-amazon-ec2-persistent-server.html
---

# Deployment Pattern 5 - Amazon EC2 (Persistent Server)
<a name="deployment-pattern-5-amazon-ec2-persistent-server"></a>

Amazon Elastic Compute Cloud (EC2) provides virtual server instances where MCP servers run traditional long-running processes. Organizations gain complete control over the operating system, installed software, and runtime environment. This pattern suits scenarios requiring persistent connections, custom runtime configurations, or migrations from on-premises infrastructure. The trade-off is higher operational overhead for managing instances, patching, and scaling.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/d12204a2-3b29-40a5-8152-f366ba1b54a1.png)

**Architecture Characteristics**
+ Pros: Full control over the operating system and runtime, including custom system packages, host-level configuration, and legacy software dependencies. EC2 also provides predictable capacity and a familiar operational model for teams migrating from on-premises environments.
+ Limitations: Highest operational overhead — OS patching, AMI maintenance, and security hardening are fully self-managed. Scaling via Auto Scaling Groups is slower (2–5 min) compared to serverless patterns. Instances accrue costs 24/7 regardless of traffic. Multi-AZ high availability requires explicit configuration.
