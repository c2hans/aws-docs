---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FpgaDeviceInfo.html
---

# FpgaDeviceInfo
<a name="API_FpgaDeviceInfo"></a>

Describes the FPGA accelerator for the instance type.

## Contents
<a name="API_FpgaDeviceInfo_Contents"></a>

 ** count **
The count of FPGA accelerators for the instance type.
Type: Integer
Required: No

 ** manufacturer **
The manufacturer of the FPGA accelerator.
Type: String
Required: No

 ** memoryInfo **
Describes the memory for the FPGA accelerator for the instance type.
Type: [FpgaDeviceMemoryInfo](API_FpgaDeviceMemoryInfo.md) object
Required: No

 ** name **
The name of the FPGA accelerator.
Type: String
Required: No

## See Also
<a name="API_FpgaDeviceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FpgaDeviceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FpgaDeviceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FpgaDeviceInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
