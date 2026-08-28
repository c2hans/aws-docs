---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/monitoring-event-bridge-metrics.html
---

# Amazon CloudWatch Metrics for DRS
<a name="monitoring-event-bridge-metrics"></a>

The following are CloudWatch metrics for DRS:
+  **TotalSourceServerCount** - number of source servers
+  **LagDuration** - the age of the latest consistent snapshot, in seconds
+  **Backlog** - the amount of data yet to be synced, in bytes.
+  **DurationSinceLastSuccessfulRecoveryLaunch** - the amount of time that has passed since the last Drill or Recovery instance launch in seconds.
+  **ElapsedReplicationDuration** - the cumulative amount of time this server has been replicating for in seconds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
