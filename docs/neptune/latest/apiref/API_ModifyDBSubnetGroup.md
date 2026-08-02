---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBSubnetGroup.html
---

# ModifyDBSubnetGroup
<a name="API_ModifyDBSubnetGroup"></a>

Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.

## Request Parameters
<a name="API_ModifyDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupDescription **
The description for the DB subnet group.
Type: String
Required: No

 ** DBSubnetGroupName **
The name for the DB subnet group. This value is stored as a lowercase string. You can't modify the default subnet group.
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
Example: `mySubnetgroup`
Type: String
Required: Yes

 **SubnetIds.SubnetIdentifier.N**
The EC2 subnet IDs for the DB subnet group.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_ModifyDBSubnetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBSubnetGroup **
Contains the details of an Amazon Neptune DB subnet group.
This data type is used as a response element in the [DescribeDBSubnetGroups](API_DescribeDBSubnetGroups.md) action.
Type: [DBSubnetGroup](API_DBSubnetGroup.md) object

## Errors
<a name="API_ModifyDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupDoesNotCoverEnoughAZs **
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **
 *DBSubnetGroupName* does not refer to an existing DB subnet group.
HTTP Status Code: 404

 ** DBSubnetQuotaExceededFault **
Request would result in user exceeding the allowed number of subnets in a DB subnet groups.
HTTP Status Code: 400

 ** InvalidSubnet **
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.
HTTP Status Code: 400

 ** SubnetAlreadyInUse **
The DB subnet is already in use in the Availability Zone.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBSubnetGroup)
