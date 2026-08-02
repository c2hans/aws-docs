---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListTimelineEvents.html
---

# ListTimelineEvents
<a name="API_ListTimelineEvents"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists timeline events for the specified incident record.

## Request Syntax
<a name="API_ListTimelineEvents_RequestSyntax"></a>

```
POST /listTimelineEvents HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "condition": { ... },
         "key": "{{string}}"
      }
   ],
   "incidentRecordArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTimelineEvents_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTimelineEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-filters"></a>
Filters the timeline events based on the provided conditional values. You can filter timeline events with the following keys:
+  `eventReference`
+  `eventTime`
+  `eventType`
Note the following when deciding how to use Filters:
+ If you don't specify a Filter, the response includes all timeline events.
+ If you specify more than one filter in a single request, the response returns timeline events that match all filters.
+ If you specify a filter with more than one value, the response returns timeline events that match any of the values provided.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [incidentRecordArn](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident that includes the timeline event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [maxResults](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-maxResults"></a>
The maximum number of results per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [sortBy](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-sortBy"></a>
Sort timeline events by the specified key value pair.
Type: String
Valid Values: `EVENT_TIME`
Required: No

 ** [sortOrder](#API_ListTimelineEvents_RequestSyntax) **   <a name="IncidentManager-ListTimelineEvents-request-sortOrder"></a>
Sorts the order of timeline events by the value specified in the `sortBy` field.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListTimelineEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "eventSummaries": [
      {
         "eventId": "string",
         "eventReferences": [
            { ... }
         ],
         "eventTime": number,
         "eventType": "string",
         "eventUpdatedTime": number,
         "incidentRecordArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTimelineEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventSummaries](#API_ListTimelineEvents_ResponseSyntax) **   <a name="IncidentManager-ListTimelineEvents-response-eventSummaries"></a>
Details about each event that occurred during the incident.
Type: Array of [EventSummary](API_EventSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListTimelineEvents_ResponseSyntax) **   <a name="IncidentManager-ListTimelineEvents-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

## Errors
<a name="API_ListTimelineEvents_Errors"></a>

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
<a name="API_ListTimelineEvents_Examples"></a>

### Example
<a name="API_ListTimelineEvents_Example_1"></a>

This example illustrates one usage of ListTimelineEvents.

#### Sample Request
<a name="API_ListTimelineEvents_Example_1_Request"></a>

```
POST /listTimelineEvents HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-timeline-events
X-Amz-Date: 20210811T163348Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=AKIAIOSFODNN7EXAMPLE
Content-Length: 130

{
	"incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
}
```

#### Sample Response
<a name="API_ListTimelineEvents_Example_1_Response"></a>

```
{
    "eventSummaries": [
        {
            "eventId": "ecbd9919-bba6-d317-6cfc-7232df620b6d",
            "eventTime": "2021-08-10T22:33:58.724000+00:00",
            "eventReferences": [
                { "resource": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f" }
            ],
            "eventType": "SSM Incident Record Update",
            "eventUpdatedTime": "2021-08-10T22:33:58.724000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
        },
        {
            "eventId": "08bd9919-bad3-d3a8-58f5-f26c362fe79f",
            "eventTime": "2021-08-10T22:33:58+00:00",
            "eventReferences": [
                { "relatedItemId": "related-item/AUTOMATION/369DAA0D8B9CB4E1856C52FA2D0787EC" }
            ],
            "eventType": "SSM Automation Execution Start Failure for Incident",
            "eventUpdatedTime": "2021-08-10T22:33:58.439000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
        },
        {
            "eventId": "58bd9919-bc2e-030b-11f0-76dc0d95bb36",
            "eventTime": "2021-08-10T22:33:57+00:00",
            "eventReferences": [
                { "relatedItemId": "related-item/METRIC/F95638BAA087E072DC56189CB4D2ADEC" },
                { "resource": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f" }
            ],
            "eventType": "Custom Event",
            "eventUpdatedTime": "2021-08-10T22:33:59.132000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f"
        }
    ]
}
```

## See Also
<a name="API_ListTimelineEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListTimelineEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListTimelineEvents)
