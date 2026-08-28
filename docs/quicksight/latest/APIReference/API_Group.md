---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

A *group* in Quick Sight consists of a set of users. You can use groups to make it easier to manage access and security.

## Contents
<a name="API_Group_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Group-Arn"></a>
The Amazon Resource Name (ARN) for the group.
Type: String
Required: No

 ** Description **   <a name="QS-Type-Group-Description"></a>
The group description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** GroupName **   <a name="QS-Type-Group-GroupName"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** PrincipalId **   <a name="QS-Type-Group-PrincipalId"></a>
The principal ID of the group.
Type: String
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Group)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
