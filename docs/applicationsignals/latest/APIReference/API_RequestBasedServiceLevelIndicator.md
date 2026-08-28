---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicator.html
---

# RequestBasedServiceLevelIndicator
<a name="API_RequestBasedServiceLevelIndicator"></a>

This structure contains information about the performance metric that a request-based SLO monitors.

## Contents
<a name="API_RequestBasedServiceLevelIndicator_Contents"></a>

 ** RequestBasedSliMetric **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicator-RequestBasedSliMetric"></a>
A structure that contains information about the metric that the SLO monitors.
Type: [RequestBasedServiceLevelIndicatorMetric](API_RequestBasedServiceLevelIndicatorMetric.md) object
Required: Yes

 ** ComparisonOperator **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicator-ComparisonOperator"></a>
The arithmetic operation used when comparing the specified metric to the threshold.
Type: String
Valid Values: `GreaterThanOrEqualTo | GreaterThan | LessThan | LessThanOrEqualTo`
Required: No

 ** MetricThreshold **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicator-MetricThreshold"></a>
This value is the threshold that the observed metric values of the SLI metric are compared to.
Type: Double
Required: No

## See Also
<a name="API_RequestBasedServiceLevelIndicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/RequestBasedServiceLevelIndicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/RequestBasedServiceLevelIndicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/RequestBasedServiceLevelIndicator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
