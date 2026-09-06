---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CertificateValidity.html
---

# CertificateValidity
<a name="API_CertificateValidity"></a>

Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

## Contents
<a name="API_CertificateValidity_Contents"></a>

 ** RenewalPeriod **   <a name="PcaConnectorAd-Type-CertificateValidity-RenewalPeriod"></a>
Renewal period is the period of time before certificate expiration when a new certificate will be requested.
Type: [ValidityPeriod](API_ValidityPeriod.md) object
Required: Yes

 ** ValidityPeriod **   <a name="PcaConnectorAd-Type-CertificateValidity-ValidityPeriod"></a>
Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.
Type: [ValidityPeriod](API_ValidityPeriod.md) object
Required: Yes

## See Also
<a name="API_CertificateValidity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/CertificateValidity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/CertificateValidity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/CertificateValidity)
