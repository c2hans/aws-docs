---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchInstances.html
---

# LaunchInstances
<a name="API_LaunchInstances"></a>

 Launches a specified number of instances in an Auto Scaling group. Returns instance IDs and other details if launch is successful or error details if launch is unsuccessful.

## Request Parameters
<a name="API_LaunchInstances_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
 The name of the Auto Scaling group to launch instances into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **AvailabilityZoneIds.member.N**
 A list of Availability Zone IDs where instances should be launched. Must match or be included in the group's AZ configuration. You cannot specify both AvailabilityZones and AvailabilityZoneIds. Required for multi-AZ groups, optional for single-AZ groups.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **AvailabilityZones.member.N**
 The Availability Zones for the instance launch. Must match or be included in the Auto Scaling group's Availability Zone configuration. Either `AvailabilityZones` or `SubnetIds` must be specified for groups with multiple Availability Zone configurations.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ClientToken **
 A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: Yes

 ** RequestedCapacity **
 The number of instances to launch. Although this value can exceed 100 for instance weights, the actual instance count is limited to 100 instances per launch.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** RetryStrategy **
 Specifies whether to retry asynchronously if the synchronous launch fails. Valid values are NONE (default, no async retry) and RETRY\_WITH\_GROUP\_CONFIGURATION (increase desired capacity and retry with group configuration).
Type: String
Valid Values: `retry-with-group-configuration | none`
Required: No

 **SubnetIds.member.N**
 The subnet IDs for the instance launch. Either `AvailabilityZones` or `SubnetIds` must be specified. If both are specified, the subnets must reside in the specified Availability Zones.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_LaunchInstances_ResponseElements"></a>

The following elements are returned by the service.

 ** AutoScalingGroupName **
 The name of the Auto Scaling group where the instances were launched.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** ClientToken **
 The idempotency token used for the request, either customer-specified or auto-generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_\/]+`

 **Errors.member.N**
 A list of errors encountered during the launch attempt including details about failed instance launches with their corresponding error codes and messages.
Type: Array of [LaunchInstancesError](API_LaunchInstancesError.md) objects

 **Instances.member.N**
 A list of successfully launched instances including details such as instance type, Availability Zone, subnet, lifecycle state, and instance IDs.
Type: Array of [InstanceCollection](API_InstanceCollection.md) objects

## Errors
<a name="API_LaunchInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatch **
 Indicates that the parameters in the current request do not match the parameters from a previous request with the same client token within the idempotency window.
HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## See Also
<a name="API_LaunchInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/LaunchInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LaunchInstances)
