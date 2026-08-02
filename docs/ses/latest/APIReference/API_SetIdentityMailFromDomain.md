---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html
---

# SetIdentityMailFromDomain
<a name="API_SetIdentityMailFromDomain"></a>

Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).

**Important**
To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain's DNS settings. To ensure that your emails pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_SetIdentityMailFromDomain_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BehaviorOnMXFailure **
The action for Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose `UseDefaultValue`, Amazon SES uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose `RejectMessage`, Amazon SES returns a `MailFromDomainNotVerified` error and not send the email.
The action specified in `BehaviorOnMXFailure` is taken when the custom MAIL FROM domain setup is in the `Pending`, `Failed`, and `TemporaryFailure` states.
Type: String
Valid Values: `UseDefaultValue | RejectMessage`
Required: No

 ** Identity **
The verified identity.
Type: String
Required: Yes

 ** MailFromDomain **
The custom MAIL FROM domain for the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a "From" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html)), and 3) not be used to receive emails. A value of `null` disables the custom MAIL FROM setting for the identity.
Type: String
Required: No

## Errors
<a name="API_SetIdentityMailFromDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_SetIdentityMailFromDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SetIdentityMailFromDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SetIdentityMailFromDomain)
