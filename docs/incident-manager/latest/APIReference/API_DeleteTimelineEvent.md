---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteTimelineEvent.html
---

# DeleteTimelineEvent
<a name="API_DeleteTimelineEvent"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Deletes a timeline event from an incident.

## Request Syntax
<a name="API_DeleteTimelineEvent_RequestSyntax"></a>

```
POST /deleteTimelineEvent HTTP/1.1
Content-type: application/json

{
   "eventId": "{{string}}",
   "incidentRecordArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTimelineEvent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTimelineEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventId](#API_DeleteTimelineEvent_RequestSyntax) **   <a name="IncidentManager-DeleteTimelineEvent-request-eventId"></a>
The ID of the event to update. You can use `ListTimelineEvents` to find an event's ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

 ** [incidentRecordArn](#API_DeleteTimelineEvent_RequestSyntax) **   <a name="IncidentManager-DeleteTimelineEvent-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident that includes the timeline event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_DeleteTimelineEvent_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteTimelineEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteTimelineEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_DeleteTimelineEvent_Examples"></a>

### Example
<a name="API_DeleteTimelineEvent_Example_1"></a>

This example illustrates one usage of DeleteTimelineEvent.

#### Sample Request
<a name="API_DeleteTimelineEvent_Example_1_Request"></a>

```
POST /updateTimelineEvent HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.update-timeline-event
X-Amz-Date: 20210811T203312Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 261

{
	"eventId": "a4bd9b45-1fcf-64c3-9d53-121d0f53a7ec",
	"eventTime": 1621620657,
	"incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/64bd9b45-1d0e-2622-840d-03a87a1451fa",
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_DeleteTimelineEvent_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteTimelineEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/DeleteTimelineEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/DeleteTimelineEvent)
