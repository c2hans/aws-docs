---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_MemberGroup.html
---

# MemberGroup
<a name="API_MemberGroup"></a>

The sub groups that belong to a group.

## Contents
<a name="API_MemberGroup_Contents"></a>

 ** GroupId **   <a name="kendra-Type-MemberGroup-GroupId"></a>
The identifier of the sub group you want to map to a group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\P{C}*$`
Required: Yes

 ** DataSourceId **   <a name="kendra-Type-MemberGroup-DataSourceId"></a>
The identifier of the data source for the sub group you want to map to a group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

## See Also
<a name="API_MemberGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/MemberGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/MemberGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/MemberGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
