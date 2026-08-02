---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PublicIpv4Pool.html
---

# PublicIpv4Pool
<a name="API_PublicIpv4Pool"></a>

Describes an IPv4 address pool.

## Contents
<a name="API_PublicIpv4Pool_Contents"></a>

 ** description **
A description of the address pool.
Type: String
Required: No

 ** networkBorderGroup **
The name of the location from which the address pool is advertised. A network border group is a unique set of Availability Zones or Local Zones from where AWS advertises public IP addresses.
Type: String
Required: No

 ** PoolAddressRangeSet.N **
The address ranges.
Type: Array of [PublicIpv4PoolRange](API_PublicIpv4PoolRange.md) objects
Required: No

 ** poolId **
The ID of the address pool.
Type: String
Required: No

 ** TagSet.N **
Any tags for the address pool.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** totalAddressCount **
The total number of addresses.
Type: Integer
Required: No

 ** totalAvailableAddressCount **
The total number of available addresses.
Type: Integer
Required: No

## See Also
<a name="API_PublicIpv4Pool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PublicIpv4Pool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PublicIpv4Pool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PublicIpv4Pool)
