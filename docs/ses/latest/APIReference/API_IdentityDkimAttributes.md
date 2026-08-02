---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityDkimAttributes.html
---

# IdentityDkimAttributes
<a name="API_IdentityDkimAttributes"></a>

Represents the DKIM attributes of a verified email address or a domain.

## Contents
<a name="API_IdentityDkimAttributes_Contents"></a>

 ** DkimEnabled **
Is true if DKIM signing is enabled for email sent from the identity. It's false otherwise. The default value is true.
Type: Boolean
Required: Yes

 ** DkimVerificationStatus **
Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens) published in the domain name's DNS. (This only applies to domain identities, not email address identities.)
Type: String
Valid Values: `Pending | Success | Failed | TemporaryFailure | NotStarted`
Required: Yes

 ** DkimTokens.member.N **
A set of character strings that represent the domain's identity. Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that are hosted by Amazon SES. Amazon Web Services eventually detects that you've updated your DNS records. This detection process might take up to 72 hours. After successful detection, Amazon SES is able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)
For more information about creating DNS records using DKIM tokens, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html).
Type: Array of strings
Required: No

## See Also
<a name="API_IdentityDkimAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/IdentityDkimAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/IdentityDkimAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/IdentityDkimAttributes)
