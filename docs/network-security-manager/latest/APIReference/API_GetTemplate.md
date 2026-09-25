---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_GetTemplate.html
---

# GetTemplate
<a name="API_GetTemplate"></a>

Retrieves the details of the specified template.

## Request Syntax
<a name="API_GetTemplate_RequestSyntax"></a>

```
GET /templates/{{templateIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateIdentifier](#API_GetTemplate_RequestSyntax) **   <a name="networksecuritymanager-GetTemplate-request-uri-templateIdentifier"></a>
The identifier of the template. This is the template's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_GetTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTemplate_ResponseSyntax"></a>

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
<a name="API_GetTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedRuleList](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-associatedRuleList"></a>
The rules associated with the template.
Type: Array of [AssociatedRule](API_AssociatedRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [firewallType](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF`

 ** [hasPublishedVersion](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean

 ** [isSnapshot](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-isSnapshot"></a>
Specifies whether the resource is a snapshot of a published version.
Type: Boolean

 ** [status](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`

 ** [templateArn](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-templateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`

 ** [templateDescription](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-templateDescription"></a>
A description of the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.:/=+\-@]*`

 ** [templateId](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-templateId"></a>
The service-generated id of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [templateName](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-templateName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`

 ** [updatedAt](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp

 ** [updateToken](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-updateToken"></a>
A token used for optimistic concurrency control. Each read and write returns an `updateToken`. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})`

 ** [version](#API_GetTemplate_ResponseSyntax) **   <a name="networksecuritymanager-GetTemplate-response-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_GetTemplate_Errors"></a>

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
<a name="API_GetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/GetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/GetTemplate)
