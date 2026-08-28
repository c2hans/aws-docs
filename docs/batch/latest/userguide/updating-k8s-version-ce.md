---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/updating-k8s-version-ce.html
---

# Update the Kubernetes version of the compute environment
<a name="updating-k8s-version-ce"></a>

With AWS Batch, you can update the Kubernetes version of a compute environment to support Amazon EKS cluster upgrades. The Kubernetes version of a compute environment is the Amazon EKS AMI version for the Kubernetes nodes that AWS Batch launches to run jobs. You can perform a Kubernetes version upgrade on their Amazon EKS nodes before or after you update the version of Amazon EKS cluster's control-plane. We recommend that you update the nodes after upgrading the control plane. For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.

To upgrade the Kubernetes version of a compute environment, use the [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) API operation.

```
$ aws batch update-compute-environment \
    --compute-environment {{<compute-environment-name>}} \
    --compute-resources \
      'ec2Configuration=[{imageType=EKS_AL2023,imageKubernetesVersion={{1.36}}}]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
