---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-logs-cluster-stack-log-streams.html
---

# `list_cluster_log_streams`
<a name="pc-py-lib-api-logs-cluster-stack-log-streams"></a>

```
list_cluster_log_streams(cluster_name, region, filters, next_token)
```

List log streams for a given cluster.Parameters:

**`cluster_name` (required)**
The cluster name.

**`region`**
The cluster AWS Region.

**`filters`**
Filters the cluster log streams.
Format: `'Name=a,Values=1 Name=b,Values=2,3'`
**Accepted filters:**
**code-dns-name**
The short form of the private DNS name of the instance; for example, `ip-10-0-0-101`.
**node-type**
The node type.
Valid values: `HeadNode`

**`next_token`**
The token for the next set of results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
