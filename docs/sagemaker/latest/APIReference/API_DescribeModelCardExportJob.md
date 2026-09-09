---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCardExportJob.html
---

# DescribeModelCardExportJob
<a name="API_DescribeModelCardExportJob"></a>

Describes an Amazon SageMaker Model Card export job.

## Request Syntax
<a name="API_DescribeModelCardExportJob_RequestSyntax"></a>

```
{
   "ModelCardExportJobArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelCardExportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelCardExportJobArn](#API_DescribeModelCardExportJob_RequestSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-request-ModelCardExportJobArn"></a>
The Amazon Resource Name (ARN) of the model card export job to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}/export-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeModelCardExportJob_ResponseSyntax"></a>

```
{
   "ExportArtifacts": {
      "S3ExportArtifacts": "string"
   },
   "FailureReason": "string",
   "ModelCardExportJobArn": "string",
   "ModelCardExportJobName": "string",
   "ModelCardName": "string",
   "ModelCardVersion": number,
   "OutputConfig": {
      "S3OutputPath": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeModelCardExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportArtifacts](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-ExportArtifacts"></a>
The exported model card artifacts.
Type: [ModelCardExportArtifacts](API_ModelCardExportArtifacts.md) object

 ** [FailureReason](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-FailureReason"></a>
The failure reason if the model export job fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ModelCardExportJobArn](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-ModelCardExportJobArn"></a>
The Amazon Resource Name (ARN) of the model card export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}/export-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelCardExportJobName](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-ModelCardExportJobName"></a>
The name of the model card export job to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelCardName](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-ModelCardName"></a>
The name or Amazon Resource Name (ARN) of the model card that the model export job exports.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelCardVersion](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-ModelCardVersion"></a>
The version of the model card that the model export job exports.
Type: Integer

 ** [OutputConfig](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-OutputConfig"></a>
The export output details for the model card.
Type: [ModelCardExportOutputConfig](API_ModelCardExportOutputConfig.md) object

 ** [Status](#API_DescribeModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-DescribeModelCardExportJob-response-Status"></a>
The completion status of the model card export job.
+  `InProgress`: The model card export job is in progress.
+  `Completed`: The model card export job is complete.
+  `Failed`: The model card export job failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeModelCardExportJob` call.
Type: String
Valid Values: `InProgress | Completed | Failed`

## Errors
<a name="API_DescribeModelCardExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeModelCardExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelCardExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelCardExportJob)
