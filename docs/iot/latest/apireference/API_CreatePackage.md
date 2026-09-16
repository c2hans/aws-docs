---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackage.html
---

# CreatePackage
<a name="API_CreatePackage"></a>

Creates an AWS IoT software package that can be deployed to your fleet.

Requires permission to access the [CreatePackage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) and [GetIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) actions.

## Request Syntax
<a name="API_CreatePackage_RequestSyntax"></a>

```
PUT /packages/{{packageName}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreatePackage_RequestSyntax) **   <a name="iot-CreatePackage-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_CreatePackage_RequestSyntax) **   <a name="iot-CreatePackage-request-uri-packageName"></a>
The name of the new software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_CreatePackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreatePackage_RequestSyntax) **   <a name="iot-CreatePackage-request-description"></a>
A summary of the package being created. This can be used to outline the package's contents or purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`
Required: No

 ** [tags](#API_CreatePackage_RequestSyntax) **   <a name="iot-CreatePackage-request-tags"></a>
Metadata that can be used to manage the package.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "packageArn": "string",
   "packageName": "string"
}
```

## Response Elements
<a name="API_CreatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreatePackage_ResponseSyntax) **   <a name="iot-CreatePackage-response-description"></a>
The package description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`

 ** [packageArn](#API_CreatePackage_ResponseSyntax) **   <a name="iot-CreatePackage-response-packageArn"></a>
The Amazon Resource Name (ARN) for the package.
Type: String

 ** [packageName](#API_CreatePackage_ResponseSyntax) **   <a name="iot-CreatePackage-response-packageName"></a>
The name of the software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`

## Errors
<a name="API_CreatePackage_Errors"></a>

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
<a name="API_CreatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreatePackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreatePackage)
