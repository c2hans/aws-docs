---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html
---

# PublishLayerVersion
<a name="API_PublishLayerVersion"></a>

Creates an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) from a ZIP archive. Each time you call `PublishLayerVersion` with the same layer name, a new version is created.

Add layers to your function with [CreateFunction](API_CreateFunction.md) or [UpdateFunctionConfiguration](API_UpdateFunctionConfiguration.md).

## Request Syntax
<a name="API_PublishLayerVersion_RequestSyntax"></a>

```
POST /2018-10-31/layers/{{LayerName}}/versions HTTP/1.1
Content-type: application/json

{
   "CompatibleArchitectures": [ "{{string}}" ],
   "CompatibleRuntimes": [ "{{string}}" ],
   "Content": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}",
      "S3ObjectStorageMode": "{{string}}",
      "S3ObjectVersion": "{{string}}",
      "ZipFile": {{blob}}
   },
   "Description": "{{string}}",
   "LicenseInfo": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PublishLayerVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LayerName](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-uri-LayerName"></a>
The name or Amazon Resource Name (ARN) of the layer.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_PublishLayerVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CompatibleArchitectures](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-CompatibleArchitectures"></a>
A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `x86_64 | arm64`
Required: No

 ** [CompatibleRuntimes](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-CompatibleRuntimes"></a>
A list of compatible [function runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Used for filtering with [ListLayers](API_ListLayers.md) and [ListLayerVersions](API_ListLayerVersions.md).
The following list includes deprecated runtimes. For more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`
Required: No

 ** [Content](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-Content"></a>
The function layer archive.
Type: [LayerVersionContentInput](API_LayerVersionContentInput.md) object
Required: Yes

 ** [Description](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-Description"></a>
The description of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [LicenseInfo](#API_PublishLayerVersion_RequestSyntax) **   <a name="lambda-PublishLayerVersion-request-LicenseInfo"></a>
The layer's software license. It can be any of the following:
+ An [SPDX license identifier](https://spdx.org/licenses/). For example, `MIT`.
+ The URL of a license hosted on the internet. For example, `https://opensource.org/licenses/MIT`.
+ The full text of the license.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_PublishLayerVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "CompatibleArchitectures": [ "string" ],
   "CompatibleRuntimes": [ "string" ],
   "Content": {
      "CodeSha256": "string",
      "CodeSize": number,
      "Location": "string",
      "ResolvedS3Object": {
         "S3Bucket": "string",
         "S3Key": "string",
         "S3ObjectVersion": "string"
      },
      "SigningJobArn": "string",
      "SigningProfileVersionArn": "string"
   },
   "CreatedDate": "string",
   "Description": "string",
   "LayerArn": "string",
   "LayerVersionArn": "string",
   "LicenseInfo": "string",
   "Version": number
}
```

## Response Elements
<a name="API_PublishLayerVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [CompatibleArchitectures](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-CompatibleArchitectures"></a>
A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `x86_64 | arm64`

 ** [CompatibleRuntimes](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-CompatibleRuntimes"></a>
The layer's compatible runtimes.
The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

 ** [Content](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-Content"></a>
Details about the layer version.
Type: [LayerVersionContentOutput](API_LayerVersionContentOutput.md) object

 ** [CreatedDate](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-CreatedDate"></a>
The date that the layer version was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

 ** [Description](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-Description"></a>
The description of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [LayerArn](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-LayerArn"></a>
The ARN of the layer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+`

 ** [LayerVersionArn](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-LayerVersionArn"></a>
The ARN of the layer version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`

 ** [LicenseInfo](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-LicenseInfo"></a>
The layer's software license.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.

 ** [Version](#API_PublishLayerVersion_ResponseSyntax) **   <a name="lambda-PublishLayerVersion-response-Version"></a>
The version number.
Type: Long

## Errors
<a name="API_PublishLayerVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeStorageExceededException **
Your AWS account has exceeded its maximum total code size. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_PublishLayerVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PublishLayerVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PublishLayerVersion)
