---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html
---

# GetMetricData
<a name="API_GetMetricData"></a>

Gets historical metric data from the specified Connect Customer instance.

For a description of each historical metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.

**Note**
We recommend using the [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API. It provides more flexibility, features, and the ability to query longer time ranges than `GetMetricData`. Use it to retrieve historical agent and contact metrics for the last 3 months, at varying intervals. You can also use it to build custom dashboards to measure historical queue and agent performance. For example, you can track the number of incoming contacts for the last 7 days, with data split by day, to see how contact volume changed per day of the week.

## Request Syntax
<a name="API_GetMetricData_RequestSyntax"></a>

```
POST /metrics/historical/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "Filters": {
      "AgentStatuses": [ "{{string}}" ],
      "Channels": [ "{{string}}" ],
      "Queues": [ "{{string}}" ],
      "RoutingProfiles": [ "{{string}}" ],
      "RoutingStepExpressions": [ "{{string}}" ],
      "Subtypes": [ "{{string}}" ],
      "ValidationTestTypes": [ "{{string}}" ]
   },
   "Groupings": [ "{{string}}" ],
   "HistoricalMetrics": [
      {
         "Name": "{{string}}",
         "Statistic": "{{string}}",
         "Threshold": {
            "Comparison": "{{string}}",
            "ThresholdValue": {{number}}
         },
         "Unit": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GetMetricData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetMetricData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-EndTime"></a>
The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.
The time range between the start and end time must be less than 24 hours.
Type: Timestamp
Required: Yes

 ** [Filters](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-Filters"></a>
The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is retrieved only for the resources associated with the queues or channels included in the filter. You can include both queue IDs and queue ARNs in the same request. VOICE, CHAT, and TASK channels are supported.
RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.
To filter by `Queues`, enter the queue ID/ARN, not the name of the queue.
Type: [Filters](API_Filters.md) object
Required: Yes

 ** [Groupings](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-Groupings"></a>
The grouping applied to the metrics returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.
If no grouping is specified, a summary of metrics for all queues is returned.
RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.
Type: Array of strings
Array Members: Maximum number of 2 items.
Valid Values: `QUEUE | CHANNEL | ROUTING_PROFILE | ROUTING_STEP_EXPRESSION | AGENT_STATUS | SUBTYPE | VALIDATION_TEST_TYPE`
Required: No

 ** [HistoricalMetrics](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-HistoricalMetrics"></a>
The metrics to retrieve. Specify the name, unit, and statistic for each metric. The following historical metrics are available. For a description of each metric, see [Metrics definition](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.
This API does not support a contacts incoming metric (there's no CONTACTS\_INCOMING metric missing from the documented list).
ABANDON\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average queue abandon time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time)
AFTER\_CONTACT\_WORK\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [After contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)
API\_CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [API contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#api-contacts-handled)
AVG\_HOLD\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time)
CALLBACK\_CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [Callback contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-contacts-handled)
CONTACTS\_ABANDONED
Unit: COUNT
Statistic: SUM
UI name: [Contacts abandoned](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned)
CONTACTS\_AGENT\_HUNG\_UP\_FIRST
Unit: COUNT
Statistic: SUM
UI name: [Contacts agent hung up first](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-agent-hung-up-first)
CONTACTS\_CONSULTED
Unit: COUNT
Statistic: SUM
UI name: [Contacts consulted](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-consulted)
CONTACTS\_HANDLED
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled)
CONTACTS\_HANDLED\_INCOMING
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled incoming](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-incoming)
CONTACTS\_HANDLED\_OUTBOUND
Unit: COUNT
Statistic: SUM
UI name: [Contacts handled outbound](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-outbound)
CONTACTS\_HOLD\_ABANDONS
Unit: COUNT
Statistic: SUM
UI name: [Contacts hold disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect)
CONTACTS\_MISSED
Unit: COUNT
Statistic: SUM
UI name: [AGENT\_NON\_RESPONSE](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response)
CONTACTS\_QUEUED
Unit: COUNT
Statistic: SUM
UI name: [Contacts queued](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued)
CONTACTS\_TRANSFERRED\_IN
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred in](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-in)
CONTACTS\_TRANSFERRED\_IN\_FROM\_QUEUE
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)
CONTACTS\_TRANSFERRED\_OUT
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out)
CONTACTS\_TRANSFERRED\_OUT\_FROM\_QUEUE
Unit: COUNT
Statistic: SUM
UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)
HANDLE\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time)
INTERACTION\_AND\_HOLD\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average agent interaction and customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time)
INTERACTION\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aaverage-agent-interaction-time)
OCCUPANCY
Unit: PERCENT
Statistic: AVG
UI name: [Occupancy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy)
QUEUE\_ANSWER\_TIME
Unit: SECONDS
Statistic: AVG
UI name: [Average queue answer time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html##average-queue-answer-time)
QUEUED\_TIME
Unit: SECONDS
Statistic: MAX
UI name: [Minimum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time)
SERVICE\_LEVEL
You can include up to 20 SERVICE\_LEVEL metrics in a request.
Unit: PERCENT
Statistic: AVG
Threshold: For `ThresholdValue`, enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison`, you must enter `LT` (for "Less than").
UI name: [Average queue abandon time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time)
Type: Array of [HistoricalMetric](API_HistoricalMetric.md) objects
Required: Yes

 ** [MaxResults](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Required: No

 ** [StartTime](#API_GetMetricData_RequestSyntax) **   <a name="connect-GetMetricData-request-StartTime"></a>
The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.
The start time cannot be earlier than 24 hours before the time of the request. Historical metrics are available only for 24 hours.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetMetricData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricResults": [
      {
         "Collections": [
            {
               "Metric": {
                  "Name": "string",
                  "Statistic": "string",
                  "Threshold": {
                     "Comparison": "string",
                     "ThresholdValue": number
                  },
                  "Unit": "string"
               },
               "Value": number
            }
         ],
         "Dimensions": {
            "AgentStatus": {
               "Arn": "string",
               "Id": "string"
            },
            "Channel": "string",
            "Queue": {
               "Arn": "string",
               "Id": "string"
            },
            "RoutingProfile": {
               "Arn": "string",
               "Id": "string"
            },
            "RoutingStepExpression": "string",
            "Subtype": "string",
            "ValidationTestType": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricResults](#API_GetMetricData_ResponseSyntax) **   <a name="connect-GetMetricData-response-MetricResults"></a>
Information about the historical metrics.
If no grouping is specified, a summary of metric data is returned.
Type: Array of [HistoricalMetricResult](API_HistoricalMetricResult.md) objects

 ** [NextToken](#API_GetMetricData_ResponseSyntax) **   <a name="connect-GetMetricData-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.
Type: String

## Errors
<a name="API_GetMetricData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_GetMetricData_Examples"></a>

### Example
<a name="API_GetMetricData_Example_1"></a>

The following example retrieves the specified historical metrics.

#### Sample Request
<a name="API_GetMetricData_Example_1_Request"></a>

```
{
   "InstanceId" : "12345678-1234-5678-aabb-123456abcdef",
   "StartTime": 1548979200,
   "EndTime": 1549051200,
   "Filters" : {
      "Queues" : [
         "11111111-2222-fcfc-abab-333333333333"
      ],
      "Channels" : ["VOICE"]
   },
   "Groupings" : [
      "QUEUE",
      "CHANNEL"
   ],
   "HistoricalMetrics" : [
      {
         "Name" : "AFTER_CONTACT_WORK_TIME",
         "Unit" : "SECONDS",
         "Statistic" : "AVG"
      },
      {
         "Name" : "CONTACTS_QUEUED",
         "Unit" : "COUNT",
         "Statistic" : "SUM"
      },
      {
         "Name" : "CONTACTS_HANDLED",
         "Unit" : "COUNT",
         "Statistic" : "SUM"
      },
      {
         "Name" : "HANDLE_TIME",
         "Unit" : "SECONDS",
         "Statistic" : "AVG"
      },
      {
         "Name" : "CONTACTS_TRANSFERRED_OUT",
         "Unit" : "COUNT",
         "Statistic" : "SUM"
      },
      {
         "Name" : "CONTACTS_MISSED",
         "Unit" : "COUNT",
         "Statistic" : "SUM"
      },
      {
         "Name" : "OCCUPANCY",
         "Unit" : "PERCENT",
         "Statistic" : "AVG"
      },
      {
         "Name" : "QUEUED_TIME",
         "Unit" : "SECONDS",
         "Statistic" : "MAX"
      },
      {
         "Name" : "HOLD_TIME",
         "Unit" : "SECONDS",
         "Statistic" : "AVG"
      },
      {
         "Name" : "SERVICE_LEVEL",
         "Threshold" : {
            "Comparison" : "LT",
            "ThresholdValue" : 60.0
         },
         "Unit" : "PERCENT",
         "Statistic" : "AVG"
      },
      {
         "Name" : "SERVICE_LEVEL",
         "Threshold" : {
            "Comparison" : "LT",
            "ThresholdValue" : 120.0
         },
         "Unit" : "PERCENT",
         "Statistic" : "AVG"
      },
      {
         "Name" : "SERVICE_LEVEL",
         "Threshold" : {
            "Comparison" : "LT",
            "ThresholdValue" : 30.0
         },
         "Unit" : "PERCENT",
         "Statistic" : "AVG"
      }
   ]
}
```

#### Sample Response
<a name="API_GetMetricData_Example_1_Response"></a>

```
{
   "MetricResults": [
      {
         "Collections": [
            {
               "Metric": {
                  "Name": "OCCUPANCY",
                  "Statistic": "AVG",
                  "Threshold": null,
                  "Unit": "PERCENT"
               },
               "Value": 0
            },
            {
               "Metric": {
                  "Name": "CONTACTS_MISSED",
                  "Statistic": "SUM",
                  "Threshold": null,
                  "Unit": "COUNT"
               },
               "Value": 0
            }
         ],
         "Dimensions": {
            "Channel": "VOICE",
            "Queue": {
               "Arn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/queue/11111111-2222-fcfc-abab-333333333333",
               "Id": "11111111-2222-fcfc-abab-333333333333"
            }
         }
      }
   ]
}
```

## See Also
<a name="API_GetMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetMetricData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetMetricData)
