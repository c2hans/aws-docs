---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_InlinePolicyIdentifierType.html
---

# InlinePolicyIdentifierType
<a name="API_InlinePolicyIdentifierType"></a>

Identifies one or more inline policies that are embedded in IAM users, groups, or roles, by the name of the policy together with the type and name of the entity that it is attached to. Wildcard characters in the entity name can match multiple entities, so a single identifier can select more than one attached inline policy.

## Contents
<a name="API_InlinePolicyIdentifierType_Contents"></a>

 ** AttachmentName **
The name of the IAM user, group, or role that the inline policy is attached to. Wildcard characters are supported to match multiple entities: use at most one `*` (matches any sequence of characters, including none), and any number of `?` (each matches exactly one character).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** AttachmentType **
The type of IAM entity that the inline policy is attached to.
Type: String
Valid Values: `user | group | role`
Required: Yes

 ** PolicyName **
The name of the inline policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## See Also
<a name="API_InlinePolicyIdentifierType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/InlinePolicyIdentifierType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/InlinePolicyIdentifierType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/InlinePolicyIdentifierType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
