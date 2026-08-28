---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CreateDBClusterParameterGroup.html
---

# CreateDBClusterParameterGroup
<a name="API_CreateDBClusterParameterGroup"></a>

Creates a new DB cluster parameter group.

Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.

 A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using [ModifyDBClusterParameterGroup](API_ModifyDBClusterParameterGroup.md). Once you've created a DB cluster parameter group, you need to associate it with your DB cluster using [ModifyDBCluster](API_ModifyDBCluster.md). When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.

**Important**
After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the `character_set_database` parameter. You can use the *Parameter Groups* option of the [Amazon Neptune console](https://console.aws.amazon.com/rds/) or the [DescribeDBClusterParameters](API_DescribeDBClusterParameters.md) command to verify that your DB cluster parameter group has been created or modified.

## Request Parameters
<a name="API_CreateDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **
The name of the DB cluster parameter group.
Constraints:
+ Must match the name of an existing DBClusterParameterGroup.
This value is stored as a lowercase string.
Type: String
Required: Yes

 ** DBParameterGroupFamily **
The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
Type: String
Required: Yes

 ** Description **
The description for the DB cluster parameter group.
Type: String
Required: Yes

 **Tags.Tag.N**
The tags to be assigned to the new DB cluster parameter group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroup **
Contains the details of an Amazon Neptune DB cluster parameter group.
This data type is used as a response element in the [DescribeDBClusterParameterGroups](API_DescribeDBClusterParameterGroups.md) action.
Type: [DBClusterParameterGroup](API_DBClusterParameterGroup.md) object

## Errors
<a name="API_CreateDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupAlreadyExists **
A DB parameter group with the same name exists.
HTTP Status Code: 400

 ** DBParameterGroupQuotaExceeded **
Request would result in user exceeding the allowed number of DB parameter groups.
HTTP Status Code: 400

## See Also
<a name="API_CreateDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBClusterParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CreateDBClusterParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
