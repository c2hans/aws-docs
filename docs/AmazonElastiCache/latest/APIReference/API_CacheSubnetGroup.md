---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheSubnetGroup.html
---

# CacheSubnetGroup
<a name="API_CacheSubnetGroup"></a>

Represents the output of one of the following operations:
+  `CreateCacheSubnetGroup`
+  `ModifyCacheSubnetGroup`

## Contents
<a name="API_CacheSubnetGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN (Amazon Resource Name) of the cache subnet group.
Type: String
Required: No

 ** CacheSubnetGroupDescription **
The description of the cache subnet group.
Type: String
Required: No

 ** CacheSubnetGroupName **
The name of the cache subnet group.
Type: String
Required: No

 ** Subnets.Subnet.N **
A list of subnets associated with the cache subnet group.
Type: Array of [Subnet](API_Subnet.md) objects
Required: No

 ** SupportedNetworkTypes.member.N **
Either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: Array of strings
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** VpcId **
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.
Type: String
Required: No

## See Also
<a name="API_CacheSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheSubnetGroup)
