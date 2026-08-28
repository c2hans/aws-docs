---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IdentityInfo.html
---

# IdentityInfo
<a name="API_IdentityInfo"></a>

Information about an email identity.

## Contents
<a name="API_IdentityInfo_Contents"></a>

 ** IdentityName **   <a name="pinpoint-Type-IdentityInfo-IdentityName"></a>
The address or domain of the identity.
Type: String
Required: No

 ** IdentityType **   <a name="pinpoint-Type-IdentityInfo-IdentityType"></a>
The email identity type. The identity type can be one of the following:
+  `EMAIL_ADDRESS` – The identity is an email address.
+  `DOMAIN` – The identity is a domain.
+  `MANAGED_DOMAIN` – The identity is a domain that is managed by AWS.
Type: String
Valid Values: `EMAIL_ADDRESS | DOMAIN | MANAGED_DOMAIN`
Required: No

 ** SendingEnabled **   <a name="pinpoint-Type-IdentityInfo-SendingEnabled"></a>
Indicates whether or not you can send email from the identity.
In Amazon Pinpoint, an identity is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon Pinpoint to send email from that identity.
Type: Boolean
Required: No

## See Also
<a name="API_IdentityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/IdentityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/IdentityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/IdentityInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
