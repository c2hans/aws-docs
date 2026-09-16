---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html
---

# GetCurrentMetricData
<a name="API_GetCurrentMetricData"></a>

Gets the real-time metric data from the specified Connect Customer instance.

For a description of each metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.

**Note**
When you make a successful API request, you can expect the following metric values in the response:
 **Metric value is null**: The calculation cannot be performed due to divide by zero or insufficient data
 **Metric value is a number (including 0) of defined type**: The number provided is the calculation result
 **MetricResult list is empty**: The request cannot find any data in the system
The following guidelines can help you work with the API:
Each dimension in the metric response must contain a value
Each item in MetricResult must include all requested metrics
If the response is slow due to large result sets, try these approaches:
Add filters to reduce the amount of data returned

## Request Syntax
<a name="API_GetCurrentMetricData_RequestSyntax"></a>

```
POST /metrics/current/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "CurrentMetrics": [
      {
         "MetricId": "{{string}}",
         "Name": "{{string}}",
         "Unit": "{{string}}"
      }
   ],
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
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortCriteria": [
      {
         "SortByMetric": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetCurrentMetricData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetCurrentMetricData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CurrentMetrics](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-CurrentMetrics"></a>
The metrics to retrieve. Specify the name or metricId, and unit for each metric. The following metrics are available. For a description of all the metrics, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.
 MetricId should be used to reference custom metrics or out of the box metrics as Arn. If using MetricId, the limit is 10 MetricId per request.
AGENTS\_AFTER\_CONTACT\_WORK
Unit: COUNT
Name in real-time metrics report: [ACW](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aftercallwork-real-time)
AGENTS\_AVAILABLE
Unit: COUNT
Name in real-time metrics report: [Available](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#available-real-time)
AGENTS\_ERROR
Unit: COUNT
Name in real-time metrics report: [Error](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#error-real-time)
AGENTS\_NON\_PRODUCTIVE
Unit: COUNT
Name in real-time metrics report: [NPT (Non-Productive Time)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-productive-time-real-time)
AGENTS\_ON\_CALL
Unit: COUNT
Name in real-time metrics report: [On contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time)
AGENTS\_ON\_CONTACT
Unit: COUNT
Name in real-time metrics report: [On contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time)
AGENTS\_ONLINE
Unit: COUNT
Name in real-time metrics report: [Online](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#online-real-time)
AGENTS\_STAFFED
Unit: COUNT
Name in real-time metrics report: [Staffed](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#staffed-real-time)
CONTACTS\_IN\_QUEUE
Unit: COUNT
Name in real-time metrics report: [In queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#in-queue-real-time)
CONTACTS\_SCHEDULED
Unit: COUNT
Name in real-time metrics report: [Scheduled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled-real-time)
ESTIMATED\_WAIT\_TIME
Unit: SECONDS
This metric supports filter and grouping combination only used for core routing purpose. Valid filter and grouping use cases:
+ Filter by a list of [Queues] and a list of [Channels], group by [“QUEUE”, “CHANNEL”]
+ Filter by a singleton list of [Queue], a singleton list of [Channel], a list of [RoutingStepExpression], group by [“ROUTING\_STEP\_EXPRESSION”].
OLDEST\_CONTACT\_AGE
Unit: SECONDS
When you use groupings, Unit says SECONDS and the Value is returned in SECONDS.
When you do not use groupings, Unit says SECONDS but the Value is returned in MILLISECONDS. For example, if you get a response like this:
 `{ "Metric": { "Name": "OLDEST_CONTACT_AGE", "Unit": "SECONDS" }, "Value": 24113.0 `}
The actual OLDEST\_CONTACT\_AGE is 24 seconds.
When the filter `RoutingStepExpression` is used, this metric is still calculated from enqueue time. For example, if a contact that has been queued under `<Expression 1>` for 10 seconds has expired and `<Expression 2>` becomes active, then `OLDEST_CONTACT_AGE` for this queue will be counted starting from 10, not 0.
Name in real-time metrics report: [Oldest](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#oldest-real-time)
SLOTS\_ACTIVE
Unit: COUNT
Name in real-time metrics report: [Active](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#active-real-time)
SLOTS\_AVAILABLE
Unit: COUNT
Name in real-time metrics report: [Availability](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#availability-real-time)
Type: Array of [CurrentMetric](API_CurrentMetric.md) objects
Required: Yes

 ** [Filters](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-Filters"></a>
The filters to apply to returned metrics. You can filter up to the following limits:
+ Queues: 100
+ Routing profiles: 100
+ Channels: 3 (VOICE, CHAT, and TASK channels are supported.)
+ RoutingStepExpressions: 50
+ AgentStatuses: 50
+ Subtypes: 10
+ ValidationTestTypes: 10
Metric data is retrieved only for the resources associated with the queues or routing profiles, and by any channels included in the filter. (You cannot filter by both queue AND routing profile.) You can include both resource IDs and resource ARNs in the same request.
When using `AgentStatuses` as filter make sure Queues is added as primary filter.
When using `Subtypes` as filter make sure Queues is added as primary filter.
When using `ValidationTestTypes` as filter make sure Queues is added as primary filter.
When using the `RoutingStepExpression` filter, you need to pass exactly one `QueueId`. The filter is also case sensitive so when using the `RoutingStepExpression` filter, grouping by `ROUTING_STEP_EXPRESSION` is required.
Currently tagging is only supported on the resources that are passed in the filter.
Type: [Filters](API_Filters.md) object
Required: Yes

 ** [Groupings](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-Groupings"></a>
Defines the level of aggregation for metrics data by a dimension(s). Its similar to sorting items into buckets based on a common characteristic, then counting or calculating something for each bucket. For example, when grouped by `QUEUE`, the metrics returned apply to each queue rather than aggregated for all queues.
The grouping list is an ordered list, with the first item in the list defined as the primary grouping. If no grouping is included in the request, the aggregation happens at the instance-level.
+ If you group by `CHANNEL`, you should include a Channels filter. VOICE, CHAT, and TASK channels are supported.
+ If you group by `AGENT_STATUS`, you must include the `QUEUE` as the primary grouping and use queue filter. When you group by `AGENT_STATUS`, the only metric available is the `AGENTS_ONLINE` metric.
+ If you group by `SUBTYPE` or `VALIDATION_TEST_TYPE` as secondary grouping then you must include `QUEUE` as primary grouping and use Queue as filter
+ If you group by `ROUTING_PROFILE`, you must include either a queue or routing profile filter. In addition, a routing profile filter is required for metrics `CONTACTS_SCHEDULED`, `CONTACTS_IN_QUEUE`, and ` OLDEST_CONTACT_AGE`.
+ When using the `RoutingStepExpression` filter, group by `ROUTING_STEP_EXPRESSION` is required.
Type: Array of strings
Array Members: Maximum number of 2 items.
Valid Values: `QUEUE | CHANNEL | ROUTING_PROFILE | ROUTING_STEP_EXPRESSION | AGENT_STATUS | SUBTYPE | VALIDATION_TEST_TYPE`
Required: No

 ** [MaxResults](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.
Type: String
Required: No

 ** [SortCriteria](#API_GetCurrentMetricData_RequestSyntax) **   <a name="connect-GetCurrentMetricData-request-SortCriteria"></a>
The way to sort the resulting response based on metrics. You can enter one sort criteria. By default resources are sorted based on `AGENTS_ONLINE`, `DESCENDING`. The metric collection is sorted based on the input metrics.
Note the following:
+ Sorting on `SLOTS_ACTIVE` and `SLOTS_AVAILABLE` is not supported.
Type: Array of [CurrentMetricSortCriteria](API_CurrentMetricSortCriteria.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_GetCurrentMetricData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "DataSnapshotTime": number,
   "MetricResults": [
      {
         "Collections": [
            {
               "Metric": {
                  "MetricId": "string",
                  "Name": "string",
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
<a name="API_GetCurrentMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_GetCurrentMetricData_ResponseSyntax) **   <a name="connect-GetCurrentMetricData-response-ApproximateTotalCount"></a>
The total count of the result, regardless of the current page size.
Type: Long

 ** [DataSnapshotTime](#API_GetCurrentMetricData_ResponseSyntax) **   <a name="connect-GetCurrentMetricData-response-DataSnapshotTime"></a>
The time at which the metrics were retrieved and cached for pagination.
Type: Timestamp

 ** [MetricResults](#API_GetCurrentMetricData_ResponseSyntax) **   <a name="connect-GetCurrentMetricData-response-MetricResults"></a>
Information about the real-time metrics.
Type: Array of [CurrentMetricResult](API_CurrentMetricResult.md) objects

 ** [NextToken](#API_GetCurrentMetricData_ResponseSyntax) **   <a name="connect-GetCurrentMetricData-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.
Type: String

## Errors
<a name="API_GetCurrentMetricData_Errors"></a>

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
<a name="API_GetCurrentMetricData_Examples"></a>

### Example
<a name="API_GetCurrentMetricData_Example_1"></a>

The following example retrieves the specified real-time metrics.

#### Sample Request
<a name="API_GetCurrentMetricData_Example_1_Request"></a>

```
{{
  "InstanceId": "12345678-1234-5678-aabb-123456abcdef",
  "Filters": {
    "Queues": [
      "11111111-2222-fcfc-abab-333333333333",
      "arn:aws:connect:us-east-1:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/queue/11111111-2222-fcfc-abab-333333333333"
    ],
    "Channels": ["VOICE"]
  },
  "Groupings": ["CHANNEL", "QUEUE"],
  "CurrentMetrics": [
    {
      "Name": "AGENTS_ONLINE",
      "Unit": "COUNT"
    },
    {
      "Name": "AGENTS_AVAILABLE",
      "Unit": "COUNT"
    },
    {
      "Name": "OLDEST_CONTACT_AGE",
      "Unit": "SECONDS"
    },
    {
      "Name": "AGENTS_ERROR",
      "Unit": "COUNT"
    },
    {
    "Name": "ESTIMATED_WAIT_TIME",
    "Unit": "SECONDS"
    }
  ],
  "SortCriteria": {
    "SortByMetric": "OLDEST_CONTACT_AGE",
    "SortOrder": "ASCENDING"
  }
}
```

#### Sample Response
<a name="API_GetCurrentMetricData_Example_1_Response"></a>

```
{
  "DataSnapshotTime": 1671222098.739,
  "ApproximateTotalCount": 1,
  "MetricResults": [
    {
      "Collections": [
        {
          "Metric": {
            "Name": "AGENTS_ONLINE",
            "Unit": "COUNT"
          },
          "Value": 1
        },
        {
          "Metric": {
            "Name": "AGENTS_AVAILABLE",
            "Unit": "COUNT"
          },
          "Value": 1
        },
        {
          "Metric": {
            "Name": "OLDEST_CONTACT_AGE",
            "Unit": "SECONDS"
          },
          "Value": 0
        },
        {
          "Metric": {
            "Name": "AGENTS_ERROR",
            "Unit": "COUNT"
          },
          "Value": 0
        },
        {
            "Metric": {
                "Name": "ESTIMATED_WAIT_TIME",
                "Unit": "SECONDS"
            },
            "Value": 1.00
        }
      ],
      "Dimensions": {
        "Channel": "VOICE",
        "Queue": {
          "Arn": "arn:aws:connect:us-east-1:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/queue/11111111-2222-fcfc-abab-333333333333",
          "Id": "11111111-2222-fcfc-abab-333333333333"
        }
      }
    }
  ]
}
```

### Sample GetCurrentMetricData Request Using RoutingStepExpression
<a name="API_GetCurrentMetricData_Example_2"></a>

This example illustrates one usage of GetCurrentMetricData.

```
{
     "InstanceId": "12345678-1234-5678-aabb-123456abcdef",
    "CurrentMetrics": [
        {
            "Name": "OLDEST_CONTACT_AGE",
            "Unit": "SECONDS"
        },
        {
            "Name": "CONTACTS_IN_QUEUE",
            "Unit": "COUNT"
        }
    ],
    "Filters": {
        "Queues": [
            "11111111-2222-fcfc-abab-333333333333"
        ],
        "RoutingStepExpressions": [
            "{\"attributeCondition\":{\"proficiencyLevel\":1.0,\"comparisonOperator\":\"NumberGreaterOrEqualTo\",\"name\":\"Location\",\"value\":\"Earth\"}}"
        ]
    },
    "Groupings": [
        "ROUTING_STEP_EXPRESSION"
    ],
    "MaxResults": 10
}
```

## See Also
<a name="API_GetCurrentMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetCurrentMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetCurrentMetricData)
