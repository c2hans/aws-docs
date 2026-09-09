---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgePackagingJobSummary.html
---

# EdgePackagingJobSummary
<a name="API_EdgePackagingJobSummary"></a>

Summary of edge packaging job.

## Contents
<a name="API_EdgePackagingJobSummary_Contents"></a>

 ** EdgePackagingJobArn **   <a name="sagemaker-Type-EdgePackagingJobSummary-EdgePackagingJobArn"></a>
The Amazon Resource Name (ARN) of the edge packaging job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-packaging-job/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** EdgePackagingJobName **   <a name="sagemaker-Type-EdgePackagingJobSummary-EdgePackagingJobName"></a>
The name of the edge packaging job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EdgePackagingJobStatus **   <a name="sagemaker-Type-EdgePackagingJobSummary-EdgePackagingJobStatus"></a>
The status of the edge packaging job.
Type: String
Valid Values: `STARTING | INPROGRESS | COMPLETED | FAILED | STOPPING | STOPPED`
Required: Yes

 ** CompilationJobName **   <a name="sagemaker-Type-EdgePackagingJobSummary-CompilationJobName"></a>
The name of the SageMaker Neo compilation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelName **   <a name="sagemaker-Type-EdgePackagingJobSummary-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelVersion **   <a name="sagemaker-Type-EdgePackagingJobSummary-ModelVersion"></a>
The version of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: No

## See Also
<a name="API_EdgePackagingJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgePackagingJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgePackagingJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgePackagingJobSummary)
