---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateResponsePlan.html
---

# CreateResponsePlan
<a name="API_CreateResponsePlan"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Creates a response plan that automates the initial response to incidents. A response plan engages contacts, starts chat channel collaboration, and initiates runbooks at the beginning of an incident.

## Request Syntax
<a name="API_CreateResponsePlan_RequestSyntax"></a>

```
POST /createResponsePlan HTTP/1.1
Content-type: application/json

{
   "actions": [
      { ... }
   ],
   "chatChannel": { ... },
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "engagements": [ "{{string}}" ],
   "incidentTemplate": {
      "dedupeString": "{{string}}",
      "impact": {{number}},
      "incidentTags": {
         "{{string}}" : "{{string}}"
      },
      "notificationTargets": [
         { ... }
      ],
      "summary": "{{string}}",
      "title": "{{string}}"
   },
   "integrations": [
      { ... }
   ],
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateResponsePlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResponsePlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-actions"></a>
The actions that the response plan starts at the beginning of an incident.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [chatChannel](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-chatChannel"></a>
The Amazon Q Developer in chat applications chat channel used for collaboration during an incident.
Type: [ChatChannel](API_ChatChannel.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [clientToken](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-clientToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [displayName](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-displayName"></a>
The long format of the response plan name. This field can contain spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** [engagements](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-engagements"></a>
The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-contacts:[a-z0-9-]*:([0-9]{12}):contact/[a-z0-9_-]+`
Required: No

 ** [incidentTemplate](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-incidentTemplate"></a>
Details used to create an incident when using this response plan.
Type: [IncidentTemplate](API_IncidentTemplate.md) object
Required: Yes

 ** [integrations](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-integrations"></a>
Information about third-party services integrated into the response plan.
Type: Array of [Integration](API_Integration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [name](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-name"></a>
The short format name of the response plan. Can't include spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** [tags](#API_CreateResponsePlan_RequestSyntax) **   <a name="IncidentManager-CreateResponsePlan-request-tags"></a>
A list of tags that you are adding to the response plan.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]*`
Required: No

## Response Syntax
<a name="API_CreateResponsePlan_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_CreateResponsePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateResponsePlan_ResponseSyntax) **   <a name="IncidentManager-CreateResponsePlan-response-arn"></a>
The Amazon Resource Name (ARN) of the response plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

## Errors
<a name="API_CreateResponsePlan_Errors"></a>

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
<a name="API_CreateResponsePlan_Examples"></a>

### Example
<a name="API_CreateResponsePlan_Example_1"></a>

This example illustrates one usage of CreateResponsePlan.

#### Sample Request
<a name="API_CreateResponsePlan_Example_1_Request"></a>

```
POST /createResponsePlan HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.create-response-plan
X-Amz-Date: 20210810T213532Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 652

{
	"actions": [
		{
			"ssmAutomation": {
				"documentName": "AWSIncidents-CriticalIncidentRunbookTemplate",
				"documentVersion": "$DEFAULT",
				"roleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager",
				"targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"
			}
		}
	],
	"chatChannel": {
		"chatbotSns": ["arn:aws:sns:us-east-1:111122223333:Standard_User"]
	},
	"displayName": "Example response plan",
	"engagements": ["arn:aws:ssm-contacts:us-east-1:111122223333:contact/example"],
	"incidentTemplate": {
		"impact": 5,
		"title": "example-incident"
	},
	"name": "example-response",
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateResponsePlan_Example_1_Response"></a>

```
{
	"arn":"arn:aws:ssm-incidents::111122223333:response-plan/example-response"
}
```

## See Also
<a name="API_CreateResponsePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/CreateResponsePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/CreateResponsePlan)
