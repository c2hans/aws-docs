---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_MailFromAttributes.html
---

# MailFromAttributes
<a name="API_MailFromAttributes"></a>

A list of attributes that are associated with a MAIL FROM domain.

## Contents
<a name="API_MailFromAttributes_Contents"></a>

 ** BehaviorOnMxFailure **   <a name="pinpoint-Type-MailFromAttributes-BehaviorOnMxFailure"></a>
The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to `UseDefaultValue`, Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to `RejectMessage`, Amazon Pinpoint returns a `MailFromDomainNotVerified` error, and doesn't attempt to deliver the email.
These behaviors are taken when the custom MAIL FROM domain configuration is in the `Pending`, `Failed`, and `TemporaryFailure` states.
Type: String
Valid Values: `USE_DEFAULT_VALUE | REJECT_MESSAGE`
Required: Yes

 ** MailFromDomain **   <a name="pinpoint-Type-MailFromAttributes-MailFromDomain"></a>
The name of a domain that an email identity uses as a custom MAIL FROM domain.
Type: String
Required: Yes

 ** MailFromDomainStatus **   <a name="pinpoint-Type-MailFromAttributes-MailFromDomainStatus"></a>
The status of the MAIL FROM domain. This status can have the following values:
+  `PENDING` – Amazon Pinpoint hasn't started searching for the MX record yet.
+  `SUCCESS` – Amazon Pinpoint detected the required MX record for the MAIL FROM domain.
+  `FAILED` – Amazon Pinpoint can't find the required MX record, or the record no longer exists.
+  `TEMPORARY_FAILURE` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE`
Required: Yes

## See Also
<a name="API_MailFromAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/MailFromAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/MailFromAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/MailFromAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
