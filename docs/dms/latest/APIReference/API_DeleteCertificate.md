---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteCertificate.html
---

# DeleteCertificate
<a name="API_DeleteCertificate"></a>

Deletes the specified certificate.

## Request Syntax
<a name="API_DeleteCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateArn](#API_DeleteCertificate_RequestSyntax) **   <a name="DMS-DeleteCertificate-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteCertificate_ResponseSyntax"></a>

```
{
   "Certificate": {
      "CertificateArn": "string",
      "CertificateCreationDate": number,
      "CertificateIdentifier": "string",
      "CertificateOwner": "string",
      "CertificatePem": "string",
      "CertificateWallet": blob,
      "KeyLength": number,
      "KmsKeyId": "string",
      "SigningAlgorithm": "string",
      "ValidFromDate": number,
      "ValidToDate": number
   }
}
```

## Response Elements
<a name="API_DeleteCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_DeleteCertificate_ResponseSyntax) **   <a name="DMS-DeleteCertificate-response-Certificate"></a>
The Secure Sockets Layer (SSL) certificate.
Type: [Certificate](API_Certificate.md) object

## Errors
<a name="API_DeleteCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DeleteCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteCertificate)
