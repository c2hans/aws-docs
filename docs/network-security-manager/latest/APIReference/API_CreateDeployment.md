---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_CreateDeployment.html
---

# CreateDeployment
<a name="API_CreateDeployment"></a>

Creates a deployment. A deployment applies one or more policies to the accounts and resources selected by a scope. Use `isPublished` to create the deployment in published (`ACTIVE`) or draft (`DRAFT`) state. The response includes coverage information and any warnings about the deployment.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
POST /deployments HTTP/1.1
Content-type: application/json

{
   "associatedPolicyList": [
      {
         "policyIdentifier": "{{string}}"
      }
   ],
   "associatedScopeList": [
      {
         "scopeIdentifier": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "deploymentConfiguration": {
      "enableCrossAccountVisibility": {{boolean}}
   },
   "deploymentDescription": "{{string}}",
   "deploymentName": "{{string}}",
   "isPublished": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedPolicyList](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-associatedPolicyList"></a>
The policies associated with the deployment.
Type: Array of [PolicyReference](API_PolicyReference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [associatedScopeList](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-associatedScopeList"></a>
The scope associated with the deployment. A deployment has exactly one scope.
Type: Array of [ScopeReference](API_ScopeReference.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [clientToken](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-clientToken"></a>
A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [deploymentConfiguration](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-deploymentConfiguration"></a>
The configuration settings for the deployment.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: Yes

 ** [deploymentDescription](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-deploymentDescription"></a>
A description of the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** [deploymentName](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: Yes

 ** [isPublished](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-isPublished"></a>
Specifies whether to publish the resource. When `true`, the resource is saved in published (`ACTIVE`) state. When `false`, it is saved as a draft (`DRAFT`). Default: `true`.
Type: Boolean
Required: No

 ** [tags](#API_CreateDeployment_RequestSyntax) **   <a name="networksecuritymanager-CreateDeployment-request-tags"></a>
The tags to add to the resource when it is created.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "associatedPolicyList": [
      {
         "policyArn": "string"
      }
   ],
   "associatedScopeList": [
      {
         "scopeArn": "string"
      }
   ],
   "deploymentArn": "string",
   "deploymentConfiguration": {
      "enableCrossAccountVisibility": boolean
   },
   "deploymentCoverage": [
      {
         "firewallType": "string",
         "inScopeResourceTypes": [ "string" ],
         "policyArns": [ "string" ]
      }
   ],
   "deploymentDescription": "string",
   "deploymentId": "string",
   "deploymentName": "string",
   "hasPublishedVersion": boolean,
   "isSnapshot": boolean,
   "status": "string",
   "updatedAt": "string",
   "updateToken": "string",
   "version": "string",
   "warnings": [
      {
         "code": "string",
         "message": "string",
         "policyArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [associatedPolicyList](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-associatedPolicyList"></a>
The policies associated with the deployment.
Type: Array of [AssociatedPolicy](API_AssociatedPolicy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [associatedScopeList](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-associatedScopeList"></a>
The scope associated with the deployment. A deployment has exactly one scope.
Type: Array of [AssociatedScope](API_AssociatedScope.md) objects
Array Members: Fixed number of 1 item.

 ** [deploymentArn](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentArn"></a>
The Amazon Resource Name (ARN) of the deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [deploymentConfiguration](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentConfiguration"></a>
The configuration settings for the deployment.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object

 ** [deploymentCoverage](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentCoverage"></a>
The coverage information for the deployment. For each firewall type, it shows which policies have that firewall type and which in-scope resource types the firewall type protects.
Type: Array of [DeploymentCoverageEntry](API_DeploymentCoverageEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [deploymentDescription](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentDescription"></a>
A description of the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [deploymentId](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentId"></a>
The service-generated id of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [deploymentName](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [hasPublishedVersion](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [status](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [updatedAt](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

 ** [warnings](#API_CreateDeployment_ResponseSyntax) **   <a name="networksecuritymanager-CreateDeployment-response-warnings"></a>
Warnings about potential issues, such as a policy that has no applicable resources in the deployment's scope.
Type: Array of [DeploymentWarningEntry](API_DeploymentWarningEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_CreateDeployment_Errors"></a>

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
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/CreateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/CreateDeployment)
