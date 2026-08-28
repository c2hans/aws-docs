---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateImageVersion.html
---

# CreateImageVersion
<a name="API_CreateImageVersion"></a>

Creates a version of the SageMaker AI image specified by `ImageName`. The version represents the Amazon ECR container image specified by `BaseImage`.

## Request Syntax
<a name="API_CreateImageVersion_RequestSyntax"></a>

```
{
   "Aliases": [ "{{string}}" ],
   "BaseImage": "{{string}}",
   "ClientToken": "{{string}}",
   "Horovod": {{boolean}},
   "ImageName": "{{string}}",
   "JobType": "{{string}}",
   "MLFramework": "{{string}}",
   "Processor": "{{string}}",
   "ProgrammingLang": "{{string}}",
   "ReleaseNotes": "{{string}}",
   "VendorGuidance": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateImageVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aliases](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-Aliases"></a>
A list of aliases created with the image version.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [BaseImage](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-BaseImage"></a>
The registry path of the container image to use as the starting point for this version. The path is an Amazon ECR URI in the following format:
 `<acct-id>.dkr.ecr.<region>.amazonaws.com/<repo-name[:tag] or [@digest]>`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** [ClientToken](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-ClientToken"></a>
A unique ID. If not specified, the AWS CLI and AWS SDKs, such as the SDK for Python (Boto3), add a unique value to the call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Horovod](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-Horovod"></a>
Indicates Horovod compatibility.
Type: Boolean
Required: No

 ** [ImageName](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-ImageName"></a>
The `ImageName` of the `Image` to create a version of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [JobType](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-JobType"></a>
Indicates SageMaker AI job type compatibility.
+  `TRAINING`: The image version is compatible with SageMaker AI training jobs.
+  `INFERENCE`: The image version is compatible with SageMaker AI inference jobs.
+  `NOTEBOOK_KERNEL`: The image version is compatible with SageMaker AI notebook kernels.
Type: String
Valid Values: `TRAINING | INFERENCE | NOTEBOOK_KERNEL`
Required: No

 ** [MLFramework](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-MLFramework"></a>
The machine learning framework vended in the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`
Required: No

 ** [Processor](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-Processor"></a>
Indicates CPU or GPU compatibility.
+  `CPU`: The image version is compatible with CPU.
+  `GPU`: The image version is compatible with GPU.
Type: String
Valid Values: `CPU | GPU`
Required: No

 ** [ProgrammingLang](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-ProgrammingLang"></a>
The supported programming language and its version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`
Required: No

 ** [ReleaseNotes](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-ReleaseNotes"></a>
The maintainer description of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [VendorGuidance](#API_CreateImageVersion_RequestSyntax) **   <a name="sagemaker-CreateImageVersion-request-VendorGuidance"></a>
The stability of the image version, specified by the maintainer.
+  `NOT_PROVIDED`: The maintainers did not provide a status for image version stability.
+  `STABLE`: The image version is stable.
+  `TO_BE_ARCHIVED`: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.
+  `ARCHIVED`: The image version is archived. Archived image versions are not searchable and are no longer actively supported.
Type: String
Valid Values: `NOT_PROVIDED | STABLE | TO_BE_ARCHIVED | ARCHIVED`
Required: No

## Response Syntax
<a name="API_CreateImageVersion_ResponseSyntax"></a>

```
{
   "ImageVersionArn": "string"
}
```

## Response Elements
<a name="API_CreateImageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageVersionArn](#API_CreateImageVersion_ResponseSyntax) **   <a name="sagemaker-CreateImageVersion-response-ImageVersionArn"></a>
The ARN of the image version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+|None)`

## Errors
<a name="API_CreateImageVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateImageVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
