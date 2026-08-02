---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DeleteDBSubnetGroup.html
---

# DeleteDBSubnetGroup
<a name="API_DeleteDBSubnetGroup"></a>

Deletes a DB subnet group.

**Note**
The specified database subnet group must not be associated with any DB instances.

## Request Parameters
<a name="API_DeleteDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **
The name of the database subnet group to delete.
You can't delete the default subnet group.
Constraints:
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
Example: `mySubnetgroup`
Type: String
Required: Yes

## Errors
<a name="API_DeleteDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupNotFoundFault **
 *DBSubnetGroupName* does not refer to an existing DB subnet group.
HTTP Status Code: 404

 ** InvalidDBSubnetGroupStateFault **
The DB subnet group cannot be deleted because it is in use.
HTTP Status Code: 400

 ** InvalidDBSubnetStateFault **
The DB subnet is not in the *available* state.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DeleteDBSubnetGroup)
