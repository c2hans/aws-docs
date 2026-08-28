---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_delete.html
---

# Deleting a compute node group in AWS PCS
<a name="working-with_cng_delete"></a>

This topic provides an overview of available options and describes what to consider when you delete an compute node group in AWS PCS.

## Considerations when deleting a compute node group
<a name="working-with_cng_delete_considerations"></a>

 Compute node groups define EC2 instances that are used to process jobs, provide interactive shell access, and other tasks. They are often associated with one or more AWS PCS queues. Before you delete a compute node group, consider the following:
+ Any EC2 instances launched by the compute node group will be terminated. This will cancel jobs that are running on these instances, and terminate running interactive processes.
+  You must disassociate the compute node group from all queues before you can delete it. For more information, see [Updating an AWS PCS queue](working-with_queues_update.md).

## Delete the compute node group
<a name="working-with_cng_delete_methods"></a>

You can use the AWS Management Console or AWS CLI to delete a compute node group.

------
#### [ AWS Management Console ]

**To delete a compute node group**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Select the cluster of the compute node group.

1. Navigate to **Compute node groups** and select the compute node group to delete.

1. Choose **Delete**.

1. The **Status** field shows `Deleting`. It can take several minutes to complete.

**Note**
You can use commands native to your scheduler to confirm that the compute node group is deleted. For example, use `sinfo` or `squeue` for Slurm.

------
#### [ AWS CLI ]

**To delete a compute node group**
+ Use the following command to delete a compute node group, with these replacements:
  +  Replace {{region-code}} with the AWS Region your cluster is in.
  +  Replace {{my-node-group}} with the name or ID of your compute node group.
  +  Replace {{my-cluster}} with the name or ID of your cluster.

  ```
  aws pcs delete-compute-node-group --region {{region-code}} \
         --compute-node-group-identifier {{my-node-group}} \
         --cluster-identifier {{my-cluster}}
  ```

   It can take several minutes to delete the compute node group.
**Note**
You can use commands native to your scheduler to confirm that the compute node group is deleted. For example, use `sinfo` or `squeue` for Slurm.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
