---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_UpdateScope.html
---

# UpdateScope
<a name="API_UpdateScope"></a>

Updates the specified scope. To prevent conflicting concurrent updates, provide the current `updateToken`. Use `isPublished` to publish the update or keep the scope as a draft.

## Request Syntax
<a name="API_UpdateScope_RequestSyntax"></a>

```
PATCH /scopes/{{scopeIdentifier}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "isPublished": {{boolean}},
   "scopeConfiguration": {
      "accountFilter": { ... },
      "resourceScopes": {
         "{{string}}" : {
            "exclude": {
               "explicitArns": [ "{{string}}" ],
               "expression": { ... }
            },
            "include": {
               "explicitArns": [ "{{string}}" ],
               "expression": { ... }
            },
            "includeAll": {{boolean}}
         }
      }
   },
   "scopeDescription": "{{string}}",
   "updateToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scopeIdentifier](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-uri-scopeIdentifier"></a>
The identifier of the scope. This is the scope's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_UpdateScope_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-clientToken"></a>
A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [isPublished](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-isPublished"></a>
Specifies whether to publish the resource. When `true`, the resource is saved in published (`ACTIVE`) state. When `false`, it is saved as a draft (`DRAFT`).
Type: Boolean
Required: Yes

 ** [scopeConfiguration](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-scopeConfiguration"></a>
The configuration that defines which accounts and resources are in scope. If you don't include this member, the scope keeps its existing configuration.
A new configuration can change which accounts and resources are selected, but it can't add or remove the account filter itself: a scope created for multi-account use stays multi-account, and a scope created for single-account use stays single-account.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

 ** [scopeDescription](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-scopeDescription"></a>
A description of the scope.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** [updateToken](#API_UpdateScope_RequestSyntax) **   <a name="networksecuritymanager-UpdateScope-request-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`
Required: Yes

## Response Syntax
<a name="API_UpdateScope_ResponseSyntax"></a>

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
<a name="API_UpdateScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasPublishedVersion](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [scopeArn](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [scopeConfiguration](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-scopeConfiguration"></a>
The configuration that defines which accounts and resources are in scope.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object

 ** [scopeDescription](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-scopeDescription"></a>
A description of the scope.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [scopeId](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-scopeId"></a>
The service-generated id of the scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [scopeName](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-scopeName"></a>
The name of the scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [status](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [updatedAt](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_UpdateScope_ResponseSyntax) **   <a name="networksecuritymanager-UpdateScope-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_UpdateScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.
 ** resourceId **
The ID of the resource that is in conflict with the request.
 ** resourceType **
The type of the resource that is in conflict with the request.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota.
 ** quotaCode **
The code that identifies the service quota that was exceeded.
 ** resourceId **
The ID of the resource associated with the quota that was exceeded.
 ** resourceType **
The type of the resource associated with the quota that was exceeded.
 ** serviceCode **
The code for the AWS service that owns the quota that was exceeded.
HTTP Status Code: 402

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
<a name="API_UpdateScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/UpdateScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/UpdateScope)
