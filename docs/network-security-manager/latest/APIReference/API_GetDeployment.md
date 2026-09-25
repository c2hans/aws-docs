---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_GetDeployment.html
---

# GetDeployment
<a name="API_GetDeployment"></a>

Retrieves the details of the specified deployment, including coverage information and any warnings.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
GET /deployments/{{deploymentIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deploymentIdentifier](#API_GetDeployment_RequestSyntax) **   <a name="networksecuritymanager-GetDeployment-request-uri-deploymentIdentifier"></a>
The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_GetDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedPolicyList](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-associatedPolicyList"></a>
The policies associated with the deployment.
Type: Array of [AssociatedPolicy](API_AssociatedPolicy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [associatedScopeList](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-associatedScopeList"></a>
The scope associated with the deployment. A deployment has exactly one scope.
Type: Array of [AssociatedScope](API_AssociatedScope.md) objects
Array Members: Fixed number of 1 item.

 ** [deploymentArn](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentArn"></a>
The Amazon Resource Name (ARN) of the deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [deploymentConfiguration](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentConfiguration"></a>
The configuration settings for the deployment.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object

 ** [deploymentCoverage](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentCoverage"></a>
The coverage information for the deployment. For each firewall type, it shows which policies have that firewall type and which in-scope resource types the firewall type protects.
Type: Array of [DeploymentCoverageEntry](API_DeploymentCoverageEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [deploymentDescription](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentDescription"></a>
A description of the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [deploymentId](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentId"></a>
The service-generated id of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [deploymentName](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [hasPublishedVersion](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [status](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable), `ACTIVE` (published, in use), or `DISABLED` (deactivated; changes cannot be published until the resource is re-enabled).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [updatedAt](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

 ** [warnings](#API_GetDeployment_ResponseSyntax) **   <a name="networksecuritymanager-GetDeployment-response-warnings"></a>
Warnings about potential issues, such as a policy that has no applicable resources in the deployment's scope.
Type: Array of [DeploymentWarningEntry](API_DeploymentWarningEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_GetDeployment_Errors"></a>

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
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/GetDeployment)
