---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GpuDeviceInfo.html
---

# GpuDeviceInfo
<a name="API_GpuDeviceInfo"></a>

Describes the GPU accelerators for the instance type.

## Contents
<a name="API_GpuDeviceInfo_Contents"></a>

 ** count **
The number of GPUs for the instance type.
Type: Integer
Required: No

 ** gpuPartitionSize **
The size of each GPU as a fraction of a full GPU, between 0 (excluded) and 1 (included).
Type: Double
Required: No

 ** logicalGpuCount **
Total number of GPU devices of this type.
Type: Integer
Required: No

 ** manufacturer **
The manufacturer of the GPU accelerator.
Type: String
Required: No

 ** memoryInfo **
Describes the memory available to the GPU accelerator.
Type: [GpuDeviceMemoryInfo](API_GpuDeviceMemoryInfo.md) object
Required: No

 ** name **
The name of the GPU accelerator.
Type: String
Required: No

 ** WorkloadSet.N **
A list of workload types this GPU supports.
Type: Array of strings
Required: No

## See Also
<a name="API_GpuDeviceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GpuDeviceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GpuDeviceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GpuDeviceInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
