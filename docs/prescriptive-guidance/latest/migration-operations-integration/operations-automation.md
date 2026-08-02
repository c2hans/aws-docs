---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/operations-automation.html
---

# Operations automation
<a name="operations-automation"></a>

You are not expected to have all your IT operations fully automated on day 1. Take a phased approach instead. Start by carefully prioritizing the core operations functions that are listed in the following table. Use the AWS services listed in the[ AWS services for automation ](aws-services-for-automation.md)section to streamline the modernization process.

|
|
| Core operations functions | Capabilities and considerations |
| --- |--- |
| **Platform architecture and governance** | [Account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html), [virtual private cloud (VPC) strategy](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html), [multi-Region and Multi-AZ strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.html), [tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html), IP addressing and connectivity, [security strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html), audit and compliance |
| **Event and incident management** | Alerting and alarming, incident management process, AWS Support engagement, service desk, [observability toolsets and integrations](https://docs.aws.amazon.com/en_us/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/), cloud runbooks |
| **Provisioning and configuration management** | Provisioning, continuous integration and continuous delivery (CI/CD) pipeline and toolset, release management, testing framework and toolset, code repository, branching strategy, blue/green deployments, configuration management database (CMDB), configuration items |
| **Availability and continuity management** | High availability architecture, automatic scaling, [backup and restore](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/welcome.html), replication, recovery time objective (RTO) and recovery point objective (RPO), data storage and retention policy, [disaster recovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/defining.html), automation and bots, hybrid options, storage gateways |
| **Monitoring and observability** | Metrics, logging, application performance, user experience, network monitoring, unified dashboards |
