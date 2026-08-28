---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_AccessControlRule.html
---

# AccessControlRule
<a name="API_AccessControlRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

A rule that controls access to an WorkMail organization.

## Contents
<a name="API_AccessControlRule_Contents"></a>

 ** Actions **   <a name="workmail-Type-AccessControlRule-Actions"></a>
Access protocol actions to include in the rule. Valid values include `ActiveSync`, `AutoDiscover`, `EWS`, `IMAP`, `SMTP`, `WindowsOutlook`, and `WebMail`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]+`
Required: No

 ** DateCreated **   <a name="workmail-Type-AccessControlRule-DateCreated"></a>
The date that the rule was created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="workmail-Type-AccessControlRule-DateModified"></a>
The date that the rule was modified.
Type: Timestamp
Required: No

 ** Description **   <a name="workmail-Type-AccessControlRule-Description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** Effect **   <a name="workmail-Type-AccessControlRule-Effect"></a>
The rule effect.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** ImpersonationRoleIds **   <a name="workmail-Type-AccessControlRule-ImpersonationRoleIds"></a>
Impersonation role IDs to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** IpRanges **   <a name="workmail-Type-AccessControlRule-IpRanges"></a>
IPv4 CIDR ranges to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1024 items.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[12][0-9]|3[0-2])$`
Required: No

 ** Name **   <a name="workmail-Type-AccessControlRule-Name"></a>
The rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** NotActions **   <a name="workmail-Type-AccessControlRule-NotActions"></a>
Access protocol actions to exclude from the rule. Valid values include `ActiveSync`, `AutoDiscover`, `EWS`, `IMAP`, `SMTP`, `WindowsOutlook`, and `WebMail`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]+`
Required: No

 ** NotImpersonationRoleIds **   <a name="workmail-Type-AccessControlRule-NotImpersonationRoleIds"></a>
Impersonation role IDs to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** NotIpRanges **   <a name="workmail-Type-AccessControlRule-NotIpRanges"></a>
IPv4 CIDR ranges to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1024 items.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[12][0-9]|3[0-2])$`
Required: No

 ** NotUserIds **   <a name="workmail-Type-AccessControlRule-NotUserIds"></a>
User IDs to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** UserIds **   <a name="workmail-Type-AccessControlRule-UserIds"></a>
User IDs to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

## See Also
<a name="API_AccessControlRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/AccessControlRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/AccessControlRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/AccessControlRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
