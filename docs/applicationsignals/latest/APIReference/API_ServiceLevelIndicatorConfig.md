---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorConfig.html
---

# ServiceLevelIndicatorConfig
<a name="API_ServiceLevelIndicatorConfig"></a>

This structure specifies the information about the service and the performance metric that a period-based SLO is to monitor.

## Contents
<a name="API_ServiceLevelIndicatorConfig_Contents"></a>

 ** SliMetricConfig **   <a name="applicationsignals-Type-ServiceLevelIndicatorConfig-SliMetricConfig"></a>
Use this structure to specify the metric to be used for the SLO.
Type: [ServiceLevelIndicatorMetricConfig](API_ServiceLevelIndicatorMetricConfig.md) object
Required: Yes

 ** ComparisonOperator **   <a name="applicationsignals-Type-ServiceLevelIndicatorConfig-ComparisonOperator"></a>
The arithmetic operation to use when comparing the specified metric to the threshold.
This is not required if `CreateRecommendedSlo` is set to `true`.
Type: String
Valid Values: `GreaterThanOrEqualTo | GreaterThan | LessThan | LessThanOrEqualTo`
Required: No

 ** MetricThreshold **   <a name="applicationsignals-Type-ServiceLevelIndicatorConfig-MetricThreshold"></a>
This parameter is used only when a request-based SLO tracks the `Latency` metric. Specify the threshold value that the observed `Latency` metric values are to be compared to.
This is not required if `CreateRecommendedSlo` is set to `true`.
Type: Double
Required: No

## See Also
<a name="API_ServiceLevelIndicatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelIndicatorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelIndicatorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelIndicatorConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
