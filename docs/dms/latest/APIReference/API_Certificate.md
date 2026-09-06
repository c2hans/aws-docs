---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

The SSL certificate that can be used to encrypt connections between the endpoints and the replication instance.

## Contents
<a name="API_Certificate_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-Certificate-CertificateArn"></a>
The Amazon Resource Name (ARN) for the certificate.
Type: String
Required: No

 ** CertificateCreationDate **   <a name="DMS-Type-Certificate-CertificateCreationDate"></a>
The date that the certificate was created.
Type: Timestamp
Required: No

 ** CertificateIdentifier **   <a name="DMS-Type-Certificate-CertificateIdentifier"></a>
A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** CertificateOwner **   <a name="DMS-Type-Certificate-CertificateOwner"></a>
The owner of the certificate.
Type: String
Required: No

 ** CertificatePem **   <a name="DMS-Type-Certificate-CertificatePem"></a>
The contents of a `.pem` file, which contains an X.509 certificate.
Type: String
Required: No

 ** CertificateWallet **   <a name="DMS-Type-Certificate-CertificateWallet"></a>
The location of an imported Oracle Wallet certificate for use with SSL. Example: `filebase64("${path.root}/rds-ca-2019-root.sso")`
Type: Base64-encoded binary data object
Required: No

 ** KeyLength **   <a name="DMS-Type-Certificate-KeyLength"></a>
The key length of the cryptographic algorithm being used.
Type: Integer
Required: No

 ** KmsKeyId **   <a name="DMS-Type-Certificate-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the certificate.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** SigningAlgorithm **   <a name="DMS-Type-Certificate-SigningAlgorithm"></a>
The signing algorithm for the certificate.
Type: String
Required: No

 ** ValidFromDate **   <a name="DMS-Type-Certificate-ValidFromDate"></a>
The beginning date that the certificate is valid.
Type: Timestamp
Required: No

 ** ValidToDate **   <a name="DMS-Type-Certificate-ValidToDate"></a>
The final date that the certificate is valid.
Type: Timestamp
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Certificate)
