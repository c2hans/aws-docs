---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetrics.html
---

# GetResourceMetrics
<a name="API_GetResourceMetrics"></a>

Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide filtering criteria for each group. You must specify an aggregate function for each metric.

**Note**
Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.

## Request Syntax
<a name="API_GetResourceMetrics_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "Identifier": "{{string}}",
   "MaxResults": {{number}},
   "MetricQueries": [
      {
         "Filter": {
            "{{string}}" : "{{string}}"
         },
         "GroupBy": {
            "Dimensions": [ "{{string}}" ],
            "Group": "{{string}}",
            "Limit": {{number}}
         },
         "Metric": "{{string}}"
      }
   ],
   "NextToken": "{{string}}",
   "PeriodAlignment": "{{string}}",
   "PeriodInSeconds": {{number}},
   "ServiceType": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_GetResourceMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [EndTime](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-EndTime"></a>
The date and time specifying the end of the requested time series query range. The value specified is *exclusive*. Thus, the command returns data points less than (but not equal to) `EndTime`.
The value for `EndTime` must be later than the value for `StartTime`.
Type: Timestamp
Required: Yes

 ** [Identifier](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [MetricQueries](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-MetricQueries"></a>
An array of one or more queries to perform. Each query must specify a Performance Insights metric and specify an aggregate function, and you can provide filtering criteria. You must append the aggregate function to the metric. For example, to find the average for the metric `db.load` you must use `db.load.avg`. Valid values for aggregate functions include `.avg`, `.min`, `.max`, and `.sum`.
Type: Array of [MetricQuery](API_MetricQuery.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: Yes

 ** [ServiceType](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics. Valid values are as follows:
+  `RDS`
+  `DOCDB`
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [StartTime](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-StartTime"></a>
The date and time specifying the beginning of the requested time series query range. You can't specify a `StartTime` that is earlier than 7 days ago. By default, Performance Insights has 7 days of retention, but you can extend this range up to 2 years. The value specified is *inclusive*. Thus, the command returns data points equal to or greater than `StartTime`.
The value for `StartTime` must be earlier than the value for `EndTime`.
Type: Timestamp
Required: Yes

 ** [MaxResults](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-MaxResults"></a>
The maximum number of items to return in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

 ** [PeriodAlignment](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-PeriodAlignment"></a>
The returned timestamp which is the start or end time of the time periods. The default value is `END_TIME`.
Type: String
Valid Values: `END_TIME | START_TIME`
Required: No

 ** [PeriodInSeconds](#API_GetResourceMetrics_RequestSyntax) **   <a name="performanceinsights-GetResourceMetrics-request-PeriodInSeconds"></a>
The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:
+  `1` (one second)
+  `60` (one minute)
+  `300` (five minutes)
+  `3600` (one hour)
+  `86400` (twenty-four hours)
If you don't specify `PeriodInSeconds`, then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.
Type: Integer
Required: No

## Response Syntax
<a name="API_GetResourceMetrics_ResponseSyntax"></a>

```
{
   "AlignedEndTime": number,
   "AlignedStartTime": number,
   "Identifier": "string",
   "MetricList": [
      {
         "DataPoints": [
            {
               "Timestamp": number,
               "Value": number
            }
         ],
         "Key": {
            "Dimensions": {
               "string" : "string"
            },
            "Metric": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetResourceMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlignedEndTime](#API_GetResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetrics-response-AlignedEndTime"></a>
The end time for the returned metrics, after alignment to a granular boundary (as specified by `PeriodInSeconds`). `AlignedEndTime` will be greater than or equal to the value of the user-specified `Endtime`.
Type: Timestamp

 ** [AlignedStartTime](#API_GetResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetrics-response-AlignedStartTime"></a>
The start time for the returned metrics, after alignment to a granular boundary (as specified by `PeriodInSeconds`). `AlignedStartTime` will be less than or equal to the value of the user-specified `StartTime`.
Type: Timestamp

 ** [Identifier](#API_GetResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetrics-response-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`

 ** [MetricList](#API_GetResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetrics-response-MetricList"></a>
An array of metric results, where each array element contains all of the data points for a particular dimension.
Type: Array of [MetricKeyDataPoints](API_MetricKeyDataPoints.md) objects

 ** [NextToken](#API_GetResourceMetrics_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetrics-response-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

## Errors
<a name="API_GetResourceMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
The request failed due to an unknown error.
HTTP Status Code: 500

 ** InvalidArgumentException **
One of the arguments provided is invalid for this request.
HTTP Status Code: 400

 ** NotAuthorizedException **
The user is not authorized to perform this request.
HTTP Status Code: 400

## Examples
<a name="API_GetResourceMetrics_Examples"></a>

### Retrieve Data Points for All Dimensions Within a Group
<a name="API_GetResourceMetrics_Example_1"></a>

The following example requests data points for the `db.wait_event` dimension group, and for the `db.wait_event.name` dimension within that group. In the response, the relevant data points are grouped by the requested dimension (`db.wait_event.name`).

#### Sample Request
<a name="API_GetResourceMetrics_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "MetricQueries": [
        {
            "Metric": "db.load.avg",
            "GroupBy": {
                "Group": "db.wait_event",
                "Dimensions": ["db.wait_event.type"]
            }
        }
    ],
    "StartTime": 1527026400,
    "EndTime": 1527080400,
    "PeriodInSeconds": 300
}
```

#### Sample Response
<a name="API_GetResourceMetrics_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "AlignedEndTime": 1.5270804E9,
    "AlignedStartTime": 1.5270264E9,
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "MetricList": [
        {
            "Key": {
                "Metric": "db.load.avg"
            },
            "DataPoints": [
                {
                    "Timestamp": 1527026700.0,
                    "Value": 1.3533333333333333
                },
                {
                    "Timestamp": 1527027000.0,
                    "Value": 0.88
                },
                ...
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1527026700.0,
                    "Value": 0.8566666666666667
                },
                {
                    "Timestamp": 1527027000.0,
                    "Value": 0.8633333333333333
                },
                ...
            ],
        },
        ...
    ]
}
```

## See Also
<a name="API_GetResourceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/GetResourceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/GetResourceMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
