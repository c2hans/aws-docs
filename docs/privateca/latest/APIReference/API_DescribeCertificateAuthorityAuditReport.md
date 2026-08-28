---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthorityAuditReport.html
---

# DescribeCertificateAuthorityAuditReport
<a name="API_DescribeCertificateAuthorityAuditReport"></a>

Lists information about a specific audit report created by calling the [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html) action. Audit information is created every time the certificate authority (CA) private key is used. The private key is used when you call the [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) action or the [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html) action.

## Request Syntax
<a name="API_DescribeCertificateAuthorityAuditReport_RequestSyntax"></a>

```
{
   "AuditReportId": "{{string}}",
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCertificateAuthorityAuditReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditReportId](#API_DescribeCertificateAuthorityAuditReport_RequestSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-request-AuditReportId"></a>
The report ID returned by calling the [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html) action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}`
Required: Yes

 ** [CertificateAuthorityArn](#API_DescribeCertificateAuthorityAuditReport_RequestSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the private CA. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_DescribeCertificateAuthorityAuditReport_ResponseSyntax"></a>

```
{
   "AuditReportStatus": "string",
   "CreatedAt": number,
   "S3BucketName": "string",
   "S3Key": "string"
}
```

## Response Elements
<a name="API_DescribeCertificateAuthorityAuditReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuditReportStatus](#API_DescribeCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-response-AuditReportStatus"></a>
Specifies whether report creation is in progress, has succeeded, or has failed.
Type: String
Valid Values: `CREATING | SUCCESS | FAILED`

 ** [CreatedAt](#API_DescribeCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-response-CreatedAt"></a>
The date and time at which the report was created.
Type: Timestamp

 ** [S3BucketName](#API_DescribeCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-response-S3BucketName"></a>
Name of the S3 bucket that contains the report.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.

 ** [S3Key](#API_DescribeCertificateAuthorityAuditReport_ResponseSyntax) **   <a name="privateca-DescribeCertificateAuthorityAuditReport-response-S3Key"></a>
S3 **key** that uniquely identifies the report file in your S3 bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_DescribeCertificateAuthorityAuditReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgsException **
One or more of the specified arguments was not valid.
HTTP Status Code: 400

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_DescribeCertificateAuthorityAuditReport_Examples"></a>

### Example
<a name="API_DescribeCertificateAuthorityAuditReport_Example_1"></a>

This example illustrates one usage of DescribeCertificateAuthorityAuditReport.

#### Sample Request
<a name="API_DescribeCertificateAuthorityAuditReport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 185
X-Amz-Target: ACMPrivateCA.DescribeCertificateAuthorityAuditReport
X-Amz-Date: 20180226T185916Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=96531073ea22cc7057267543f332911b97a5db830dca85a74a7324c9737cee7a

{
  "AuditReportId": "11111111-2222-3333-4444-555555555555",
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_DescribeCertificateAuthorityAuditReport_Example_2"></a>

This example illustrates one usage of DescribeCertificateAuthorityAuditReport.

#### Sample Response
<a name="API_DescribeCertificateAuthorityAuditReport_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 16:33:26 GMT
Content-Type: application/xget-amz-json-1.1
Content-Length: 211
x-amzn-RequestId: 3af6a588-856c-48eb-81ab-f2f08fbc618c
Connection: keep-alive

{
  "AuditReportStatus": "SUCCESS",
  "CreatedAt": 1.526401743081E9,
  "S3BucketName": "your-bucket-name",
  "S3Key": "audit-report/PCA_ID/Audit_Report_ID.json"
}
```

## See Also
<a name="API_DescribeCertificateAuthorityAuditReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
