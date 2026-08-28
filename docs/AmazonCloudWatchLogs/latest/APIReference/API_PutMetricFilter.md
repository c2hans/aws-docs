---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.html
---

# PutMetricFilter
<a name="API_PutMetricFilter"></a>

Creates or updates a metric filter and associates it with the specified log group. With metric filters, you can configure rules to extract metric data from log events ingested through [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html).

The maximum number of metric filters that can be associated with a log group is 100.

Using regular expressions in filter patterns is supported. For these filters, there is a quota of two regular expression patterns within a single filter pattern. There is also a quota of five regular expression patterns per log group. For more information about using regular expressions in filter patterns, see [ Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

When you create a metric filter, you can also optionally assign a unit and dimensions to the metric that is created.

**Important**
Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as `IPAddress` or `requestID` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.
CloudWatch Logs might disable a metric filter if it generates 1,000 different name/value pairs for your specified dimensions within one hour.
You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see [ Creating a Billing Alarm to Monitor Your Estimated AWS Charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html).

## Request Syntax
<a name="API_PutMetricFilter_RequestSyntax"></a>

```
{
   "applyOnTransformedLogs": {{boolean}},
   "emitSystemFieldDimensions": [ "{{string}}" ],
   "fieldSelectionCriteria": "{{string}}",
   "filterName": "{{string}}",
   "filterPattern": "{{string}}",
   "logGroupName": "{{string}}",
   "metricTransformations": [
      {
         "defaultValue": {{number}},
         "dimensions": {
            "{{string}}" : "{{string}}"
         },
         "metricName": "{{string}}",
         "metricNamespace": "{{string}}",
         "metricValue": "{{string}}",
         "unit": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutMetricFilter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applyOnTransformedLogs](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-applyOnTransformedLogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If the log group uses either a log-group level or account-level transformer, and you specify `true`, the metric filter will be applied on the transformed version of the log events instead of the original ingested log events.
Type: Boolean
Required: No

 ** [emitSystemFieldDimensions](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-emitSystemFieldDimensions"></a>
A list of system fields to emit as additional dimensions in the generated metrics. Valid values are `@aws.account` and `@aws.region`. These dimensions help identify the source of centralized log data and count toward the total dimension limit for metric filters.
Type: Array of strings
Required: No

 ** [fieldSelectionCriteria](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-fieldSelectionCriteria"></a>
A filter expression that specifies which log events should be processed by this metric filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like `=`, `!=`, `AND`, `OR`, `IN`, `NOT IN`. Example: `@aws.region = "us-east-1"` or `@aws.account IN ["123456789012", "987654321098"]`. Maximum length: 2000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [filterName](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-filterName"></a>
A name for the metric filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: Yes

 ** [filterPattern](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-filterPattern"></a>
A filter pattern for extracting metric data out of ingested log events.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** [logGroupName](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [metricTransformations](#API_PutMetricFilter_RequestSyntax) **   <a name="CWL-PutMetricFilter-request-metricTransformations"></a>
A collection of information that defines how metric data gets emitted.
Type: Array of [MetricTransformation](API_MetricTransformation.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Elements
<a name="API_PutMetricFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutMetricFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutMetricFilter_Examples"></a>

### To create or update a metric filter
<a name="API_PutMetricFilter_Example_1"></a>

The following example creates a metric filter for the specified log group.

#### Sample Request
<a name="API_PutMetricFilter_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.PutMetricFilter
{
  "logGroupName": "my-log-group",
  "filterName": "my-metric-filter",
  "filterPattern": "[ip, identity, user_id, timestamp, request, status_code, size]",
  "metricTransformations": [
    {
      "defaultValue": "0",
      "metricValue": "$size",
      "metricNamespace": "MyApp",
      "metricName": "Volume",
      "dimensions": {"Request": "$request","UserId": "$user_id"},
      "unit": "Count"
    }
  ]
}
```

#### Sample Response
<a name="API_PutMetricFilter_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_PutMetricFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutMetricFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutMetricFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
