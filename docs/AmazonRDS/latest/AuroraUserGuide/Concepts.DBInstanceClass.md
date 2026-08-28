---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html
---

# Amazon AuroraDB instance classes
<a name="Concepts.DBInstanceClass"></a>

The DB instance class determines the computation and memory capacity of an Amazon Aurora DB instance. The DB instance class that you need depends on your processing power and memory requirements.

A DB instance class consists of both the DB instance class type and the size. For example, db.r6g is a memory-optimized DB instance class type powered by AWS Graviton2 processors. Within the db.r6g instance class type, db.r6g.2xlarge is a DB instance class. The size of this class is 2xlarge.

For more information about instance class pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

For more information about DB instance class types, supported DB engines, supported AWS Regions, or hardware specifications for DB instance classes, see the following sections.

**Topics**
+ [DB instance class types](Concepts.DBInstanceClass.Types.md)
+ [Supported DB engines for DB instance classes](Concepts.DBInstanceClass.SupportAurora.md)
+ [Determining DB instance class support in AWS Regions](Concepts.DBInstanceClass.RegionSupportAurora.md)
+ [Hardware specifications for DB instance classes for Aurora](Concepts.DBInstanceClass.Summary.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
