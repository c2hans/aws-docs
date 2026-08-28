---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Ec2AsgCapacityIncreaseConfiguration.html
---

# Ec2AsgCapacityIncreaseConfiguration
<a name="API_Ec2AsgCapacityIncreaseConfiguration"></a>

Configuration for increasing the capacity of Amazon EC2 Auto Scaling groups during a Region switch.

## Contents
<a name="API_Ec2AsgCapacityIncreaseConfiguration_Contents"></a>

 ** asgs **   <a name="regionswitch-Type-Ec2AsgCapacityIncreaseConfiguration-asgs"></a>
The EC2 Auto Scaling groups for the configuration.
Type: Array of [Asg](API_Asg.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** capacityMonitoringApproach **   <a name="regionswitch-Type-Ec2AsgCapacityIncreaseConfiguration-capacityMonitoringApproach"></a>
The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.
Type: String
Valid Values: `sampledMaxInLast24Hours | autoscalingMaxInLast24Hours`
Required: No

 ** targetPercent **   <a name="regionswitch-Type-Ec2AsgCapacityIncreaseConfiguration-targetPercent"></a>
The target percentage that you specify for EC2 Auto Scaling groups. The default is 100.
Type: Integer
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-Ec2AsgCapacityIncreaseConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-Ec2AsgCapacityIncreaseConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [Ec2Ungraceful](API_Ec2Ungraceful.md) object
Required: No

## See Also
<a name="API_Ec2AsgCapacityIncreaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Ec2AsgCapacityIncreaseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Ec2AsgCapacityIncreaseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Ec2AsgCapacityIncreaseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
