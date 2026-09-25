---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_UpdateTemplate.html
---

# UpdateTemplate
<a name="API_UpdateTemplate"></a>

Updates the specified template. To prevent conflicting concurrent updates, provide the current `updateToken`. Use `isPublished` to publish the update or keep the template as a draft.

## Request Syntax
<a name="API_UpdateTemplate_RequestSyntax"></a>

```
PATCH /templates/{{templateIdentifier}} HTTP/1.1
Content-type: application/json

{
   "associatedRuleList": [
      {
         "ruleIdentifier": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "isPublished": {{boolean}},
   "templateDescription": "{{string}}",
   "updateToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateIdentifier](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-uri-templateIdentifier"></a>
The identifier of the template. This is the template's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_UpdateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedRuleList](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-associatedRuleList"></a>
The rules associated with the template.
Type: Array of [RuleReference](API_RuleReference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [clientToken](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-clientToken"></a>
A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [isPublished](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-isPublished"></a>
Specifies whether to publish the resource. When `true`, the resource is saved in published (`ACTIVE`) state. When `false`, it is saved as a draft (`DRAFT`).
Type: Boolean
Required: Yes

 ** [templateDescription](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-templateDescription"></a>
A description of the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** [updateToken](#API_UpdateTemplate_RequestSyntax) **   <a name="networksecuritymanager-UpdateTemplate-request-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`
Required: Yes

## Response Syntax
<a name="API_UpdateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedRuleList": [
      {
         "ruleArn": "string"
      }
   ],
   "firewallType": "string",
   "hasPublishedVersion": boolean,
   "isSnapshot": boolean,
   "status": "string",
   "templateArn": "string",
   "templateDescription": "string",
   "templateId": "string",
   "templateName": "string",
   "updatedAt": "string",
   "updateToken": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_UpdateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedRuleList](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-associatedRuleList"></a>
The rules associated with the template.
Type: Array of [AssociatedRule](API_AssociatedRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [firewallType](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF`

 ** [hasPublishedVersion](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [status](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [templateArn](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-templateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [templateDescription](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-templateDescription"></a>
A description of the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [templateId](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-templateId"></a>
The service-generated id of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [templateName](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-templateName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [updatedAt](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_UpdateTemplate_ResponseSyntax) **   <a name="networksecuritymanager-UpdateTemplate-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_UpdateTemplate_Errors"></a>

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
<a name="API_UpdateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/UpdateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/UpdateTemplate)
