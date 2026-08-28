---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-migration-methods.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data migration methods
<a name="data-migration-methods"></a>

 The remainder of this whitepaper provides details about each method for migrating data from Oracle Database to AWS. Before you get to the details, you can scan the following table for a quick summary of each method.

 Each method depends upon business recovery point objective (RPO), recovery time objective (RTO), and overall availability SLA. Migration administrators must evaluate and map these business agreements with the appropriate methods. Choose the method depending upon your application SLA, RTO, RPO, tool, and license availability.

* Table 1 – Migration methods and tools *

|  Data migration method  |  Database size  |  Works for:  |  Recommended for:  |
| --- | --- | --- | --- |
|  [AWS Database Migration Service](https://aws.amazon.com/dms/)  |  Any size  |  Amazon RDS <br /> Amazon EC2  |  Minimal downtime migration <br /> Database size limited by internet bandwidth  |
|  [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) <br /> [Database copy](https://www.oracle.com/webfolder/technetwork/tutorials/obe/db/sqldev/r31/DatabaseCopy/DatabaseCopy.html)  |  Up to 200 MB  |  Amazon RDS <br /> Amazon EC2  |  Small databases with any number of objects  |
|  [Oracle Materialized Views](https://docs.oracle.com/cd/B10501_01/server.920/a96567/repmview.htm)  |  Up to 500 MB  |  Amazon RDS <br /> Amazon EC2  |  Small databases with limited number of objects  |
|  [Oracle SQL\*Loader](https://docs.oracle.com/cd/B19306_01/server.102/b14215/part_ldr.htm)  |  Up to 10 GB  |  Amazon RDS <br /> Amazon EC2  |  Small to medium size databases with limited number of objects  |
|  [Oracle Export and Import](https://docs.oracle.com/cd/B10501_01/server.920/a96652/part1.htm) <br /> [Oracle Utilities](https://www.oracle.com/industries/utilities/)  |  Up to 10 GB  |  Amazon RDS <br /> Amazon EC2  |  Small to medium size databases with large number of objects  |
|  [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm)  |  Up to 5 TB  |  Amazon RDS <br /> Amazon EC2 <br /> VMware Cloud on AWS  |  Preferred method for any database from 10 GB to 5 TB  |
|  [External tables](https://docs.oracle.com/cd/B19306_01/server.102/b14215/et_concepts.htm)  |  Up to 1 TB  |  Amazon RDS <br /> Amazon EC2 <br /> VMware Cloud on AWS  |  Scenarios where this is the standard method in use  |
|  [Oracle RMAN](https://www.oracle.com/database/technologies/high-availability/rman.html)  |  Any size  |  Amazon EC2 <br /> VMware Cloud on AWS  |  Databases over 5 TB, or if database backup is already in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3)  |
|  [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/)  |  Any size  |  Amazon RDS <br /> Amazon EC2 <br /> VMware Cloud on AWS  |  Minimal downtime migration  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
