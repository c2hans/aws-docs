---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Connecting.JDBCDriver.html
---

# Connecting to RDS for PostgreSQL with the Amazon Web Services (AWS) JDBC Driver
<a name="PostgreSQL.Connecting.JDBCDriver"></a>

The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper. This wrapper is complementary to and extends the functionality of an existing JDBC driver. The driver is drop-in compatible with the community pgJDBC driver.

To install the AWS JDBC Driver, append the AWS JDBC Driver .jar file (located in the application `CLASSPATH`), and keep references to the respective community driver. Update the respective connection URL prefix as follows:
+ `jdbc:postgresql://` to `jdbc:aws-wrapper:postgresql://`

For more information about the AWS JDBC Driver and complete instructions for using it, see the [Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/awslabs/aws-advanced-jdbc-wrapper).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
