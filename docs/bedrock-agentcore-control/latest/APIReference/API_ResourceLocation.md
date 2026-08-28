---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ResourceLocation.html
---

# ResourceLocation
<a name="API_ResourceLocation"></a>

The location of a resource.

## Contents
<a name="API_ResourceLocation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="bedrockagentcorecontrol-Type-ResourceLocation-s3"></a>
The Amazon S3 location for storing data. This structure defines where in Amazon S3 data is stored.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_ResourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ResourceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ResourceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ResourceLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
