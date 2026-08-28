---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetTimelineEvent.html
---

# GetTimelineEvent
<a name="API_GetTimelineEvent"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves a timeline event based on its ID and incident record.

## Request Syntax
<a name="API_GetTimelineEvent_RequestSyntax"></a>

```
GET /getTimelineEvent?eventId={{eventId}}&incidentRecordArn={{incidentRecordArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTimelineEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [eventId](#API_GetTimelineEvent_RequestSyntax) **   <a name="IncidentManager-GetTimelineEvent-request-uri-eventId"></a>
The ID of the event. You can get an event's ID when you create it, or by using `ListTimelineEvents`.
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

 ** [incidentRecordArn](#API_GetTimelineEvent_RequestSyntax) **   <a name="IncidentManager-GetTimelineEvent-request-uri-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident that includes the timeline event.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_GetTimelineEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTimelineEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "event": {
      "eventData": "string",
      "eventId": "string",
      "eventReferences": [
         { ... }
      ],
      "eventTime": number,
      "eventType": "string",
      "eventUpdatedTime": number,
      "incidentRecordArn": "string"
   }
}
```

## Response Elements
<a name="API_GetTimelineEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [event](#API_GetTimelineEvent_ResponseSyntax) **   <a name="IncidentManager-GetTimelineEvent-response-event"></a>
Details about the timeline event.
Type: [TimelineEvent](API_TimelineEvent.md) object

## Errors
<a name="API_GetTimelineEvent_Errors"></a>

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
<a name="API_GetTimelineEvent_Examples"></a>

### Example
<a name="API_GetTimelineEvent_Example_1"></a>

This example illustrates one usage of GetTimelineEvent.

#### Sample Request
<a name="API_GetTimelineEvent_Example_1_Request"></a>

```
GET /getTimelineEvent?eventId=ecbd9919-bba6-d317-6cfc-7232df620b6d&incidentRecordArn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Aincident-record%2Fexample-response%2F78bd9919-b9ac-962d-91e0-149960600e3f HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.get-timeline-event
X-Amz-Date: 20210811T165600Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetTimelineEvent_Example_1_Response"></a>

```
{
    "event": {
        "eventData": "{\"modifiedBy\":\"arn:aws:sts::111122223333:assumed-role/Admin/exampleUser\",\"modifiedAttributes\":[{\"attributeName\":\"relatedItems\",\"newValue\":\"{\\\"itemToAdd\\\":{\\\"identifier\\\":{\\\"type\\\":\\\"PARENT\\\",\\\"value\\\":{\\\"arn\\\":\\\"arn:aws:ssm:us-east-1:111122223333:opsItem/oi-4008965bf3a7\\\"}},\\\"title\\\":\\\"parentItem\\\"}}\"}],\"incidentTitle\":\"example-incident\"}",
        "eventId": "ecbd9919-bba6-d317-6cfc-7232df620b6d",
        "eventTime": "2021-08-10T22:33:58.724000+00:00",
       "eventReferences": [
            {"relatedItemId": "related-item/OTHER/0515FAE92F4A572650D73DC0224D00EF"},
            {"resource": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"}
         ],
        "eventType": "SSM Incident Record Update",
        "eventUpdatedTime": "2021-08-10T22:33:58.724000+00:00",
        "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
    }
}
```

## See Also
<a name="API_GetTimelineEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/GetTimelineEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/GetTimelineEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
