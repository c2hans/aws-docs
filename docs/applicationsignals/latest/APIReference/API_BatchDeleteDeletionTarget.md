---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteDeletionTarget.html
---

# BatchDeleteDeletionTarget
<a name="API_BatchDeleteDeletionTarget"></a>

The batch delete target selection. Exactly one of the two modes must be specified.

## Contents
<a name="API_BatchDeleteDeletionTarget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ResourceArns **   <a name="applicationsignals-Type-BatchDeleteDeletionTarget-ResourceArns"></a>
Delete specific configurations by ARN list.
Type: [BatchDeleteByResourceArns](API_BatchDeleteByResourceArns.md) object
Required: No

 ** Scope **   <a name="applicationsignals-Type-BatchDeleteDeletionTarget-Scope"></a>
Delete all configurations matching the specified scope.
Type: [BatchDeleteScope](API_BatchDeleteScope.md) object
Required: No

## See Also
<a name="API_BatchDeleteDeletionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteDeletionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteDeletionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteDeletionTarget)
