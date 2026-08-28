---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html
---

# DescribeCompilationJob
<a name="API_DescribeCompilationJob"></a>

Returns information about a model compilation job.

To create a model compilation job, use [CreateCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html). To get information about multiple model compilation jobs, use [ListCompilationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html).

## Request Syntax
<a name="API_DescribeCompilationJob_RequestSyntax"></a>

```
{
   "CompilationJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCompilationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CompilationJobName](#API_DescribeCompilationJob_RequestSyntax) **   <a name="sagemaker-DescribeCompilationJob-request-CompilationJobName"></a>
The name of the model compilation job that you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeCompilationJob_ResponseSyntax"></a>

```
{
   "CompilationEndTime": number,
   "CompilationJobArn": "string",
   "CompilationJobName": "string",
   "CompilationJobStatus": "string",
   "CompilationStartTime": number,
   "CreationTime": number,
   "DerivedInformation": {
      "DerivedDataInputConfig": "string"
   },
   "FailureReason": "string",
   "InferenceImage": "string",
   "InputConfig": {
      "DataInputConfig": "string",
      "Framework": "string",
      "FrameworkVersion": "string",
      "S3Uri": "string"
   },
   "LastModifiedTime": number,
   "ModelArtifacts": {
      "S3ModelArtifacts": "string"
   },
   "ModelDigests": {
      "ArtifactDigest": "string"
   },
   "ModelPackageVersionArn": "string",
   "OutputConfig": {
      "CompilerOptions": "string",
      "KmsKeyId": "string",
      "S3OutputLocation": "string",
      "TargetDevice": "string",
      "TargetPlatform": {
         "Accelerator": "string",
         "Arch": "string",
         "Os": "string"
      }
   },
   "RoleArn": "string",
   "StoppingCondition": {
      "MaxPendingTimeInSeconds": number,
      "MaxRuntimeInSeconds": number,
      "MaxWaitTimeInSeconds": number
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeCompilationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompilationEndTime](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CompilationEndTime"></a>
The time when the model compilation job on a compilation job instance ended. For a successful or stopped job, this is when the job's model artifacts have finished uploading. For a failed job, this is when Amazon SageMaker AI detected that the job failed.
Type: Timestamp

 ** [CompilationJobArn](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CompilationJobArn"></a>
The Amazon Resource Name (ARN) of the model compilation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compilation-job/.*`

 ** [CompilationJobName](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CompilationJobName"></a>
The name of the model compilation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [CompilationJobStatus](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CompilationJobStatus"></a>
The status of the model compilation job.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`

 ** [CompilationStartTime](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CompilationStartTime"></a>
The time when the model compilation job started the `CompilationJob` instances.
You are billed for the time between this timestamp and the timestamp in the `CompilationEndTime` field. In Amazon CloudWatch Logs, the start time might be later than this time. That's because it takes time to download the compilation job, which depends on the size of the compilation job container.
Type: Timestamp

 ** [CreationTime](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-CreationTime"></a>
The time that the model compilation job was created.
Type: Timestamp

 ** [DerivedInformation](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-DerivedInformation"></a>
Information that SageMaker Neo automatically derived about the model.
Type: [DerivedInformation](API_DerivedInformation.md) object

 ** [FailureReason](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-FailureReason"></a>
If a model compilation job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [InferenceImage](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-InferenceImage"></a>
The inference image to use when compiling a model. Specify an image only if the target device is a cloud instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [InputConfig](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-InputConfig"></a>
Information about the location in Amazon S3 of the input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
Type: [InputConfig](API_InputConfig.md) object

 ** [LastModifiedTime](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-LastModifiedTime"></a>
The time that the status of the model compilation job was last modified.
Type: Timestamp

 ** [ModelArtifacts](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-ModelArtifacts"></a>
Information about the location in Amazon S3 that has been configured for storing the model artifacts used in the compilation job.
Type: [ModelArtifacts](API_ModelArtifacts.md) object

 ** [ModelDigests](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-ModelDigests"></a>
Provides a BLAKE2 hash value that identifies the compiled model artifacts in Amazon S3.
Type: [ModelDigests](API_ModelDigests.md) object

 ** [ModelPackageVersionArn](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-ModelPackageVersionArn"></a>
The Amazon Resource Name (ARN) of the versioned model package that was provided to SageMaker Neo when you initiated a compilation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`

 ** [OutputConfig](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-OutputConfig"></a>
Information about the output location for the compiled model and the target device that the model runs on.
Type: [OutputConfig](API_OutputConfig.md) object

 ** [RoleArn](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI assumes to perform the model compilation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-StoppingCondition"></a>
Specifies a limit to how long a model compilation job can run. When the job reaches the time limit, Amazon SageMaker AI ends the compilation job. Use this API to cap model training costs.
Type: [StoppingCondition](API_StoppingCondition.md) object

 ** [VpcConfig](#API_DescribeCompilationJob_ResponseSyntax) **   <a name="sagemaker-DescribeCompilationJob-response-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your compilation job to connect to. Control access to your models by configuring the VPC. For more information, see [Protect Compilation Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html).
Type: [NeoVpcConfig](API_NeoVpcConfig.md) object

## Errors
<a name="API_DescribeCompilationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCompilationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeCompilationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeCompilationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
