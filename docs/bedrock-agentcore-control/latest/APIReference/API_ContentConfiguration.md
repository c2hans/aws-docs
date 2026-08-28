---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ContentConfiguration.html
---

# ContentConfiguration
<a name="API_ContentConfiguration"></a>

Defines what content to stream and at what level of detail.

## Contents
<a name="API_ContentConfiguration_Contents"></a>

 ** type **   <a name="bedrockagentcorecontrol-Type-ContentConfiguration-type"></a>
Type of content to stream.
Type: String
Valid Values: `MEMORY_RECORDS`
Required: Yes

 ** level **   <a name="bedrockagentcorecontrol-Type-ContentConfiguration-level"></a>
Level of detail for streamed content.
Type: String
Valid Values: `METADATA_ONLY | FULL_CONTENT`
Required: No

## See Also
<a name="API_ContentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ContentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ContentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ContentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
