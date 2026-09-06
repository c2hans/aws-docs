---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthorityConfiguration.html
---

# CertificateAuthorityConfiguration
<a name="API_CertificateAuthorityConfiguration"></a>

Contains configuration information for your private certificate authority (CA). This includes information about the class of public key algorithm and the key pair that your private CA creates when it issues a certificate. It also includes the signature algorithm that it uses when issuing certificates, and its X.500 distinguished name. You must specify this information when you call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action.

## Contents
<a name="API_CertificateAuthorityConfiguration_Contents"></a>

 ** KeyAlgorithm **   <a name="privateca-Type-CertificateAuthorityConfiguration-KeyAlgorithm"></a>
Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87 | SM2`
Required: Yes

 ** SigningAlgorithm **   <a name="privateca-Type-CertificateAuthorityConfiguration-SigningAlgorithm"></a>
Name of the algorithm your private CA uses to sign certificate requests.
This parameter should not be confused with the `SigningAlgorithm` parameter of the `IssueCertificate` API action, which is used to sign certificates when they are issued.
Type: String
Valid Values: `SHA256WITHECDSA | SHA384WITHECDSA | SHA512WITHECDSA | SHA256WITHRSA | SHA384WITHRSA | SHA512WITHRSA | SM3WITHSM2 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87`
Required: Yes

 ** Subject **   <a name="privateca-Type-CertificateAuthorityConfiguration-Subject"></a>
Structure that contains X.500 distinguished name information for your private CA.
Type: [ASN1Subject](API_ASN1Subject.md) object
Required: Yes

 ** CsrExtensions **   <a name="privateca-Type-CertificateAuthorityConfiguration-CsrExtensions"></a>
Specifies information to be added to the extension section of the certificate signing request (CSR).
Type: [CsrExtensions](API_CsrExtensions.md) object
Required: No

## See Also
<a name="API_CertificateAuthorityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CertificateAuthorityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CertificateAuthorityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CertificateAuthorityConfiguration)
