---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GroupMember.html
---

# GroupMember
<a name="API_GroupMember"></a>

A member of an Quick Sight group. Currently, group members must be users. Groups can't be members of another group. .

## Contents
<a name="API_GroupMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-GroupMember-Arn"></a>
The Amazon Resource Name (ARN) for the group member (user).
Type: String
Required: No

 ** MemberName **   <a name="QS-Type-GroupMember-MemberName"></a>
The name of the group member (user).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_GroupMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GroupMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GroupMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GroupMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
