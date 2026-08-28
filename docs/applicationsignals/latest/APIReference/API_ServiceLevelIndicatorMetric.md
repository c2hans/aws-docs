---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelIndicatorMetric.html
---

# ServiceLevelIndicatorMetric
<a name="API_ServiceLevelIndicatorMetric"></a>

This structure contains the information about the metric that is used for a period-based SLO.

## Contents
<a name="API_ServiceLevelIndicatorMetric_Contents"></a>

 ** MetricDataQueries **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-MetricDataQueries"></a>
If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, this structure includes the information about that metric or expression.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: Yes

 ** CompositeSliConfig **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-CompositeSliConfig"></a>
The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.
Type: [CompositeSliConfig](API_CompositeSliConfig.md) object
Required: No

 ** DependencyConfig **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-DependencyConfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
Type: [DependencyConfig](API_DependencyConfig.md) object
Required: No

 ** KeyAttributes **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-KeyAttributes"></a>
This is a string-to-string map that contains information about the type of object that this SLO is related to. It can include the following fields.
+  `Type` designates the type of object that this SLO is related to.
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

 ** MetricSource **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-MetricSource"></a>
Identifies the metric source for SLOs on resources other than Application Signals services.
Type: [MetricSource](API_MetricSource.md) object
Required: No

 ** MetricType **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-MetricType"></a>
If the SLO monitors either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, this field displays which of those metrics is used.
Type: String
Valid Values: `LATENCY | AVAILABILITY`
Required: No

 ** OperationName **   <a name="applicationsignals-Type-ServiceLevelIndicatorMetric-OperationName"></a>
If the SLO monitors a specific operation of the service, this field displays that operation name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ServiceLevelIndicatorMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelIndicatorMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelIndicatorMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelIndicatorMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
