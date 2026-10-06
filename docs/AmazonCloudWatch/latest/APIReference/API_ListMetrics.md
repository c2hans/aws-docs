---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html
---

# ListMetrics
<a name="API_ListMetrics"></a>

List the specified metrics. You can use the returned metrics with [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) to get statistical data.

Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.

After you create a metric, allow up to 15 minutes for the metric to appear. To see metric statistics sooner, use [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view metrics from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

 `ListMetrics` doesn't return information about metrics if those metrics haven't reported data in the past two weeks. To retrieve those metrics, use [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

## Request Syntax
<a name="API_ListMetrics_RequestSyntax"></a>

```
{
   "Dimensions": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "IncludeLinkedAccounts": {{boolean}},
   "MetricName": "{{string}}",
   "Namespace": "{{string}}",
   "NextToken": "{{string}}",
   "OwningAccount": "{{string}}",
   "RecentlyActive": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Dimensions](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-Dimensions"></a>
The dimensions to filter against. Only the dimension with names that match exactly will be returned. If you specify one dimension name and a metric has that dimension and also other dimensions, it will be returned.
Type: Array of [DimensionFilter](API_DimensionFilter.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [IncludeLinkedAccounts](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-IncludeLinkedAccounts"></a>
If you are using this operation in a monitoring account, specify `true` to include metrics from source accounts in the returned data.
The default is `false`.
Type: Boolean
Required: No

 ** [MetricName](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-MetricName"></a>
The name of the metric to filter against. Only the metrics with names that match exactly will be returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Namespace](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-Namespace"></a>
The metric namespace to filter against. Only the namespace that matches exactly will be returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: No

 ** [NextToken](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-NextToken"></a>
The token returned by a previous call to indicate that there is more data available.
Type: String
Required: No

 ** [OwningAccount](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-OwningAccount"></a>
When you use this operation in a monitoring account, use this field to return metrics only from one source account. To do so, specify that source account ID in this field, and also specify `true` for `IncludeLinkedAccounts`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [RecentlyActive](#API_ListMetrics_RequestSyntax) **   <a name="ACW-ListMetrics-request-RecentlyActive"></a>
To filter the results to show only metrics that have had data points published in the past three hours, specify this parameter with a value of `PT3H`. This is the only valid value for this parameter.
The results that are returned are an approximation of the value you specify. There is a low probability that the returned results include metrics with last published data as much as 50 minutes more than the specified time interval.
Type: String
Valid Values: `PT3H`
Required: No

## Response Syntax
<a name="API_ListMetrics_ResponseSyntax"></a>

```
{
   "Metrics": [
      {
         "Dimensions": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "MetricName": "string",
         "Namespace": "string"
      }
   ],
   "NextToken": "string",
   "OwningAccounts": [ "string" ]
}
```

## Response Elements
<a name="API_ListMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metrics](#API_ListMetrics_ResponseSyntax) **   <a name="ACW-ListMetrics-response-Metrics"></a>
The metrics that match your request.
Type: Array of [Metric](API_Metric.md) objects

 ** [NextToken](#API_ListMetrics_ResponseSyntax) **   <a name="ACW-ListMetrics-response-NextToken"></a>
The token that marks the start of the next batch of returned results.
Type: String

 ** [OwningAccounts](#API_ListMetrics_ResponseSyntax) **   <a name="ACW-ListMetrics-response-OwningAccounts"></a>
If you are using this operation in a monitoring account, this array contains the account IDs of the source accounts where the metrics in the returned data are from.
This field is a 1:1 mapping between each metric that is returned and the ID of the owning account.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_ListMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListMetrics_Examples"></a>

### List metrics in a specified namespace from all source accounts and from the monitoring account
<a name="API_ListMetrics_Example_1"></a>

The following example lists metrics in the `AWS/EC2` namespace from the monitoring account itself and all source accounts.

#### Sample Request
<a name="API_ListMetrics_Example_1_Request"></a>

```
{
  "IncludeLinkedAccounts": true,
  "Namespace" : "AWS/EC2"
}
```

### List metrics from a namespace in just one source account
<a name="API_ListMetrics_Example_2"></a>

The following example lists metrics in the `AWS/EC2` namespace from only the source account with the ID `111111111111`.

#### Sample Request
<a name="API_ListMetrics_Example_2_Request"></a>

```
{
  "IncludeLinkedAccounts": "true",
  "OwningAccount" : "111111111111",
  "Namespace" : "AWS/EC2"
}
```

## See Also
<a name="API_ListMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetrics)
