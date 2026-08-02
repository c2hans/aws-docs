---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_UserGroupPendingChanges.html
---

# UserGroupPendingChanges
<a name="API_UserGroupPendingChanges"></a>

Returns the updates being applied to the user group.

## Contents
<a name="API_UserGroupPendingChanges_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** UserIdsToAdd.member.N **
The list of user IDs to add.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** UserIdsToRemove.member.N **
The list of user IDs to remove.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_UserGroupPendingChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/UserGroupPendingChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/UserGroupPendingChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/UserGroupPendingChanges)
