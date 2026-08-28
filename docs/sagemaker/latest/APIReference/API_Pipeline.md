---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Pipeline.html
---

# Pipeline
<a name="API_Pipeline"></a>

A SageMaker Model Building Pipeline instance.

## Contents
<a name="API_Pipeline_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-Pipeline-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-Pipeline-CreationTime"></a>
The creation time of the pipeline.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-Pipeline-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-Pipeline-LastModifiedTime"></a>
The time that the pipeline was last modified.
Type: Timestamp
Required: No

 ** LastRunTime **   <a name="sagemaker-Type-Pipeline-LastRunTime"></a>
The time when the pipeline was last run.
Type: Timestamp
Required: No

 ** ParallelismConfiguration **   <a name="sagemaker-Type-Pipeline-ParallelismConfiguration"></a>
The parallelism configuration applied to the pipeline.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** PipelineArn **   <a name="sagemaker-Type-Pipeline-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: No

 ** PipelineDescription **   <a name="sagemaker-Type-Pipeline-PipelineDescription"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** PipelineDisplayName **   <a name="sagemaker-Type-Pipeline-PipelineDisplayName"></a>
The display name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** PipelineName **   <a name="sagemaker-Type-Pipeline-PipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** PipelineStatus **   <a name="sagemaker-Type-Pipeline-PipelineStatus"></a>
The status of the pipeline.
Type: String
Valid Values: `Active | Deleting`
Required: No

 ** RoleArn **   <a name="sagemaker-Type-Pipeline-RoleArn"></a>
The Amazon Resource Name (ARN) of the role that created the pipeline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Tags **   <a name="sagemaker-Type-Pipeline-Tags"></a>
A list of tags that apply to the pipeline.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Pipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Pipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Pipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Pipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
