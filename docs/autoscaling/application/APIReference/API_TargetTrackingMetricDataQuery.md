---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetricDataQuery.html
---

# TargetTrackingMetricDataQuery
<a name="API_TargetTrackingMetricDataQuery"></a>

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

You can use `TargetTrackingMetricDataQuery` structures with a [PutScalingPolicy](API_PutScalingPolicy.md) operation when you specify a [TargetTrackingScalingPolicyConfiguration](API_TargetTrackingScalingPolicyConfiguration.md) in the request.

You can call for a single metric or perform math expressions on multiple metrics. Any expressions used in a metric specification must eventually return a single time series.

For more information and examples, see [Create a target tracking scaling policy for Application Auto Scaling using metric math](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking-metric-math.html) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_TargetTrackingMetricDataQuery_Contents"></a>

 ** Id **   <a name="autoscaling-Type-TargetTrackingMetricDataQuery-Id"></a>
A short name that identifies the object's results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Expression **   <a name="autoscaling-Type-TargetTrackingMetricDataQuery-Expression"></a>
The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.
Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Label **   <a name="autoscaling-Type-TargetTrackingMetricDataQuery-Label"></a>
A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MetricStat **   <a name="autoscaling-Type-TargetTrackingMetricDataQuery-MetricStat"></a>
Information about the metric data to return.
Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
Type: [TargetTrackingMetricStat](API_TargetTrackingMetricStat.md) object
Required: No

 ** ReturnData **   <a name="autoscaling-Type-TargetTrackingMetricDataQuery-ReturnData"></a>
Indicates whether to return the timestamps and raw data values of this metric.
If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.
If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData`. This sets it to its default (`true`).
Type: Boolean
Required: No

## See Also
<a name="API_TargetTrackingMetricDataQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/TargetTrackingMetricDataQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/TargetTrackingMetricDataQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/TargetTrackingMetricDataQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
