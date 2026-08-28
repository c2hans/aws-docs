---
source_url: https://docs.aws.amazon.com/app-mesh/latest/userguide/disaster-recovery-resiliency.html
---

# Resilience in AWS App Mesh
<a name="disaster-recovery-resiliency"></a>

**Important**
End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect).

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

App Mesh runs its control plane instances across multiple Availability Zones to ensure high availability. App Mesh automatically detects and replaces unhealthy control plane instances, and it provides automated version upgrades and patching for them.

## Disaster recovery in AWS App Mesh
<a name="disaster-recovery"></a>

The App Mesh service manages backups of customer data. There is nothing that you need to do to manage backups. The backed-up data is encrypted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
