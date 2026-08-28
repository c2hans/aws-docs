---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.monitoring.html
---

# Monitoring MemoryDB Multi-Region
<a name="multi-Region.monitoring"></a>

You can use Amazon CloudWatch to monitor the behavior and performance of a Multi-Region cluster. MemoryDB publishes the `MultiRegionClusterReplicationLag` metric for each regional cluster within the Multi-Region cluster.

`MultiRegionClusterReplicationLag` shows the elapsed time between when an update is written to the remote Multi-Region regional cluster multi-AZ transaction log, and when that update is written to the primary node in the local Multi-Region regional cluster. This metric is expressed in milliseconds, is emitted for every source- and destination-Region pair at shard level.

During normal operation, `MultiRegionClusterReplicationLag` should be fairly constant. An elevated value for `MultiRegionClusterReplicationLag` could indicate that updates from one regional cluster are not propagating to other regional clusters in a timely manner. Over time, this could result in other regional clusters *falling behind* because they no longer receive updates consistently.

`MultiRegionClusterReplicationLag` can increase if an AWS Region becomes isolated or degraded and you have a regional cluster in that Region. In this case, you can temporarily redirect your application's read and write activity to a different healthy AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
