---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HostCpuOptions.html
---

# HostCpuOptions
<a name="API_HostCpuOptions"></a>

Contains the CPU options for a Dedicated Host, including AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) settings.

## Contents
<a name="API_HostCpuOptions_Contents"></a>

 ** amdSevSnp **
Specifies whether AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) is enabled or disabled for the Dedicated Host. If you don't specify a value, AMD SEV-SNP is `disabled`.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_HostCpuOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HostCpuOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HostCpuOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HostCpuOptions)
