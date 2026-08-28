---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html
---

# Managing an RDS Proxy
<a name="rds-proxy-managing"></a>

 This section provides information on how to manage RDS Proxy operation and configuration. These procedures help your application make the most efficient use of database connections and achieve maximum connection reuse. The more that you can take advantage of connection reuse, the more CPU and memory overhead that you can save. This in turn reduces latency for your application and enables the database to devote more of its resources to processing application requests.

**Topics**
+ [Modifying an RDS Proxy](rds-proxy-modifying-proxy.md)
+ [Adding a new database user when using RDS Proxy](rds-proxy-new-db-user.md)
+ [Moving from standard IAM authentication to end-to-end IAM authentication for RDS Proxy](rds-proxy-iam-migration.md)
+ [RDS Proxy connection considerations](rds-proxy-connections.md)
+ [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md)
+ [Deleting an RDS Proxy](rds-proxy-deleting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
