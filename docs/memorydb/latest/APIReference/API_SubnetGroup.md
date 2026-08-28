---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_SubnetGroup.html
---

# SubnetGroup
<a name="API_SubnetGroup"></a>

Represents the output of one of the following operations:
+ CreateSubnetGroup
+ UpdateSubnetGroup

A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment.

## Contents
<a name="API_SubnetGroup_Contents"></a>

 ** ARN **   <a name="MemoryDB-Type-SubnetGroup-ARN"></a>
The ARN (Amazon Resource Name) of the subnet group.
Type: String
Required: No

 ** Description **   <a name="MemoryDB-Type-SubnetGroup-Description"></a>
A description of the subnet group
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-SubnetGroup-Name"></a>
The name of the subnet group
Type: String
Required: No

 ** Subnets **   <a name="MemoryDB-Type-SubnetGroup-Subnets"></a>
A list of subnets associated with the subnet group.
Type: Array of [Subnet](API_Subnet.md) objects
Required: No

 ** SupportedNetworkTypes **   <a name="MemoryDB-Type-SubnetGroup-SupportedNetworkTypes"></a>
The network types supported by this subnet group. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating the IP address types that can be used for clusters deployed in this subnet group.
Type: Array of strings
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** VpcId **   <a name="MemoryDB-Type-SubnetGroup-VpcId"></a>
The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
Type: String
Required: No

## See Also
<a name="API_SubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/SubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/SubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/SubnetGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
