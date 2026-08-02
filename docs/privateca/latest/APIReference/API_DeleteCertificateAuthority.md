---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html
---

# DeleteCertificateAuthority
<a name="API_DeleteCertificateAuthority"></a>

Deletes a private certificate authority (CA). You must provide the Amazon Resource Name (ARN) of the private CA that you want to delete. You can find the ARN by calling the [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) action.

**Note**
Deleting a CA will invalidate other CAs and certificates below it in your CA hierarchy.

Before you can delete a CA that you have created and activated, you must disable it. To do this, call the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) action and set the **CertificateAuthorityStatus** parameter to `DISABLED`.

Additionally, you can delete a CA if you are waiting for it to be created (that is, the status of the CA is `CREATING`). You can also delete it if the CA has been created but you haven't yet imported the signed certificate into AWS Private CA (that is, the status of the CA is `PENDING_CERTIFICATE`).

When you successfully call [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html), the CA's status changes to `DELETED`. However, the CA won't be permanently deleted until the restoration period has passed. By default, if you do not set the `PermanentDeletionTimeInDays` parameter, the CA remains restorable for 30 days. You can set the parameter from 7 to 30 days. The [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html) action returns the time remaining in the restoration window of a private CA in the `DELETED` state. To restore an eligible CA, call the [RestoreCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html) action.

**Important**
A private CA can be deleted if it is in the `PENDING_CERTIFICATE`, `CREATING`, `EXPIRED`, `DISABLED`, or `FAILED` state. To delete a CA in the `ACTIVE` state, you must first disable it, or else the delete request results in an exception. If you are deleting a private CA in the `PENDING_CERTIFICATE` or `DISABLED` state, you can set the length of its restoration period to 7-30 days. The default is 30. During this time, the status is set to `DELETED` and the CA can be restored. A private CA deleted in the `CREATING` or `FAILED` state has no assigned restoration period and cannot be restored.

## Request Syntax
<a name="API_DeleteCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "PermanentDeletionTimeInDays": {{number}}
}
```

## Request Parameters
<a name="API_DeleteCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_DeleteCertificateAuthority_RequestSyntax) **   <a name="privateca-DeleteCertificateAuthority-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must have the following form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [PermanentDeletionTimeInDays](#API_DeleteCertificateAuthority_RequestSyntax) **   <a name="privateca-DeleteCertificateAuthority-request-PermanentDeletionTimeInDays"></a>
The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.
Type: Integer
Valid Range: Minimum value of 7. Maximum value of 30.
Required: No

## Response Elements
<a name="API_DeleteCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
A previous update to your private CA is still ongoing.
HTTP Status Code: 400

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
<a name="API_DeleteCertificateAuthority_Examples"></a>

### Example
<a name="API_DeleteCertificateAuthority_Example_1"></a>

This example illustrates one usage of DeleteCertificateAuthority.

#### Sample Request
<a name="API_DeleteCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 163
X-Amz-Target: ACMPrivateCA.DeleteCertificateAuthority
X-Amz-Date: 20180515T160248Z
User-Agent: aws-cli/1.15.4 Python/2.7.9 Windows/8 botocore/1.10.4
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180515/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=8f7e5b799989c607156141bc6856eb48acd45def7eecd2b2b7fbaa11f34d7bd1

{"PermanentDeletionTimeInDays": 17, "CertificateAuthorityArn": "arn:aws:acm-pca:us-west-2:493619779192:certificate-authority/4ce5e894-a076-4ed8-9d5c-42afbd4cbf88"}
```

### Example
<a name="API_DeleteCertificateAuthority_Example_2"></a>

This example illustrates one usage of DeleteCertificateAuthority.

#### Sample Response
<a name="API_DeleteCertificateAuthority_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_DeleteCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/DeleteCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/DeleteCertificateAuthority)
