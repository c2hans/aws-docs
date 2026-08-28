---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pc-py-lib-api-fleet-update.html
---

# `update_compute_fleet`
<a name="pc-py-lib-api-fleet-update"></a>

```
update_compute_fleet(cluster_name, status, region)
```

Update the status of the cluster compute fleet.Parameters:

**`cluster_name` (required)**
The cluster name.

**`status` (required)**
The status to update to.
Valid values: `START_REQUESTED` \| `STOP_REQUESTED` \| `ENABLED` \| `DISABLED`

**`region`**
The cluster AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
