---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/disaster-recovery-resiliency.html
---

# Resilience in AWS Device Farm
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Because Device Farm is available in the `us-west-2` Region only, we strongly recommend that you implement backup and recovery processes. Device Farm should not be the only source of any uploaded content.

Device Farm makes no guarantees of the availability of public devices. These devices are taken in and out of the public device pool depending on a variety of factors, such as failure rate and quarantine status. We do not recommend that you depend on the availability of any one device in the public device pool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
