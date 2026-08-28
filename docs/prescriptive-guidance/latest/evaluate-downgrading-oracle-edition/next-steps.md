---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/next-steps.html
---

# Next steps
<a name="next-steps"></a>

After you determine that you can safely downgrade a database to Oracle Database Standard Edition 2 (SE2) on Amazon RDS for Oracle, you can migrate the database by using one or a combination of the following tools:
+ Oracle import and export** **utilities can move Oracle data in and out of Oracle databases. Oracle offers two types of database import and export utilities: Oracle Export and Import (for earlier releases) and Oracle Data Pump (available in Oracle Database 10g and later).
+ AWS Database Migration Service (AWS DMS) helps you migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud, between on-premises instances (through an AWS Cloud setup), or between combinations of cloud and on-premises databases. The change data capture (CDC) option of AWS DMS offers continuous replication, so that you can reduce the total downtime during migration. For information about the Oracle database versions and editions that AWS DMS supports, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html).
+ [Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html)** **offers real-time replication capabilities so that you can synchronize your target database after an initial load. This option can help reduce application downtime during go-live

Depending on your availability requirements during the downgrade, you can adopt any of the following options to safely downgrade your Enterprise Edition database to Standard Edition 2 on Amazon RDS for Oracle.

## Downgrading with downtime
<a name="downtime"></a>
+ Use Oracle Data Pump to create consistent export of data from the Enterprise Edition database and import that data into the Standard Edition 2 database. For more information, see [Step by Step Procedure to Convert from Enterprise Edition to Standard Edition (Doc ID 465189.1)](https://support.oracle.com/knowledge/Oracle%20Database%20Products/465189_1.html). Oracle credentials are required.
+ Use AWS DMS to perform a full load of data from the Enterprise Edition database to the Standard Edition 2 database.
+ Use Oracle GoldenGate to perform a full instantiation of the Standard Edition 2 database from the Enterprise Edition database.

## Downgrading with reduced downtime
<a name="reduced-downtime"></a>
+ Use Oracle Data Pump for consistent export and import of the initial load, and use AWS DMS CDC for data synchronization.
+ Use Oracle Data Pump for consistent export and import of the initial load, and use Oracle GoldenGate for data synchronization.
+ Use AWS DMS for the full load and for data synchronization.
+ Use Oracle GoldenGate for full instantiation and for data synchronization.

For more information on migrating Oracle databases to Amazon RDS for Oracle, see the following AWS Prescriptive Guidance documentation:
+ [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/) (guide)
+ [Migrate an Oracle database from Amazon EC2 to Amazon RDS for Oracle using AWS DMS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms.html) (pattern)
+ [Migrate an on-premises Oracle database to Amazon RDS for Oracle using Oracle Data Pump](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump.html) (pattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
