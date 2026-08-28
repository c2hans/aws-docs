---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-preparing.html
---

# Preparing for Ongoing Replication
<a name="chap-manageddatabases.postgresql-rds-postgresql-full-load-preparing"></a>

Before you start full load, make sure that you record the current log sequence number (LSN) as the starting position for ongoing replication. Use this LSN when you configure the ongoing replication task in AWS DMS.

To avoid data loss or duplication with hybrid approach, make sure of the following:
+ You create a replication slot on the source database before you start the full load using the following command:

  ```
  SELECT * FROM pg_create_logical_replication_slot('test_slot', 'test_decoding');
  ```
+ When you create a replication slot, your source database doesn’t have open transactions. To confirm, use the following command:

  ```
  SELECT * FROM pg_stat_activity where state <> 'idle';
  ```
+ If you have open transactions, wait for them to complete or cancel them.

To capture the LSN, use the following command.

```
SELECT slot_name, confirmed_flush_lsn from pg_replication_slots where slot_name like 'test_slot';

slot_name | confirmed_flush_lsn
test_slot | 12/68000000
```

From the output of the preceding command, copy the `confirmed_flush_lsn` value. In the example preceding, this value is set to `12/68000000`. After you complete the full load, you can use this value as the start position for the AWS DMS task.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
