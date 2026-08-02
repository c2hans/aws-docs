---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html
---

# RestoreCertificateAuthority
<a name="API_RestoreCertificateAuthority"></a>

Restores a certificate authority (CA) that is in the `DELETED` state. You can restore a CA during the period that you defined in the **PermanentDeletionTimeInDays** parameter of the [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html) action. Currently, you can specify 7 to 30 days. If you did not specify a **PermanentDeletionTimeInDays** value, by default you can restore the CA at any time in a 30 day period. You can check the time remaining in the restoration period of a private CA in the `DELETED` state by calling the [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html) or [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) actions. The status of a restored CA is set to its pre-deletion status when the **RestoreCertificateAuthority** action returns. To change its status to `ACTIVE`, call the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) action. If the private CA was in the `PENDING_CERTIFICATE` state at deletion, you must use the [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html) action to import a certificate authority into the private CA before it can be activated. You cannot restore a CA after the restoration period has ended.

## Request Syntax
<a name="API_RestoreCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_RestoreCertificateAuthority_RequestSyntax) **   <a name="privateca-RestoreCertificateAuthority-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Elements
<a name="API_RestoreCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RestoreCertificateAuthority_Errors"></a>

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
<a name="API_RestoreCertificateAuthority_Examples"></a>

### Example
<a name="API_RestoreCertificateAuthority_Example_1"></a>

This example illustrates one usage of RestoreCertificateAuthority.

#### Sample Request
<a name="API_RestoreCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 128
X-Amz-Target: ACMPrivateCA.RestoreCertificateAuthority
X-Amz-Date: 20180514T174156Z
User-Agent: aws-cli/1.15.4 Python/2.7.9 Windows/8 botocore/1.10.4
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180514/AWS_Region/acm-pca/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=a47d3316aee9992689407c40f877138c261cef8e73996f608c5ffcaf46c593f8

{"CertificateAuthorityArn": "arn:aws:acm-pca:AWS_region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012"}
```

### Example
<a name="API_RestoreCertificateAuthority_Example_2"></a>

This example illustrates one usage of RestoreCertificateAuthority.

#### Sample Response
<a name="API_RestoreCertificateAuthority_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_RestoreCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/RestoreCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/RestoreCertificateAuthority)
