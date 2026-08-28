---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ImportCertificate.html
---

# ImportCertificate
<a name="API_ImportCertificate"></a>

Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.

You can import both the certificate and its chain in the `Certificate` parameter.

After importing a certificate, AWS Transfer Family automatically creates a Amazon CloudWatch metric called `DaysUntilExpiry` that tracks the number of days until the certificate expires. The metric is based on the `InactiveDate` parameter and is published daily in the `AWS/Transfer` namespace.

**Important**
It can take up to a full day after importing a certificate for Transfer Family to emit the `DaysUntilExpiry` metric to your account.

**Note**
If you use the `Certificate` parameter to upload both the certificate and its chain, don't use the `CertificateChain` parameter.

 **CloudWatch monitoring**

The `DaysUntilExpiry` metric includes the following specifications:
+  **Units:** Count (days)
+  **Dimensions:** `CertificateId` (always present), `Description` (if provided during certificate import)
+  **Statistics:** Minimum, Maximum, Average
+  **Frequency:** Published daily

## Request Syntax
<a name="API_ImportCertificate_RequestSyntax"></a>

```
{
   "ActiveDate": {{number}},
   "Certificate": "{{string}}",
   "CertificateChain": "{{string}}",
   "Description": "{{string}}",
   "InactiveDate": {{number}},
   "PrivateKey": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Usage": "{{string}}"
}
```

## Request Parameters
<a name="API_ImportCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActiveDate](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-ActiveDate"></a>
An optional date that specifies when the certificate becomes active. If you do not specify a value, `ActiveDate` takes the same value as `NotBeforeDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** [Certificate](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-Certificate"></a>
+ For the CLI, provide a file path for a certificate in URI format. For example, `--certificate file://encryption-cert.pem`. Alternatively, you can provide the raw content.
+ For the SDK, specify the raw content of a certificate file. For example, `--certificate "`cat encryption-cert.pem`"`.
You can provide both the certificate and its chain in this parameter, without needing to use the `CertificateChain` parameter. If you use this parameter for both the certificate and its chain, do not use the `CertificateChain` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\t\n\r\u0020-\u00FF]+`
Required: Yes

 ** [CertificateChain](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-CertificateChain"></a>
An optional list of certificates that make up the chain for the certificate that's being imported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2097152.
Pattern: `[\t\n\r\u0020-\u00FF]+`
Required: No

 ** [Description](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-Description"></a>
A short description that helps identify the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [InactiveDate](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-InactiveDate"></a>
An optional date that specifies when the certificate becomes inactive. If you do not specify a value, `InactiveDate` takes the same value as `NotAfterDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** [PrivateKey](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-PrivateKey"></a>
+ For the CLI, provide a file path for a private key in URI format. For example, `--private-key file://encryption-key.pem`. Alternatively, you can provide the raw content of the private key file.
+ For the SDK, specify the raw content of a private key file. For example, `--private-key "`cat encryption-key.pem`"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\t\n\r\u0020-\u00FF]+`
Required: No

 ** [Tags](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-Tags"></a>
Key-value pairs that can be used to group and search for certificates.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [Usage](#API_ImportCertificate_RequestSyntax) **   <a name="TransferFamily-ImportCertificate-request-Usage"></a>
Specifies how this certificate is used. It can be used in the following ways:
+  `SIGNING`: For signing AS2 messages
+  `ENCRYPTION`: For encrypting AS2 messages
+  `TLS`: For securing AS2 communications sent over HTTPS
Type: String
Valid Values: `SIGNING | ENCRYPTION | TLS`
Required: Yes

## Response Syntax
<a name="API_ImportCertificate_ResponseSyntax"></a>

```
{
   "CertificateId": "string"
}
```

## Response Elements
<a name="API_ImportCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateId](#API_ImportCertificate_ResponseSyntax) **   <a name="TransferFamily-ImportCertificate-response-CertificateId"></a>
An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `cert-([0-9a-f]{17})`

## Errors
<a name="API_ImportCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

## Examples
<a name="API_ImportCertificate_Examples"></a>

### Example
<a name="API_ImportCertificate_Example_1"></a>

The following example imports a certificate to use for encryption. In the first command, we provide the contents of the certificate and certificate chain files. Use this format for SDK commands.

```
aws transfer import-certificate --usage ENCRYPTION --certificate "`cat encryption-cert.pem`" \
    --private-key "`cat encryption-key.pem`" --certificate-chain "`cat root-ca.pem`"
```

### Example
<a name="API_ImportCertificate_Example_2"></a>

The following example is identical to the preceding command, except that we provide the file locations for the private key, certificate, and certificate chain files. This version of the command doesn't work if you are using an SDK.

```
aws transfer import-certificate --usage ENCRYPTION --certificate file://encryption-cert.pem \
    --private-key file://encryption-key.pem --certificate-chain file://root-ca.pem
```

### Example
<a name="API_ImportCertificate_Example_3"></a>

You can create CloudWatch alarms to monitor certificate expiration. The following example creates an alarm that triggers when a certificate has 30 days or fewer until expiration:

```
aws cloudwatch put-metric-alarm \
  --alarm-name "Certificate-Expiry-30-Days" \
  --alarm-description "Certificate expires in 30 days or less" \
  --metric-name DaysUntilExpiry \
  --namespace AWS/Transfer \
  --statistic Maximum \
  --period 86400 \
  --threshold 30 \
  --comparison-operator LessThanOrEqualToThreshold \
  --treat-missing-data notBreaching \
  --dimensions Name=CertificateId,Value=c-1234567890abcdef0 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:certificate-alerts
```

## See Also
<a name="API_ImportCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/ImportCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ImportCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
