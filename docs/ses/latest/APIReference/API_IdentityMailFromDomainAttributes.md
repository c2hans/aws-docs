---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityMailFromDomainAttributes.html
---

# IdentityMailFromDomainAttributes
<a name="API_IdentityMailFromDomainAttributes"></a>

Represents the custom MAIL FROM domain attributes of a verified identity (email address or domain).

## Contents
<a name="API_IdentityMailFromDomainAttributes_Contents"></a>

 ** BehaviorOnMXFailure **
The action that Amazon SES takes if it cannot successfully read the required MX record when you send an email. A value of `UseDefaultValue` indicates that if Amazon SES cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. A value of `RejectMessage` indicates that if Amazon SES cannot read the required MX record, Amazon SES returns a `MailFromDomainNotVerified` error and does not send the email.
The custom MAIL FROM setup states that result in this behavior are `Pending`, `Failed`, and `TemporaryFailure`.
Type: String
Valid Values: `UseDefaultValue | RejectMessage`
Required: Yes

 ** MailFromDomain **
The custom MAIL FROM domain that the identity is configured to use.
Type: String
Required: Yes

 ** MailFromDomainStatus **
The state that indicates whether Amazon SES has successfully read the MX record required for custom MAIL FROM domain setup. If the state is `Success`, Amazon SES uses the specified custom MAIL FROM domain when the verified identity sends an email. All other states indicate that Amazon SES takes the action described by `BehaviorOnMXFailure`.
Type: String
Valid Values: `Pending | Success | Failed | TemporaryFailure`
Required: Yes

## See Also
<a name="API_IdentityMailFromDomainAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/IdentityMailFromDomainAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/IdentityMailFromDomainAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/IdentityMailFromDomainAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
