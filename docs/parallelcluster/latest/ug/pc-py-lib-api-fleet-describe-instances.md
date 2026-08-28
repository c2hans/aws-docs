---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-fleet-describe-instances.html
---

# `describe_cluster_instances`
<a name="pc-py-lib-api-fleet-describe-instances"></a>

```
describe_cluster_instances(cluster_name, region, next_token, node_type, queue_name)
```

Describe a cluster's instances.Parameters:

**`cluster_name` (required)**
The cluster name.

**`region`**
The cluster AWS Region.

**`next_token`**
The token for the next set of results.

**`node_type`**
Filters the instances by `node_type`.
Valid values: `HeadNode` \| `ComputeNode`

**`queue_name`**
Filters the instances by queue name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
