---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailConverseImageBlock.html
---

# GuardrailConverseImageBlock
<a name="API_runtime_GuardrailConverseImageBlock"></a>

An image block that contains images that you want to assess with a guardrail.

## Contents
<a name="API_runtime_GuardrailConverseImageBlock_Contents"></a>

 ** format **   <a name="bedrock-Type-runtime_GuardrailConverseImageBlock-format"></a>
The format details for the image type of the guardrail converse image block.
Type: String
Valid Values: `png | jpeg`
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_GuardrailConverseImageBlock-source"></a>
The image source (image bytes) of the guardrail converse image block.
Type: [GuardrailConverseImageSource](API_runtime_GuardrailConverseImageSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_runtime_GuardrailConverseImageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailConverseImageBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailConverseImageBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailConverseImageBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
