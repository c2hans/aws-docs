---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjective.html
---

# ServiceLevelObjective
<a name="API_ServiceLevelObjective"></a>

A structure containing information about one service level objective (SLO) that has been created in Application Signals. Creating SLOs can help you ensure your services are performing to the level that you expect. SLOs help you set and track a specific target level for the reliability and availability of your applications and services. Each SLO uses a service level indicator (SLI), which is a key performance metric, to calculate how much underperformance can be tolerated before the goal that you set for the SLO is not achieved.

## Contents
<a name="API_ServiceLevelObjective_Contents"></a>

 ** Arn **   <a name="applicationsignals-Type-ServiceLevelObjective-Arn"></a>
The ARN of this SLO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** CreatedTime **   <a name="applicationsignals-Type-ServiceLevelObjective-CreatedTime"></a>
The date and time that this SLO was created. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example, `2019-07-01T23:59:59`.
Type: Timestamp
Required: Yes

 ** Goal **   <a name="applicationsignals-Type-ServiceLevelObjective-Goal"></a>
This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.
Type: [Goal](API_Goal.md) object
Required: Yes

 ** LastUpdatedTime **   <a name="applicationsignals-Type-ServiceLevelObjective-LastUpdatedTime"></a>
The time that this SLO was most recently updated. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example, `2019-07-01T23:59:59`.
Type: Timestamp
Required: Yes

 ** Name **   <a name="applicationsignals-Type-ServiceLevelObjective-Name"></a>
The name of this SLO.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** BurnRateConfigurations **   <a name="applicationsignals-Type-ServiceLevelObjective-BurnRateConfigurations"></a>
Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.
Type: Array of [BurnRateConfiguration](API_BurnRateConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Description **   <a name="applicationsignals-Type-ServiceLevelObjective-Description"></a>
The description that you created for this SLO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EvaluationType **   <a name="applicationsignals-Type-ServiceLevelObjective-EvaluationType"></a>
Displays whether this is a period-based SLO or a request-based SLO.
Type: String
Valid Values: `PeriodBased | RequestBased`
Required: No

 ** MetricSourceType **   <a name="applicationsignals-Type-ServiceLevelObjective-MetricSourceType"></a>
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

 ** RequestBasedSli **   <a name="applicationsignals-Type-ServiceLevelObjective-RequestBasedSli"></a>
A structure containing information about the performance metric that this SLO monitors, if this is a request-based SLO.
Type: [RequestBasedServiceLevelIndicator](API_RequestBasedServiceLevelIndicator.md) object
Required: No

 ** Sli **   <a name="applicationsignals-Type-ServiceLevelObjective-Sli"></a>
A structure containing information about the performance metric that this SLO monitors, if this is a period-based SLO.
Type: [ServiceLevelIndicator](API_ServiceLevelIndicator.md) object
Required: No

## See Also
<a name="API_ServiceLevelObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelObjective)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
