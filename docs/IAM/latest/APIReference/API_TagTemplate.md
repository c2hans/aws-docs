---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagTemplate.html
---

# TagTemplate
<a name="API_TagTemplate"></a>

Represents a tag that is applied to roles that are created from a role template. The key and value can include `@{parameter}` placeholders that are replaced with template parameter values when the role is created.

## Contents
<a name="API_TagTemplate_Contents"></a>

 ** Key **
The key name of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@{}]+`
Required: Yes

 ** Value **
The value associated with the tag key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@{}]*`
Required: Yes

## See Also
<a name="API_TagTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/TagTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/TagTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/TagTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
