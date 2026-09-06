---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceRecommendationsJob.html
---

# InferenceRecommendationsJob
<a name="API_InferenceRecommendationsJob"></a>

A structure that contains a list of recommendation jobs.

## Contents
<a name="API_InferenceRecommendationsJob_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-InferenceRecommendationsJob-CreationTime"></a>
A timestamp that shows when the job was created.
Type: Timestamp
Required: Yes

 ** JobArn **   <a name="sagemaker-Type-InferenceRecommendationsJob-JobArn"></a>
The Amazon Resource Name (ARN) of the recommendation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-recommendations-job/.*`
Required: Yes

 ** JobDescription **   <a name="sagemaker-Type-InferenceRecommendationsJob-JobDescription"></a>
The job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** JobName **   <a name="sagemaker-Type-InferenceRecommendationsJob-JobName"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** JobType **   <a name="sagemaker-Type-InferenceRecommendationsJob-JobType"></a>
The recommendation job type.
Type: String
Valid Values: `Default | Advanced`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-InferenceRecommendationsJob-LastModifiedTime"></a>
A timestamp that shows when the job was last modified.
Type: Timestamp
Required: Yes

 ** RoleArn **   <a name="sagemaker-Type-InferenceRecommendationsJob-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** Status **   <a name="sagemaker-Type-InferenceRecommendationsJob-Status"></a>
The status of the job.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | STOPPING | STOPPED | DELETING | DELETED`
Required: Yes

 ** CompletionTime **   <a name="sagemaker-Type-InferenceRecommendationsJob-CompletionTime"></a>
A timestamp that shows when the job completed.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-InferenceRecommendationsJob-FailureReason"></a>
If the job fails, provides information why the job failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ModelName **   <a name="sagemaker-Type-InferenceRecommendationsJob-ModelName"></a>
The name of the created model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** ModelPackageVersionArn **   <a name="sagemaker-Type-InferenceRecommendationsJob-ModelPackageVersionArn"></a>
The Amazon Resource Name (ARN) of a versioned model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** SamplePayloadUrl **   <a name="sagemaker-Type-InferenceRecommendationsJob-SamplePayloadUrl"></a>
The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_InferenceRecommendationsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceRecommendationsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceRecommendationsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceRecommendationsJob)
