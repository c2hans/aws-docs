---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationRule.html
---

# ImpersonationRule
<a name="API_ImpersonationRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The rules for the given impersonation role.

## Contents
<a name="API_ImpersonationRule_Contents"></a>

 ** Effect **   <a name="workmail-Type-ImpersonationRule-Effect"></a>
The effect of the rule when it matches the input. Allowed effect values are `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** ImpersonationRuleId **   <a name="workmail-Type-ImpersonationRule-ImpersonationRuleId"></a>
The identifier of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** Description **   <a name="workmail-Type-ImpersonationRule-Description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F\x3C\x3E\x5C]+`
Required: No

 ** Name **   <a name="workmail-Type-ImpersonationRule-Name"></a>
The rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
Required: No

 ** NotTargetUsers **   <a name="workmail-Type-ImpersonationRule-NotTargetUsers"></a>
A list of user IDs that don't match the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: No

 ** TargetUsers **   <a name="workmail-Type-ImpersonationRule-TargetUsers"></a>
A list of user IDs that match the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: No

## See Also
<a name="API_ImpersonationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ImpersonationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ImpersonationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ImpersonationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
