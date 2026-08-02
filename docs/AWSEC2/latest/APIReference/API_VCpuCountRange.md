---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VCpuCountRange.html
---

# VCpuCountRange
<a name="API_VCpuCountRange"></a>

The minimum and maximum number of vCPUs.

## Contents
<a name="API_VCpuCountRange_Contents"></a>

 ** Max ** (request), ** max ** (response)
The maximum number of vCPUs. If this parameter is not specified, there is no maximum limit.
Type: Integer
Required: No

 ** Min ** (request), ** min ** (response)
The minimum number of vCPUs. If the value is `0`, there is no minimum limit.
Type: Integer
Required: No

## See Also
<a name="API_VCpuCountRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VCpuCountRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VCpuCountRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VCpuCountRange)
