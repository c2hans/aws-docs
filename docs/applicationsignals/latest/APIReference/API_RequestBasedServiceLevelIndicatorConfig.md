---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicatorConfig.html
---

# RequestBasedServiceLevelIndicatorConfig
<a name="API_RequestBasedServiceLevelIndicatorConfig"></a>

This structure specifies the information about the service and the performance metric that a request-based SLO is to monitor.

## Contents
<a name="API_RequestBasedServiceLevelIndicatorConfig_Contents"></a>

 ** RequestBasedSliMetricConfig **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorConfig-RequestBasedSliMetricConfig"></a>
Use this structure to specify the metric to be used for the SLO.
Type: [RequestBasedServiceLevelIndicatorMetricConfig](API_RequestBasedServiceLevelIndicatorMetricConfig.md) object
Required: Yes

 ** ComparisonOperator **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorConfig-ComparisonOperator"></a>
The arithmetic operation to use when comparing the specified metric to the threshold. This parameter is required if this SLO is tracking the `Latency` metric.
Type: String
Valid Values: `GreaterThanOrEqualTo | GreaterThan | LessThan | LessThanOrEqualTo`
Required: No

 ** MetricThreshold **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorConfig-MetricThreshold"></a>
The value that the SLI metric is compared to. This parameter is required if this SLO is tracking the `Latency` metric.
Type: Double
Required: No

## See Also
<a name="API_RequestBasedServiceLevelIndicatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
