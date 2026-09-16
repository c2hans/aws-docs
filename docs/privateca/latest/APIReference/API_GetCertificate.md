---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html
---

# GetCertificate
<a name="API_GetCertificate"></a>

Retrieves a certificate from your private CA or one that has been shared with you. The ARN of the certificate is returned when you call the [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) action. You must specify both the ARN of your private CA and the ARN of the issued certificate when calling the **GetCertificate** action. You can retrieve the certificate if it is in the **ISSUED**, **EXPIRED**, or **REVOKED** state. You can call the [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html) action to create a report that contains information about all of the certificates issued and revoked by your private CA.

## Request Syntax
<a name="API_GetCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateArn](#API_GetCertificate_RequestSyntax) **   <a name="privateca-GetCertificate-request-CertificateArn"></a>
The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/286535153982981100925020015808220737245 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [CertificateAuthorityArn](#API_GetCertificate_RequestSyntax) **   <a name="privateca-GetCertificate-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_GetCertificate_ResponseSyntax"></a>

```
{
   "Certificate": "string",
   "CertificateChain": "string"
}
```

## Response Elements
<a name="API_GetCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_GetCertificate_ResponseSyntax) **   <a name="privateca-GetCertificate-response-Certificate"></a>
The base64 PEM-encoded certificate specified by the `CertificateArn` parameter.
Type: String

 ** [CertificateChain](#API_GetCertificate_ResponseSyntax) **   <a name="privateca-GetCertificate-response-CertificateChain"></a>
The base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate.
Type: String

## Errors
<a name="API_GetCertificate_Errors"></a>

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
<a name="API_GetCertificate_Examples"></a>

### Example
<a name="API_GetCertificate_Example_1"></a>

This example illustrates one usage of GetCertificate.

#### Sample Request
<a name="API_GetCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 292
X-Amz-Target: ACMPrivateCA.GetCertificate
X-Amz-Date: 20180226T194913Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=4fe34fdad8c09d5b608be6f5d4f4939444dd7cdd542ec09b1002182e4ef9fcee

{
  "CertificateArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/e8cbd2bedb122329f97706bcfec990f8",
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_GetCertificate_Example_2"></a>

This example illustrates one usage of GetCertificate.

#### Sample Response
<a name="API_GetCertificate_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 17:35:47 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 4184
x-amzn-RequestId: 9f537e0a-993c-4a03-8aec-0fc52c772b84
Connection: keep-alive

{
  "Certificate": "-----BEGIN CERTIFICATE----- base64-encoded certificate -----END CERTIFICATE-----",
  "CertificateChain": "-----BEGIN CERTIFICATE----- base64-encoded certificate -----END CERTIFICATE-----"
}
```

## See Also
<a name="API_GetCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/GetCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/GetCertificate)
