---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This section discusses the following business outcomes:
+ Increase application scalability
+ Increase application performance
+ Increase application availability
+ Increase application security
+ Decrease operational complexity

## Increase application scalability
<a name="increase-application-scalability"></a>

An application's scalability depends on its database's ability to handle concurrent connections. The number of concurrent connections depends on the database instance type. For example, a t3.small instance type can support 187 concurrent database connections. Additional client connection attempts to the database will result in a failure. Using an Amazon RDS Proxy endpoint to interact with the database enables the application to continue working even when the client connections required exceed the maximum connections supported by the instance type, as shown in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/images/guide-img/a636f483-11c8-4c7b-ad56-b8c47e65c2ef/images/bb2b8139-18a7-460f-9564-d153038feb1e.png)

Because RDS Proxy uses connection pooling, a test application using an RDS Proxy endpoint was able to scale to 20,000 client connections even when the database instance was capped at 187 concurrent connections.

Amazon RDS Proxy is a valuable component in an architecture that needs to scale.

## Increase application performance
<a name="increase-application-performance"></a>

Idle connections are database connections that are not processing any transactions but are still using memory and CPU on the database server. An idle client session with an open transaction will also block the autovacuum process from cleaning up dead tuples. The dead tuples will cause bloat in the database tables, resulting in a slowdown of SQL queries. An Amazon RDS for PostgreSQL database keeps the idle connections open for 24 hours by default (set by the `idle_in_transaction_session_timeout` parameter).

RDS Proxy actively manages idle connections by closing them if they remain idle for more than 30 minutes by default (set by the [IdleClientTimeout](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-connection-pooling-tuning.idleclienttimeout) parameter). Clearing the idle sessions along with the resources used by them sooner reduces the impact on the CPU, memory, and the autovacuum process.

Amazon RDS Proxy manages idle connections efficiently, which improves application performance.

## Increase application availability
<a name="increase-application-availability"></a>

An application's availability depends on its database failover response time. During a database failover, the application will experience errors for in-flight transactions. This reduces the application's availability to its end users.

RDS Proxy is database failover aware. When database failover occurs, RDS Proxy queues the incoming requests from the application side until it is able to create new connections with the database. This helps prevent errors for in-flight transactions, thereby increasing the application's availability.

The blog post [Improving application availability with Amazon RDS Proxy](https://aws.amazon.com/blogs/database/improving-application-availability-with-amazon-rds-proxy/) highlights the benefits of using RDS Proxy with an Amazon Aurora database. When using RDS Proxy, the average failover time was 3.1 seconds, compared with 24 seconds when using a direct connection to the database. This represents an 87 percent increase.

Amazon RDS Proxy helps increase application availability.

## Increase application security
<a name="increase-application-security"></a>

Because RDS Proxy uses TLS/SSL and AWS Identity and Access Management (IAM), it can act as an additional layer of security between client applications and the underlying Postgres database. With RDS Proxy, you can use stronger security requirements (TLS 1.2 and IAM roles) for applications connections to the proxy.

RDS Proxy can retrieve database credentials from AWS Secrets Manager, and you can configure IAM authentication for RDS Proxy users. By doing so, you can enforce IAM authentication for database access even when the databases use native authentication mechanisms, such as user name and password. This reduces the need for the applications to manage database credentials, and it improves the application security posture.

## Decrease operational complexity
<a name="decrease-application-management"></a>

A connection pooler must be complemented with additional proxy servers to deliver high availability and load balancing. This setup increases operational complexity. Traditional proxy servers are difficult to deploy, patch, and manage. Using them consumes time and energy that could be better spent on developing products.

Amazon RDS Proxy gives you the benefits of a database proxy without requiring the additional burden of patching and managing your own proxy server. RDS Proxy is serverless and scales automatically to accommodate your workload. With its self-service setup option, RDS Proxy can increase developer velocity, resulting in faster delivery of new applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
