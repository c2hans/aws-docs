---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EcsCapacityIncreaseConfiguration.html
---

# EcsCapacityIncreaseConfiguration
<a name="API_EcsCapacityIncreaseConfiguration"></a>

The configuration for an AWS ECS capacity increase.

## Contents
<a name="API_EcsCapacityIncreaseConfiguration_Contents"></a>

 ** services **   <a name="regionswitch-Type-EcsCapacityIncreaseConfiguration-services"></a>
The services specified for the configuration.
Type: Array of [Service](API_Service.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** capacityMonitoringApproach **   <a name="regionswitch-Type-EcsCapacityIncreaseConfiguration-capacityMonitoringApproach"></a>
The monitoring approach specified for the configuration, for example, `Most_Recent`.
Type: String
Valid Values: `sampledMaxInLast24Hours | containerInsightsMaxInLast24Hours`
Required: No

 ** targetPercent **   <a name="regionswitch-Type-EcsCapacityIncreaseConfiguration-targetPercent"></a>
The target percentage specified for the configuration. The default is 100.
Type: Integer
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-EcsCapacityIncreaseConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-EcsCapacityIncreaseConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [EcsUngraceful](API_EcsUngraceful.md) object
Required: No

## See Also
<a name="API_EcsCapacityIncreaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/EcsCapacityIncreaseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/EcsCapacityIncreaseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/EcsCapacityIncreaseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
