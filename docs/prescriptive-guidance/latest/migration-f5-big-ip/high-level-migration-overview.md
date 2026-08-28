---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/high-level-migration-overview.html
---

# High-level migration overview
<a name="high-level-migration-overview"></a>

Before you begin the migration, it helps to lay out the entire process from a high level. The following is an example of the steps you might take to migrate an F5 BIG-IP workload to the AWS Cloud. More detailed steps and processes for an F5 BIG-IP migration can be found in the pattern [Migrate an F5 BIG-IP workload to F5 BIG-IP VE on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud.html?did=pg_card&trk=pg_card).

1. Deploy the required number of VPCs based on your individual requirements. This can be manual or automated through a tool such as [AWS Landing Zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/).

1. Evaluate current F5 licenses, utilizations, and configurations.

1. Evaluate public and internal applications.

1. Evaluate current F5 configurations.

1. Evaluate size and IP address requirements, and choose the required number and type of F5 and AWS instances.

1. Identify which migration strategy to deploy. For example, lift and shift; lift, shift and modernize; or hybrid.

1. Evaluate and identify the DNS design.

1. Evaluate how traffic will be directed to the application if it exists both on premises and in the AWS Cloud.

1. Perform initial deployments of F5 instances by using AWS CloudFormation templates.

1. Modify deployments to meet topology requirements with additional elastic network interfaces and route tables.

1. Align Elastic IP addresses to self IPs or management IPs, and plan out Elastic IP to virtual IP (VIP) mapping.

1. Create secondary addresses on elastic network interfaces for VIPs.

1. Apply secondary addresses in the AWS Cloud.

1. Map Elastic IP addresses to secondary address for VIPs.

1. Pull configurations and compile a list of objects to move.

1. Deploy the configurations to F5 BIG-IP.

1. Map the secondary addresses to VIPs.

1. Test traffic.

1. Test failover.

1. If you are building a hybrid, make sure you incorporate the system into F5 DNS.

|
|
| Important: Access to the AWS API endpoints is required. NAT or Elastic IP addresses are also required for high availability within or between Availability Zones. |
| --- |

The following diagram shows the high-level process flow for an F5 BIG-IP migration.

![High-level process flow for an F5 BIG-IP migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-high-level.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
