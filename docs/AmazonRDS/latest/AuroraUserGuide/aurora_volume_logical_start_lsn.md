---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_volume_logical_start_lsn.html
---

# aurora\_volume\_logical\_start\_lsn
<a name="aurora_volume_logical_start_lsn"></a>

Returns the log sequence number (LSN) used for identifying the beginning of a record in the logical write-ahead log (WAL) stream of the Aurora cluster volume.

## Syntax
<a name="aurora_volume_logical_start_lsn-syntax"></a>

```
aurora_volume_logical_start_lsn()
```

## Arguments
<a name="aurora_volume_logical_start_lsn-arguments"></a>

None

## Return type
<a name="aurora_volume_logical_start_lsn-return-type"></a>

`pg_lsn`

## Usage notes
<a name="aurora_volume_logical_start_lsn-usage-notes"></a>

This function identifies the beginning of the record in the logical WAL stream for a given Aurora cluster volume. You can use this function while performing major version upgrade using logical replication and Aurora fast cloning to determine the LSN at which a snapshot or database clone is taken. You can then use logical replication to continuously stream the newer data recorded after the LSN and synchronize the changes from publisher to subscriber.

For more information on using logical replication for a major version upgrade, see [Using logical replication to perform a major version upgrade for Aurora PostgreSQL](AuroraPostgreSQL.MajorVersionUpgrade.md).

This function is available on the following versions of Aurora PostgreSQL:
+ 15.2 and higher 15 versions
+ 14.3 and higher 14 versions
+ 13.6 and higher 13 versions
+ 12.10 and higher 12 versions
+ 11.15 and higher 11 versions
+ 10.20 and higher 10 versions

## Examples
<a name="aurora_volume_logical_start_lsn-examples"></a>

You can obtain the log sequence number (LSN) using the following query:

```
postgres=> SELECT aurora_volume_logical_start_lsn();

aurora_volume_logical_start_lsn
---------------
0/402E2F0
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
