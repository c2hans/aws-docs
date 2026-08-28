---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/use-custom-model-on-demand.html
---

# Use a deployment for on-demand inference
<a name="use-custom-model-on-demand"></a>

After you deploy your custom model for on-demand inference, you can use it to generate responses by making inference requests. For `InvokeModel` or `Converse` operations, you use the deployment Amazon Resource Name (ARN) as the `modelId`.

For information about making inference requests, see the following topics:
+ [Submit prompts and generate responses with model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)
+ [Prerequisites for running model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-prereq.html)
+ [Submit prompts and generate responses using the API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-api.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
