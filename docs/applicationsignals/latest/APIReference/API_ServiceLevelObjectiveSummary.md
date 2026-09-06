---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveSummary.html
---

# ServiceLevelObjectiveSummary
<a name="API_ServiceLevelObjectiveSummary"></a>

A structure that contains information about one service level objective (SLO) created in Application Signals.

## Contents
<a name="API_ServiceLevelObjectiveSummary_Contents"></a>

 ** Arn **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-Arn"></a>
The ARN of this service level objective.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** Name **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-Name"></a>
The name of the service level objective.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** CompositeSliConfig **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-CompositeSliConfig"></a>
The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.
Type: [CompositeSliConfig](API_CompositeSliConfig.md) object
Required: No

 ** CreatedTime **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-CreatedTime"></a>
The date and time that this service level objective was created. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
Type: Timestamp
Required: No

 ** DependencyConfig **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-DependencyConfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
Type: [DependencyConfig](API_DependencyConfig.md) object
Required: No

 ** EvaluationType **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-EvaluationType"></a>
Displays whether this is a period-based SLO or a request-based SLO.
Type: String
Valid Values: `PeriodBased | RequestBased`
Required: No

 ** KeyAttributes **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-KeyAttributes"></a>
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this service level objective is for.
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

 ** MetricSource **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-MetricSource"></a>
Identifies the metric source for SLOs on resources other than Application Signals services.
Type: [MetricSource](API_MetricSource.md) object
Required: No

 ** MetricSourceType **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-MetricSourceType"></a>
Displays the SLI metric source type for this SLO. Supported types are:
+ Service operation
+ Service dependency
+ Service
+ CloudWatch metric
+ AppMonitor
+ Canary
Type: String
Valid Values: `ServiceOperation | CloudWatchMetric | ServiceDependency | AppMonitor | Canary | Service`
Required: No

 ** OperationName **   <a name="applicationsignals-Type-ServiceLevelObjectiveSummary-OperationName"></a>
If this service level objective is specific to a single operation, this field displays the name of that operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ServiceLevelObjectiveSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelObjectiveSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelObjectiveSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelObjectiveSummary)
