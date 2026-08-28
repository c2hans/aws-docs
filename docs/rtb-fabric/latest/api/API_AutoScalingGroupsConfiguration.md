---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AutoScalingGroupsConfiguration.html
---

# AutoScalingGroupsConfiguration
<a name="API_AutoScalingGroupsConfiguration"></a>

Describes the configuration of an auto scaling group.

## Contents
<a name="API_AutoScalingGroupsConfiguration_Contents"></a>

 ** autoScalingGroupNames **   <a name="rtbfabric-Type-AutoScalingGroupsConfiguration-autoScalingGroupNames"></a>
The names of the auto scaling group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** roleArn **   <a name="rtbfabric-Type-AutoScalingGroupsConfiguration-roleArn"></a>
The role ARN of the auto scaling group.
Type: String
Pattern: `arn:aws:iam::[0-9]{12}:role/.{1,2048}`
Required: Yes

 ** healthCheckConfig **   <a name="rtbfabric-Type-AutoScalingGroupsConfiguration-healthCheckConfig"></a>
The health check configuration for the Auto Scaling group managed endpoint.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

## See Also
<a name="API_AutoScalingGroupsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/AutoScalingGroupsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/AutoScalingGroupsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/AutoScalingGroupsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
