---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricDataQuery.html
---

# MetricDataQuery
<a name="API_MetricDataQuery"></a>

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData`. The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

## Contents
<a name="API_MetricDataQuery_Contents"></a>

 ** Id **   <a name="applicationsignals-Type-MetricDataQuery-Id"></a>
A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** AccountId **   <a name="applicationsignals-Type-MetricDataQuery-AccountId"></a>
The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Expression **   <a name="applicationsignals-Type-MetricDataQuery-Expression"></a>
This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.
A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide*.
Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Label **   <a name="applicationsignals-Type-MetricDataQuery-Label"></a>
A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.
You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html).
Type: String
Required: No

 ** MetricStat **   <a name="applicationsignals-Type-MetricDataQuery-MetricStat"></a>
A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.
Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.
Type: [MetricStat](API_MetricStat.md) object
Required: No

 ** Period **   <a name="applicationsignals-Type-MetricDataQuery-Period"></a>
The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.
If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:
+ Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
+ Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
+ Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ReturnData **   <a name="applicationsignals-Type-MetricDataQuery-ReturnData"></a>
Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false`.
Type: Boolean
Required: No

## See Also
<a name="API_MetricDataQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MetricDataQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MetricDataQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MetricDataQuery)
