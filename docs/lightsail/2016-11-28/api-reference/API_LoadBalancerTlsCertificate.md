---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificate.html
---

# LoadBalancerTlsCertificate
<a name="API_LoadBalancerTlsCertificate"></a>

Describes a load balancer SSL/TLS certificate.

TLS is just an updated, more secure version of Secure Socket Layer (SSL).

## Contents
<a name="API_LoadBalancerTlsCertificate_Contents"></a>

 ** arn **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-arn"></a>
The Amazon Resource Name (ARN) of the SSL/TLS certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-createdAt"></a>
The time when you created your SSL/TLS certificate.
Type: Timestamp
Required: No

 ** domainName **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-domainName"></a>
The domain name for your SSL/TLS certificate.
Type: String
Required: No

 ** domainValidationRecords **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-domainValidationRecords"></a>
An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.
Type: Array of [LoadBalancerTlsCertificateDomainValidationRecord](API_LoadBalancerTlsCertificateDomainValidationRecord.md) objects
Required: No

 ** failureReason **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-failureReason"></a>
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
Valid Values: `NO_AVAILABLE_CONTACTS | ADDITIONAL_VERIFICATION_REQUIRED | DOMAIN_NOT_ALLOWED | INVALID_PUBLIC_DOMAIN | OTHER`
Required: No

 ** isAttached **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-isAttached"></a>
When `true`, the SSL/TLS certificate is attached to the Lightsail load balancer.
Type: Boolean
Required: No

 ** issuedAt **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-issuedAt"></a>
The time when the SSL/TLS certificate was issued.
Type: Timestamp
Required: No

 ** issuer **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-issuer"></a>
The issuer of the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** keyAlgorithm **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-keyAlgorithm"></a>
The algorithm used to generate the key pair (the public and private key).
Type: String
Pattern: `.*\S.*`
Required: No

 ** loadBalancerName **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-loadBalancerName"></a>
The load balancer name where your SSL/TLS certificate is attached.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** location **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-location"></a>
The AWS Region and Availability Zone where you created your certificate.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-name"></a>
The name of the SSL/TLS certificate (`my-certificate`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** notAfter **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-notAfter"></a>
The timestamp when the SSL/TLS certificate expires.
Type: Timestamp
Required: No

 ** notBefore **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-notBefore"></a>
The timestamp when the SSL/TLS certificate is first valid.
Type: Timestamp
Required: No

 ** renewalSummary **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-renewalSummary"></a>
An object that describes the status of the certificate renewal managed by Lightsail.
Type: [LoadBalancerTlsCertificateRenewalSummary](API_LoadBalancerTlsCertificateRenewalSummary.md) object
Required: No

 ** resourceType **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-resourceType"></a>
The resource type (`LoadBalancerTlsCertificate`).
+  ** `Instance` ** - A Lightsail instance (a virtual private server)
+  ** `StaticIp` ** - A static IP address
+  ** `KeyPair` ** - The key pair used to connect to a Lightsail instance
+  ** `InstanceSnapshot` ** - A Lightsail instance snapshot
+  ** `Domain` ** - A DNS zone
+  ** `PeeredVpc` ** - A peered VPC
+  ** `LoadBalancer` ** - A Lightsail load balancer
+  ** `LoadBalancerTlsCertificate` ** - An SSL/TLS certificate associated with a Lightsail load balancer
+  ** `Disk` ** - A Lightsail block storage disk
+  ** `DiskSnapshot` ** - A block storage disk snapshot
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** revocationReason **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-revocationReason"></a>
The reason the certificate was revoked. This value is present only when the certificate status is `REVOKED`.
Type: String
Valid Values: `UNSPECIFIED | KEY_COMPROMISE | CA_COMPROMISE | AFFILIATION_CHANGED | SUPERCEDED | CESSATION_OF_OPERATION | CERTIFICATE_HOLD | REMOVE_FROM_CRL | PRIVILEGE_WITHDRAWN | A_A_COMPROMISE`
Required: No

 ** revokedAt **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-revokedAt"></a>
The timestamp when the certificate was revoked. This value is present only when the certificate status is `REVOKED`.
Type: Timestamp
Required: No

 ** serial **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-serial"></a>
The serial number of the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** signatureAlgorithm **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-signatureAlgorithm"></a>
The algorithm that was used to sign the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** status **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-status"></a>
The validation status of the SSL/TLS certificate. Valid values are below.
Type: String
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED | UNKNOWN`
Required: No

 ** subject **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-subject"></a>
The name of the entity that is associated with the public key contained in the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** subjectAlternativeNames **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-subjectAlternativeNames"></a>
An array of strings that specify the alternate domains (`example2.com`) and subdomains (`blog.example.com`) for the certificate.
Type: Array of strings
Required: No

 ** supportCode **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or SSL/TLS certificate. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-LoadBalancerTlsCertificate-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LoadBalancerTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsCertificate)
