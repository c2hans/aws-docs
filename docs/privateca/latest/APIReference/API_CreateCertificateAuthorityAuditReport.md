---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html
---

# CreateCertificateAuthorityAuditReport
<a name="API_CreateCertificateAuthorityAuditReport"></a>

Creates an audit report that lists every time that your CA private key is used to issue a certificate. The [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) and [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html) actions use the private key.

To save the audit report to your designated Amazon S3 bucket, you must create a bucket policy that grants AWS Private CA permission to access and write to it. For an example policy, see [Prepare an Amazon S3 bucket for audit reports](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html#s3-access).

 AWS Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see [Encrypting Your Audit Reports](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html#audit-report-encryption).

**Note**
You can generate a maximum of one report every 30 minutes.

## Request Syntax
<a name="API_CreateCertificateAuthorityAuditReport_RequestSyntax"></a>

```
{
   "AuditReportResponseFormat": "{{string}}",
   "CertificateAuthorityArn": "{{string}}",
   "S3BucketName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCertificateAuthorityAuditReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditReportResponseFormat](#API_CreateCertificateAuthorityAuditReport_RequestSyntax) **   <a name="privateca-CreateCertificateAuthorityAuditReport-request-AuditReportResponseFormat"></a>
The format in which to create the report. This can be either **JSON** or **CSV**.
Type: String
Valid Values: `JSON | CSV`
Required: Yes

 ** [CertificateAuthorityArn](#API_CreateCertificateAuthorityAuditReport_RequestSyntax) **   <a name="privateca-CreateCertificateAuthorityAuditReport-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the CA to be audited. This is of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [S3BucketName](#API_CreateCertificateAuthorityAuditReport_RequestSyntax) **   <a name="privateca-CreateCertificateAuthorityAuditReport-request-S3BucketName"></a>
The name of the S3 bucket that will contain the audit report.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

## Response Syntax
<a name="API_CreateCertificateAuthorityAuditReport_ResponseSyntax"></a>

```
{
   "AuditReportId": "string",
   "S3Key": "string"
}
```

## Response Elements
<a name="API_CreateCertificateAuthorityAuditReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuditReportId](#API_CreateCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-CreateCertificateAuthorityAuditReport-response-AuditReportId"></a>
An alphanumeric string that contains a report identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}`

 ** [S3Key](#API_CreateCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-CreateCertificateAuthorityAuditReport-response-S3Key"></a>
The **key** that uniquely identifies the report file in your S3 bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_CreateCertificateAuthorityAuditReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgsException **
One or more of the specified arguments was not valid.
HTTP Status Code: 400

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
<a name="API_CreateCertificateAuthorityAuditReport_Examples"></a>

### Example
<a name="API_CreateCertificateAuthorityAuditReport_Example_1"></a>

This example illustrates one usage of CreateCertificateAuthorityAuditReport.

#### Sample Request
<a name="API_CreateCertificateAuthorityAuditReport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 216
X-Amz-Target: ACMPrivateCA.CreateCertificateAuthorityAuditReport
X-Amz-Date: 20180226T184819Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=62380db816189148e510734f0ef2bfec08248fb3f447f64d740f31757e1beda0

{
  "AuditReportResponseFormat": "JSON",
  "S3BucketName": "your-bucket-name",
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_CreateCertificateAuthorityAuditReport_Example_2"></a>

This example illustrates one usage of CreateCertificateAuthorityAuditReport.

#### Sample Response
<a name="API_CreateCertificateAuthorityAuditReport_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 16:29:03 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 158
x-amzn-RequestId: e8516078-ff66-4e2a-bc38-eb1aaae2d886
Connection: keep-alive

{
  "AuditReportId": "9654b603-d6a9-4c57-952a-ebcc95631fab",
  "S3Key": "audit-reportPCA_ID/9654b603-d6a9-4c57-952a-ebcc95631fab.json"
}
```

## See Also
<a name="API_CreateCertificateAuthorityAuditReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport)
