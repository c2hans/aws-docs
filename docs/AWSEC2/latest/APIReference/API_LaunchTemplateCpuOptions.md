---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateCpuOptions.html
---

# LaunchTemplateCpuOptions
<a name="API_LaunchTemplateCpuOptions"></a>

The CPU options for the instance.

## Contents
<a name="API_LaunchTemplateCpuOptions_Contents"></a>

 ** amdSevSnp **
Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see [AMD SEV-SNP for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html).
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** coreCount **
The number of CPU cores for the instance.
Type: Integer
Required: No

 ** nestedVirtualization **
Indicates whether the instance is enabled for nested virtualization.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** threadsPerCore **
The number of threads per CPU core.
Type: Integer
Required: No

## See Also
<a name="API_LaunchTemplateCpuOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateCpuOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateCpuOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateCpuOptions)
