---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ACL.html
---

# ACL
<a name="API_ACL"></a>

An Access Control List. You can authenticate users with Access Contol Lists. ACLs enable you to control cluster access by grouping users. These Access control lists are designed as a way to organize access to clusters.

## Contents
<a name="API_ACL_Contents"></a>

 ** ARN **   <a name="MemoryDB-Type-ACL-ARN"></a>
The Amazon Resource Name (ARN) of the ACL
Type: String
Required: No

 ** Clusters **   <a name="MemoryDB-Type-ACL-Clusters"></a>
A list of clusters associated with the ACL.
Type: Array of strings
Required: No

 ** MinimumEngineVersion **   <a name="MemoryDB-Type-ACL-MinimumEngineVersion"></a>
The minimum engine version supported for the ACL
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-ACL-Name"></a>
The name of the Access Control List
Type: String
Required: No

 ** PendingChanges **   <a name="MemoryDB-Type-ACL-PendingChanges"></a>
A list of updates being applied to the ACL.
Type: [ACLPendingChanges](API_ACLPendingChanges.md) object
Required: No

 ** Status **   <a name="MemoryDB-Type-ACL-Status"></a>
Indicates ACL status. Can be "creating", "active", "modifying", "deleting".
Type: String
Required: No

 ** UserNames **   <a name="MemoryDB-Type-ACL-UserNames"></a>
The list of user names that belong to the ACL.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_ACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ACL)
