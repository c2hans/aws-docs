---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-clusters.html
---

# Clusters in AWS CloudHSM
<a name="manage-clusters"></a>

A cluster is a collection of individual hardware security modules (HSM) that AWS CloudHSM keeps in sync. When you perform a task or operation on one HSM in a cluster, the other HSMs in that cluster are automatically kept up to date.

You can manage your AWS CloudHSM clusters from the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/) or one of the [AWS SDKs or command line tools](https://aws.amazon.com/tools/). For more information, see the following topics.

To create a cluster, see [Getting started](getting-started.md).

The following topics provide more information about clusters.

**Topics**
+ [Cluster architecture](cluster-architecture.md)
+ [Cluster synchronization](cluster-synchronization.md)
+ [Cluster high availability and load balancing](cluster-high-availability-load-balancing.md)
+ [Cluster modes](cluster-hsm-types.md)
+ [HSM types](hsm-types.md)
+ [Connecting to the cluster](cluster-connect.md)
+ [Scaling HSMs](add-remove-hsm.md)
+ [Deleting a cluster](delete-cluster.md)
+ [Creating clusters from backups](create-cluster-from-backup.md)
+ [Migrating HSM cluster types](cluster-hsm-type-modification.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
