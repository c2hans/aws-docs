---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring-waits.html
---

# Wait events for Aurora PostgreSQL Limitless Database
<a name="limitless-monitoring-waits"></a>

A wait event in Aurora PostgreSQL indicates a resource for which a session is waiting, such as input/output (I/O) and locks. Wait events are helpful in finding out why sessions are waiting for resources, and identifying bottlenecks. For more information, see [Aurora PostgreSQL wait events](AuroraPostgreSQL.Tuning.concepts.md#AuroraPostgreSQL.Tuning.concepts.waits).

Aurora PostgreSQL Limitless Database has its own wait events that are related to routers and shards. Many of them are for routers waiting on shards to complete tasks. Shard wait events contain details on tasks that are being performed.

**Topics**
+ [Querying for wait events](#limitless-monitoring-waits.query)
+ [Limitless Database wait events](limitless-waits-reference.md)

## Querying for wait events
<a name="limitless-monitoring-waits.query"></a>

You can use the [limitless\_stat\_activity](limitless-monitoring-views.md#limitless_stat_activity) view to query for wait events, as shown in the following example.

```
SELECT wait_event FROM rds_aurora.limitless_stat_activity WHERE wait_event_type='AuroraLimitless';

      wait_event
----------------------
 RemoteStatementSetup
 RemoteStatementSetup
(2 rows)
```

You can also use the `aurora_stat_system_waits` function to list the number of waits and the total time spent on each wait event, as shown in the following example.

```
postgres_limitless=> SELECT type_name,event_name,waits,wait_time
    FROM aurora_stat_system_waits()
    NATURAL JOIN aurora_stat_wait_event()
    NATURAL JOIN aurora_stat_wait_type()
    WHERE type_name='AuroraLimitless'
    ORDER BY wait_time DESC;

    type_name    |       event_name          |  waits  |  wait_time
-----------------+---------------------------+---------+-------------
 AuroraLimitless | RemoteStatementSetup      |    7518 | 75236507897
 AuroraLimitless | RemoteStatementExecution  |      40 |      132986
 AuroraLimitless | Connect                   |       5 |        1453
(3 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
