---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineVersionSummary.html
---

# PipelineVersionSummary
<a name="API_PipelineVersionSummary"></a>

The summary of the pipeline version.

## Contents
<a name="API_PipelineVersionSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-PipelineVersionSummary-CreationTime"></a>
The creation time of the pipeline version.
Type: Timestamp
Required: No

 ** LastExecutionPipelineExecutionArn **   <a name="sagemaker-Type-PipelineVersionSummary-LastExecutionPipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the most recent pipeline execution created from this pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: No

 ** PipelineArn **   <a name="sagemaker-Type-PipelineVersionSummary-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: No

 ** PipelineVersionDescription **   <a name="sagemaker-Type-PipelineVersionSummary-PipelineVersionDescription"></a>
The description of the pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** PipelineVersionDisplayName **   <a name="sagemaker-Type-PipelineVersionSummary-PipelineVersionDisplayName"></a>
The display name of the pipeline version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** PipelineVersionId **   <a name="sagemaker-Type-PipelineVersionSummary-PipelineVersionId"></a>
The ID of the pipeline version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_PipelineVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
