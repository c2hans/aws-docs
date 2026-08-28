---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingAutoScalingGroupDetails.html
---

# AwsAutoScalingAutoScalingGroupDetails
<a name="API_AwsAutoScalingAutoScalingGroupDetails"></a>

Provides details about an auto scaling group.

## Contents
<a name="API_AwsAutoScalingAutoScalingGroupDetails_Contents"></a>

 ** AvailabilityZones **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-AvailabilityZones"></a>
The list of Availability Zones for the automatic scaling group.
Type: Array of [AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails](API_AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails.md) objects
Required: No

 ** CapacityRebalance **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-CapacityRebalance"></a>
Indicates whether capacity rebalancing is enabled.
Type: Boolean
Required: No

 ** CreatedTime **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-CreatedTime"></a>
Indicates when the auto scaling group was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** HealthCheckGracePeriod **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-HealthCheckGracePeriod"></a>
The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before it checks the health status of an EC2 instance that has come into service.
Type: Integer
Required: No

 ** HealthCheckType **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-HealthCheckType"></a>
The service to use for the health checks. Valid values are `EC2` or `ELB`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchConfigurationName **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-LaunchConfigurationName"></a>
The name of the launch configuration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchTemplate **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-LaunchTemplate"></a>
The launch template to use.
Type: [AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification](API_AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification.md) object
Required: No

 ** LoadBalancerNames **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-LoadBalancerNames"></a>
The list of load balancers associated with the group.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MixedInstancesPolicy **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupDetails-MixedInstancesPolicy"></a>
The mixed instances policy for the automatic scaling group.
Type: [AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails](API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails.md) object
Required: No

## See Also
<a name="API_AwsAutoScalingAutoScalingGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
