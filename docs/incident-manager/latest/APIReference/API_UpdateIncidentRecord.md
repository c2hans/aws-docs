---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateIncidentRecord.html
---

# UpdateIncidentRecord
<a name="API_UpdateIncidentRecord"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Update the details of an incident record. You can use this operation to update an incident record from the defined chat channel. For more information about using actions in chat channels, see [Interacting through chat](https://docs.aws.amazon.com/incident-manager/latest/userguide/chat.html#chat-interact).

## Request Syntax
<a name="API_UpdateIncidentRecord_RequestSyntax"></a>

```
POST /updateIncidentRecord HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "chatChannel": { ... },
   "clientToken": "{{string}}",
   "impact": {{number}},
   "notificationTargets": [
      { ... }
   ],
   "status": "{{string}}",
   "summary": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIncidentRecord_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIncidentRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-arn"></a>
The Amazon Resource Name (ARN) of the incident record you are updating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [chatChannel](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-chatChannel"></a>
The Amazon Q Developer in chat applications chat channel where responders can collaborate.
Type: [ChatChannel](API_ChatChannel.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [clientToken](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-clientToken"></a>
A token that ensures that a client calls the operation only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [impact](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-impact"></a>
Defines the impact of the incident to customers and applications. If you provide an impact for an incident, it overwrites the impact provided by the response plan.

**Supported impact codes**
+  `1` - Critical
+  `2` - High
+  `3` - Medium
+  `4` - Low
+  `5` - No Impact
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [notificationTargets](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-notificationTargets"></a>
The Amazon SNS targets that Incident Manager notifies when a client updates an incident.
Using multiple SNS topics creates redundancy in the event that a Region is down during the incident.
Type: Array of [NotificationTargetItem](API_NotificationTargetItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [status](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-status"></a>
The status of the incident. Possible statuses are `Open` or `Resolved`.
Type: String
Valid Values: `OPEN | RESOLVED`
Required: No

 ** [summary](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-summary"></a>
A longer description of what occurred during the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Required: No

 ** [title](#API_UpdateIncidentRecord_RequestSyntax) **   <a name="IncidentManager-UpdateIncidentRecord-request-title"></a>
A brief description of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

## Response Syntax
<a name="API_UpdateIncidentRecord_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateIncidentRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateIncidentRecord_Errors"></a>

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
<a name="API_UpdateIncidentRecord_Examples"></a>

### Example
<a name="API_UpdateIncidentRecord_Example_1"></a>

This example illustrates one usage of UpdateIncidentRecord.

#### Sample Request
<a name="API_UpdateIncidentRecord_Example_1_Request"></a>

```
POST /updateIncidentRecord HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.update-incident-record
X-Amz-Date: 20210811T184336Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 193

{
	"arn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/1abd9b35-ff4c-eb47-f20f-712a6c4c88cc",
	"status": "RESOLVED",
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateIncidentRecord_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateIncidentRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/UpdateIncidentRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/UpdateIncidentRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
