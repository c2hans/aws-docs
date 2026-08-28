---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-delete.html
---

# Delete an application inference profile
<a name="inference-profiles-delete"></a>

If you no longer need an application inference profile, you can delete it. You can only delete inference profiles through the Amazon Bedrock API.

To delete an inference profile, send a [DeleteInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteInferenceProfiles.html) request with an [Amazon Bedrock control plane endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#br-cp) and specify the Amazon Resource Name (ARN) or ID of the inference profile to delete in the `inferenceProflieIdentifier` field.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
