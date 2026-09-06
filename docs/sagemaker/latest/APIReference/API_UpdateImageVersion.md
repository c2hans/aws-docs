---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateImageVersion.html
---

# UpdateImageVersion
<a name="API_UpdateImageVersion"></a>

Updates the properties of a SageMaker AI image version.

## Request Syntax
<a name="API_UpdateImageVersion_RequestSyntax"></a>

```
{
   "Alias": "{{string}}",
   "AliasesToAdd": [ "{{string}}" ],
   "AliasesToDelete": [ "{{string}}" ],
   "Horovod": {{boolean}},
   "ImageName": "{{string}}",
   "JobType": "{{string}}",
   "MLFramework": "{{string}}",
   "Processor": "{{string}}",
   "ProgrammingLang": "{{string}}",
   "ReleaseNotes": "{{string}}",
   "VendorGuidance": "{{string}}",
   "Version": {{number}}
}
```

## Request Parameters
<a name="API_UpdateImageVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Alias](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-Alias"></a>
The alias of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [AliasesToAdd](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-AliasesToAdd"></a>
A list of aliases to add.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [AliasesToDelete](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-AliasesToDelete"></a>
A list of aliases to delete.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [Horovod](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-Horovod"></a>
Indicates Horovod compatibility.
Type: Boolean
Required: No

 ** [ImageName](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-ImageName"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [JobType](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-JobType"></a>
Indicates SageMaker AI job type compatibility.
+  `TRAINING`: The image version is compatible with SageMaker AI training jobs.
+  `INFERENCE`: The image version is compatible with SageMaker AI inference jobs.
+  `NOTEBOOK_KERNEL`: The image version is compatible with SageMaker AI notebook kernels.
Type: String
Valid Values: `TRAINING | INFERENCE | NOTEBOOK_KERNEL`
Required: No

 ** [MLFramework](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-MLFramework"></a>
The machine learning framework vended in the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`
Required: No

 ** [Processor](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-Processor"></a>
Indicates CPU or GPU compatibility.
+  `CPU`: The image version is compatible with CPU.
+  `GPU`: The image version is compatible with GPU.
Type: String
Valid Values: `CPU | GPU`
Required: No

 ** [ProgrammingLang](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-ProgrammingLang"></a>
The supported programming language and its version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`
Required: No

 ** [ReleaseNotes](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-ReleaseNotes"></a>
The maintainer description of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [VendorGuidance](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-VendorGuidance"></a>
The availability of the image version specified by the maintainer.
+  `NOT_PROVIDED`: The maintainers did not provide a status for image version stability.
+  `STABLE`: The image version is stable.
+  `TO_BE_ARCHIVED`: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.
+  `ARCHIVED`: The image version is archived. Archived image versions are not searchable and are no longer actively supported.
Type: String
Valid Values: `NOT_PROVIDED | STABLE | TO_BE_ARCHIVED | ARCHIVED`
Required: No

 ** [Version](#API_UpdateImageVersion_RequestSyntax) **   <a name="sagemaker-UpdateImageVersion-request-Version"></a>
The version of the image.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateImageVersion_ResponseSyntax"></a>

```
{
   "ImageVersionArn": "string"
}
```

## Response Elements
<a name="API_UpdateImageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageVersionArn](#API_UpdateImageVersion_ResponseSyntax) **   <a name="sagemaker-UpdateImageVersion-response-ImageVersionArn"></a>
The ARN of the image version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+|None)`

## Errors
<a name="API_UpdateImageVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateImageVersion)
