---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineSummary.html
---

# PipelineSummary
<a name="API_PipelineSummary"></a>

A summary of a pipeline.

## Contents
<a name="API_PipelineSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-PipelineSummary-CreationTime"></a>
The creation time of the pipeline.
Type: Timestamp
Required: No

 ** LastExecutionTime **   <a name="sagemaker-Type-PipelineSummary-LastExecutionTime"></a>
The last time that a pipeline execution began.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-PipelineSummary-LastModifiedTime"></a>
The time that the pipeline was last modified.
Type: Timestamp
Required: No

 ** PipelineArn **   <a name="sagemaker-Type-PipelineSummary-PipelineArn"></a>
 The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: No

 ** PipelineDescription **   <a name="sagemaker-Type-PipelineSummary-PipelineDescription"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** PipelineDisplayName **   <a name="sagemaker-Type-PipelineSummary-PipelineDisplayName"></a>
The display name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** PipelineName **   <a name="sagemaker-Type-PipelineSummary-PipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** RoleArn **   <a name="sagemaker-Type-PipelineSummary-RoleArn"></a>
The Amazon Resource Name (ARN) that the pipeline used to execute.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_PipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineSummary)
