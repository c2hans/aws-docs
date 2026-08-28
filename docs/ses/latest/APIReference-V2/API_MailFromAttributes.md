---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MailFromAttributes.html
---

# MailFromAttributes
<a name="API_MailFromAttributes"></a>

A list of attributes that are associated with a MAIL FROM domain.

## Contents
<a name="API_MailFromAttributes_Contents"></a>

 ** BehaviorOnMxFailure **   <a name="SES-Type-MailFromAttributes-BehaviorOnMxFailure"></a>
The action to take if the required MX record can't be found when you send an email. When you set this value to `USE_DEFAULT_VALUE`, the mail is sent using *amazonses.com* as the MAIL FROM domain. When you set this value to `REJECT_MESSAGE`, the Amazon SES API v2 returns a `MailFromDomainNotVerified` error, and doesn't attempt to deliver the email.
These behaviors are taken when the custom MAIL FROM domain configuration is in the `Pending`, `Failed`, and `TemporaryFailure` states.
Type: String
Valid Values: `USE_DEFAULT_VALUE | REJECT_MESSAGE`
Required: Yes

 ** MailFromDomain **   <a name="SES-Type-MailFromAttributes-MailFromDomain"></a>
The name of a domain that an email identity uses as a custom MAIL FROM domain.
Type: String
Required: Yes

 ** MailFromDomainStatus **   <a name="SES-Type-MailFromAttributes-MailFromDomainStatus"></a>
The status of the MAIL FROM domain. This status can have the following values:
+  `PENDING` – Amazon SES hasn't started searching for the MX record yet.
+  `SUCCESS` – Amazon SES detected the required MX record for the MAIL FROM domain.
+  `FAILED` – Amazon SES can't find the required MX record, or the record no longer exists.
+  `TEMPORARY_FAILURE` – A temporary issue occurred, which prevented Amazon SES from determining the status of the MAIL FROM domain.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE`
Required: Yes

## See Also
<a name="API_MailFromAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MailFromAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MailFromAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MailFromAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
