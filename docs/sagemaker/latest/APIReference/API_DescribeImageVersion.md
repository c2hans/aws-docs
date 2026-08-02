---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeImageVersion.html
---

# DescribeImageVersion
<a name="API_DescribeImageVersion"></a>

Describes a version of a SageMaker AI image.

## Request Syntax
<a name="API_DescribeImageVersion_RequestSyntax"></a>

```
{
   "Alias": "{{string}}",
   "ImageName": "{{string}}",
   "Version": {{number}}
}
```

## Request Parameters
<a name="API_DescribeImageVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Alias](#API_DescribeImageVersion_RequestSyntax) **   <a name="sagemaker-DescribeImageVersion-request-Alias"></a>
The alias of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [ImageName](#API_DescribeImageVersion_RequestSyntax) **   <a name="sagemaker-DescribeImageVersion-request-ImageName"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Version](#API_DescribeImageVersion_RequestSyntax) **   <a name="sagemaker-DescribeImageVersion-request-Version"></a>
The version of the image. If not specified, the latest version is described.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_DescribeImageVersion_ResponseSyntax"></a>

```
{
   "BaseImage": "string",
   "ContainerImage": "string",
   "CreationTime": number,
   "FailureReason": "string",
   "Horovod": boolean,
   "ImageArn": "string",
   "ImageVersionArn": "string",
   "ImageVersionStatus": "string",
   "JobType": "string",
   "LastModifiedTime": number,
   "MLFramework": "string",
   "Processor": "string",
   "ProgrammingLang": "string",
   "ReleaseNotes": "string",
   "VendorGuidance": "string",
   "Version": number
}
```

## Response Elements
<a name="API_DescribeImageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaseImage](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-BaseImage"></a>
The registry path of the container image on which this image version is based.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [ContainerImage](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ContainerImage"></a>
The registry path of the container image that contains this image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreationTime](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-CreationTime"></a>
When the version was created.
Type: Timestamp

 ** [FailureReason](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-FailureReason"></a>
When a create or delete operation fails, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Horovod](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-Horovod"></a>
Indicates Horovod compatibility.
Type: Boolean

 ** [ImageArn](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ImageArn"></a>
The ARN of the image the version is based on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`

 ** [ImageVersionArn](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ImageVersionArn"></a>
The ARN of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+|None)`

 ** [ImageVersionStatus](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ImageVersionStatus"></a>
The status of the version.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | DELETING | DELETE_FAILED`

 ** [JobType](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-JobType"></a>
Indicates SageMaker AI job type compatibility.
+  `TRAINING`: The image version is compatible with SageMaker AI training jobs.
+  `INFERENCE`: The image version is compatible with SageMaker AI inference jobs.
+  `NOTEBOOK_KERNEL`: The image version is compatible with SageMaker AI notebook kernels.
Type: String
Valid Values: `TRAINING | INFERENCE | NOTEBOOK_KERNEL`

 ** [LastModifiedTime](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-LastModifiedTime"></a>
When the version was last modified.
Type: Timestamp

 ** [MLFramework](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-MLFramework"></a>
The machine learning framework vended in the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`

 ** [Processor](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-Processor"></a>
Indicates CPU or GPU compatibility.
+  `CPU`: The image version is compatible with CPU.
+  `GPU`: The image version is compatible with GPU.
Type: String
Valid Values: `CPU | GPU`

 ** [ProgrammingLang](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ProgrammingLang"></a>
The supported programming language and its version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z]+ ?\d+\.\d+(\.\d+)?`

 ** [ReleaseNotes](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-ReleaseNotes"></a>
The maintainer description of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [VendorGuidance](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-VendorGuidance"></a>
The stability of the image version specified by the maintainer.
+  `NOT_PROVIDED`: The maintainers did not provide a status for image version stability.
+  `STABLE`: The image version is stable.
+  `TO_BE_ARCHIVED`: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.
+  `ARCHIVED`: The image version is archived. Archived image versions are not searchable and are no longer actively supported.
Type: String
Valid Values: `NOT_PROVIDED | STABLE | TO_BE_ARCHIVED | ARCHIVED`

 ** [Version](#API_DescribeImageVersion_ResponseSyntax) **   <a name="sagemaker-DescribeImageVersion-response-Version"></a>
The version number.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_DescribeImageVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeImageVersion)
