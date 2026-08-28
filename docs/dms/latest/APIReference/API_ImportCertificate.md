---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ImportCertificate.html
---

# ImportCertificate
<a name="API_ImportCertificate"></a>

Uploads the specified certificate.

## Request Syntax
<a name="API_ImportCertificate_RequestSyntax"></a>

```
{
   "CertificateIdentifier": "{{string}}",
   "CertificatePem": "{{string}}",
   "CertificateWallet": {{blob}},
   "KmsKeyId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateIdentifier](#API_ImportCertificate_RequestSyntax) **   <a name="DMS-ImportCertificate-request-CertificateIdentifier"></a>
A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: Yes

 ** [CertificatePem](#API_ImportCertificate_RequestSyntax) **   <a name="DMS-ImportCertificate-request-CertificatePem"></a>
The contents of a `.pem` file, which contains an X.509 certificate.
Type: String
Required: No

 ** [CertificateWallet](#API_ImportCertificate_RequestSyntax) **   <a name="DMS-ImportCertificate-request-CertificateWallet"></a>
The location of an imported Oracle Wallet certificate for use with SSL. Provide the name of a `.sso` file using the `fileb://` prefix. You can't provide the certificate inline.
Example: `filebase64("${path.root}/rds-ca-2019-root.sso")`
Type: Base64-encoded binary data object
Required: No

 ** [KmsKeyId](#API_ImportCertificate_RequestSyntax) **   <a name="DMS-ImportCertificate-request-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the certificate.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** [Tags](#API_ImportCertificate_RequestSyntax) **   <a name="DMS-ImportCertificate-request-Tags"></a>
The tags associated with the certificate.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_ImportCertificate_ResponseSyntax"></a>

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
<a name="API_ImportCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_ImportCertificate_ResponseSyntax) **   <a name="DMS-ImportCertificate-response-Certificate"></a>
The certificate to be uploaded.
Type: [Certificate](API_Certificate.md) object

## Errors
<a name="API_ImportCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidCertificateFault **
The certificate was not valid.
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ImportCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ImportCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ImportCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
