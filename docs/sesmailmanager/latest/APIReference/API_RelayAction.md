---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RelayAction.html
---

# RelayAction
<a name="API_RelayAction"></a>

The action relays the email via SMTP to another specific SMTP server.

## Contents
<a name="API_RelayAction_Contents"></a>

 ** Relay **   <a name="sesmailmanager-Type-RelayAction-Relay"></a>
The identifier of the relay resource to be used when relaying an email.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-RelayAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified relay has been deleted.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

 ** MailFrom **   <a name="sesmailmanager-Type-RelayAction-MailFrom"></a>
This action specifies whether to preserve or replace original mail from address while relaying received emails to a destination server.
Type: String
Valid Values: `REPLACE | PRESERVE`
Required: No

## See Also
<a name="API_RelayAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RelayAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RelayAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RelayAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
