---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/introduction.html
---

# Migrating on-premises PostgreSQL databases to Amazon EC2
<a name="introduction"></a>

*Rajesh Madiwale, Suhas Basavaraj, and Sachin Kotwal, Amazon Web Services*

This guide provides an overview of options, best practices, and common scenarios for migrating your on-premises PostgreSQL databases to Amazon Elastic Compute Cloud (Amazon EC2). This type of migration is called a homogeneous migration—a [rehosting](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/rehost.html) approach that doesn't require you to make any changes to your operating system or database. A homogeneous migration is ideal if you want to maintain the same on-premises PostgreSQL database environment in the AWS Cloud, while maintaining full control of the database (including superuser access) and the operating system. This guide is intended for managers, product owners, database administrators, database engineers, and delivery managers who are planning a homogeneous migration of a PostgreSQL database to Amazon EC2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
