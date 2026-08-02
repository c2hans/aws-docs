---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AvailableCapacity.html
---

# AvailableCapacity
<a name="API_AvailableCapacity"></a>

The capacity information for instances that can be launched onto the Dedicated Host.

## Contents
<a name="API_AvailableCapacity_Contents"></a>

 ** AvailableInstanceCapacity.N **
The number of instances that can be launched onto the Dedicated Host depending on the host's available capacity. For Dedicated Hosts that support multiple instance types, this parameter represents the number of instances for each instance size that is supported on the host.
Type: Array of [InstanceCapacity](API_InstanceCapacity.md) objects
Required: No

 ** availableVCpus **
The number of vCPUs available for launching instances onto the Dedicated Host.
Type: Integer
Required: No

## See Also
<a name="API_AvailableCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AvailableCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AvailableCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AvailableCapacity)
