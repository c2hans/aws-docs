---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-modify.html
---

# Modify the tags for an application inference profile
<a name="inference-profiles-modify"></a>

After you create an application inference profile, you can still manage tags through the Amazon Bedrock API by submitting a [TagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_UntagResource.html) request with an [Amazon Bedrock control plane endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#br-cp) and specifying the ARN of the application inference profile in the `resourceArn` field. To learn more about tagging, see [Tagging Amazon Bedrock resources](tagging.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
