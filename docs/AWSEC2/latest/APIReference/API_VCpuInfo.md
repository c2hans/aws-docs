---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VCpuInfo.html
---

# VCpuInfo
<a name="API_VCpuInfo"></a>

Describes the vCPU configurations for the instance type.

## Contents
<a name="API_VCpuInfo_Contents"></a>

 ** defaultCores **
The default number of cores for the instance type.
Type: Integer
Required: No

 ** defaultThreadsPerCore **
The default number of threads per core for the instance type.
Type: Integer
Required: No

 ** defaultVCpus **
The default number of vCPUs for the instance type.
Type: Integer
Required: No

 ** ValidCores.N **
The valid number of cores that can be configured for the instance type.
Type: Array of integers
Required: No

 ** ValidThreadsPerCore.N **
The valid number of threads per core that can be configured for the instance type.
Type: Array of integers
Required: No

## See Also
<a name="API_VCpuInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VCpuInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VCpuInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VCpuInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
