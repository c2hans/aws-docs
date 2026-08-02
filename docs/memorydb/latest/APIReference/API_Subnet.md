---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Subnet.html
---

# Subnet
<a name="API_Subnet"></a>

Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with MemoryDB.

## Contents
<a name="API_Subnet_Contents"></a>

 ** AvailabilityZone **   <a name="MemoryDB-Type-Subnet-AvailabilityZone"></a>
The Availability Zone where the subnet resides
Type: [AvailabilityZone](API_AvailabilityZone.md) object
Required: No

 ** Identifier **   <a name="MemoryDB-Type-Subnet-Identifier"></a>
The unique identifier for the subnet.
Type: String
Required: No

 ** SupportedNetworkTypes **   <a name="MemoryDB-Type-Subnet-SupportedNetworkTypes"></a>
The network types supported by this subnet. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating whether the subnet supports IPv4 only, IPv6 only, or dual-stack deployments.
Type: Array of strings
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

## See Also
<a name="API_Subnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Subnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Subnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Subnet)
