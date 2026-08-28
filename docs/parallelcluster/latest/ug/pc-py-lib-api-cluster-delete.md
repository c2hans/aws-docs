---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-cluster-delete.html
---

# `delete_cluster`
<a name="pc-py-lib-api-cluster-delete"></a>

```
delete_cluster(cluster_name, region, wait)
```

Delete a cluster in a given Region.Parameters:

**`cluster_name` (required)**
The cluster name.

**`region`**
The cluster AWS Region.

**`wait`**
If set to `True`, waits for the operation to complete. The default is `False`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
