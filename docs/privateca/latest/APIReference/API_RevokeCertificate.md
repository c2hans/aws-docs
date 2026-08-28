---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html
---

# RevokeCertificate
<a name="API_RevokeCertificate"></a>

Revokes a certificate that was issued inside AWS Private CA. If you enable a certificate revocation list (CRL) when you create or update your private CA, information about the revoked certificates will be included in the CRL. AWS Private CA writes the CRL to an S3 bucket that you specify. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason the CRL update fails, AWS Private CA attempts makes further attempts every 15 minutes. With Amazon CloudWatch, you can create alarms for the metrics `CRLGenerated` and `MisconfiguredCRLBucket`. For more information, see [Supported CloudWatch Metrics](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCloudWatch.html).

**Note**
Both AWS Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see [Access policies for CRLs in Amazon S3](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies).

 AWS Private CA also writes revocation information to the audit report. For more information, see [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html).

**Note**
You cannot revoke a root CA self-signed certificate.

## Request Syntax
<a name="API_RevokeCertificate_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "CertificateSerial": "{{string}}",
   "RevocationReason": "{{string}}"
}
```

## Request Parameters
<a name="API_RevokeCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_RevokeCertificate_RequestSyntax) **   <a name="privateca-RevokeCertificate-request-CertificateAuthorityArn"></a>
Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [CertificateSerial](#API_RevokeCertificate_RequestSyntax) **   <a name="privateca-RevokeCertificate-request-CertificateSerial"></a>
Serial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The **GetCertificate** action retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number.
 `openssl x509 -in file_path -text -noout`
You can also copy the serial number from the console or use the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) action in the * AWS Certificate Manager API Reference*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** [RevocationReason](#API_RevokeCertificate_RequestSyntax) **   <a name="privateca-RevokeCertificate-request-RevocationReason"></a>
Specifies why you revoked the certificate.
Type: String
Valid Values: `UNSPECIFIED | KEY_COMPROMISE | CERTIFICATE_AUTHORITY_COMPROMISE | AFFILIATION_CHANGED | SUPERSEDED | CESSATION_OF_OPERATION | PRIVILEGE_WITHDRAWN | A_A_COMPROMISE`
Required: Yes

## Response Elements
<a name="API_RevokeCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** LimitExceededException **
An AWS Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.
HTTP Status Code: 400

 ** RequestAlreadyProcessedException **
Your request has already been completed.
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
<a name="API_RevokeCertificate_Examples"></a>

### Example
<a name="API_RevokeCertificate_Example_1"></a>

This example illustrates one usage of RevokeCertificate.

#### Sample Request
<a name="API_RevokeCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 238
X-Amz-Target: ACMPrivateCA.RevokeCertificate
X-Amz-Date: 20180226T200035Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=ab19c4301eb2e8e9f188f3d478cb1d5a28bfb41de3d54b5006c0738d411cfd86

{
  "CertificateSerial": "e8:cb:d2:be:db:12:23:29:f9:77:06:bc:fe:c9:90:f8",
  "RevocationReason": "KEY_COMPROMISE",
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_RevokeCertificate_Example_2"></a>

This example illustrates one usage of RevokeCertificate.

#### Sample Response
<a name="API_RevokeCertificate_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_RevokeCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/RevokeCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/RevokeCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
