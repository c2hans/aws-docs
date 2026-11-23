---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetAvailableModuleVersion.html
---

# GetAvailableModuleVersion

Returns an ACTIVE or DEPRECATED version of a module that you can attach. If you can't attach the module, or the version is in another status, the operation returns ResourceNotFoundException, the same as for a missing one.

## Request Syntax
<a name="API_GetAvailableModuleVersion_RequestSyntax"></a>

```
GET /available-modules/{{moduleId}}/versions/{{version}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAvailableModuleVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [moduleId](#API_GetAvailableModuleVersion_RequestSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-request-uri-moduleId"></a>
The module's ID.
Pattern: `module-[a-zA-Z0-9]{1,25}`
Required: Yes

 ** [version](#API_GetAvailableModuleVersion_RequestSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-request-uri-version"></a>
The version.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`
Required: Yes

## Request Body
<a name="API_GetAvailableModuleVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAvailableModuleVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurableActions": [ "string" ],
   "configurationSchema": "string",
   "createdAt": number,
   "moduleId": "string",
   "moduleVersionArn": "string",
   "permissions": [ "string" ],
   "releaseNotes": "string",
   "status": "string",
   "updatedAt": number,
   "version": "string"
}
```

## Response Elements
<a name="API_GetAvailableModuleVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurableActions](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-configurableActions"></a>
The capabilities that you can turn on in `selectedActions` when you attach the version:
+  `FILTER`: the module can end a request with a no-bid response.
+  `ENRICH_REQUEST_EXT`: the module adds its data to the request's `ext` object.
+  `ENRICH_REQUEST_HEADERS`: the module adds a header to the request. Only the OpenRTB Attribute Module supports it.
+  `OBSERVE`: the module records its result without acting on the request.
You can't select both FILTER and OBSERVE.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Valid Values: `FILTER | ENRICH_REQUEST_EXT | ENRICH_REQUEST_HEADERS | OBSERVE`

 ** [configurationSchema](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-configurationSchema"></a>
The JSON Schema for the parameters that you can set in `configurationValues` when you attach the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.

 ** [createdAt](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-createdAt"></a>
The time when the version was created.
Type: Timestamp

 ** [moduleId](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-moduleId"></a>
The module's ID.
Type: String
Pattern: `module-[a-zA-Z0-9]{1,25}`

 ** [moduleVersionArn](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-moduleVersionArn"></a>
The version's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `arn:aws[a-zA-Z-]*:rtbfabric:[a-z0-9-]+::modules/module-[a-zA-Z0-9]{1,25}/versions/(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`

 ** [permissions](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-permissions"></a>
The kinds of bid request access that the module version declares. These aren't IAM permissions, and `selectedActions` doesn't change them.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Valid Values: `READ_REQUEST_BODY | READ_REQUEST_HEADERS | MUTATE_REQUEST_BODY | ENRICH_REQUEST_HEADERS | ENRICH_REQUEST_EXT | FILTER`

 ** [releaseNotes](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-releaseNotes"></a>
The vendor's release notes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [status](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-status"></a>
ACTIVE or DEPRECATED.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DEPRECATED`

 ** [updatedAt](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-updatedAt"></a>
The time when the version last changed.
Type: Timestamp

 ** [version](#API_GetAvailableModuleVersion_ResponseSyntax) **   <a name="rtbfabric-GetAvailableModuleVersion-response-version"></a>
The version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`

## Errors
<a name="API_GetAvailableModuleVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetAvailableModuleVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetAvailableModuleVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetAvailableModuleVersion)
