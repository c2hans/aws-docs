---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-mtrl-quotas.html
---

# Quotas
<a name="model-customize-mtrl-quotas"></a>

The following quotas apply to multi-turn reinforcement learning jobs. These quotas are adjustable. To request an increase, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas). For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

| Quota | Default value | Adjustable |
| --- | --- | --- |
| Maximum number of concurrent multi-turn reinforcement fine tuning jobs | 1 | Yes |
| Maximum number of concurrent multi-turn reinforcement evaluation jobs | 1 | Yes |

API throttling limits for `CreateJob`, `DescribeJob`, and other management APIs are not adjustable. For the full list of Amazon SageMaker AI quotas, see [Amazon SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) in the *AWS General Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
