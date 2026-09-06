---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackage.html
---

# UpdatePackage
<a name="API_UpdatePackage"></a>

Updates the supported fields for a specific software package.

Requires permission to access the [UpdatePackage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) and [GetIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) actions.

## Request Syntax
<a name="API_UpdatePackage_RequestSyntax"></a>

```
PATCH /packages/{{packageName}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "defaultVersionName": "{{string}}",
   "description": "{{string}}",
   "unsetDefaultVersion": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdatePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdatePackage_RequestSyntax) **   <a name="iot-UpdatePackage-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_UpdatePackage_RequestSyntax) **   <a name="iot-UpdatePackage-request-uri-packageName"></a>
The name of the target software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_UpdatePackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultVersionName](#API_UpdatePackage_RequestSyntax) **   <a name="iot-UpdatePackage-request-defaultVersionName"></a>
The name of the default package version.
 **Note:** You cannot name a `defaultVersion` and set `unsetDefaultVersion` equal to `true` at the same time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: No

 ** [description](#API_UpdatePackage_RequestSyntax) **   <a name="iot-UpdatePackage-request-description"></a>
The package description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`
Required: No

 ** [unsetDefaultVersion](#API_UpdatePackage_RequestSyntax) **   <a name="iot-UpdatePackage-request-unsetDefaultVersion"></a>
Indicates whether you want to remove the named default package version from the software package. Set as `true` to remove the default package version.
 **Note:** You cannot name a `defaultVersion` and set `unsetDefaultVersion` equal to `true` at the same time.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdatePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePackage_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdatePackage)
