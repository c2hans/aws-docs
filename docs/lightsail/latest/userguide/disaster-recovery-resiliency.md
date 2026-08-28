---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/disaster-recovery-resiliency.html
---

# Resilience in Amazon Lightsail
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, Amazon Lightsail offers several features to help support your data resiliency and backup needs.
+ Copying instance and disk snapshots across Regions. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).
+ Automating instance and disk snapshots. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).
+ Distributing incoming traffic across multiple instances in a single Availability Zone or multiple Availability Zones using a load balancer. For more information, see [Load balancers](understanding-lightsail-load-balancers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
