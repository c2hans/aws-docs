---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html
---

# UpdateCertificateOptions
<a name="API_UpdateCertificateOptions"></a>

Updates certificate options. You can use this operation to change the domain validation method or specify whether to export your certificate. For more information, see [Migrate from email to DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/email-to-dns-migration.html) and [AWS Certificate Manager Exportable Managed Certificates](https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html).

## Request Syntax
<a name="API_UpdateCertificateOptions_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "Options": {
      "CertificateTransparencyLoggingPreference": "{{string}}",
      "Export": "{{string}}",
      "ValidationMethod": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateCertificateOptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_UpdateCertificateOptions_RequestSyntax) **   <a name="ACM-UpdateCertificateOptions-request-CertificateArn"></a>
ARN of the requested certificate to update. This must be of the form:
 `arn:aws:acm:us-east-1:account:certificate/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [Options](#API_UpdateCertificateOptions_RequestSyntax) **   <a name="ACM-UpdateCertificateOptions-request-Options"></a>
Use to update the options for your certificate. Currently, you can change the domain validation method or specify whether to export your certificate. For more information about migrating from email to DNS validation, see [Migrate from email to DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/email-to-dns-migration.html).
Type: [CertificateOptions](API_CertificateOptions.md) object
Required: Yes

## Response Elements
<a name="API_UpdateCertificateOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCertificateOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.
HTTP Status Code: 400

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
Processing has reached an invalid state.
HTTP Status Code: 400

 ** LimitExceededException **
An ACM quota has been exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_UpdateCertificateOptions_Examples"></a>

### UpdateCertificateOptions
<a name="API_UpdateCertificateOptions_Example_1"></a>

This example illustrates one usage of UpdateCertificateOptions.

#### Sample Request
<a name="API_UpdateCertificateOptions_Example_1_Request"></a>

```
POST / HTTP/1.1
acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 210
X-Amz-Target: CertificateManager.UpdateCertificateOptions
X-Amz-Date: 20260701T120000Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20260701/us-east-1/acm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=EXAMPLE

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012",
  "Options": {
    "ValidationMethod": "DNS"
  }
}
```

### Example
<a name="API_UpdateCertificateOptions_Example_2"></a>

This example illustrates one usage of UpdateCertificateOptions.

#### Sample Response
<a name="API_UpdateCertificateOptions_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 01 Jul 2026 12:00:00 GMT
```

## See Also
<a name="API_UpdateCertificateOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/UpdateCertificateOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/UpdateCertificateOptions)
