---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ImageBlock.html
---

# ImageBlock
<a name="API_agent-runtime_ImageBlock"></a>

Image content for an invocation step.

## Contents
<a name="API_agent-runtime_ImageBlock_Contents"></a>

 ** format **   <a name="bedrock-Type-agent-runtime_ImageBlock-format"></a>
The format of the image.
Type: String
Valid Values: `png | jpeg | gif | webp`
Required: Yes

 ** source **   <a name="bedrock-Type-agent-runtime_ImageBlock-source"></a>
The source for the image.
Type: [ImageSource](API_agent-runtime_ImageSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_agent-runtime_ImageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ImageBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ImageBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ImageBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
