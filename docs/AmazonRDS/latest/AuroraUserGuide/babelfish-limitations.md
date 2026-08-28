---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-limitations.html
---

# Babelfish limitations
<a name="babelfish-limitations"></a>

 The following limitations currently apply to Babelfish for Aurora PostgreSQL:
+  Babelfish doesn't support the following Aurora features:
  + AWS Identity and Access Management
  + Database Activity Streams (DAS)
  + RDS Data API with Aurora PostgreSQL Aurora serverless and provisioned
  + RDS Proxy with RDS for SQL Server
  + Salted challenge response authentication mechanism (SCRAM)
  + Query editor
  + Zero-ETL integrations
+  Babelfish doesn't provide the following client driver API support:
  +  API requests with the connection attributes related to Microsoft Distributed Transaction Coordinator (MSDTC) aren't supported. These include XA calls by the SQLServerXAResource class in the SQL server JDBC driver.
+ Babelfish currently doesn't support the following Aurora PostgreSQL extensions:
  + `bloom`
  + `btree_gin`
  + `btree_gist`
  + `citext`
  + `cube`
  + `hstore`
  + `hypopg`
  + Logical replication using `pglogical`
  + `ltree`
  + `pgcrypto`
  + Query plan management using `apg_plan_mgmt`

  To learn more about PostgreSQL extensions, see [Working with extensions and foreign data wrappers](Appendix.PostgreSQL.CommonDBATasks.md).
+ The open source [jTDS driver](https://github.com/milesibastos/jTDS/) that is designed as an alternative to the Microsoft JDBC driver is not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
