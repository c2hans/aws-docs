---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_VCpuCountRequest.html
---

# VCpuCountRequest
<a name="API_VCpuCountRequest"></a>

Specifies the minimum and maximum for the `VCpuCount` object when you specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) for an Auto Scaling group.

## Contents
<a name="API_VCpuCountRequest_Contents"></a>

 ** Min **
The minimum number of vCPUs.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Max **
The maximum number of vCPUs.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_VCpuCountRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/VCpuCountRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/VCpuCountRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/VCpuCountRequest)
