---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBParameterGroupStatus.html
---

# DBParameterGroupStatus
<a name="API_DBParameterGroupStatus"></a>

The status of the DB parameter group.

This data type is used as a response element in the following actions:
+  [CreateDBInstance](API_CreateDBInstance.md)
+  [DeleteDBInstance](API_DeleteDBInstance.md)
+  [ModifyDBInstance](API_ModifyDBInstance.md)
+  [RebootDBInstance](API_RebootDBInstance.md)

## Contents
<a name="API_DBParameterGroupStatus_Contents"></a>

 ** DBParameterGroupName **
The name of the DP parameter group.
Type: String
Required: No

 ** ParameterApplyStatus **
The status of parameter updates.
Type: String
Required: No

## See Also
<a name="API_DBParameterGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBParameterGroupStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBParameterGroupStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBParameterGroupStatus)
