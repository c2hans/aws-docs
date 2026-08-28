---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_StartQuery.html
---

# StartQuery
<a name="API_StartQuery"></a>

Start a query to return data for a specific query type for the Internet Monitor query interface. Specify a time period for the data that you want returned by using `StartTime` and `EndTime`. You filter the query results to return by providing parameters that you specify with `FilterParameters`.

For more information about using the query interface, including examples, see [Using the Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Internet Monitor User Guide.

## Request Syntax
<a name="API_StartQuery_RequestSyntax"></a>

```
POST /v20210603/Monitors/{{MonitorName}}/Queries HTTP/1.1
Content-type: application/json

{
   "EndTime": "{{string}}",
   "FilterParameters": [
      {
         "Field": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "LinkedAccountId": "{{string}}",
   "QueryType": "{{string}}",
   "StartTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MonitorName](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-uri-MonitorName"></a>
The name of the monitor to query.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_StartQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-EndTime"></a>
The timestamp that is the end of the period that you want to retrieve data for with your query.
Type: Timestamp
Required: Yes

 ** [FilterParameters](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-FilterParameters"></a>
The `FilterParameters` field that you use with Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.
For more information about specifying filter parameters, see [Using the Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Internet Monitor User Guide.
Type: Array of [FilterParameter](API_FilterParameter.md) objects
Required: No

 ** [LinkedAccountId](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-LinkedAccountId"></a>
The account ID for an account that you've set up cross-account sharing for in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Internet Monitor User Guide.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** [QueryType](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-QueryType"></a>
The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:
+  `MEASUREMENTS`: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.
+  `TOP_LOCATIONS`: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.
+  `TOP_LOCATION_DETAILS`: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.
+  `OVERALL_TRAFFIC_SUGGESTIONS`: Provides TTFB, using a 30-day weighted average, for all traffic in each AWS location that is monitored.
+  `OVERALL_TRAFFIC_SUGGESTIONS_DETAILS`: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed AWS location. Must provide an AWS location to search.
+  `ROUTING_SUGGESTIONS`: Provides the predicted average round-trip time (RTT) from an IP prefix toward an AWS location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.
For lists of the fields returned with each query type and more information about how each type of query is performed, see [ Using the Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Internet Monitor User Guide.
Type: String
Valid Values: `MEASUREMENTS | TOP_LOCATIONS | TOP_LOCATION_DETAILS | OVERALL_TRAFFIC_SUGGESTIONS | OVERALL_TRAFFIC_SUGGESTIONS_DETAILS | ROUTING_SUGGESTIONS`
Required: Yes

 ** [StartTime](#API_StartQuery_RequestSyntax) **   <a name="internetmonitor-StartQuery-request-StartTime"></a>
The timestamp that is the beginning of the period that you want to retrieve data for with your query.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_StartQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QueryId": "string"
}
```

## Response Elements
<a name="API_StartQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueryId](#API_StartQuery_ResponseSyntax) **   <a name="internetmonitor-StartQuery-response-QueryId"></a>
The internally-generated identifier of a specific query.
Type: String

## Errors
<a name="API_StartQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
The request exceeded a service quota.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_StartQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/StartQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/StartQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
