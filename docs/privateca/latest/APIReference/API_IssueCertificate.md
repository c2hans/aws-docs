---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html
---

# IssueCertificate
<a name="API_IssueCertificate"></a>

Uses your private certificate authority (CA), or one that has been shared with you, to issue a client certificate. This action returns the Amazon Resource Name (ARN) of the certificate. You can retrieve the certificate by calling the [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) action and specifying the ARN.

**Note**
You cannot use the ACM **ListCertificateAuthorities** action to retrieve the ARNs of the certificates that you issue by using AWS Private CA.

## Request Syntax
<a name="API_IssueCertificate_RequestSyntax"></a>

```
{
   "ApiPassthrough": {
      "Extensions": {
         "CertificatePolicies": [
            {
               "CertPolicyId": "{{string}}",
               "PolicyQualifiers": [
                  {
                     "PolicyQualifierId": "{{string}}",
                     "Qualifier": {
                        "CpsUri": "{{string}}"
                     }
                  }
               ]
            }
         ],
         "CustomExtensions": [
            {
               "Critical": {{boolean}},
               "ObjectIdentifier": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "ExtendedKeyUsage": [
            {
               "ExtendedKeyUsageObjectIdentifier": "{{string}}",
               "ExtendedKeyUsageType": "{{string}}"
            }
         ],
         "KeyUsage": {
            "CRLSign": {{boolean}},
            "DataEncipherment": {{boolean}},
            "DecipherOnly": {{boolean}},
            "DigitalSignature": {{boolean}},
            "EncipherOnly": {{boolean}},
            "KeyAgreement": {{boolean}},
            "KeyCertSign": {{boolean}},
            "KeyEncipherment": {{boolean}},
            "NonRepudiation": {{boolean}}
         },
         "SubjectAlternativeNames": [
            {
               "DirectoryName": {
                  "CommonName": "{{string}}",
                  "Country": "{{string}}",
                  "CustomAttributes": [
                     {
                        "ObjectIdentifier": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ],
                  "DistinguishedNameQualifier": "{{string}}",
                  "GenerationQualifier": "{{string}}",
                  "GivenName": "{{string}}",
                  "Initials": "{{string}}",
                  "Locality": "{{string}}",
                  "Organization": "{{string}}",
                  "OrganizationalUnit": "{{string}}",
                  "Pseudonym": "{{string}}",
                  "SerialNumber": "{{string}}",
                  "State": "{{string}}",
                  "Surname": "{{string}}",
                  "Title": "{{string}}"
               },
               "DnsName": "{{string}}",
               "EdiPartyName": {
                  "NameAssigner": "{{string}}",
                  "PartyName": "{{string}}"
               },
               "IpAddress": "{{string}}",
               "OtherName": {
                  "TypeId": "{{string}}",
                  "Value": "{{string}}"
               },
               "RegisteredId": "{{string}}",
               "Rfc822Name": "{{string}}",
               "UniformResourceIdentifier": "{{string}}"
            }
         ]
      },
      "Subject": {
         "CommonName": "{{string}}",
         "Country": "{{string}}",
         "CustomAttributes": [
            {
               "ObjectIdentifier": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "DistinguishedNameQualifier": "{{string}}",
         "GenerationQualifier": "{{string}}",
         "GivenName": "{{string}}",
         "Initials": "{{string}}",
         "Locality": "{{string}}",
         "Organization": "{{string}}",
         "OrganizationalUnit": "{{string}}",
         "Pseudonym": "{{string}}",
         "SerialNumber": "{{string}}",
         "State": "{{string}}",
         "Surname": "{{string}}",
         "Title": "{{string}}"
      }
   },
   "CertificateAuthorityArn": "{{string}}",
   "Csr": {{blob}},
   "IdempotencyToken": "{{string}}",
   "SigningAlgorithm": "{{string}}",
   "TemplateArn": "{{string}}",
   "Validity": {
      "Type": "{{string}}",
      "Value": {{number}}
   },
   "ValidityNotBefore": {
      "Type": "{{string}}",
      "Value": {{number}}
   }
}
```

## Request Parameters
<a name="API_IssueCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApiPassthrough](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-ApiPassthrough"></a>
Specifies X.509 certificate information to be included in the issued certificate. An `APIPassthrough` or `APICSRPassthrough` template variant must be selected, or else this parameter is ignored. For more information about using these templates, see [Understanding Certificate Templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html).
If conflicting or duplicate certificate information is supplied during certificate issuance, AWS Private CA applies [order of operation rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations) to determine what information is used.
Type: [ApiPassthrough](API_ApiPassthrough.md) object
Required: No

 ** [CertificateAuthorityArn](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [Csr](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-Csr"></a>
The certificate signing request (CSR) for the certificate you want to issue. As an example, you can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key.
 `openssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr`
If you have a configuration file, you can then use the following OpenSSL command. The `usr_cert` block in the configuration file contains your X509 version 3 extensions.
 `openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr`
Note: A CSR must provide either a *subject name* or a *subject alternative name* or the request will be rejected.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: Yes

 ** [IdempotencyToken](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-IdempotencyToken"></a>
Alphanumeric string that can be used to distinguish between calls to the **IssueCertificate** action. Idempotency tokens for **IssueCertificate** time out after five minutes. Therefore, if you call **IssueCertificate** multiple times with the same idempotency token within five minutes, AWS Private CA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, AWS Private CA recognizes that you are requesting multiple certificates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]*`
Required: No

 ** [SigningAlgorithm](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-SigningAlgorithm"></a>
The name of the algorithm that will be used to sign the certificate to be issued.
This parameter should not be confused with the `SigningAlgorithm` parameter used to sign a CSR in the `CreateCertificateAuthority` action.
The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.
Type: String
Valid Values: `SHA256WITHECDSA | SHA384WITHECDSA | SHA512WITHECDSA | SHA256WITHRSA | SHA384WITHRSA | SHA512WITHRSA | SM3WITHSM2 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87`
Required: Yes

 ** [TemplateArn](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-TemplateArn"></a>
Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, AWS Private CA defaults to the `EndEntityCertificate/V1` template. For CA certificates, you should choose the shortest path length that meets your needs. The path length is indicated by the PathLen*N* portion of the ARN, where *N* is the [CA depth](https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html#terms-cadepth).
Note: The CA depth configured on a subordinate CA certificate must not exceed the limit set by its parents in the CA hierarchy.
For a list of `TemplateArn` values supported by AWS Private CA, see [Understanding Certificate Templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: No

 ** [Validity](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-Validity"></a>
Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate.
Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see [Validity](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5) in RFC 5280.
This value is unaffected when `ValidityNotBefore` is also specified. For example, if `Validity` is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the `ValidityNotBefore` value.
The end of the validity period configured on a certificate must not exceed the limit set on its parents in the CA hierarchy.
Type: [Validity](API_Validity.md) object
Required: Yes

 ** [ValidityNotBefore](#API_IssueCertificate_RequestSyntax) **   <a name="privateca-IssueCertificate-request-ValidityNotBefore"></a>
Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate.
By default, when issuing a certificate, AWS Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The `ValidityNotBefore` parameter can be used to customize the “Not Before” value.
Unlike the `Validity` parameter, the `ValidityNotBefore` parameter is optional.
The `ValidityNotBefore` value is expressed as an explicit date and time, using the `Validity` type value `ABSOLUTE`. For more information, see [Validity](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html) in this API reference and [Validity](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5) in RFC 5280.
Type: [Validity](API_Validity.md) object
Required: No

## Response Syntax
<a name="API_IssueCertificate_ResponseSyntax"></a>

```
{
   "CertificateArn": "string"
}
```

## Response Elements
<a name="API_IssueCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateArn](#API_IssueCertificate_ResponseSyntax) **   <a name="privateca-IssueCertificate-response-CertificateArn"></a>
The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number. This is of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/286535153982981100925020015808220737245 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`

## Errors
<a name="API_IssueCertificate_Errors"></a>

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

 ** LimitExceededException **
An AWS Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.
HTTP Status Code: 400

 ** MalformedCSRException **
The certificate signing request is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_IssueCertificate_Examples"></a>

### Example
<a name="API_IssueCertificate_Example_1"></a>

This example illustrates one usage of IssueCertificate.

#### Sample Request
<a name="API_IssueCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 1680
X-Amz-Target: ACMPrivateCA.IssueCertificate
X-Amz-Date: 20180226T193956Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=c6cac56b2eac254d53616072c55d2c2c1f24f4670aa16911c76ae492a92fdd00

{
  "IdempotencyToken": "1234",
  "SigningAlgorithm": "SHA256WITHRSA",
  "Validity": {
    "Type": "DAYS",
    "Value": 365
  },
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012",
  "Csr": "LS0tL...tLS0K"
}
```

### Example
<a name="API_IssueCertificate_Example_2"></a>

This example illustrates one usage of IssueCertificate.

#### Sample Response
<a name="API_IssueCertificate_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 18:08:50 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 163
x-amzn-RequestId: 629173f2-4697-44fa-a599-b757a8da6c7e
Connection: keep-alive

{
    "CertificateArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/e8cbd2bedb122329f97706bcfec990f8"
}
```

## See Also
<a name="API_IssueCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/IssueCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/IssueCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
