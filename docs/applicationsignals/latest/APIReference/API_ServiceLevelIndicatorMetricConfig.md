---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorMetricConfig.html
---

# ServiceLevelIndicatorMetricConfig
<a name="API_ServiceLevelIndicatorMetricConfig"></a>

Use this structure to specify the information for the metric that a period-based SLO will monitor.

## Contents
<a name="API_ServiceLevelIndicatorMetricConfig_Contents"></a>

 ** CompositeSliConfig **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-CompositeSliConfig"></a>
The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.
Type: [CompositeSliConfig](API_CompositeSliConfig.md) object
Required: No

 ** DependencyConfig **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-DependencyConfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
Type: [DependencyConfig](API_DependencyConfig.md) object
Required: No

 ** KeyAttributes **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-KeyAttributes"></a>
If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the `Type`, `Name`, and `Environment` attributes.
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: No

 ** MetricDataQueries **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-MetricDataQueries"></a>
If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

 ** MetricName **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-MetricName"></a>
The name of the CloudWatch metric to use for the SLO, when using a custom metric rather than Application Signals standard metrics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** MetricSource **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-MetricSource"></a>
Identifies the metric source for SLOs on resources other than Application Signals services.
Type: [MetricSource](API_MetricSource.md) object
Required: No

 ** MetricType **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-MetricType"></a>
If the SLO is to monitor either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, use this field to specify which of those metrics is used.
Type: String
Valid Values: `LATENCY | AVAILABILITY`
Required: No

 ** OperationName **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-OperationName"></a>
If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PeriodSeconds **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-PeriodSeconds"></a>
The number of seconds to use as the period for SLO evaluation. Your application's performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 900.
Required: No

 ** Statistic **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetricConfig-Statistic"></a>
The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9.]+`
Required: No

## See Also
<a name="API_ServiceLevelIndicatorMetricConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelIndicatorMetricConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelIndicatorMetricConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelIndicatorMetricConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
