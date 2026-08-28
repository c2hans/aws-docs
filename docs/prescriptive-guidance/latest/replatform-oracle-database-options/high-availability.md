---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/high-availability.html
---

# High availability
<a name="high-availability"></a>

Amazon RDS for Oracle supports Multi-AZ deployment, which automatically creates a standby instance in a different Availability Zone. A Multi-AZ deployment provides automatic failover during planned maintenance and unplanned disruptions.

Amazon RDS Custom for Oracle doesn't support Multi-AZ deployment. As an alternative, you can use a replica to manually build a high availability (HA) solution. Depending on the design, you can implement both synchronous and asynchronous data replication. For more information, see the [Build high availability for Amazon RDS Custom for Oracle using read replicas](https://aws.amazon.com/blogs/database/build-high-availability-for-amazon-rds-custom-for-oracle-using-read-replicas/) blog post.

Both Amazon RDS for Oracle and Amazon RDS Custom for Oracle support up to five managed read replicas. You can automatically create the read replicas from the AWS Management Console or by using AWS Command Line Interface (AWS CLI).

With Amazon RDS Custom for Oracle, you can also create your own manually configured external Oracle replicas. This offers you the flexibility to host replicas on Amazon EC2 instances in the same or another AWS Region, and also in an on-premises environment. External replicas don't count toward the instance limit within the AWS account. They also lie outside the RDS Custom support perimeter. For more information about the support perimeter, see [RDS Custom support perimeter](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-concept.html#custom-troubleshooting.support-perimeter).

|
|
|  HA support | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Multi-AZ deployment | Yes | No |
| Standby replication | Synchronous | Asynchronous or synchronous |
| AWS managed automatic failover | Yes | No |
| Automatic creation of read replica | Yes | Yes |
| Maximum managed read replicas | 5 | 5 |
| AWS managed cross-Region read replica | Yes | No |
| Modification of AWS managed read replica | No | Yes |
| Creation of self-managed read replica | No | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
