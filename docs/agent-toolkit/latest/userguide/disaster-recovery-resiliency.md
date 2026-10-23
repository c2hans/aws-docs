---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/disaster-recovery-resiliency.html
---

# Resilience in AWS MCP Server
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

AWS MCP Server is a stateless proxy that runs AWS API calls on your behalf. It does not use persistent storage to store customer content, so there is no AWS MCP Server data for you to back up or restore. For more information, see [Data protection in AWS MCP Server](data-protection.md).
