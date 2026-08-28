---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/migrating-data-for-small-oracle-databases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating data for small Oracle databases
<a name="migrating-data-for-small-oracle-databases"></a>

 You should base your strategy for data migration on the database size, reliability, and bandwidth of your network connection to AWS, and the amount of time available for migration. Many Oracle databases tend to be medium to large in size, ranging anywhere from 10 GB to 5 TB, with some as large as 20 TB or more. However, you also might need to migrate smaller databases. This is especially true for phased migrations where the databases are broken up by schema, making each migration effort small in size.

 If the source database is under 10 GB, and if you have a reliable high-speed internet connection, you can use one of the following methods for your data migration. All the methods discussed in this section work with Amazon RDS Oracle or Oracle Database running on Amazon EC2.

**Note**
The 10 GB size is just a guideline; you can use the same methods for larger databases as well. The migration time varies based on the data size and the network throughput. However, if your database size exceeds 50 GB, you should use one of the methods listed in the [Migrating data for large Oracle databases](migrating-data-for-large-oracle-databases.md) section in this whitepaper.

**Topics**
+ [Oracle SQL Developer database copy](oracle-sql-developer-database-copy.md)
+ [Oracle materialized views](oracle-materialized-views.md)
+ [Oracle SQL\*Loader](oracle-sqlloader.md)
+ [Oracle Export and Import utilities](oracle-export-and-import-utilities.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
