---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_GroupMembers.html
---

# GroupMembers
<a name="API_GroupMembers"></a>

A list of users that belong to a group. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

## Contents
<a name="API_GroupMembers_Contents"></a>

 ** MemberGroups **   <a name="kendra-Type-GroupMembers-MemberGroups"></a>
A list of users that belong to a group. This can also include sub groups. For example, the sub groups "Research", "Engineering", and "Sales and Marketing" all belong to the group "Company A".
Type: Array of [MemberGroup](API_MemberGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** MemberUsers **   <a name="kendra-Type-GroupMembers-MemberUsers"></a>
A list of users that belong to a group. For example, a list of interns all belong to the "Interns" group.
Type: Array of [MemberUser](API_MemberUser.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** S3PathforGroupMembers **   <a name="kendra-Type-GroupMembers-S3PathforGroupMembers"></a>
If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.
You can download this [example S3 file](https://docs.aws.amazon.com/kendra/latest/dg/samples/group_members.zip) that uses the correct format for listing group members. Note, `dataSourceId` is optional. The value of `type` for a group is always `GROUP` and for a user it is always `USER`.
Type: [S3Path](API_S3Path.md) object
Required: No

## See Also
<a name="API_GroupMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/GroupMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/GroupMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/GroupMembers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
