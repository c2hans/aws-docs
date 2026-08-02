---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateResponsePlan.html
---

# UpdateResponsePlan
<a name="API_UpdateResponsePlan"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Updates the specified response plan.

## Request Syntax
<a name="API_UpdateResponsePlan_RequestSyntax"></a>

```
POST /updateResponsePlan HTTP/1.1
Content-type: application/json

{
   "actions": [
      { ... }
   ],
   "arn": "{{string}}",
   "chatChannel": { ... },
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "engagements": [ "{{string}}" ],
   "incidentTemplateDedupeString": "{{string}}",
   "incidentTemplateImpact": {{number}},
   "incidentTemplateNotificationTargets": [
      { ... }
   ],
   "incidentTemplateSummary": "{{string}}",
   "incidentTemplateTags": {
      "{{string}}" : "{{string}}"
   },
   "incidentTemplateTitle": "{{string}}",
   "integrations": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateResponsePlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateResponsePlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-actions"></a>
The actions that this response plan takes at the beginning of an incident.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [arn](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-arn"></a>
The Amazon Resource Name (ARN) of the response plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [chatChannel](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-chatChannel"></a>
The Amazon Q Developer in chat applications chat channel used for collaboration during an incident.
Use the empty structure to remove the chat channel from the response plan.
Type: [ChatChannel](API_ChatChannel.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [clientToken](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-clientToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [displayName](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-displayName"></a>
The long format name of the response plan. The display name can't contain spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** [engagements](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-engagements"></a>
The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-contacts:[a-z0-9-]*:([0-9]{12}):contact/[a-z0-9_-]+`
Required: No

 ** [incidentTemplateDedupeString](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateDedupeString"></a>
The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [incidentTemplateImpact](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateImpact"></a>
Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.

**Supported impact codes**
+  `1` - Critical
+  `2` - High
+  `3` - Medium
+  `4` - Low
+  `5` - No Impact
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [incidentTemplateNotificationTargets](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateNotificationTargets"></a>
The Amazon SNS targets that are notified when updates are made to an incident.
Type: Array of [NotificationTargetItem](API_NotificationTargetItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [incidentTemplateSummary](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateSummary"></a>
A brief summary of the incident. This typically contains what has happened, what's currently happening, and next steps.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Required: No

 ** [incidentTemplateTags](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateTags"></a>
Tags to assign to the template. When the `StartIncident` API action is called, Incident Manager assigns the tags specified in the template to the incident. To call this action, you must also have permission to call the `TagResource` API action for the incident record resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]*`
Required: No

 ** [incidentTemplateTitle](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-incidentTemplateTitle"></a>
The short format name of the incident. The title can't contain spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** [integrations](#API_UpdateResponsePlan_RequestSyntax) **   <a name="IncidentManager-UpdateResponsePlan-request-integrations"></a>
Information about third-party services integrated into the response plan.
Type: Array of [Integration](API_Integration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_UpdateResponsePlan_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateResponsePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateResponsePlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_UpdateResponsePlan_Examples"></a>

### Example
<a name="API_UpdateResponsePlan_Example_1"></a>

This example illustrates one usage of UpdateResponsePlan.

#### Sample Request
<a name="API_UpdateResponsePlan_Example_1_Request"></a>

```
POST /updateResponsePlan HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.update-response-plan
X-Amz-Date: 20210811T202606Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 162

{
	"arn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response",
	"chatChannel": {"empty": {}},
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateResponsePlan_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateResponsePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/UpdateResponsePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/UpdateResponsePlan)
