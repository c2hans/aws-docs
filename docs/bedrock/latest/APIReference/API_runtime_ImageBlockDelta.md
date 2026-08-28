---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ImageBlockDelta.html
---

# ImageBlockDelta
<a name="API_runtime_ImageBlockDelta"></a>

A streaming delta event that contains incremental image data during streaming responses.

## Contents
<a name="API_runtime_ImageBlockDelta_Contents"></a>

 ** error **   <a name="bedrock-Type-runtime_ImageBlockDelta-error"></a>
Error information if this image delta could not be processed.
Type: [ErrorBlock](API_runtime_ErrorBlock.md) object
Required: No

 ** source **   <a name="bedrock-Type-runtime_ImageBlockDelta-source"></a>
The incremental image source data for this delta event.
Type: [ImageSource](API_runtime_ImageSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_runtime_ImageBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ImageBlockDelta)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ImageBlockDelta)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ImageBlockDelta)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
