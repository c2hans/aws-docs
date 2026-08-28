---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/choosing-postgresql-ec2.html
---

# Choosing PostgreSQL on Amazon EC2
<a name="choosing-postgresql-ec2"></a>

You have the option to migrate your on-premises PostgreSQL database to Amazon EC2 or Amazon Relational Database Service (Amazon RDS). Important considerations include cost, storage options, high availability and disaster recovery (HADR) capabilities, organizational requirements, and business goals.

In general, we recommend that you use PostgreSQL on Amazon EC2 if any of the following requirements fit your use case:
+ You want more flexibility to control database instances and to access the database file system, but you don't have time to test modernization options (for example, you have the dependency of copying the files on a database server).
+ You have a mission-critical dependency for an application on a specific PostgreSQL extension like PL/Java or any earlier version on PostGIS.
+ You want to exit your data center as quickly as possible.
+ Your application depends on a deprecated version of PostgreSQL, and you don't want to upgrade to a more recent version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
