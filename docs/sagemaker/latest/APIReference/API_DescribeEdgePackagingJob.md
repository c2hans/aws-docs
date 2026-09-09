---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEdgePackagingJob.html
---

# DescribeEdgePackagingJob
<a name="API_DescribeEdgePackagingJob"></a>

A description of edge packaging jobs.

## Request Syntax
<a name="API_DescribeEdgePackagingJob_RequestSyntax"></a>

```
{
   "EdgePackagingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEdgePackagingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EdgePackagingJobName](#API_DescribeEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-request-EdgePackagingJobName"></a>
The name of the edge packaging job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeEdgePackagingJob_ResponseSyntax"></a>

```
{
   "CompilationJobName": "string",
   "EdgePackagingJobArn": "string",
   "EdgePackagingJobName": "string",
   "EdgePackagingJobStatus": "string",
   "EdgePackagingJobStatusMessage": "string",
   "ModelArtifact": "string",
   "ModelName": "string",
   "ModelSignature": "string",
   "ModelVersion": "string",
   "OutputConfig": {
      "KmsKeyId": "string",
      "PresetDeploymentConfig": "string",
      "PresetDeploymentType": "string",
      "S3OutputLocation": "string"
   },
   "PresetDeploymentOutput": {
      "Artifact": "string",
      "Status": "string",
      "StatusMessage": "string",
      "Type": "string"
   },
   "ResourceKey": "string",
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribeEdgePackagingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompilationJobName](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-CompilationJobName"></a>
The name of the SageMaker Neo compilation job that is used to locate model artifacts that are being packaged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EdgePackagingJobArn](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-EdgePackagingJobArn"></a>
The Amazon Resource Name (ARN) of the edge packaging job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z\-]*:\d{12}:edge-packaging-job/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [EdgePackagingJobName](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-EdgePackagingJobName"></a>
The name of the edge packaging job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EdgePackagingJobStatus](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-EdgePackagingJobStatus"></a>
The current status of the packaging job.
Type: String
Valid Values: `STARTING | INPROGRESS | COMPLETED | FAILED | STOPPING | STOPPED`

 ** [EdgePackagingJobStatusMessage](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-EdgePackagingJobStatusMessage"></a>
Returns a message describing the job status and error messages.
Type: String

 ** [ModelArtifact](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-ModelArtifact"></a>
The Amazon Simple Storage (S3) URI where model artifacts ares stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`

 ** [ModelName](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelSignature](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-ModelSignature"></a>
The signature document of files in the model artifact.
Type: String

 ** [ModelVersion](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-ModelVersion"></a>
The version of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`

 ** [OutputConfig](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-OutputConfig"></a>
The output configuration for the edge packaging job.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object

 ** [PresetDeploymentOutput](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-PresetDeploymentOutput"></a>
The output of a SageMaker Edge Manager deployable resource.
Type: [EdgePresetDeploymentOutput](API_EdgePresetDeploymentOutput.md) object

 ** [ResourceKey](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-ResourceKey"></a>
The AWS KMS key to use when encrypting the EBS volume the job run on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [RoleArn](#API_DescribeEdgePackagingJob_ResponseSyntax) **   <a name="sagemaker-DescribeEdgePackagingJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to download and upload the model, and to contact Neo.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribeEdgePackagingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEdgePackagingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeEdgePackagingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeEdgePackagingJob)
