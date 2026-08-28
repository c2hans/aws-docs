---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-jdbc.html
---

# Amazon Neptune JDBC connectivity
<a name="neptune-jdbc"></a>

Amazon Neptune has released an [open-source JDBC driver](https://github.com/aws/amazon-neptune-jdbc-driver) that supports openCypher, Gremlin, SQL-Gremlin, and SPARQL queries. JDBC connectivity makes it easy to connect to Neptune with business intelligence (BI) tools such as Tableau. There is no additional cost to using the JDBC driver with Neptune — you still pay only for the Neptune resources that are consumed.

The driver is compatible with JDBC 4.2, and requires at least Java 8. See the [JDBC API documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/) for information about how to use a JDBC driver.

The GitHub project, where you can file issues and open feature requests, contains detailed documentation for the driver:

**[JDBC Driver for Amazon Neptune](https://github.com/aws/amazon-neptune-jdbc-driver#readme)**
+ [Using SQL with the JDBC driver](https://github.com/aws/amazon-neptune-jdbc-driver/blob/develop/markdown/sql.md)
+ [Using Gremlin with the JDBC Driver](https://github.com/aws/amazon-neptune-jdbc-driver/blob/develop/markdown/gremlin.md)
+ [Using openCypher with the JDBC Driver](https://github.com/aws/amazon-neptune-jdbc-driver/blob/develop/markdown/opencypher.md)
+ [Using SPARQL with the JDBC Driver](https://github.com/aws/amazon-neptune-jdbc-driver/blob/develop/markdown/sparql.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
