---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-5-amazon-ec2-persistent-server.html
---

# Deployment Pattern 5 - Amazon EC2 (Persistent Server)
<a name="deployment-pattern-5-amazon-ec2-persistent-server"></a>

Amazon EC2 provides virtual server instances where MCP servers run traditional long-running processes. You have full control over the operating system, installed software, and runtime environment. This pattern suits scenarios that require persistent connections, custom runtime configurations, or migrations from on-premises infrastructure. The trade-off is higher operational overhead for managing instances, patching, and scaling.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/d12204a2-3b29-40a5-8152-f366ba1b54a1.png)

**Architecture Characteristics**
+ Pros: Control over the operating system and runtime, including custom system packages, host-level configuration, and legacy software dependencies. Amazon EC2 also provides predictable capacity and a familiar operational model for teams migrating from on-premises environments.
+ Limitations: Higher operational overhead than serverless options. You manage operating system (OS) patching, Amazon Machine Image (AMI) maintenance, and security hardening. Scaling with Amazon EC2 Auto Scaling groups is typically slower (often several minutes) than with serverless patterns. Running instances incur costs even when traffic is low. High availability across multiple Availability Zones requires explicit configuration.
