---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/deletion-protection.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Protect EKS clusters from accidental deletion
<a name="deletion-protection"></a>

Accidentally deleting an EKS cluster may impair Kubernetes cluster operations.

You can now protect EKS clusters from accidental deletion. If you enable deletion protection on a cluster, you must first disable deletion protection before you can delete the cluster.

The purpose of deletion protection is to prevent accidents. You should carefully restrict who is authorized to delete clusters.

If you try to delete an active cluster that has deletion protection turned on, you will receive an `InvalidRequestException`.

**Important**
If you enable deletion protection on a cluster, you must have **both** the UpdateClusterConfig and DeleteCluster IAM permissions to first remove the deletion protection, and finally delete the cluster.

**Note**
If the cluster state is creating, failed, or deleting, you can delete the cluster even if deletion protection is turned on.

## To enable deletion protection for an existing cluster
<a name="_to_enable_deletion_protection_for_an_existing_cluster"></a>

You can only run this on a cluster in the active status.

```
aws eks update-cluster-config --name <cluster-name> --region <aws-region> --deletion-protection
```

## To disable deletion protection for an existing cluster
<a name="_to_disable_deletion_protection_for_an_existing_cluster"></a>

```
aws eks update-cluster-config --name <cluster-name> --region <aws-region> --no-deletion-protection
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
