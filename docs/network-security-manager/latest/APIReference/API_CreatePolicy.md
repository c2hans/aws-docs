---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_CreatePolicy.html
---

# CreatePolicy
<a name="API_CreatePolicy"></a>

Creates a policy. A policy combines templates and rules with enforcement settings for a firewall type, such as AWS WAF or AWS Shield Advanced. Use `isPublished` to create the policy in published (`ACTIVE`) or draft (`DRAFT`) state.

## Request Syntax
<a name="API_CreatePolicy_RequestSyntax"></a>

```
POST /policies HTTP/1.1
Content-type: application/json

{
   "associatedTemplateAndRuleList": [
      { ... }
   ],
   "clientToken": "{{string}}",
   "firewallType": "{{string}}",
   "isPublished": {{boolean}},
   "policyConfiguration": {
      "remediationEnabled": {{boolean}},
      "resourcesCleanUp": {{boolean}},
      "wafConfig": {
         "conflictResolution": "{{string}}",
         "existingCustomerWebACLResolution": "{{string}}"
      }
   },
   "policyDescription": "{{string}}",
   "policyName": "{{string}}",
   "priority": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedTemplateAndRuleList](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-associatedTemplateAndRuleList"></a>
The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.
Type: Array of [TemplateOrRuleReference](API_TemplateOrRuleReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [clientToken](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-clientToken"></a>
A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [firewallType](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF | SHIELD_ADVANCED`
Required: Yes

 ** [isPublished](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-isPublished"></a>
Specifies whether to publish the resource. When `true`, the resource is saved in published (`ACTIVE`) state. When `false`, it is saved as a draft (`DRAFT`). Default: `true`.
Type: Boolean
Required: No

 ** [policyConfiguration](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-policyConfiguration"></a>
The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.
Type: [PolicyConfiguration](API_PolicyConfiguration.md) object
Required: Yes

 ** [policyDescription](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-policyDescription"></a>
A description of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** [policyName](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-policyName"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: Yes

 ** [priority](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-priority"></a>
The priority of the resource. A lower number indicates a higher priority.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [tags](#API_CreatePolicy_RequestSyntax) **   <a name="networksecuritymanager-CreatePolicy-request-tags"></a>
The tags to add to the resource when it is created.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePolicy_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "associatedTemplateAndRuleList": [
      { ... }
   ],
   "firewallType": "string",
   "hasPublishedVersion": boolean,
   "isSnapshot": boolean,
   "policyArn": "string",
   "policyConfiguration": {
      "remediationEnabled": boolean,
      "resourcesCleanUp": boolean,
      "wafConfig": {
         "conflictResolution": "string",
         "existingCustomerWebACLResolution": "string"
      }
   },
   "policyDescription": "string",
   "policyId": "string",
   "policyName": "string",
   "priority": number,
   "status": "string",
   "updatedAt": "string",
   "updateToken": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [associatedTemplateAndRuleList](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-associatedTemplateAndRuleList"></a>
The templates and rules associated with the policy. For AWS WAF policies, this list contains 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list is empty.
Type: Array of [AssociatedTemplateOrRule](API_AssociatedTemplateOrRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [firewallType](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF | SHIELD_ADVANCED`

 ** [hasPublishedVersion](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [policyArn](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [policyConfiguration](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-policyConfiguration"></a>
The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.
Type: [PolicyConfiguration](API_PolicyConfiguration.md) object

 ** [policyDescription](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-policyDescription"></a>
A description of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [policyId](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-policyId"></a>
The service-generated id of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [policyName](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-policyName"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [priority](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-priority"></a>
The priority of the resource. A lower number indicates a higher priority.
Type: Integer
Valid Range: Minimum value of 1.

 ** [status](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [updatedAt](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_CreatePolicy_ResponseSyntax) **   <a name="networksecuritymanager-CreatePolicy-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_CreatePolicy_Errors"></a>

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

 ** ServiceUnavailableException **
The service is temporarily unavailable. This is a retryable error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 503

 ** TagPolicyViolationException **
The request violates a tag policy that is in effect for the account or organization.
HTTP Status Code: 400

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
<a name="API_CreatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/CreatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/CreatePolicy)
