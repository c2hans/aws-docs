---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.mysqldump.html
---

# Logical migration from MySQL to Amazon Aurora MySQL by using mysqldump
<a name="AuroraMySQL.Migrating.ExtMySQL.mysqldump"></a>

Because Amazon Aurora MySQL is a MySQL-compatible database, you can use the `mysqldump` utility to copy data from your MySQL database or the `mariadb-dump` utility to copy your data from your MariaDB database to an existing Aurora MySQL DB cluster.

For a discussion of how to do so with MySQL or MariaDB databases that are very large, see the following topics in the *Amazon Relational Database Service User Guide*:
+ MySQL – [Importing data to an Amazon RDS for MySQL database with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-importing-data-reduced-downtime.html)
+ MariaDB – [Importing data to an Amazon RDS for MariaDB database with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-importing-data-reduced-downtime.html)

For MySQL or MariaDB databases that have smaller amounts of data, see the following topics in the *Amazon Relational Database Service User Guide*:
+ MySQL – [Importing data from an external MySQL database to an Amazon RDS for MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-importing-data-external-database.html)
+ MariaDB – [Importing data from an external MariaDB database to an Amazon RDS for MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-importing-data-external-database.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
