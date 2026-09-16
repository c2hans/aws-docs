---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html
---

# ImportCertificateAuthorityCertificate
<a name="API_ImportCertificateAuthorityCertificate"></a>

Imports a signed private CA certificate into AWS Private CA. This action is used when you are using a chain of trust whose root is located outside AWS Private CA. Before you can call this action, the following preparations must in place:

1. In AWS Private CA, call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action to create the private CA that you plan to back with the imported certificate.

1. Call the [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html) action to generate a certificate signing request (CSR).

1. Sign the CSR using a root or intermediate CA hosted by either an on-premises PKI hierarchy or by a commercial CA.

1. Create a certificate chain and copy the signed certificate and the certificate chain to your working directory.

 AWS Private CA supports three scenarios for installing a CA certificate:
+ Installing a certificate for a root CA hosted by AWS Private CA.
+ Installing a subordinate CA certificate whose parent authority is hosted by AWS Private CA.
+ Installing a subordinate CA certificate whose parent authority is externally hosted.

The following additional requirements apply when you import a CA certificate.
+ Only a self-signed certificate can be imported as a root CA.
+ A self-signed certificate cannot be imported as a subordinate CA.
+ Your certificate chain must not include the private CA certificate that you are importing.
+ Your root CA must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built.
+ The chain must be PEM-encoded.
+ The maximum allowed size of a certificate is 32 KB.
+ The maximum allowed size of a certificate chain is 2 MB.

 *Enforcement of Critical Constraints*

 AWS Private CA allows the following extensions to be marked critical in the imported CA certificate or chain.
+ Authority key identifier
+ Basic constraints (*must* be marked critical)
+ Certificate policies
+ Extended key usage
+ Inhibit anyPolicy
+ Issuer alternative name
+ Key usage
+ Name constraints
+ Policy mappings
+ Subject alternative name
+ Subject directory attributes
+ Subject key identifier
+ Subject information access

 AWS Private CA rejects the following extensions when they are marked critical in an imported CA certificate or chain.
+ Authority information access
+ CRL distribution points
+ Freshest CRL
+ Policy constraints

 AWS Private Certificate Authority will also reject any other extension marked as critical not contained on the preceding list of allowed extensions.

## Request Syntax
<a name="API_ImportCertificateAuthorityCertificate_RequestSyntax"></a>

```
{
   "Certificate": {{blob}},
   "CertificateAuthorityArn": "{{string}}",
   "CertificateChain": {{blob}}
}
```

## Request Parameters
<a name="API_ImportCertificateAuthorityCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Certificate](#API_ImportCertificateAuthorityCertificate_RequestSyntax) **   <a name="privateca-ImportCertificateAuthorityCertificate-request-Certificate"></a>
The PEM-encoded certificate for a private CA. This may be a self-signed certificate in the case of a root CA, or it may be signed by another CA that you control.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: Yes

 ** [CertificateAuthorityArn](#API_ImportCertificateAuthorityCertificate_RequestSyntax) **   <a name="privateca-ImportCertificateAuthorityCertificate-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [CertificateChain](#API_ImportCertificateAuthorityCertificate_RequestSyntax) **   <a name="privateca-ImportCertificateAuthorityCertificate-request-CertificateChain"></a>
A PEM-encoded file that contains all of your certificates, other than the certificate you're importing, chaining up to your root CA. Your AWS Private CA-hosted or on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding.
This parameter must be supplied when you import a subordinate CA. When you import a root CA, there is no chain.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 2097152.
Required: No

## Response Elements
<a name="API_ImportCertificateAuthorityCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ImportCertificateAuthorityCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateMismatchException **
The certificate authority certificate you are importing does not comply with conditions specified in the certificate that signed it.
HTTP Status Code: 400

 ** ConcurrentModificationException **
A previous update to your private CA is still ongoing.
HTTP Status Code: 400

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidRequestException **
The request action cannot be performed or is prohibited.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** MalformedCertificateException **
One or more fields in the certificate are invalid.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** RequestInProgressException **
Your request is already in progress.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_ImportCertificateAuthorityCertificate_Examples"></a>

### Example
<a name="API_ImportCertificateAuthorityCertificate_Example_1"></a>

This example illustrates one usage of ImportCertificateAuthorityCertificate.

#### Sample Request
<a name="API_ImportCertificateAuthorityCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 3375
X-Amz-Target: ACMPrivateCA.ImportCertificateAuthorityCertificate
X-Amz-Date: 20180226T203302Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=cdf100cc3972f9df2e0f94295a6e378fbac8c1f489363689805504450e605d83

{
	"CertificateChain": "base64-encoded certificate chain",
	"Certificate": "base64-encoded certificate",
	"CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_ImportCertificateAuthorityCertificate_Example_2"></a>

This example illustrates one usage of ImportCertificateAuthorityCertificate.

#### Sample Response
<a name="API_ImportCertificateAuthorityCertificate_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_ImportCertificateAuthorityCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)
