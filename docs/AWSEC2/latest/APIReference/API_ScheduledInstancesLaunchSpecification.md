---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstancesLaunchSpecification.html
---

# ScheduledInstancesLaunchSpecification
<a name="API_ScheduledInstancesLaunchSpecification"></a>

Describes the launch specification for a Scheduled Instance.

If you are launching the Scheduled Instance in EC2-VPC, you must specify the ID of the subnet. You can specify the subnet using either `SubnetId` or `NetworkInterface`.

## Contents
<a name="API_ScheduledInstancesLaunchSpecification_Contents"></a>

 ** ImageId **
The ID of the Amazon Machine Image (AMI).
Type: String
Required: Yes

 ** BlockDeviceMapping.N **
The block device mapping entries.
Type: Array of [ScheduledInstancesBlockDeviceMapping](API_ScheduledInstancesBlockDeviceMapping.md) objects
Required: No

 ** EbsOptimized **
Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
Default: `false`
Type: Boolean
Required: No

 ** IamInstanceProfile **
The IAM instance profile.
Type: [ScheduledInstancesIamInstanceProfile](API_ScheduledInstancesIamInstanceProfile.md) object
Required: No

 ** InstanceType **
The instance type.
Type: String
Required: No

 ** KernelId **
The ID of the kernel.
Type: String
Required: No

 ** KeyName **
The name of the key pair.
Type: String
Required: No

 ** Monitoring **
Enable or disable monitoring for the instances.
Type: [ScheduledInstancesMonitoring](API_ScheduledInstancesMonitoring.md) object
Required: No

 ** NetworkInterface.N **
The network interfaces.
Type: Array of [ScheduledInstancesNetworkInterface](API_ScheduledInstancesNetworkInterface.md) objects
Required: No

 ** Placement **
The placement information.
Type: [ScheduledInstancesPlacement](API_ScheduledInstancesPlacement.md) object
Required: No

 ** RamdiskId **
The ID of the RAM disk.
Type: String
Required: No

 ** SecurityGroupId.N **
The IDs of the security groups.
Type: Array of strings
Required: No

 ** SubnetId **
The ID of the subnet in which to launch the instances.
Type: String
Required: No

 ** UserData **
The base64-encoded MIME user data.
Type: String
Required: No

## See Also
<a name="API_ScheduledInstancesLaunchSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstancesLaunchSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstancesLaunchSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstancesLaunchSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
