---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/update-workers.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Update self-managed nodes for your cluster
<a name="update-workers"></a>

When a new Amazon EKS optimized AMI is released, consider replacing the nodes in your self-managed node group with the new AMI. Likewise, if you have updated the Kubernetes version for your Amazon EKS cluster, update the nodes to use nodes with the same Kubernetes version.

**Important**
This topic covers node updates for self-managed nodes. If you are using [managed node groups](managed-node-groups.md), see [Update a managed node group for your cluster](update-managed-node-group.md).

There are two basic ways to update self-managed node groups in your clusters to use a new AMI:

 ** [Migrate applications to a new node group](migrate-stack.md) **
Create a new node group and migrate your Pods to that group. Migrating to a new node group is more graceful than simply updating the AMI ID in an existing AWS CloudFormation stack. This is because the migration process [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) the old node group as `NoSchedule` and drains the nodes after a new stack is ready to accept the existing Pod workload.

 ** [Update an AWS CloudFormation node stack](update-stack.md) **
Update the AWS CloudFormation stack for an existing node group to use the new AMI. This method isn’t supported for node groups that were created with `eksctl`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
