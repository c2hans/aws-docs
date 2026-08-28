---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-detaching.html
---

# Removing a DB cluster from a Neptune global database
<a name="neptune-gdb-detaching"></a>

There are several reasons you might want to remove a DB cluster from a global database. For example:
+ If the primary cluster becomes degraded or isolated, you can remove it from the global database and it becomes a standalone provisioned cluster that can be used to create a new global database (see [Detach-and-promote a Neptune global database in the case of an unplanned outage](neptune-gdb-disaster-recovery.md#neptune-gdb-detach-and-promote)).
+ If you want to delete a global database, first you have to you remove (detach) all associated clusters from it, leaving the primary for last (see [Deleting a Neptune global database](neptune-gdb-deleting.md).

You can use the [remove-from-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/remove-from-global-cluster.html) CLI command (which wraps the [RemoveFromGlobalCluster](api-global-dbs.md#RemoveFromGlobalCluster) API) to detach a Neptune DB cluster from a global database:

```
aws neptune remove-from-global-cluster \
  --region {{(region of the cluster to remove)}} \
  --global-cluster-identifier {{(global database ID)}} \
  --db-cluster-identifier {{(ARN of the cluster to remove)}}
```

The detached DB cluster then becomes a standalone DB cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
