---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html
---

# GetCertificateAuthorityCertificate
<a name="API_GetCertificateAuthorityCertificate"></a>

Retrieves the certificate and certificate chain for your private certificate authority (CA) or one that has been shared with you. Both the certificate and the chain are base64 PEM-encoded. The chain does not include the CA certificate. Each certificate in the chain signs the one before it.

## Request Syntax
<a name="API_GetCertificateAuthorityCertificate_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCertificateAuthorityCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_GetCertificateAuthorityCertificate_RequestSyntax) **   <a name="privateca-GetCertificateAuthorityCertificate-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of your private CA. This is of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_GetCertificateAuthorityCertificate_ResponseSyntax"></a>

```
{
   "Certificate": "string",
   "CertificateChain": "string"
}
```

## Response Elements
<a name="API_GetCertificateAuthorityCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_GetCertificateAuthorityCertificate_ResponseSyntax) **   <a name="privateca-GetCertificateAuthorityCertificate-response-Certificate"></a>
Base64-encoded certificate authority (CA) certificate.
Type: String

 ** [CertificateChain](#API_GetCertificateAuthorityCertificate_ResponseSyntax) **   <a name="privateca-GetCertificateAuthorityCertificate-response-CertificateChain"></a>
Base64-encoded certificate chain that includes any intermediate certificates and chains up to root certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. If this is a root CA, the value will be null.
Type: String

## Errors
<a name="API_GetCertificateAuthorityCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_GetCertificateAuthorityCertificate_Examples"></a>

### Example
<a name="API_GetCertificateAuthorityCertificate_Example_1"></a>

This example illustrates one usage of GetCertificateAuthorityCertificate.

#### Sample Request
<a name="API_GetCertificateAuthorityCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 128
X-Amz-Target: ACMPrivateCA.GetCertificateAuthorityCertificate
X-Amz-Date: 20180226T174831Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=2675f0e4055c234f5b6e155bd3245ca327382d47a16e0c20f2abc802e1f0eab6

{"CertificateAuthorityArn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012"}
```

### Example
<a name="API_GetCertificateAuthorityCertificate_Example_2"></a>

This example illustrates one usage of GetCertificateAuthorityCertificate.

#### Sample Response
<a name="API_GetCertificateAuthorityCertificate_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 17:43:38 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2552
x-amzn-RequestId: 8c607f26-6d9e-4972-a529-02cc5608c81a
Connection: keep-alive

{
  "Certificate": "-----BEGIN CERTIFICATE-----  base64-encoded certificate  -----END CERTIFICATE-----",
  "CertificateChain": "-----BEGIN CERTIFICATE-----  base64-encoded certificate chain  -----END CERTIFICATE-----"
}
```

## See Also
<a name="API_GetCertificateAuthorityCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/GetCertificateAuthorityCertificate)
