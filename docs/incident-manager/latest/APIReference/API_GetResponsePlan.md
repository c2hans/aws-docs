---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetResponsePlan.html
---

# GetResponsePlan
<a name="API_GetResponsePlan"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves the details of the specified response plan.

## Request Syntax
<a name="API_GetResponsePlan_RequestSyntax"></a>

```
GET /getResponsePlan?arn={{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResponsePlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetResponsePlan_RequestSyntax) **   <a name="IncidentManager-GetResponsePlan-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the response plan.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_GetResponsePlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResponsePlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actions": [
      { ... }
   ],
   "arn": "string",
   "chatChannel": { ... },
   "displayName": "string",
   "engagements": [ "string" ],
   "incidentTemplate": {
      "dedupeString": "string",
      "impact": number,
      "incidentTags": {
         "string" : "string"
      },
      "notificationTargets": [
         { ... }
      ],
      "summary": "string",
      "title": "string"
   },
   "integrations": [
      { ... }
   ],
   "name": "string"
}
```

## Response Elements
<a name="API_GetResponsePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actions](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-actions"></a>
The actions that this response plan takes at the beginning of the incident.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [arn](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-arn"></a>
The ARN of the response plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

 ** [chatChannel](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-chatChannel"></a>
The Amazon Q Developer in chat applications chat channel used for collaboration during an incident.
Type: [ChatChannel](API_ChatChannel.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [displayName](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-displayName"></a>
The long format name of the response plan. Can contain spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [engagements](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-engagements"></a>
The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-contacts:[a-z0-9-]*:([0-9]{12}):contact/[a-z0-9_-]+`

 ** [incidentTemplate](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-incidentTemplate"></a>
Details used to create the incident when using this response plan.
Type: [IncidentTemplate](API_IncidentTemplate.md) object

 ** [integrations](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-integrations"></a>
Information about third-party services integrated into the Incident Manager response plan.
Type: Array of [Integration](API_Integration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [name](#API_GetResponsePlan_ResponseSyntax) **   <a name="IncidentManager-GetResponsePlan-response-name"></a>
The short format name of the response plan. The name can't contain spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-_]*`

## Errors
<a name="API_GetResponsePlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

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
<a name="API_GetResponsePlan_Examples"></a>

### Example
<a name="API_GetResponsePlan_Example_1"></a>

This example illustrates one usage of GetResponsePlan.

#### Sample Request
<a name="API_GetResponsePlan_Example_1_Request"></a>

```
GET /getResponsePlan?arn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Aresponse-plan%2Fexample-response HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.get-response-plan
X-Amz-Date: 20210810T230500Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetResponsePlan_Example_1_Response"></a>

```
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
    "arn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response",
    "chatChannel": {
        "chatbotSns": [
            "arn:aws:sns:us-east-1:111122223333:Standard_User"
        ]
    },
    "displayName": "Example response plan",
    "engagements": [
        "arn:aws:ssm-contacts:us-east-1:111122223333:contact/example"
    ],
    "incidentTemplate": {
        "impact": 5,
        "title": "example-incident"
    },
    "name": "example-response"
}
```

## See Also
<a name="API_GetResponsePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/GetResponsePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/GetResponsePlan)
