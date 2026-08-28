---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-structured-outputs.html
---

# Get validated JSON results from models
<a name="claude-messages-structured-outputs"></a>

You can use structured outputs with Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.5, and Claude Opus 4.6 through the Converse API ([Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)) or the InvokeModel API ([InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) or [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)) on the `bedrock-runtime` endpoint. Structured outputs is *not* supported on the Anthropic Messages API path on the `bedrock-mantle` endpoint (`https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`); the `output_config.format` parameter is rejected with a `400` error.

To learn more, see [Get validated JSON results from models](structured-output.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
