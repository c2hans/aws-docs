---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ServiceManagedEc2InstanceCapabilities.html
---

# ServiceManagedEc2InstanceCapabilities
<a name="API_ServiceManagedEc2InstanceCapabilities"></a>

The Amazon EC2 instance capabilities.

## Contents
<a name="API_ServiceManagedEc2InstanceCapabilities_Contents"></a>

 ** cpuArchitectureType **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-cpuArchitectureType"></a>
The CPU architecture type.
Type: String
Valid Values: `x86_64 | arm64`
Required: Yes

 ** memoryMiB **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-memoryMiB"></a>
The memory, as MiB, for the Amazon EC2 instance type.
Type: [MemoryMiBRange](API_MemoryMiBRange.md) object
Required: Yes

 ** osFamily **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-osFamily"></a>
The operating system (OS) family.
Type: String
Valid Values: `WINDOWS | LINUX`
Required: Yes

 ** vCpuCount **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-vCpuCount"></a>
The amount of vCPU to require for instances in this fleet.
Type: [VCpuCountRange](API_VCpuCountRange.md) object
Required: Yes

 ** acceleratorCapabilities **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-acceleratorCapabilities"></a>
Describes the GPU accelerator capabilities required for worker host instances in this fleet.
Type: [AcceleratorCapabilities](API_AcceleratorCapabilities.md) object
Required: No

 ** allowedInstanceTypes **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-allowedInstanceTypes"></a>
The allowable Amazon EC2 instance types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** customAmounts **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-customAmounts"></a>
The custom capability amounts to require for instances in this fleet.
Type: Array of [FleetAmountCapability](API_FleetAmountCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** customAttributes **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-customAttributes"></a>
The custom capability attributes to require for instances in this fleet.
Type: Array of [FleetAttributeCapability](API_FleetAttributeCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** excludedInstanceTypes **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-excludedInstanceTypes"></a>
The instance types to exclude from the fleet.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** rootEbsVolume **   <a name="deadlinecloud-Type-ServiceManagedEc2InstanceCapabilities-rootEbsVolume"></a>
The root EBS volume.
Type: [Ec2EbsVolume](API_Ec2EbsVolume.md) object
Required: No

## See Also
<a name="API_ServiceManagedEc2InstanceCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2InstanceCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
