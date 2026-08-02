---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DkimAttributes.html
---

# DkimAttributes
<a name="API_DkimAttributes"></a>

An object that contains information about the DKIM configuration for an email identity.

## Contents
<a name="API_DkimAttributes_Contents"></a>

 ** SigningEnabled **   <a name="pinpoint-Type-DkimAttributes-SigningEnabled"></a>
If the value is `true`, then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is `false`, then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.
Type: Boolean
Required: No

 ** Status **   <a name="pinpoint-Type-DkimAttributes-Status"></a>
Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:
+  `PENDING` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them.
+  `SUCCESS` – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email from the identity.
+  `FAILED` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won't continue to search for them.
+  `TEMPORARY_FAILURE` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain.
+  `NOT_STARTED` – Amazon Pinpoint hasn't yet started searching for the DKIM records in the DKIM records for the domain.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE | NOT_STARTED`
Required: No

 ** Tokens **   <a name="pinpoint-Type-DkimAttributes-Tokens"></a>
A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.
Type: Array of strings
Required: No

## See Also
<a name="API_DkimAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DkimAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DkimAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DkimAttributes)
