---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-browse-view-edit.html
---

# Browsing, viewing, and editing SageMaker HyperPod clusters
<a name="sagemaker-hyperpod-eks-operate-console-ui-browse-view-edit"></a>

Use the following instructions to browse, view, and edit SageMaker HyperPod clusters orchestrated by Amazon EKS in the SageMaker AI console.

**Topics**
+ [To browse your SageMaker HyperPod clusters](#sagemaker-hyperpod-eks-operate-console-ui-browse-clusters)
+ [To view details of each SageMaker HyperPod cluster](#sagemaker-hyperpod-eks-operate-console-ui-view-details-of-clusters)
+ [To edit a SageMaker HyperPod cluster](#sagemaker-hyperpod-eks-operate-console-ui-edit-clusters)

## To browse your SageMaker HyperPod clusters
<a name="sagemaker-hyperpod-eks-operate-console-ui-browse-clusters"></a>

Under **Clusters** on the SageMaker HyperPod page in the SageMaker AI console, all created clusters should be listed under the **Clusters** section, which provides a summary view of clusters, their ARNs, status, and creation time.

## To view details of each SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-eks-operate-console-ui-view-details-of-clusters"></a>

Under **Clusters** on the SageMaker HyperPod page in the SageMaker AI console, the cluster names are activated as links. Choose the cluster name link to see details of each cluster.

## To edit a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-eks-operate-console-ui-edit-clusters"></a>

1. Under **Clusters** in the main pane of the SageMaker HyperPod console, choose the cluster you want to update.

1. Select your cluster, and choose **Edit**.

1. In the **Edit <your-cluster>** page, you can edit the configurations of existing instance groups, add more instance groups, delete instance groups, and change tags for the cluster. After making changes, choose **Submit**.

   1. In the **Configure instance groups** section, you can add more instance groups by choosing **Create instance group**.

   1. In the **Configure instance groups** section, you can choose **Edit** to change its configuration or **Delete** to remove the instance group permanently.
**Important**
When deleting an instance group, consider the following points:
Your SageMaker HyperPod cluster must always maintain at least one instance group.
Ensure all critical data is backed up before removal.
The removal process cannot be undone.
**Note**
Deleting an instance group will terminate all compute resources associated with that group.

   1. In the **Tags** section, you can update tags for the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
