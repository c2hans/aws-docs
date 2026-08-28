---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.distributed.html
---

# Distributed queries in Aurora PostgreSQL Limitless Database
<a name="limitless-query.distributed"></a>

Distributed queries run on a router and more than one shard. The query is received by one of the routers. The router creates and manages the distributed transaction, which is sent to the participating shards. The shards create a local transaction with the context provided by the router, and the query is run.

When the transaction is committed, the router uses an optimized two-phase commit protocol if needed, and time-based Multi Version Concurrency Control (MVCC) to provide [ACID](https://en.wikipedia.org/wiki/ACID) semantics in a distributed database system.

Time-based MVCC records the commit time for each transaction and uses the transaction start time to generate the data snapshot time. To identify whether a transaction is committed (visible) given a reader’s snapshot, the database compares its commit time with the snapshot time. If its commit time is less than the reader’s snapshot time, it is visible; otherwise, invisible. Under this protocol, you will always expect to see strongly consistent data on Aurora PostgreSQL Limitless Database.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
