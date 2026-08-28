---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-cleanup.html
---

# Clean up an AWS PCS cluster in CloudFormation
<a name="get-started-cfn-cleanup"></a>

If you used CloudFormation to create your AWS PCS cluster, you can open the [CloudFormation console](https://console.aws.amazon.com/cloudformation) and delete the stack to delete the cluster and all its associated resources.

**Important**
For the sample cluster, if you created additional compute node groups or queues in your cluster (beyond the `login` and `compute-1` groups that the sample CloudFormation template created), you must use the [AWS PCS console](https://console.aws.amazon.com/pcs) or AWS CLI to delete those resources before you delete the CloudFormation stack. For more information, see [Deleting a cluster in AWS PCS](working-with_clusters_delete.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
