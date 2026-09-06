---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/cross-region-aurora-replicas.html
---

# Cross-Region Aurora Replicas
<a name="cross-region-aurora-replicas"></a>

With Amazon Aurora MySQL-Compatible Edition clusters, you can use cross-Region Aurora Replicas to create a replica of your primary DB cluster in another AWS Region by using the database engine native replication mechanism. Aurora MySQL-Compatible Edition uses binary log (binlog) replication. This kind of replication is based on the change data capture (CDC) process. CDC identifies and tracks changes to data in a database. Changes to the database on the primary are recorded in a change log file, which is transferred to the machine that runs the Aurora Replica in the second Region. A process on the secondary machine reads these change logs and generates SQL statements that are then applied to the secondary database.

The following diagram shows the high-level architecture of a cross-Region Aurora Replica.

![Description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/images/guide-img/51785086-3f1b-4c1a-91fa-c2aba26e3f1a/images/a7132127-d9e9-40f5-ae3f-774138a04313.png)

The diagram shows the following transaction flow:

1. Transactions are committed on the primary Aurora clusters.

1. A process records these changes on the source by using the binlog dump thread, which writes them to a binary log file.

1. A replication agent sends the change logs through an I/O thread to relay logs in the secondary Region.

1. A process reads the change logs, generates SQL statements, and applies the statements to the secondary Aurora cluster.

[Aurora MySQL-Compatible clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.AuroraMySQL) can have up to five read replicas created this way, each in a different Region. Aurora PostgreSQL-Compatible doesn't support cross-Region Aurora Replicas. However, for Aurora PostgreSQL DB clusters, you can use an [Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html).
