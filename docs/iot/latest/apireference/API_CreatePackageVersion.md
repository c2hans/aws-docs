---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackageVersion.html
---

# CreatePackageVersion
<a name="API_CreatePackageVersion"></a>

Creates a new version for an existing AWS IoT software package.

Requires permission to access the [CreatePackageVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) and [GetIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) actions.

## Request Syntax
<a name="API_CreatePackageVersion_RequestSyntax"></a>

```
PUT /packages/{{packageName}}/versions/{{versionName}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "artifact": {
      "s3Location": {
         "bucket": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      }
   },
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "description": "{{string}}",
   "recipe": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-uri-packageName"></a>
The name of the associated software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

 ** [versionName](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-uri-versionName"></a>
The name of the new package version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_CreatePackageVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [artifact](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-artifact"></a>
The various build components created during the build process such as libraries and configuration files that make up a software package version.
Type: [PackageVersionArtifact](API_PackageVersionArtifact.md) object
Required: No

 ** [attributes](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-attributes"></a>
Metadata that can be used to define a package version’s configuration. For example, the S3 file location, configuration options that are being sent to the device or fleet.
The combined size of all the attributes on a package version is limited to 3KB.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** [description](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-description"></a>
A summary of the package version being created. This can be used to outline the package's contents or purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`
Required: No

 ** [recipe](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-recipe"></a>
The inline job document associated with a software package version used for a quick job deployment.
Type: String
Length Constraints: Maximum length of 3072.
Required: No

 ** [tags](#API_CreatePackageVersion_RequestSyntax) **   <a name="iot-CreatePackageVersion-request-tags"></a>
Metadata that can be used to manage the package version.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributes": {
      "string" : "string"
   },
   "description": "string",
   "errorReason": "string",
   "packageName": "string",
   "packageVersionArn": "string",
   "status": "string",
   "versionName": "string"
}
```

## Response Elements
<a name="API_CreatePackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributes](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-attributes"></a>
Metadata that were added to the package version that can be used to define a package version’s configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`

 ** [description](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-description"></a>
The package version description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`

 ** [errorReason](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-errorReason"></a>
Error reason for a package version failure during creation or update.
Type: String

 ** [packageName](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-packageName"></a>
The name of the associated software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`

 ** [packageVersionArn](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-packageVersionArn"></a>
The Amazon Resource Name (ARN) for the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [status](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-status"></a>
The status of the package version. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
Type: String
Valid Values: `DRAFT | PUBLISHED | DEPRECATED`

 ** [versionName](#API_CreatePackageVersion_ResponseSyntax) **   <a name="iot-CreatePackageVersion-response-versionName"></a>
The name of the new package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`

## Errors
<a name="API_CreatePackageVersion_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Service quota has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreatePackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreatePackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreatePackageVersion)
