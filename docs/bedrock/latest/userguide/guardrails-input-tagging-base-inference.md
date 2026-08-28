---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-input-tagging-base-inference.html
---

# Use your guardrail with inference operations to evaluate user input
<a name="guardrails-input-tagging-base-inference"></a>

You can use guardrails with the base inference operations, [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) (streaming). This section covers how you selectively evaluate user input and how you can configure streaming response behavior. Note that for conversational applications, you can achieve the same results with the [Converse API](guardrails-use-converse-api.md).

For example code that calls the base inference operations, see [Submit a single prompt with InvokeModel](inference-invoke.md). For information about using a guardrail with the base inference operations, follow the steps in the API tab of [Test your guardrail](guardrails-test.md).

**Topics**
+ [Apply tags to user input to filter content](guardrails-tagging.md)
+ [Configure streaming response behavior to filter content](guardrails-streaming.md)
+ [Include a guardrail with the Converse API](guardrails-use-converse-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
