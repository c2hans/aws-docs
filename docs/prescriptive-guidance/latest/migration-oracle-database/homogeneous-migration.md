---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/homogeneous-migration.html
---

# Homogeneous database migration
<a name="homogeneous-migration"></a>

AWS offers you the ability to run Oracle Database in a cloud environment. For developers and database administrators, running Oracle Database in the AWS Cloud is very similar to running Oracle Database in a data center. This section describes options for migrating Oracle Database from an on-premises environment or a data center to the AWS Cloud.

AWS offers four options for running Oracle Database on AWS, as described in the following table.

|
|
| Option | Highlights | More information |
| --- |--- |--- |
| **Oracle Database on Amazon RDS ** | Managed service, provides easy provisioning and licensing | Amazon RDS for Oracle section |
| **Oracle Database on Amazon RDS Custom** | Managed service, but you retain administrative rights to the database and the underlying operating system | Amazon RDS Custom for Oracle section |
| **Oracle Database on Amazon EC2** | Self-managed, provides full control and flexibility | Amazon EC2 for Oracle section |
| **Oracle Database on VMware Cloud on AWS** | Minimal disruption, easy to manage | VMware Cloud on AWS for Oracle section |

Your application requirements, database features, functionality, growth capacity, and overall architecture complexity will determine which option to choose. If you are migrating multiple Oracle databases to AWS, some of them might be a great fit for Amazon RDS whereas others might be better suited to run directly on Amazon EC2. You might have databases that are running on Oracle Enterprise Edition (EE) but are a good fit for Oracle Standard Edition Two (SE2). You can save on cost and licenses for those databases. Many AWS customers run multiple Oracle Database workloads across Amazon RDS, Amazon EC2, and VMware Cloud on AWS. If you're moving to Amazon RDS Custom, make sure to review the [requirements and limitations for Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
