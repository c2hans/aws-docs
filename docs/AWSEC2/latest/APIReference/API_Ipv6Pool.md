---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Ipv6Pool.html
---

# Ipv6Pool
<a name="API_Ipv6Pool"></a>

Describes an IPv6 address pool.

## Contents
<a name="API_Ipv6Pool_Contents"></a>

 ** description **
The description for the address pool.
Type: String
Required: No

 ** PoolCidrBlockSet.N **
The CIDR blocks for the address pool.
Type: Array of [PoolCidrBlock](API_PoolCidrBlock.md) objects
Required: No

 ** poolId **
The ID of the address pool.
Type: String
Required: No

 ** TagSet.N **
Any tags for the address pool.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Ipv6Pool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Ipv6Pool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Ipv6Pool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Ipv6Pool)
