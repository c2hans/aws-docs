---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CustomerManagedWorkerCapabilities.html
---

# CustomerManagedWorkerCapabilities
<a name="API_CustomerManagedWorkerCapabilities"></a>

The worker capabilities for a customer managed workflow.

## Contents
<a name="API_CustomerManagedWorkerCapabilities_Contents"></a>

 ** cpuArchitectureType **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-cpuArchitectureType"></a>
The CPU architecture type for the customer managed worker capabilities.
Type: String
Valid Values: `x86_64 | arm64`
Required: Yes

 ** memoryMiB **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-memoryMiB"></a>
The memory (MiB).
Type: [MemoryMiBRange](API_MemoryMiBRange.md) object
Required: Yes

 ** osFamily **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-osFamily"></a>
The operating system (OS) family.
Type: String
Valid Values: `WINDOWS | LINUX | MACOS`
Required: Yes

 ** vCpuCount **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-vCpuCount"></a>
The vCPU count for the customer manged worker capabilities.
Type: [VCpuCountRange](API_VCpuCountRange.md) object
Required: Yes

 ** acceleratorCount **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-acceleratorCount"></a>
The range of the accelerator.
Type: [AcceleratorCountRange](API_AcceleratorCountRange.md) object
Required: No

 ** acceleratorTotalMemoryMiB **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-acceleratorTotalMemoryMiB"></a>
The total memory (MiB) for the customer managed worker capabilities.
Type: [AcceleratorTotalMemoryMiBRange](API_AcceleratorTotalMemoryMiBRange.md) object
Required: No

 ** acceleratorTypes **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-acceleratorTypes"></a>
The accelerator types for the customer managed worker capabilities.
Type: Array of strings
Valid Values: `gpu`
Required: No

 ** customAmounts **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-customAmounts"></a>
Custom requirement ranges for customer managed worker capabilities.
Type: Array of [FleetAmountCapability](API_FleetAmountCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** customAttributes **   <a name="deadlinecloud-Type-CustomerManagedWorkerCapabilities-customAttributes"></a>
Custom attributes for the customer manged worker capabilities.
Type: Array of [FleetAttributeCapability](API_FleetAttributeCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

## See Also
<a name="API_CustomerManagedWorkerCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedWorkerCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedWorkerCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedWorkerCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
