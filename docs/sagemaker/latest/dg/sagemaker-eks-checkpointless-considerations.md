---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-considerations.html
---

# Special considerations
<a name="sagemaker-eks-checkpointless-considerations"></a>

We collect certain routine aggregated and anonymized operational metrics to provide essential service availability. The creation of these metrics is fully automated and does not involve human review of the underlying model training workload. These metrics relate to job operations, resource management, and essential service functionality.

HyperPod managed tiered checkpointing and elastic training: note that HyperPod checkpointless training is currently incompatible with HyperPod managed tiered checkpointing and elastic training.

Checkpointless training recipes for GPT OSS 120B and Llama models are provided to simplify getting started. These recipes have been verified on ml.p5 instances. Using other instance types may require additional modifications to the underlying recipes. These recipes can be adapted to full finetuning workflows as well. For custom models, we recommend reviewing the [getting started examples](https://docs.aws.amazon.com/sagemaker-eks-checkpointless-recipes-custom).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
