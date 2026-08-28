---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-special-considerations.html
---

# Considerations
<a name="cluster-specific-configurations-special-considerations"></a>

When you're using a Amazon SageMaker HyperPod recipes, there are some factors that can impact the process of model training.
+ The `transformers` version must be `4.45.2` or greater for Llama 3.2. If you're using a Slurm or K8s workflow, the version is automatically updated.
+ Mixtral does not support 8-bit floating point precision (FP8)
+ Amazon EC2 p4 instance does not support FP8

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
