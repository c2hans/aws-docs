---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

Describes the full details of an Amazon Lightsail SSL/TLS certificate.

**Note**
To get a summary of a certificate, use the `GetCertificates` action and omit `includeCertificateDetails` from your request. The response will include only the certificate Amazon Resource Name (ARN), certificate name, domain name, and tags.

## Contents
<a name="API_Certificate_Contents"></a>

 ** arn **   <a name="Lightsail-Type-Certificate-arn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-Certificate-createdAt"></a>
The timestamp when the certificate was created.
Type: Timestamp
Required: No

 ** domainName **   <a name="Lightsail-Type-Certificate-domainName"></a>
The domain name of the certificate.
Type: String
Required: No

 ** domainValidationRecords **   <a name="Lightsail-Type-Certificate-domainValidationRecords"></a>
An array of objects that describe the domain validation records of the certificate.
Type: Array of [DomainValidationRecord](API_DomainValidationRecord.md) objects
Required: No

 ** eligibleToRenew **   <a name="Lightsail-Type-Certificate-eligibleToRenew"></a>
The renewal eligibility of the certificate.
Type: String
Required: No

 ** inUseResourceCount **   <a name="Lightsail-Type-Certificate-inUseResourceCount"></a>
The number of Lightsail resources that the certificate is attached to.
Type: Integer
Required: No

 ** issuedAt **   <a name="Lightsail-Type-Certificate-issuedAt"></a>
The timestamp when the certificate was issued.
Type: Timestamp
Required: No

 ** issuerCA **   <a name="Lightsail-Type-Certificate-issuerCA"></a>
The certificate authority that issued the certificate.
Type: String
Required: No

 ** keyAlgorithm **   <a name="Lightsail-Type-Certificate-keyAlgorithm"></a>
The algorithm used to generate the key pair (the public and private key) of the certificate.
Type: String
Required: No

 ** name **   <a name="Lightsail-Type-Certificate-name"></a>
The name of the certificate (`my-certificate`).
Type: String
Required: No

 ** notAfter **   <a name="Lightsail-Type-Certificate-notAfter"></a>
The timestamp when the certificate expires.
Type: Timestamp
Required: No

 ** notBefore **   <a name="Lightsail-Type-Certificate-notBefore"></a>
The timestamp when the certificate is first valid.
Type: Timestamp
Required: No

 ** renewalSummary **   <a name="Lightsail-Type-Certificate-renewalSummary"></a>
An object that describes the status of the certificate renewal managed by Lightsail.
Type: [RenewalSummary](API_RenewalSummary.md) object
Required: No

 ** requestFailureReason **   <a name="Lightsail-Type-Certificate-requestFailureReason"></a>
The validation failure reason, if any, of the certificate.
The following failure reasons are possible:
+  ** `NO_AVAILABLE_CONTACTS` ** - This failure applies to email validation, which is not available for Lightsail certificates.
+  ** `ADDITIONAL_VERIFICATION_REQUIRED` ** - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the [AWS Support Center](https://console.aws.amazon.com/support/home) to contact AWS Support.
**Note**
You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.
+  ** `DOMAIN_NOT_ALLOWED` ** - One or more of the domain names in the certificate request was reported as an unsafe domain by [VirusTotal](https://www.virustotal.com/gui/home/url). To correct the problem, search for your domain name on the [VirusTotal](https://www.virustotal.com/gui/home/url) website. If your domain is reported as suspicious, see [Google Help for Hacked Websites](https://developers.google.com/web/fundamentals/security/hacked) to learn what you can do.

  If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate.

  If you see this error and your domain is not included in the VirusTotal list, visit the [AWS Support Center](https://console.aws.amazon.com/support/home) and create a case.
+  ** `INVALID_PUBLIC_DOMAIN` ** - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for `example.invalidpublicdomain` because `invalidpublicdomain` is not a valid top-level domain.
+  ** `OTHER` ** - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request.
Type: String
Required: No

 ** revocationReason **   <a name="Lightsail-Type-Certificate-revocationReason"></a>
The reason the certificate was revoked. This value is present only when the certificate status is `REVOKED`.
Type: String
Required: No

 ** revokedAt **   <a name="Lightsail-Type-Certificate-revokedAt"></a>
The timestamp when the certificate was revoked. This value is present only when the certificate status is `REVOKED`.
Type: Timestamp
Required: No

 ** serialNumber **   <a name="Lightsail-Type-Certificate-serialNumber"></a>
The serial number of the certificate.
Type: String
Required: No

 ** status **   <a name="Lightsail-Type-Certificate-status"></a>
The validation status of the certificate.
Type: String
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`
Required: No

 ** subjectAlternativeNames **   <a name="Lightsail-Type-Certificate-subjectAlternativeNames"></a>
An array of strings that specify the alternate domains (`example2.com`) and subdomains (`blog.example.com`) of the certificate.
Type: Array of strings
Required: No

 ** supportCode **   <a name="Lightsail-Type-Certificate-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail certificate. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Certificate-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Certificate)
