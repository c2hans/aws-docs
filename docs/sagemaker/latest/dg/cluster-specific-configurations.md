---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations.html
---

# Cluster-specific configurations
<a name="cluster-specific-configurations"></a>

SageMaker HyperPod offers flexibility in running training jobs across different cluster environments. Each environment has its own configuration requirements and setup process. This section outlines the steps and configurations needed for running training jobs in SageMaker HyperPod Slurm, SageMaker HyperPod k8s, and SageMaker training jobs. Understanding these configurations is crucial for effectively leveraging the power of distributed training in your chosen environment.

You can use a recipe in the following cluster environments:
+ SageMaker HyperPod Slurm Orchestration
+ SageMaker HyperPod Amazon Elastic Kubernetes Service Orchestration
+ SageMaker training jobs

To launch a training job in a cluster, set and install the corresponding cluster configuration and environment.

**Topics**
+ [Running a training job on HyperPod Slurm](cluster-specific-configurations-run-training-job-hyperpod-slurm.md)
+ [Running a training job on HyperPod k8s](cluster-specific-configurations-run-training-job-hyperpod-k8s.md)
+ [Running a SageMaker training job](cluster-specific-configurations-run-sagemaker-training-job.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
