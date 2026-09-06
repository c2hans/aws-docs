---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DeleteDBParameterGroup.html
---

# DeleteDBParameterGroup
<a name="API_DeleteDBParameterGroup"></a>

Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can't be associated with any DB instances.

## Request Parameters
<a name="API_DeleteDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupName **
The name of the DB parameter group.
Constraints:
+ Must be the name of an existing DB parameter group
+ You can't delete a default DB parameter group
+ Cannot be associated with any DB instances
Type: String
Required: Yes

## Errors
<a name="API_DeleteDBParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DeleteDBParameterGroup)
