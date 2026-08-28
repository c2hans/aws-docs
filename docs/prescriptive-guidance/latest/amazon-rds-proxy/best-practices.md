---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend configuring Amazon RDS Proxy to connect to Amazon RDS databases using security mechanisms such as TLS/SSL. This way, RDS Proxy can act as an additional layer of security between client applications and the database. RDS Proxy supports TLS protocol version 1.2. RDS Proxy uses certificates from AWS Certificate Manager (ACM), which allows rotation of certificates without any need to update the proxy connection.

We also recommend the use of AWS Identity and Access Management (IAM) based authentication for RDS Proxy. In this configuration, you authorize the RDS Proxy endpoint to retrieve the Amazon RDS database secret (containing the user name and password credentials) from AWS Secrets Manager. Secrets Manager keeps the Amazon RDS database user names and passwords confidential and can rotate the passwords at defined regular intervals. For further details on the security and authentication setup of RDS Proxy, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html#rds-proxy-security).

Connection *pinning* is an important metric to monitor for both the Amazon RDS for PostgreSQL database and the RDS Proxy endpoint. Pinning occurs when a client session relies on state information from previous requests, and so the database does not enable the client session to run transactions across different database connections. The pinning can be caused by using `SET` commands or by creating temporary sequences, tables, or views. This results in a decrease in multiplexing of the proxy—that is, a decrease of the available connections for the client from RDS Proxy. To check for pinned connections, monitor the following Amazon CloudWatch metrics:
+ ClientConnections
+ DatabaseConnections
+ MaxDatabaseConnectionsAllowed
+ DatabaseConnectionsCurrentlySessionPinned

For more information, see the [Amazon RDS for PostgreSQL workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2a5fc82d-2b5f-4105-83c2-91a1b4d7abfe/en-US/3-intermediate/rds-proxy/task6).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
