---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/introduction.html
---

# Increasing application scalability, performance, and availability by using Amazon RDS Proxy
<a name="introduction"></a>

*Anand Komandooru, Noorul Hasan, Varun Kumar, and Venkat Nalajala, Amazon Web Services*

This guide will walk through the need for database connection pooling, the challenges associated with implementing a self-hosted solution, and the benefits of using [Amazon Relational Database Service (Amazon RDS) Proxy](https://aws.amazon.com/rds/proxy/) with Amazon RDS for PostgreSQL in an application architecture on Amazon Web Services (AWS).

## Challenge
<a name="challenge"></a>

PostgreSQL is implemented by using a [process-per-user client/server model](https://www.postgresql.org/docs/8.3/connect-estab.html). When a new connection is received, the main process starts a child process to handle this new connection. The main process then waits for the next connection, and the child process takes care of all activities related to this new client connection. A new child process is started for each new connection received by the database.

Many applications, including those built on modern serverless architectures, can have a large number of open connections to the database server. They might open and close database connections at a high rate, exhausting database memory and compute resources.

Transactional applications that are frequently opening and closing the connections will experience higher connection latency, resulting in lower transactions per second. This will increase application latency.

A failover occurs when the primary database instance becomes inaccessible, and another instance takes over as the new primary. This disrupts client connections. Failovers can be planned, when they are induced by administrative actions such as a rolling upgrade, or unplanned, when they occur because of failures. In both cases, operators must reduce downtime to minimize client disruption.

## Common practice
<a name="common-practice"></a>

To address the challenges of application scalability and performance, a connection pool is used. Connection pooling significantly reduces connection latency by reusing existing connections, and it enables higher database throughput (transactions per second) on the server. A connection pool queues or throttles application connections that can't be served immediately from the pool of connections.

Additional challenges arise after implementing this connection pooling. Operators must self-manage the infrastructure and software to operate the connection pooling service. For handling a failover event, application developers must manage the connection complexity for every application. The application has to detect the connection failure, discover a new primary, and reconnect to it as quickly as possible.

## Recommendation
<a name="recommendation"></a>

To reduce the challenges associated with a self-hosted connection pooling solution, while taking advantage of the benefits, we recommend evaluating [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) for your workloads.

RDS Proxy is a fully managed, highly available database proxy. RDS Proxy uses [connection pooling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html#rds-proxy-connection-pooling) to make applications more scalable, more resilient to database failures, and more secure.
