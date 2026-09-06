---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/migrating-data-for-large-oracle-databases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating data for large Oracle databases
<a name="migrating-data-for-large-oracle-databases"></a>

 For larger databases, use one of the methods described in this section rather than one of the methods described in [Migrating Data for small Oracle Databases](migrating-data-for-small-oracle-databases.md). For the purpose of this whitepaper, define a large database as any database 10 GB or more.

 This section describes three methods for migrating large databases:
+  [**Data migration using Oracle Data Pump**](data-migration-using-oracle-data-pump.md) – [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) is an excellent tool for migrating large amounts of data, and it can be used with databases on either Amazon RDS or Amazon EC2.
+  [**Data migration using Oracle external tables**](data-migration-using-oracle-external-tables.md) – The process involved in data migration using Oracle external tables is very similar to that of Oracle Data Pump. Use this method if you already have processes built around it; otherwise, it is better to use the Oracle Data Pump method.
+  [**Data migration using Oracle RMAN**](data-migration-using-oracle-rman.md) – Migration using RMAN can be useful if you are already backing up the database to AWS, or using the AWS Import/Export service to bring the data to AWS. Oracle RMAN can be used only for databases on Amazon EC2, not Amazon RDS.
