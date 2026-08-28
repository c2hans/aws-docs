---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloned-clusters.html
---

# Cloned clusters in AWS CloudHSM
<a name="cloned-clusters"></a>

Use CloudHSM CLI to synchronize a cluster in a remote region, *if the cluster in that region was originally created from the backup of a cluster in another region*. Let's say you copied a cluster to another region (destination) and then later you want to synchronize changes from the original cluster (source). In scenarios like this, you use the [key replicate](cloudhsm_cli-key-replicate.md) and [user replicate](cloudhsm_cli-user-replicate.md) commands to synchronize the clusters. If you haven't installed CloudHSM CLI, see the instructions in [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md).

## Related topics
<a name="clone-cluster-related"></a>
+ [user replicate](cloudhsm_cli-user-replicate.md)
+ [key replicate](cloudhsm_cli-key-replicate.md)
+ [Copying Backups Across Regions](copy-backup-to-region.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
