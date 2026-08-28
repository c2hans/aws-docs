---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-modifying.html
---

# Modifying a Neptune global database
<a name="neptune-gdb-modifying"></a>

The DB cluster parameter groups can be configured independently for each Neptune DB cluster in a global database, but it's best to keep settings consistent across the clusters to avoid unexpected behavior changes if a secondary cluster has to be promoted to primary.

You can modify the settings of the global database itself using the [modify-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/neptune/modify-global-cluster.html) CLI command (which wraps the [ModifyGlobalCluster](api-global-dbs.md#ModifyGlobalCluster) API). For example, you could change the global database identifier and at the same time turn off deletion protection like this:

```
aws neptune modify-global-cluster \
  --region {{(region of the DB cluster to modify)}} \
  --global-cluster-identifier {{(current global database ID)}} \
  --new-global-cluster-identifier {{(new global database ID to assign)}} \
  --no-deletion-protection
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
