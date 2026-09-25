---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_GetScope.html
---

# GetScope
<a name="API_GetScope"></a>

Retrieves the details of the specified scope.

## Request Syntax
<a name="API_GetScope_RequestSyntax"></a>

```
GET /scopes/{{scopeIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scopeIdentifier](#API_GetScope_RequestSyntax) **   <a name="networksecuritymanager-GetScope-request-uri-scopeIdentifier"></a>
The identifier of the scope. This is the scope's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_GetScope_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetScope_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "hasPublishedVersion": boolean,
   "isSnapshot": boolean,
   "scopeArn": "string",
   "scopeConfiguration": {
      "accountFilter": { ... },
      "resourceScopes": {
         "string" : {
            "exclude": {
               "explicitArns": [ "string" ],
               "expression": { ... }
            },
            "include": {
               "explicitArns": [ "string" ],
               "expression": { ... }
            },
            "includeAll": boolean
         }
      }
   },
   "scopeDescription": "string",
   "scopeId": "string",
   "scopeName": "string",
   "status": "string",
   "updatedAt": "string",
   "updateToken": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_GetScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasPublishedVersion](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [scopeArn](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [scopeConfiguration](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-scopeConfiguration"></a>
The configuration that defines which accounts and resources are in scope.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object

 ** [scopeDescription](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-scopeDescription"></a>
A description of the scope.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [scopeId](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-scopeId"></a>
The service-generated id of the scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [scopeName](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-scopeName"></a>
The name of the scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [status](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable), `ACTIVE` (published, in use), or `DISABLED` (deactivated; changes cannot be published until the resource is re-enabled).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [updatedAt](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_GetScope_ResponseSyntax) **   <a name="networksecuritymanager-GetScope-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_GetScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing failed because of an internal error in the service. This is a retryable error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Reduce your request rate and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation. For details, see the `reason` and `fieldList` members of the response.
 ** fieldList **
The list of request fields that failed validation, if any.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/GetScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/GetScope)
