---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-managing.html
---

# Managing an Amazon Neptune global database
<a name="neptune-gdb-managing"></a>

With the exception of the managed planned failover process, you perform most management operations on the individual clusters that make up a Neptune global database. The managed planned failover process is available only to Neptune global databases, not to individual Neptune DB clusters. To learn more, see [Performing managed planned failovers for Neptune global databases](neptune-gdb-disaster-recovery.md#neptune-gdb-managed-failover).

To recover a Neptune global database from an unplanned outage in its primary region, see [Detach-and-promote a Neptune global database in the case of an unplanned outage](neptune-gdb-disaster-recovery.md#neptune-gdb-detach-and-promote).

Although you can configure the DB cluster parameter groups independently for each Neptune cluster in a global database, it is best to keep settings consistent among all the clusters to avoid unexpected behavior changes if a secondary cluster is promoted to be the primary. For example, use the same settings for object indexes, streams, and so forth in all the DB clusters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
