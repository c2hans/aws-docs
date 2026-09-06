---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.html
---

# DescribeMetricFilters
<a name="API_DescribeMetricFilters"></a>

Lists the specified metric filters. You can list all of the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.

## Request Syntax
<a name="API_DescribeMetricFilters_RequestSyntax"></a>

```
{
   "filterNamePrefix": "{{string}}",
   "limit": {{number}},
   "logGroupName": "{{string}}",
   "metricName": "{{string}}",
   "metricNamespace": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMetricFilters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filterNamePrefix](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-filterNamePrefix"></a>
The prefix to match. CloudWatch Logs uses the value that you set here only if you also include the `logGroupName` parameter in your request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** [limit](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-limit"></a>
The maximum number of items returned. If you don't specify a value, the default is up to 50 items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [logGroupName](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [metricName](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-metricName"></a>
Filters results to include only those with the specified metric name. If you include this parameter in your request, you must also include the `metricNamespace` parameter.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[^:*$]*`
Required: No

 ** [metricNamespace](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-metricNamespace"></a>
Filters results to include only those in the specified namespace. If you include this parameter in your request, you must also include the `metricName` parameter.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[^:*$]*`
Required: No

 ** [nextToken](#API_DescribeMetricFilters_RequestSyntax) **   <a name="CWL-DescribeMetricFilters-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeMetricFilters_ResponseSyntax"></a>

```
{
   "metricFilters": [
      {
         "applyOnTransformedLogs": boolean,
         "creationTime": number,
         "emitSystemFieldDimensions": [ "string" ],
         "fieldSelectionCriteria": "string",
         "filterName": "string",
         "filterPattern": "string",
         "logGroupName": "string",
         "metricTransformations": [
            {
               "defaultValue": number,
               "dimensions": {
                  "string" : "string"
               },
               "metricName": "string",
               "metricNamespace": "string",
               "metricValue": "string",
               "unit": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeMetricFilters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricFilters](#API_DescribeMetricFilters_ResponseSyntax) **   <a name="CWL-DescribeMetricFilters-response-metricFilters"></a>
The metric filters.
Type: Array of [MetricFilter](API_MetricFilter.md) objects

 ** [nextToken](#API_DescribeMetricFilters_ResponseSyntax) **   <a name="CWL-DescribeMetricFilters-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeMetricFilters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMetricFilters_Examples"></a>

### To list the metric filters for a log group
<a name="API_DescribeMetricFilters_Example_1"></a>

The following example lists the metric filters for the specified log group.

#### Sample Request
<a name="API_DescribeMetricFilters_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.DescribeMetricFilters
{
  "logGroupName": "my-log-group"
}
```

#### Sample Response
<a name="API_DescribeMetricFilters_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "metricFilters": [
    {
      "applyOnTransformedLogs": true,
      "creationTime": 1396224000000,
      "filterName": "my-metric-filter",
      "filterPattern": "[ip, identity, user_id, timestamp, request, status_code, size]",
      "logGroupName": "my-log-group",
      "metricTransformations": [
        {
          "defaultValue": "0",
          "metricValue": "$size",
          "metricNamespace": "my-app",
          "metricName": "Volume"
         }
      ]
    }
  ]
}
```

## See Also
<a name="API_DescribeMetricFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeMetricFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeMetricFilters)
