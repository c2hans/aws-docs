---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/db-clusters.html
---

# Managing Amazon DocumentDB clusters
<a name="db-clusters"></a>

To manage an Amazon DocumentDB cluster, you must have an IAM policy with the appropriate Amazon DocumentDB control plane permissions. These permissions allow you to create, modify, and delete clusters and instances. The `AmazonDocDBFullAccess` policy provides all the required permissions for administering an Amazon DocumentDB cluster.

The following topics show how to perform various tasks when working with Amazon DocumentDB clusters, including creating, deleting, modifying, connecting to, and viewing clusters.

**Topics**
+ [Understanding clusters](db-clusters-understanding.md)
+ [Cluster settings](db-cluster-parameters.md)
+ [Cluster storage configurations](db-cluster-storage-configs.md)
+ [Determining a cluster's status](db-cluster-status.md)
+ [Cluster lifecycle](db-cluster-life-cycle.md)
+ [Scaling clusters](db-cluster-manage-performance.md)
+ [Cloning a volume for a cluster](db-cluster-cloning.md)
+ [Understanding cluster fault tolerance](db-cluster-fault-tolerance.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
