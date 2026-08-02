---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GroupMembers.html
---

# GroupMembers
<a name="API_GroupMembers"></a>

A list of users or sub groups that belong to a group. This is for generating Amazon Q Business chat results only from document a user has access to.

## Contents
<a name="API_GroupMembers_Contents"></a>

 ** memberGroups **   <a name="qbusiness-Type-GroupMembers-memberGroups"></a>
A list of sub groups that belong to a group. For example, the sub groups "Research", "Engineering", and "Sales and Marketing" all belong to the group "Company".
Type: Array of [MemberGroup](API_MemberGroup.md) objects
Required: No

 ** memberUsers **   <a name="qbusiness-Type-GroupMembers-memberUsers"></a>
A list of users that belong to a group. For example, a list of interns all belong to the "Interns" group.
Type: Array of [MemberUser](API_MemberUser.md) objects
Required: No

 ** s3PathForGroupMembers **   <a name="qbusiness-Type-GroupMembers-s3PathForGroupMembers"></a>
Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.
Type: [S3](API_S3.md) object
Required: No

## See Also
<a name="API_GroupMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GroupMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GroupMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GroupMembers)
