---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html
---

# CrlConfiguration
<a name="API_CrlConfiguration"></a>

Contains configuration information for a certificate revocation list (CRL). Your private certificate authority (CA) creates base CRLs. Delta CRLs are not supported. You can enable CRLs for your new or an existing private CA by setting the **Enabled** parameter to `true`. Your private CA writes CRLs to an S3 bucket that you specify in the **S3BucketName** parameter. You can hide the name of your bucket by specifying a value for the **CustomCname** parameter. Your private CA by default copies the CNAME or the S3 bucket name to the **CRL Distribution Points** extension of each certificate it issues. If you want to configure this default behavior to be something different, you can set the **CrlDistributionPointExtensionConfiguration** parameter. Your S3 bucket policy must give write permission to AWS Private CA.

 AWS Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see [Encrypting Your CRLs](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#crl-encryption).

Your private CA uses the value in the **ExpirationInDays** parameter to calculate the **nextUpdate** field in the CRL. The CRL is refreshed prior to a certificate's expiration date or when a certificate is revoked. When a certificate is revoked, it appears in the CRL until the certificate expires, and then in one additional CRL after expiration, and it always appears in the audit report.

A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, AWS Private CA makes further attempts every 15 minutes.

CRLs contain the following fields:
+  **Version**: The current version number defined in RFC 5280 is V2. The integer value is 0x1.
+  **Signature Algorithm**: The name of the algorithm used to sign the CRL.
+  **Issuer**: The X.500 distinguished name of your private CA that issued the CRL.
+  **Last Update**: The issue date and time of this CRL.
+  **Next Update**: The day and time by which the next CRL will be issued.
+  **Revoked Certificates**: List of revoked certificates. Each list item contains the following information.
  +  **Serial Number**: The serial number, in hexadecimal format, of the revoked certificate.
  +  **Revocation Date**: Date and time the certificate was revoked.
  +  **CRL Entry Extensions**: Optional extensions for the CRL entry.
    +  **X509v3 CRL Reason Code**: Reason the certificate was revoked.
+  **CRL Extensions**: Optional extensions for the CRL.
  +  **X509v3 Authority Key Identifier**: Identifies the public key associated with the private key used to sign the certificate.
  +  **X509v3 CRL Number:**: Decimal sequence number for the CRL.
+  **Signature Algorithm**: Algorithm used by your private CA to sign the CRL.
+  **Signature Value**: Signature computed over the CRL.

Certificate revocation lists created by AWS Private CA are DER-encoded. You can use the following OpenSSL command to list a CRL.

 `openssl crl -inform DER -text -in crl_path -noout`

For more information, see [Planning a certificate revocation list (CRL)](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) in the * AWS Private Certificate Authority User Guide*

## Contents
<a name="API_CrlConfiguration_Contents"></a>

 ** Enabled **   <a name="privateca-Type-CrlConfiguration-Enabled"></a>
Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action or for an existing CA when you call the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) action.
Type: Boolean
Required: Yes

 ** CrlDistributionPointExtensionConfiguration **   <a name="privateca-Type-CrlConfiguration-CrlDistributionPointExtensionConfiguration"></a>
Configures the behavior of the CRL Distribution Point extension for certificates issued by your certificate authority. If this field is not provided, then the CRl Distribution Point Extension will be present and contain the default CRL URL.
Type: [CrlDistributionPointExtensionConfiguration](API_CrlDistributionPointExtensionConfiguration.md) object
Required: No

 ** CrlType **   <a name="privateca-Type-CrlConfiguration-CrlType"></a>
Specifies whether to create a complete or partitioned CRL. This setting determines the maximum number of certificates that the certificate authority can issue and revoke. For more information, see [AWS Private CA quotas](https://docs.aws.amazon.com/general/latest/gr/pca.html#limits_pca).
+  `COMPLETE` - The default setting. AWS Private CA maintains a single CRL ﬁle for all unexpired certiﬁcates issued by a CA that have been revoked for any reason. Each certiﬁcate that AWS Private CA issues is bound to a speciﬁc CRL through its CRL distribution point (CDP) extension, deﬁned in [ RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9).
+  `PARTITIONED` - Compared to complete CRLs, partitioned CRLs dramatically increase the number of certiﬁcates your private CA can issue.
**Important**
 When using partitioned CRLs, you must validate that the CRL's associated issuing distribution point (IDP) URI matches the certiﬁcate's CDP URI to ensure the right CRL has been fetched. AWS Private CA marks the IDP extension as critical, which your client must be able to process.
Type: String
Valid Values: `COMPLETE | PARTITIONED`
Required: No

 ** CustomCname **   <a name="privateca-Type-CrlConfiguration-CustomCname"></a>
Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you don't want the name of your S3 bucket to be public.
The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Pattern: `[-a-zA-Z0-9;/?:@&=+$,%_.!~*()']*`
Required: No

 ** CustomPath **   <a name="privateca-Type-CrlConfiguration-CustomPath"></a>
Designates a custom ﬁle path in S3 for CRL(s). For example, `http://<CustomName>/ <CustomPath>/<CrlPartition_GUID>.crl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Pattern: `[-a-zA-Z0-9;?:@&=+$,%_.!~*()']+(/[-a-zA-Z0-9;?:@&=+$,%_.!~*()']+)*`
Required: No

 ** ExpirationInDays **   <a name="privateca-Type-CrlConfiguration-ExpirationInDays"></a>
Validity period of the CRL in days.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** S3BucketName **   <a name="privateca-Type-CrlConfiguration-S3BucketName"></a>
Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) operation. You must specify a [bucket policy](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies) that allows AWS Private CA to write the CRL to your bucket.
The `S3BucketName` parameter must conform to the [S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[-a-zA-Z0-9._/]+`
Required: No

 ** S3ObjectAcl **   <a name="privateca-Type-CrlConfiguration-S3ObjectAcl"></a>
Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket. If you choose PUBLIC\_READ, the CRL will be accessible over the public internet. If you choose BUCKET\_OWNER\_FULL\_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access.
If no value is specified, the default is `PUBLIC_READ`.
 *Note:* This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as `BUCKET_OWNER_FULL_CONTROL`, and not doing so results in an error. If you have disabled BPA in S3, then you can specify either `BUCKET_OWNER_FULL_CONTROL` or `PUBLIC_READ` as the value.
For more information, see [Blocking public access to the S3 bucket](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-bpa).
Type: String
Valid Values: `PUBLIC_READ | BUCKET_OWNER_FULL_CONTROL`
Required: No

## See Also
<a name="API_CrlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CrlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CrlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CrlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
