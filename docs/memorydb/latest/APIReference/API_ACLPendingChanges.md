---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ACLPendingChanges.html
---

# ACLPendingChanges
<a name="API_ACLPendingChanges"></a>

Returns the updates being applied to the ACL.

## Contents
<a name="API_ACLPendingChanges_Contents"></a>

 ** UserNamesToAdd **   <a name="MemoryDB-Type-ACLPendingChanges-UserNamesToAdd"></a>
A list of users being added to the ACL
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** UserNamesToRemove **   <a name="MemoryDB-Type-ACLPendingChanges-UserNamesToRemove"></a>
A list of user names being removed from the ACL
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_ACLPendingChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ACLPendingChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ACLPendingChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ACLPendingChanges)
