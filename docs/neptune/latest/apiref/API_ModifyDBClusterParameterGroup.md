---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBClusterParameterGroup.html
---

# ModifyDBClusterParameterGroup
<a name="API_ModifyDBClusterParameterGroup"></a>

 Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: `ParameterName`, `ParameterValue`, and `ApplyMethod`. A maximum of 20 parameters can be modified in a single request.

**Note**
Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB cluster associated with the parameter group before the change can take effect.

**Important**
After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the `character_set_database` parameter. You can use the *Parameter Groups* option of the Amazon Neptune console or the [DescribeDBClusterParameters](API_DescribeDBClusterParameters.md) command to verify that your DB cluster parameter group has been created or modified.

## Request Parameters
<a name="API_ModifyDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **
The name of the DB cluster parameter group to modify.
Type: String
Required: Yes

 **Parameters.Parameter.N**
A list of parameters in the DB cluster parameter group to modify.
Type: Array of [Parameter](API_Parameter.md) objects
Required: Yes

## Response Elements
<a name="API_ModifyDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroupName **
The name of the DB cluster parameter group.
Constraints:
+ Must be 1 to 255 letters or numbers.
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
This value is stored as a lowercase string.
Type: String

## Errors
<a name="API_ModifyDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBClusterParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBClusterParameterGroup)
