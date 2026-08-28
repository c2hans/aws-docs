---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelCardExportJob.html
---

# CreateModelCardExportJob
<a name="API_CreateModelCardExportJob"></a>

Creates an Amazon SageMaker Model Card export job.

## Request Syntax
<a name="API_CreateModelCardExportJob_RequestSyntax"></a>

```
{
   "ModelCardExportJobName": "{{string}}",
   "ModelCardName": "{{string}}",
   "ModelCardVersion": {{number}},
   "OutputConfig": {
      "S3OutputPath": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateModelCardExportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelCardExportJobName](#API_CreateModelCardExportJob_RequestSyntax) **   <a name="sagemaker-CreateModelCardExportJob-request-ModelCardExportJobName"></a>
The name of the model card export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelCardName](#API_CreateModelCardExportJob_RequestSyntax) **   <a name="sagemaker-CreateModelCardExportJob-request-ModelCardName"></a>
The name or Amazon Resource Name (ARN) of the model card to export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model-card/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [ModelCardVersion](#API_CreateModelCardExportJob_RequestSyntax) **   <a name="sagemaker-CreateModelCardExportJob-request-ModelCardVersion"></a>
The version of the model card to export. If a version is not provided, then the latest version of the model card is exported.
Type: Integer
Required: No

 ** [OutputConfig](#API_CreateModelCardExportJob_RequestSyntax) **   <a name="sagemaker-CreateModelCardExportJob-request-OutputConfig"></a>
The model card output configuration that specifies the Amazon S3 path for exporting.
Type: [ModelCardExportOutputConfig](API_ModelCardExportOutputConfig.md) object
Required: Yes

## Response Syntax
<a name="API_CreateModelCardExportJob_ResponseSyntax"></a>

```
{
   "ModelCardExportJobArn": "string"
}
```

## Response Elements
<a name="API_CreateModelCardExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardExportJobArn](#API_CreateModelCardExportJob_ResponseSyntax) **   <a name="sagemaker-CreateModelCardExportJob-response-ModelCardExportJobArn"></a>
The Amazon Resource Name (ARN) of the model card export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}/export-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateModelCardExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateModelCardExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModelCardExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModelCardExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
