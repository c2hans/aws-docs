---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBSubnetGroup.html
---

# DBSubnetGroup
<a name="API_DBSubnetGroup"></a>

Contains the details of an Amazon Neptune DB subnet group.

This data type is used as a response element in the [DescribeDBSubnetGroups](API_DescribeDBSubnetGroups.md) action.

## Contents
<a name="API_DBSubnetGroup_Contents"></a>

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
 Contains a list of [Subnet](API_Subnet.md) elements.
Type: Array of [Subnet](API_Subnet.md) objects
Required: No

 ** VpcId **
Provides the VpcId of the DB subnet group.
Type: String
Required: No

## See Also
<a name="API_DBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBSubnetGroup)
