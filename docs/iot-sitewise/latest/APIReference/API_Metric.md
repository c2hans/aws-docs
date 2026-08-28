---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Metric.html
---

# Metric
<a name="API_Metric"></a>

Contains an asset metric property. With metrics, you can calculate aggregate functions, such as an average, maximum, or minimum, as specified through an expression. A metric maps several values to a single value (such as a sum).

The maximum number of dependent/cascading variables used in any one metric calculation is 10. Therefore, a *root* metric can have up to 10 cascading metrics in its computational dependency tree. Additionally, a metric can only have a data type of `DOUBLE` and consume properties with data types of `INTEGER` or `DOUBLE`.

For more information, see [Metrics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#metrics) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_Metric_Contents"></a>

 ** window **   <a name="iotsitewise-Type-Metric-window"></a>
The window (time interval) over which AWS IoT SiteWise computes the metric's aggregation expression. AWS IoT SiteWise computes one data point per `window`.
Type: [MetricWindow](API_MetricWindow.md) object
Required: Yes

 ** expression **   <a name="iotsitewise-Type-Metric-expression"></a>
The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** processingConfig **   <a name="iotsitewise-Type-Metric-processingConfig"></a>
The processing configuration for the given metric property. You can configure metrics to be computed at the edge or in the AWS Cloud. By default, metrics are forwarded to the cloud.
Type: [MetricProcessingConfig](API_MetricProcessingConfig.md) object
Required: No

 ** variables **   <a name="iotsitewise-Type-Metric-variables"></a>
The list of variables used in the expression.
Type: Array of [ExpressionVariable](API_ExpressionVariable.md) objects
Required: No

## See Also
<a name="API_Metric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Metric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Metric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Metric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
