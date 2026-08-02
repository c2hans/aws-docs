---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/introduction.html
---

# Choosing a migration tool for rehosting databases
<a name="introduction"></a>

*Mike Kuznetsov and Harpreet Virk, Amazon Web Services*

When you plan to migrate your large workloads to AWS, we recommend that you follow [AWS guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/overview.html) and split your migration process into three stages: assess, mobilize, and migrate. The migration journey involves many factors, including scope ("what?"), strategy ("why?"), and timeline ("when?"), as discussed in [AWS large-migration strategy and best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/scope-strategy-time.html). Each workload you choose to migrate might follow a different migration strategy, as defined in [seven common strategies (7 Rs)](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html). Most workloads follow the rehost scenario for lift-and-shift migrations. After you select a strategy, you can address the question "how?", which focuses on at least three aspects of migration ([people, technology, and processes](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/best-practices.html)).

This guide is for anyone who is planning to migrate their on-premises workloads to the AWS Cloud, including IT and business executives, program and project managers, product owners, and operations and infrastructure managers.

This guide helps you determine your high-level migration approach but doesn't cover detailed implementation strategies for specific database engines or applications. For these detailed recommendations, see the [Resources](resources.md) section, which points to various workload-specific and database engine-specific guides.

The focus of this guide is on the rehost migration path, which involves moving an application to the cloud without making any changes to take advantage of cloud capabilities. For example, migrating your on-premises Microsoft SQL Server database to SQL Server on an Amazon Elastic Compute Cloud (Amazon EC2) instance in the AWS Cloud is a rehosting strategy. More specifically, the guide discusses tools best suited for lift-and-shift migrations of workloads that have databases included in their scope, and factors to consider when selecting a particular service for the migration. It answers questions such as the following:
+ Which service best supports database migrations?
+ Could the service used for non-database servers be used for database servers as well, or should database servers be treated differently?
+ What if my rehost migration turns into a mixed approach of rehosting and replatforming?
