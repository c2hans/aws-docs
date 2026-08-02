---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ResetDBParameterGroup.html
---

# ResetDBParameterGroup
<a name="API_ResetDBParameterGroup"></a>

Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: `ParameterName` and `ApplyMethod`. To reset the entire DB parameter group, specify the `DBParameterGroup` name and `ResetAllParameters` parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to `pending-reboot` to take effect on the next DB instance restart or `RebootDBInstance` request.

## Request Parameters
<a name="API_ResetDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupName **
The name of the DB parameter group.
Constraints:
+ Must match the name of an existing DBParameterGroup.
Type: String
Required: Yes

 **Parameters.Parameter.N**
To reset the entire DB parameter group, specify the `DBParameterGroup` name and `ResetAllParameters` parameters. To reset specific parameters, provide a list of the following: `ParameterName` and `ApplyMethod`. A maximum of 20 parameters can be modified in a single request.
Valid Values (for Apply method): `pending-reboot`
Type: Array of [Parameter](API_Parameter.md) objects
Required: No

 ** ResetAllParameters **
Specifies whether (`true`) or not (`false`) to reset all parameters in the DB parameter group to default values.
Default: `true`
Type: Boolean
Required: No

## Response Elements
<a name="API_ResetDBParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBParameterGroupName **
Provides the name of the DB parameter group.
Type: String

## Errors
<a name="API_ResetDBParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.
HTTP Status Code: 400

## See Also
<a name="API_ResetDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ResetDBParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ResetDBParameterGroup)
