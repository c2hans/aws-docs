---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-region-availability.html
---

# Nova Forge Region Availability
<a name="nova-forge-region-availability"></a>

Nova Forge is available in the following AWS Regions.

**Nova Forge Region Availability**

| Region | Limitations |
| --- | --- |
| US East (N. Virginia) | None |
| US West (Oregon) | Amazon Bedrock inference is not available in US West (Oregon). We recommend deploying your model using [SageMaker inference](nova-model-sagemaker-inference.md). Alternatively, you can copy your model to US East (N. Virginia) using [Amazon Bedrock model copy](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
