---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-delete-cluster.html
---

# Deleting a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-eks-operate-cli-command-delete-cluster"></a>

Run [delete-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/delete-cluster.html) to delete a cluster. You can specify either the name or the ARN of the cluster.

```
aws sagemaker delete-cluster --cluster-name {{your-hyperpod-cluster}}
```

This API only cleans up the SageMaker HyperPod resources and doesn’t delete any resources of the associated EKS cluster. This includes the Amazon EKS cluster, EKS Pod identities, Amazon FSx volumes, and EKS add-ons. This also includes the initial configuration you added to your EKS cluster. If you want to clean up all resources, make sure that you also clean up the EKS resources separately.

Make sure that you first delete the SageMaker HyperPod resources, followed by the EKS resources. Performing the deletion in the reverse order may result in lingering resources.

**Important**
When this API is called, SageMaker HyperPod doesn’t drain or redistribute the jobs (Pods) running on the nodes. Make sure to check if there are any jobs running on the nodes before calling this API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
