---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SubnetGroup.html
---

# SubnetGroup
<a name="API_dax_SubnetGroup"></a>

Represents the output of one of the following actions:
+  *CreateSubnetGroup*
+  *ModifySubnetGroup*

## Contents
<a name="API_dax_SubnetGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="DDB-Type-dax_SubnetGroup-Description"></a>
The description of the subnet group.
Type: String
Required: No

 ** SubnetGroupName **   <a name="DDB-Type-dax_SubnetGroup-SubnetGroupName"></a>
The name of the subnet group.
Type: String
Required: No

 ** Subnets **   <a name="DDB-Type-dax_SubnetGroup-Subnets"></a>
A list of subnets associated with the subnet group.
Type: Array of [Subnet](API_dax_Subnet.md) objects
Required: No

 ** SupportedNetworkTypes **   <a name="DDB-Type-dax_SubnetGroup-SupportedNetworkTypes"></a>
The network types supported by this subnet. Returns an array of strings that can include `ipv4`, `ipv6`, or both, indicating whether the subnet group supports IPv4 only, IPv6 only, or dual-stack deployments.
Type: Array of strings
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** VpcId **   <a name="DDB-Type-dax_SubnetGroup-VpcId"></a>
The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
Type: String
Required: No

## See Also
<a name="API_dax_SubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/SubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/SubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/SubnetGroup)
