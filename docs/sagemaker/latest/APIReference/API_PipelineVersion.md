---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineVersion.html
---

# PipelineVersion
<a name="API_PipelineVersion"></a>

The version of the pipeline.

## Contents
<a name="API_PipelineVersion_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-PipelineVersion-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-PipelineVersion-CreationTime"></a>
The creation time of the pipeline version.
Type: Timestamp
Required: No

 ** LastExecutedPipelineExecutionArn **   <a name="sagemaker-Type-PipelineVersion-LastExecutedPipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the most recent pipeline execution created from this pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: No

 ** LastExecutedPipelineExecutionDisplayName **   <a name="sagemaker-Type-PipelineVersion-LastExecutedPipelineExecutionDisplayName"></a>
The display name of the most recent pipeline execution created from this pipeline version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** LastExecutedPipelineExecutionStatus **   <a name="sagemaker-Type-PipelineVersion-LastExecutedPipelineExecutionStatus"></a>
The status of the most recent pipeline execution created from this pipeline version.
Type: String
Valid Values: `Executing | Stopping | Stopped | Failed | Succeeded`
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-PipelineVersion-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-PipelineVersion-LastModifiedTime"></a>
The time when the pipeline version was last modified.
Type: Timestamp
Required: No

 ** PipelineArn **   <a name="sagemaker-Type-PipelineVersion-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: No

 ** PipelineVersionDescription **   <a name="sagemaker-Type-PipelineVersion-PipelineVersionDescription"></a>
The description of the pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** PipelineVersionDisplayName **   <a name="sagemaker-Type-PipelineVersion-PipelineVersionDisplayName"></a>
The display name of the pipeline version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** PipelineVersionId **   <a name="sagemaker-Type-PipelineVersion-PipelineVersionId"></a>
The ID of the pipeline version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_PipelineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineVersion)
