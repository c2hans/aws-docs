---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_KinesisResource.html
---

# KinesisResource
<a name="API_KinesisResource"></a>

Configuration for Kinesis Data Stream delivery.

## Contents
<a name="API_KinesisResource_Contents"></a>

 ** contentConfigurations **   <a name="bedrockagentcorecontrol-Type-KinesisResource-contentConfigurations"></a>
Content configurations for stream delivery.
Type: Array of [ContentConfiguration](API_ContentConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** dataStreamArn **   <a name="bedrockagentcorecontrol-Type-KinesisResource-dataStreamArn"></a>
ARN of the Kinesis Data Stream.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## See Also
<a name="API_KinesisResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/KinesisResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/KinesisResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/KinesisResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
