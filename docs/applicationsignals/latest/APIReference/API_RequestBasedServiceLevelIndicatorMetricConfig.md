---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RequestBasedServiceLevelIndicatorMetricConfig.html
---

# RequestBasedServiceLevelIndicatorMetricConfig
<a name="API_RequestBasedServiceLevelIndicatorMetricConfig"></a>

Use this structure to specify the information for the metric that a period-based SLO will monitor.

## Contents
<a name="API_RequestBasedServiceLevelIndicatorMetricConfig_Contents"></a>

 ** CompositeSliConfig **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-CompositeSliConfig"></a>
The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.
Type: [CompositeSliConfig](API_CompositeSliConfig.md) object
Required: No

 ** DependencyConfig **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-DependencyConfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
Type: [DependencyConfig](API_DependencyConfig.md) object
Required: No

 ** KeyAttributes **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-KeyAttributes"></a>
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

 ** MetricName **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-MetricName"></a>
The name of the metric for SLOs on resources other than Application Signals services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** MetricSource **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-MetricSource"></a>
Identifies the metric source for SLOs on resources other than Application Signals services.
Type: [MetricSource](API_MetricSource.md) object
Required: No

 ** MetricType **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-MetricType"></a>
If the SLO is to monitor either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, use this field to specify which of those metrics is used.
Type: String
Valid Values: `LATENCY | AVAILABILITY`
Required: No

 ** MonitoredRequestCountMetric **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-MonitoredRequestCountMetric"></a>
Use this structure to define the metric that you want to use as the "good request" or "bad request" value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` will be divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.
Type: [MonitoredRequestCountMetricDataQueries](API_MonitoredRequestCountMetricDataQueries.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** OperationName **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-OperationName"></a>
If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** TotalRequestCountMetric **   <a name="applicationsignals-Type-RequestBasedServiceLevelIndicatorMetricConfig-TotalRequestCountMetric"></a>
Use this structure to define the metric that you want to use as the "total requests" number for a request-based SLO. This result will be divided by the "good request" or "bad request" value defined in `MonitoredRequestCountMetric`.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

## See Also
<a name="API_RequestBasedServiceLevelIndicatorMetricConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorMetricConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorMetricConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/RequestBasedServiceLevelIndicatorMetricConfig)
