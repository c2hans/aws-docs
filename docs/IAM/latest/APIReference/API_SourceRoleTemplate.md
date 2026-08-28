---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SourceRoleTemplate.html
---

# SourceRoleTemplate
<a name="API_SourceRoleTemplate"></a>

Contains information about the role template that a role was created from.

## Contents
<a name="API_SourceRoleTemplate_Contents"></a>

 ** TemplateArn **
The Amazon Resource Name (ARN) of the role template that the role was created from.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** TemplateMinorVersion **
The minor version of the role template that was used to create the role.
Type: Integer
Required: Yes

## See Also
<a name="API_SourceRoleTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SourceRoleTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SourceRoleTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SourceRoleTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
