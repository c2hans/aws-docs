---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicator.html
---

# ServiceLevelIndicator
<a name="API_ServiceLevelIndicator"></a>

This structure contains information about the performance metric that a period-based SLO monitors.

## Contents
<a name="API_ServiceLevelIndicator_Contents"></a>

 ** ComparisonOperator **   <a name="applicationsignals-Type-ServiceLevelIndicator-ComparisonOperator"></a>
The arithmetic operation used when comparing the specified metric to the threshold.
Type: String
Valid Values: `GreaterThanOrEqualTo | GreaterThan | LessThan | LessThanOrEqualTo`
Required: Yes

 ** MetricThreshold **   <a name="applicationsignals-Type-ServiceLevelIndicator-MetricThreshold"></a>
The value that the SLI metric is compared to.
Type: Double
Required: Yes

 ** SliMetric **   <a name="applicationsignals-Type-ServiceLevelIndicator-SliMetric"></a>
A structure that contains information about the metric that the SLO monitors.
Type: [ServiceLevelIndicatorMetric](API_ServiceLevelIndicatorMetric.md) object
Required: Yes

## See Also
<a name="API_ServiceLevelIndicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelIndicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelIndicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelIndicator)
