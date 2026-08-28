---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AdminAccountSummary.html
---

# AdminAccountSummary
<a name="API_AdminAccountSummary"></a>

Contains high level information about the Firewall Manager administrator account.

## Contents
<a name="API_AdminAccountSummary_Contents"></a>

 ** AdminAccount **   <a name="fms-Type-AdminAccountSummary-AdminAccount"></a>
The AWS account ID of the Firewall Manager administrator's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** DefaultAdmin **   <a name="fms-Type-AdminAccountSummary-DefaultAdmin"></a>
A boolean value that indicates if the administrator is the default administrator. If true, then this is the default administrator account. The default administrator can manage third-party firewalls and has full administrative scope. There is only one default administrator account per organization. For information about Firewall Manager default administrator accounts, see [Managing Firewall Manager administrators](https://docs.aws.amazon.com/waf/latest/developerguide/fms-administrators.html) in the *Firewall Manager Developer Guide*.
Type: Boolean
Required: No

 ** Status **   <a name="fms-Type-AdminAccountSummary-Status"></a>
The current status of the request to onboard a member account as an Firewall Manager administrator.
+  `ONBOARDING` - The account is onboarding to Firewall Manager as an administrator.
+  `ONBOARDING_COMPLETE` - Firewall Manager The account is onboarded to Firewall Manager as an administrator, and can perform actions on the resources defined in their [AdminScope](API_AdminScope.md).
+  `OFFBOARDING` - The account is being removed as an Firewall Manager administrator.
+  `OFFBOARDING_COMPLETE` - The account has been removed as an Firewall Manager administrator.
Type: String
Valid Values: `ONBOARDING | ONBOARDING_COMPLETE | OFFBOARDING | OFFBOARDING_COMPLETE`
Required: No

## See Also
<a name="API_AdminAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AdminAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AdminAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AdminAccountSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
