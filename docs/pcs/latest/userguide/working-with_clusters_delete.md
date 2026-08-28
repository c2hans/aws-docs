---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_delete.html
---

# Deleting a cluster in AWS PCS
<a name="working-with_clusters_delete"></a>

This topic provides an overview of how to delete an AWS PCS cluster.

## Considerations when deleting an AWS PCS cluster
<a name="working-with_clusters_delete_considerations"></a>
+  All queues associated with the cluster must be deleted before the cluster can be deleted. For more information, see [Deleting a queue in AWS PCS](working-with_queues_delete.md).
+  All compute node groups associated with the cluster must be deleted before the cluster can be deleted. For more information, see [Deleting a compute node group in AWS PCS](working-with_cng_delete.md).

## Delete the cluster
<a name="working-with_clusters_delete_methods"></a>

You can use the AWS Management Console or AWS CLI to delete a cluster.

------
#### [ AWS Management Console ]

**To delete a cluster**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Select the cluster to delete.

1. Choose **Delete**.

1. The cluster **Status** field shows `Deleting`. It can take several minutes to complete.

------
#### [ AWS CLI ]

**To delete a cluster**

1.  Use the following command to delete a cluster, with these replacements:
   +  Replace {{region-code}} with the AWS Region your cluster is in.
   +  Replace {{my-cluster}} with the name or ID of your cluster.

   ```
   aws pcs delete-cluster --region {{region-code}} --cluster-identifier {{my-cluster}}
   ```

1.  It can take several minutes to delete the cluster. You can check the status of your cluster with the following command.

   ```
   aws pcs get-cluster --region {{region-code}} --cluster-identifier {{my-cluster}}
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
