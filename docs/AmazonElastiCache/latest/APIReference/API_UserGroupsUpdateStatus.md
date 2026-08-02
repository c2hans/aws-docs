---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_UserGroupsUpdateStatus.html
---

# UserGroupsUpdateStatus
<a name="API_UserGroupsUpdateStatus"></a>

The status of the user group update.

## Contents
<a name="API_UserGroupsUpdateStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** UserGroupIdsToAdd.member.N **
The ID of the user group to add.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** UserGroupIdsToRemove.member.N **
The ID of the user group to remove.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_UserGroupsUpdateStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/UserGroupsUpdateStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/UserGroupsUpdateStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/UserGroupsUpdateStatus)
