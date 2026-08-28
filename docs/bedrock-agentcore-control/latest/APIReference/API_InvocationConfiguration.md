---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_InvocationConfiguration.html
---

# InvocationConfiguration
<a name="API_InvocationConfiguration"></a>

The configuration to invoke a self-managed memory processing pipeline with.

## Contents
<a name="API_InvocationConfiguration_Contents"></a>

 ** payloadDeliveryBucketName **   <a name="bedrockagentcorecontrol-Type-InvocationConfiguration-payloadDeliveryBucketName"></a>
The S3 bucket name for event payload delivery.
Type: String
Required: Yes

 ** topicArn **   <a name="bedrockagentcorecontrol-Type-InvocationConfiguration-topicArn"></a>
The ARN of the SNS topic for job notifications.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## See Also
<a name="API_InvocationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InvocationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InvocationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InvocationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
