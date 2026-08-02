---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html
---

# DescribeCertificateAuthority
<a name="API_DescribeCertificateAuthority"></a>

Lists information about your private certificate authority (CA) or one that has been shared with you. You specify the private CA on input by its ARN (Amazon Resource Name). The output contains the status of your CA. This can be any of the following:
+  `CREATING` - AWS Private CA is creating your private certificate authority.
+  `PENDING_CERTIFICATE` - The certificate is pending. You must use your AWS Private CA-hosted or on-premises root or subordinate CA to sign your private CA CSR and then import it into AWS Private CA.
+  `ACTIVE` - Your private CA is active.
+  `DISABLED` - Your private CA has been disabled.
+  `EXPIRED` - Your private CA certificate has expired.
+  `FAILED` - Your private CA has failed. Your CA can fail because of problems such a network outage or back-end AWS failure or other errors. A failed CA can never return to the pending state. You must create a new CA.
+  `DELETED` - Your private CA is within the restoration period, after which it is permanently deleted. The length of time remaining in the CA's restoration period is also included in this action's output.

## Request Syntax
<a name="API_DescribeCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_DescribeCertificateAuthority_RequestSyntax) **   <a name="privateca-DescribeCertificateAuthority-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_DescribeCertificateAuthority_ResponseSyntax"></a>

```
{
   "CertificateAuthority": {
      "Arn": "string",
      "CertificateAuthorityConfiguration": {
         "CsrExtensions": {
            "KeyUsage": {
               "CRLSign": boolean,
               "DataEncipherment": boolean,
               "DecipherOnly": boolean,
               "DigitalSignature": boolean,
               "EncipherOnly": boolean,
               "KeyAgreement": boolean,
               "KeyCertSign": boolean,
               "KeyEncipherment": boolean,
               "NonRepudiation": boolean
            },
            "SubjectInformationAccess": [
               {
                  "AccessLocation": {
                     "DirectoryName": {
                        "CommonName": "string",
                        "Country": "string",
                        "CustomAttributes": [
                           {
                              "ObjectIdentifier": "string",
                              "Value": "string"
                           }
                        ],
                        "DistinguishedNameQualifier": "string",
                        "GenerationQualifier": "string",
                        "GivenName": "string",
                        "Initials": "string",
                        "Locality": "string",
                        "Organization": "string",
                        "OrganizationalUnit": "string",
                        "Pseudonym": "string",
                        "SerialNumber": "string",
                        "State": "string",
                        "Surname": "string",
                        "Title": "string"
                     },
                     "DnsName": "string",
                     "EdiPartyName": {
                        "NameAssigner": "string",
                        "PartyName": "string"
                     },
                     "IpAddress": "string",
                     "OtherName": {
                        "TypeId": "string",
                        "Value": "string"
                     },
                     "RegisteredId": "string",
                     "Rfc822Name": "string",
                     "UniformResourceIdentifier": "string"
                  },
                  "AccessMethod": {
                     "AccessMethodType": "string",
                     "CustomObjectIdentifier": "string"
                  }
               }
            ]
         },
         "KeyAlgorithm": "string",
         "SigningAlgorithm": "string",
         "Subject": {
            "CommonName": "string",
            "Country": "string",
            "CustomAttributes": [
               {
                  "ObjectIdentifier": "string",
                  "Value": "string"
               }
            ],
            "DistinguishedNameQualifier": "string",
            "GenerationQualifier": "string",
            "GivenName": "string",
            "Initials": "string",
            "Locality": "string",
            "Organization": "string",
            "OrganizationalUnit": "string",
            "Pseudonym": "string",
            "SerialNumber": "string",
            "State": "string",
            "Surname": "string",
            "Title": "string"
         }
      },
      "CreatedAt": number,
      "FailureReason": "string",
      "KeyStorageSecurityStandard": "string",
      "LastStateChangeAt": number,
      "NotAfter": number,
      "NotBefore": number,
      "OwnerAccount": "string",
      "RestorableUntil": number,
      "RevocationConfiguration": {
         "CrlConfiguration": {
            "CrlDistributionPointExtensionConfiguration": {
               "OmitExtension": boolean
            },
            "CrlType": "string",
            "CustomCname": "string",
            "CustomPath": "string",
            "Enabled": boolean,
            "ExpirationInDays": number,
            "S3BucketName": "string",
            "S3ObjectAcl": "string"
         },
         "OcspConfiguration": {
            "Enabled": boolean,
            "OcspCustomCname": "string"
         }
      },
      "Serial": "string",
      "Status": "string",
      "Type": "string",
      "UsageMode": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateAuthority](#API_DescribeCertificateAuthority_ResponseSyntax) **   <a name="privateca-DescribeCertificateAuthority-response-CertificateAuthority"></a>
A [CertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthority.html) structure that contains information about your private CA.
Type: [CertificateAuthority](API_CertificateAuthority.md) object

## Errors
<a name="API_DescribeCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_DescribeCertificateAuthority_Examples"></a>

### Example
<a name="API_DescribeCertificateAuthority_Example_1"></a>

This example illustrates one usage of DescribeCertificateAuthority.

#### Sample Request
<a name="API_DescribeCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 128
X-Amz-Target: ACMPrivateCA.DescribeCertificateAuthority
X-Amz-Date: 20180226T175919Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=953a014106627a76d91f55fd86bb1149bf65d578886bf2371aa4c73c56e16a1d

{"CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"}
```

### Example
<a name="API_DescribeCertificateAuthority_Example_2"></a>

This example illustrates one usage of DescribeCertificateAuthority.

#### Sample Response
<a name="API_DescribeCertificateAuthority_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 17:09:51 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 713
x-amzn-RequestId: 8d51e9ff-8ae9-4ccf-816a-8e7d9c3dc1af
Connection: keep-alive

{
  "CertificateAuthority": {
    "Arn": "arn:aws:acm-pca:gh:account:certificate-authority/12345678-1234-1234-1234-123456789012",
    "CertificateAuthorityConfiguration": {
      "KeyAlgorithm": "RSA_2048",
      "SigningAlgorithm": "SHA256WITHRSA",
      "Subject": {
        "CommonName": "www.example.com",
        "Country": "US",
        "Locality": "Seattle",
        "Organization": "Example Company",
        "OrganizationalUnit": "Corporate",
        "State": "WA"
      }
    },
    "CreatedAt": 1.516130652887E9,
    "LastStateChangeAt": 1.516130652887E9,
    "NotAfter": 1.831494803E9,
    "NotBefore": 1.516134803E9,
    "RevocationConfiguration": {
      "CrlConfiguration": {
        "CustomCname": "http://somename.crl",
        "Enabled": true,
        "ExpirationInDays": 3650,
        "S3BucketName": "your-bucket-name"
      }
    },
    "Serial": "4118",
    "Status": "ACTIVE",
    "Type": "SUBORDINATE"
  }
}
```

## See Also
<a name="API_DescribeCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/DescribeCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/DescribeCertificateAuthority)
