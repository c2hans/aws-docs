---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/objectives.html
---

# Objectives
<a name="objectives"></a>

Replatforming Oracle Database to AWS provides the following benefits.

## Balance of risk and improvement
<a name="balance-risk"></a>

Replatforming is more cost-effective, faster, and carries less risk than refactoring. It also enhances automation and improves application performance, security, and scalability more than rehosting.

## Lower cost
<a name="lower-cost"></a>

Replatforming provides flexibility in payment options offered by AWS, which are pay-as-you-go, On-Demand Instances, and Reserved Instances. AWS provides various levels of discount based on use cases, and you pay only for what you use, which can reduce both fixed and variable costs.

For Oracle Database Standard Edition 2 (SE2), AWS also provides the License Included model with Amazon RDS. The price includes Oracle licenses as part of a pay-as-you-go subscription model, and you don't need to purchase the licenses separately.

When running Oracle workloads on AWS, the Amazon RDS instance size can be scaled up and down dynamically according to load fluctuation. This can further reduce cost because you can provision compute power as needed.

For more information about pricing, see [Amazon RDS for Oracle pricing](https://aws.amazon.com/rds/oracle/pricing/).

## Enhanced automation
<a name="enhanced-automation"></a>

Replatforming provides a higher level of automation on maintenance tasks, such as backup, storage scaling, logging, and monitoring, which minimizes human errors. Staff productivity can also be improved by focusing on more valuable tasks, such as business development, performance tuning, and schema optimization.

## Increased agility
<a name="agility"></a>

Provisioning Oracle databases in an on-premises environment is time-consuming and can take weeks to months. By replatforming to AWS, you can complete the same task within minutes to a couple of hours. Replatforming also gives you the flexibility to delete a full stack of database when it's no longer needed, and to stop paying for it. That isn't an option in an on-premises environment.

## Better cloud maturity
<a name="cloud-maturity"></a>

Replatforming helps align with a cloud-first approach and grows cloud maturity over time. It builds the foundation for future database and application modernization by doing the following:
+ Offloading unstructured data to [Amazon Simple Storage Service (Amazon S3](https://aws.amazon.com/s3/))
+ Migrating data warehouse functions to [Amazon Redshift](https://aws.amazon.com/redshift/)
+ Migrating transactional functions to open source database engines such as [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) or [Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html) to save licensing cost and reduce operational overhead
