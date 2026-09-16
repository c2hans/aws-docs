---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateTimelineEvent.html
---

# CreateTimelineEvent
<a name="API_CreateTimelineEvent"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Creates a custom timeline event on the incident details page of an incident record. Incident Manager automatically creates timeline events that mark key moments during an incident. You can create custom timeline events to mark important events that Incident Manager can detect automatically.

## Request Syntax
<a name="API_CreateTimelineEvent_RequestSyntax"></a>

```
POST /createTimelineEvent HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "eventData": "{{string}}",
   "eventReferences": [
      { ... }
   ],
   "eventTime": {{number}},
   "eventType": "{{string}}",
   "incidentRecordArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTimelineEvent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTimelineEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-clientToken"></a>
A token that ensures that a client calls the action only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [eventData](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-eventData"></a>
A short description of the event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12000.
Required: Yes

 ** [eventReferences](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-eventReferences"></a>
Adds one or more references to the `TimelineEvent`. A reference is an AWS resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with a resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use the table's ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.
Type: Array of [EventReference](API_EventReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [eventTime](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-eventTime"></a>
The timestamp for when the event occurred.
Type: Timestamp
Required: Yes

 ** [eventType](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-eventType"></a>
The type of event. You can create timeline events of type `Custom Event` and `Note`.
To make a Note-type event appear on the *Incident notes* panel in the console, specify `eventType` as `Note`and enter the Amazon Resource Name (ARN) of the incident as the value for `eventReference`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: Yes

 ** [incidentRecordArn](#API_CreateTimelineEvent_RequestSyntax) **   <a name="IncidentManager-CreateTimelineEvent-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident record that the action adds the incident to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_CreateTimelineEvent_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "eventId": "string",
   "incidentRecordArn": "string"
}
```

## Response Elements
<a name="API_CreateTimelineEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [eventId](#API_CreateTimelineEvent_ResponseSyntax) **   <a name="IncidentManager-CreateTimelineEvent-response-eventId"></a>
The ID of the event for easy reference later.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.

 ** [incidentRecordArn](#API_CreateTimelineEvent_ResponseSyntax) **   <a name="IncidentManager-CreateTimelineEvent-response-incidentRecordArn"></a>
The ARN of the incident record that you added the event to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

## Errors
<a name="API_CreateTimelineEvent_Errors"></a>

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
<a name="API_CreateTimelineEvent_Examples"></a>

### Example
<a name="API_CreateTimelineEvent_Example_1"></a>

This example illustrates one usage of CreateTimelineEvent.

#### Sample Request
<a name="API_CreateTimelineEvent_Example_1_Request"></a>

```
POST /createTimelineEvent HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.create-timeline-event
X-Amz-Date: 20210810T221725Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 282

{
	"eventData": "\"example timeline event"\",
	"eventTime": 1601584200,
	"eventType": "Note",
	"incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/bebd9911-63a7-672f-820b-63731EXAMPLE",
	"eventReferences": "arn:aws:ssm-incidents::111122223333:incident-record/example-incident/6cc46130-ca6c-3b38-68f1-f6abeEXAMPLE",
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateTimelineEvent_Example_1_Response"></a>

```
{
 	"eventId":"56bd9912-28e5-b4fc-ec3e-ca4f06309c99",
 	"incidentRecordArn":"arn:aws:ssm-incidents::111122223333:incident-record/example-response/bebd9911-63a7-672f-820b-63731f2543ad"
 }
```

## See Also
<a name="API_CreateTimelineEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/CreateTimelineEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/CreateTimelineEvent)
