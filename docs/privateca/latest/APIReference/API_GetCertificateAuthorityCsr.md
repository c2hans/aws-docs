---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html
---

# GetCertificateAuthorityCsr
<a name="API_GetCertificateAuthorityCsr"></a>

Retrieves the certificate signing request (CSR) for your private certificate authority (CA). The CSR is created when you call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action. Sign the CSR with your AWS Private CA-hosted or on-premises root or subordinate CA. Then import the signed certificate back into AWS Private CA by calling the [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html) action. The CSR is returned as a base64 PEM-encoded string.

## Request Syntax
<a name="API_GetCertificateAuthorityCsr_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCertificateAuthorityCsr_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_GetCertificateAuthorityCsr_RequestSyntax) **   <a name="privateca-GetCertificateAuthorityCsr-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_GetCertificateAuthorityCsr_ResponseSyntax"></a>

```
{
   "Csr": "string"
}
```

## Response Elements
<a name="API_GetCertificateAuthorityCsr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Csr](#API_GetCertificateAuthorityCsr_ResponseSyntax) **   <a name="privateca-GetCertificateAuthorityCsr-response-Csr"></a>
The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
Type: String

## Errors
<a name="API_GetCertificateAuthorityCsr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
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
<a name="API_GetCertificateAuthorityCsr_Examples"></a>

### Example
<a name="API_GetCertificateAuthorityCsr_Example_1"></a>

This example illustrates one usage of GetCertificateAuthorityCsr.

#### Sample Request
<a name="API_GetCertificateAuthorityCsr_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 128
X-Amz-Target: ACMPrivateCA.GetCertificateAuthorityCsr
X-Amz-Date: 20180226T175413Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=aa5f823a8637e4709fd4b06988934f4ed4f38f2541889a2f6894f09d75f8b071

{"CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"}
```

### Example
<a name="API_GetCertificateAuthorityCsr_Example_2"></a>

This example illustrates one usage of GetCertificateAuthorityCsr.

#### Sample Response
<a name="API_GetCertificateAuthorityCsr_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 17:50:52 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1098
x-amzn-RequestId: f96921bf-8b07-4e2a-876a-f76946e666d2
Connection: keep-alive

{
  "Csr": "-----BEGIN CERTIFICATE REQUEST----- base64-encoded CSR -----END CERTIFICATE REQUEST-----"
}
```

## See Also
<a name="API_GetCertificateAuthorityCsr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/GetCertificateAuthorityCsr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/GetCertificateAuthorityCsr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
