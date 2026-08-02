---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/driving-adoption.html
---

# Driving adoption of your disaster recovery strategy
<a name="driving-adoption"></a>

When your DR strategy is in place, you can drive adoption of the strategy throughout your organization. When your strategy reaches 100 percent adoption, all applications and their databases would be in a position to handle an adverse DR event and can pursue DR maturity through testing.

You can work with application owners and architects to drive adoption by communicating the DR strategy throughout your organization and asking employees to evaluate the current AWS databases used in their applications. This ensures that all currently used databases can meet the expectations set in the DR strategy. If application owners and architects determine that the database they chose for their applications cannot meet the requirements of the DR strategy, they will have to plan a migration to a suitable AWS database that can achieve the chosen RTO and RPO expectations. For example, if a critical application in your business that requires an RPO in seconds and an RTO in minutes currently uses an Amazon RDS for Oracle DB instance, Amazon RDS will not be able to meet these expectations. In this case, you could consider migrating the workload to [Amazon Aurora PostgreSQL-Compatible](https://aws.amazon.com/blogs/database/migrate-from-amazon-rds-for-oracle-to-aurora-postgresql-or-amazon-rds-for-postgresql-using-this-self-service-guide/) and use a global database to meet the expectations set by your DR strategy.
