---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetTimeSeriesServiceStatistics.html
---

# GetTimeSeriesServiceStatistics
<a name="API_GetTimeSeriesServiceStatistics"></a>

Get an aggregation of service statistics defined by a specific time range.

## Request Syntax
<a name="API_GetTimeSeriesServiceStatistics_RequestSyntax"></a>

```
POST /TimeSeriesServiceStatistics HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "EntitySelectorExpression": "{{string}}",
   "ForecastStatistics": {{boolean}},
   "GroupARN": "{{string}}",
   "GroupName": "{{string}}",
   "NextToken": "{{string}}",
   "Period": {{number}},
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GetTimeSeriesServiceStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTimeSeriesServiceStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-EndTime"></a>
The end of the time frame for which to aggregate statistics.
Type: Timestamp
Required: Yes

 ** [EntitySelectorExpression](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-EntitySelectorExpression"></a>
A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [ForecastStatistics](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-ForecastStatistics"></a>
The forecasted high and low fault count values. Forecast enabled requests require the EntitySelectorExpression ID be provided.
Type: Boolean
Required: No

 ** [GroupARN](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-GroupARN"></a>
The Amazon Resource Name (ARN) of the group for which to pull statistics from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [GroupName](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-GroupName"></a>
The case-sensitive name of the group for which to pull statistics from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [NextToken](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-NextToken"></a>
Pagination token.
Type: String
Required: No

 ** [Period](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-Period"></a>
Aggregation period in seconds.
Type: Integer
Required: No

 ** [StartTime](#API_GetTimeSeriesServiceStatistics_RequestSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-request-StartTime"></a>
The start of the time frame for which to aggregate statistics.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetTimeSeriesServiceStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContainsOldGroupVersions": boolean,
   "NextToken": "string",
   "TimeSeriesServiceStatistics": [
      {
         "EdgeSummaryStatistics": {
            "ErrorStatistics": {
               "OtherCount": number,
               "ThrottleCount": number,
               "TotalCount": number
            },
            "FaultStatistics": {
               "OtherCount": number,
               "TotalCount": number
            },
            "OkCount": number,
            "TotalCount": number,
            "TotalResponseTime": number
         },
         "ResponseTimeHistogram": [
            {
               "Count": number,
               "Value": number
            }
         ],
         "ServiceForecastStatistics": {
            "FaultCountHigh": number,
            "FaultCountLow": number
         },
         "ServiceSummaryStatistics": {
            "ErrorStatistics": {
               "OtherCount": number,
               "ThrottleCount": number,
               "TotalCount": number
            },
            "FaultStatistics": {
               "OtherCount": number,
               "TotalCount": number
            },
            "OkCount": number,
            "TotalCount": number,
            "TotalResponseTime": number
         },
         "Timestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_GetTimeSeriesServiceStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainsOldGroupVersions](#API_GetTimeSeriesServiceStatistics_ResponseSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-response-ContainsOldGroupVersions"></a>
A flag indicating whether or not a group's filter expression has been consistent, or if a returned aggregation might show statistics from an older version of the group's filter expression.
Type: Boolean

 ** [NextToken](#API_GetTimeSeriesServiceStatistics_ResponseSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-response-NextToken"></a>
Pagination token.
Type: String

 ** [TimeSeriesServiceStatistics](#API_GetTimeSeriesServiceStatistics_ResponseSyntax) **   <a name="xray-GetTimeSeriesServiceStatistics-response-TimeSeriesServiceStatistics"></a>
The collection of statistics.
Type: Array of [TimeSeriesServiceStatistics](API_TimeSeriesServiceStatistics.md) objects

## Errors
<a name="API_GetTimeSeriesServiceStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetTimeSeriesServiceStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetTimeSeriesServiceStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetTimeSeriesServiceStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
