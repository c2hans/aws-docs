---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-v3-on-node-updated.html
---

# Cluster update failed on `onNodeUpdated` custom action
<a name="troubleshooting-v3-on-node-updated"></a>

When a [`HeadNode`](HeadNode-v3.md) / [`CustomActions`](HeadNode-v3.md#HeadNode-v3-CustomActions) / [`OnNodeUpdated`](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated) script fails, the update fails and the script is not run at rollback time. It's your responsibility to manually perform the cleanups needed after the rollback is completed. For example, if the `OnNodeUpdated` script changes the status of a field in a configuration file (for example, from `true` to `false`) and then fails, you need to manually restore that field value to the pre-update state (for example, `false` to `true`). For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
