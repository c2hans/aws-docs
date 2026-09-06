---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSubnetGroup.html
---

# DBSubnetGroup
<a name="API_DBSubnetGroup"></a>

Contains the details of an Amazon RDS DB subnet group.

This data type is used as a response element in the `DescribeDBSubnetGroups` action.

## Contents
<a name="API_DBSubnetGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBSubnetGroupArn **
The Amazon Resource Name (ARN) for the DB subnet group.
Type: String
Required: No

 ** DBSubnetGroupDescription **
Provides the description of the DB subnet group.
Type: String
Required: No

 ** DBSubnetGroupName **
The name of the DB subnet group.
Type: String
Required: No

 ** SubnetGroupStatus **
Provides the status of the DB subnet group.
Type: String
Required: No

 ** Subnets.Subnet.N **
Contains a list of `Subnet` elements. The list of subnets shown here might not reflect the current state of your VPC. For the most up-to-date information, we recommend checking your VPC configuration directly.
Type: Array of [Subnet](API_Subnet.md) objects
Required: No

 ** SupportedNetworkTypes.member.N **
The network type of the DB subnet group.
Valid values:
+  `IPV4`
+  `DUAL`
A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*
Type: Array of strings
Required: No

 ** VpcId **
Provides the VpcId of the DB subnet group.
Type: String
Required: No

## See Also
<a name="API_DBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSubnetGroup)
