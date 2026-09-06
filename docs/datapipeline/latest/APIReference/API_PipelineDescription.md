---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PipelineDescription.html
---

# PipelineDescription
<a name="API_PipelineDescription"></a>

Contains pipeline metadata.

## Contents
<a name="API_PipelineDescription_Contents"></a>

 ** fields **   <a name="DP-Type-PipelineDescription-fields"></a>
A list of read-only fields that contain metadata about the pipeline: @userId, @accountId, and @pipelineState.
Type: Array of [Field](API_Field.md) objects
Required: Yes

 ** name **   <a name="DP-Type-PipelineDescription-name"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** pipelineId **   <a name="DP-Type-PipelineDescription-pipelineId"></a>
The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form `df-297EG78HU43EEXAMPLE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** description **   <a name="DP-Type-PipelineDescription-description"></a>
Description of the pipeline.
Type: String
Required: No

 ** tags **   <a name="DP-Type-PipelineDescription-tags"></a>
A list of tags to associated with a pipeline. Tags let you control access to pipelines. For more information, see [Controlling User Access to Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) in the *AWS Data Pipeline Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_PipelineDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/PipelineDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/PipelineDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/PipelineDescription)
