---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/faq.html
---

# FAQ
<a name="faq"></a>

## Does this guide cover all the use cases for migrating an on-premises PostgreSQL database to Amazon EC2?
<a name="all-use-cases"></a>

This guide covers the most common use cases, but it doesn't cover every possible use case. Commercial tools, for example, are beyond the scope of this guide.

## Are the migration options covered in this guide applicable to all PostgreSQL versions?
<a name="all-versions"></a>

It depends on the use case. For example, if you're planning to use physical replication for your PostgreSQL migration, then you must have PostgreSQL 9.2 or later versions. In contrast, if you're planning to use logical replication for your migration, then you must have PostgreSQL 10 or later versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
