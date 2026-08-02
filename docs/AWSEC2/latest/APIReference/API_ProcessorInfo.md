---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProcessorInfo.html
---

# ProcessorInfo
<a name="API_ProcessorInfo"></a>

Describes the processor used by the instance type.

## Contents
<a name="API_ProcessorInfo_Contents"></a>

 ** manufacturer **
The manufacturer of the processor.
Type: String
Required: No

 ** SupportedArchitectures.N **
The architectures supported by the instance type.
Type: Array of strings
Valid Values: `i386 | x86_64 | arm64 | x86_64_mac | arm64_mac`
Required: No

 ** SupportedFeatures.N **
Indicates whether the instance type supports AMD SEV-SNP. If the request returns `amd-sev-snp`, AMD SEV-SNP is supported. Otherwise, it is not supported. For more information, see [ AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html).
Type: Array of strings
Valid Values: `amd-sev-snp | nested-virtualization`
Required: No

 ** sustainedClockSpeedInGhz **
The speed of the processor, in GHz.
Type: Double
Required: No

## See Also
<a name="API_ProcessorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ProcessorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ProcessorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ProcessorInfo)
