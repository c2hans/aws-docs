---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Subnet.html
---

# Subnet
<a name="API_Subnet"></a>

Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

## Contents
<a name="API_Subnet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SubnetAvailabilityZone **
The Availability Zone associated with the subnet.
Type: [AvailabilityZone](API_AvailabilityZone.md) object
Required: No

 ** SubnetIdentifier **
The unique identifier for the subnet.
Type: String
Required: No

 ** SubnetOutpost **
The outpost ARN of the subnet.
Type: [SubnetOutpost](API_SubnetOutpost.md) object
Required: No

 ** SupportedNetworkTypes.member.N **
Either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: Array of strings
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

## See Also
<a name="API_Subnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Subnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Subnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Subnet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
