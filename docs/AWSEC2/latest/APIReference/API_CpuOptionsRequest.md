---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CpuOptionsRequest.html
---

# CpuOptionsRequest
<a name="API_CpuOptionsRequest"></a>

The CPU options for the instance. Both the core count and threads per core must be specified in the request.

## Contents
<a name="API_CpuOptionsRequest_Contents"></a>

 ** AmdSevSnp **
Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only. For more information, see [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html).
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** CoreCount **
The number of CPU cores for the instance.
Type: Integer
Required: No

 ** NestedVirtualization **
Indicates whether to enable the instance for nested virtualization. Nested virtualization is supported only on 8th generation Intel-based instance types (c8i, m8i, r8i, and their flex variants). When nested virtualization is enabled, Virtual Secure Mode (VSM) is automatically disabled for the instance.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** ThreadsPerCore **
The number of threads per CPU core. To disable multithreading for the instance, specify a value of `1`. Otherwise, specify the default value of `2`.
Type: Integer
Required: No

## See Also
<a name="API_CpuOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CpuOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CpuOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CpuOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
