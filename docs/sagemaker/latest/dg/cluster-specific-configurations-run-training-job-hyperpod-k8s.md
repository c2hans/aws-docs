---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-run-training-job-hyperpod-k8s.html
---

# Running a training job on HyperPod k8s
<a name="cluster-specific-configurations-run-training-job-hyperpod-k8s"></a>

SageMaker HyperPod Recipes supports submitting a training job to a GPU/Trainium Kubernetes cluster. Before you submit the training job do one of the following:
+ Modify the `k8s.yaml` cluster configuration file
+ Override the cluster configuration through the command line

After you've done either of the preceding steps, install the corresponding environment.

## Configure the cluster using `k8s.yaml`
<a name="cluster-specific-configurations-configure-cluster-k8s-yaml"></a>

To submit a training job to a Kubernetes cluster, you specify Kubernetes-specific configurations. The configurations include the cluster namespace or the location of the persistent volume.

```
pullPolicy: Always
restartPolicy: Never
namespace: default
persistent_volume_claims:
  - null
```

1. `pullPolicy`: You can specify the pull policy when you submit a training job. If you specify "Always," the Kubernetes cluster always pulls your image from the repository. For more information, see [Image pull policy](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy).

1. `restartPolicy`: Specify whether to restart your training job if it fails.

1. `namespace`: You can specify the Kubernetes namespace where you're submitting the training job.

1. `persistent_volume_claims`: You can specify a shared volume for your training job for all training processes to access the files in the volume.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
