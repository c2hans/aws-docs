---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CopyDBClusterParameterGroup.html
---

# CopyDBClusterParameterGroup
<a name="API_CopyDBClusterParameterGroup"></a>

Copies the specified DB cluster parameter group.

## Request Parameters
<a name="API_CopyDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBClusterParameterGroupIdentifier **
The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see [ Constructing an Amazon Resource Name (ARN)](https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
Constraints:
+ Must specify a valid DB cluster parameter group.
+ If the source DB cluster parameter group is in the same Amazon Region as the copy, specify a valid DB parameter group identifier, for example `my-db-cluster-param-group`, or a valid ARN.
+ If the source DB parameter group is in a different Amazon Region than the copy, specify a valid DB cluster parameter group ARN, for example `arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`.
Type: String
Required: Yes

 **Tags.Tag.N**
The tags to be assigned to the copied DB cluster parameter group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TargetDBClusterParameterGroupDescription **
A description for the copied DB cluster parameter group.
Type: String
Required: Yes

 ** TargetDBClusterParameterGroupIdentifier **
The identifier for the copied DB cluster parameter group.
Constraints:
+ Cannot be null, empty, or blank
+ Must contain from 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Example: `my-cluster-param-group1`
Type: String
Required: Yes

## Response Elements
<a name="API_CopyDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroup **
Contains the details of an Amazon Neptune DB cluster parameter group.
This data type is used as a response element in the [DescribeDBClusterParameterGroups](API_DescribeDBClusterParameterGroups.md) action.
Type: [DBClusterParameterGroup](API_DBClusterParameterGroup.md) object

## Errors
<a name="API_CopyDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupAlreadyExists **
A DB parameter group with the same name exists.
HTTP Status Code: 400

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** DBParameterGroupQuotaExceeded **
Request would result in user exceeding the allowed number of DB parameter groups.
HTTP Status Code: 400

## See Also
<a name="API_CopyDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CopyDBClusterParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CopyDBClusterParameterGroup)
