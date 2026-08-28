---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html
---

# ListCertificateAuthorities
<a name="API_ListCertificateAuthorities"></a>

Lists the private certificate authorities that you created by using the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action.

## Request Syntax
<a name="API_ListCertificateAuthorities_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceOwner": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCertificateAuthorities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="privateca-ListCertificateAuthorities-request-MaxResults"></a>
Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the `NextToken` element is sent in the response. Use this `NextToken` value in a subsequent request to retrieve additional items.
Although the maximum value is 1000, the action only returns a maximum of 100 items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="privateca-ListCertificateAuthorities-request-NextToken"></a>
Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the `NextToken` parameter from the response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.
Required: No

 ** [ResourceOwner](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="privateca-ListCertificateAuthorities-request-ResourceOwner"></a>
Use this parameter to filter the returned set of certificate authorities based on their owner. The default is SELF.
Type: String
Valid Values: `SELF | OTHER_ACCOUNTS`
Required: No

## Response Syntax
<a name="API_ListCertificateAuthorities_ResponseSyntax"></a>

```
{
   "CertificateAuthorities": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCertificateAuthorities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateAuthorities](#API_ListCertificateAuthorities_ResponseSyntax) **   <a name="privateca-ListCertificateAuthorities-response-CertificateAuthorities"></a>
Summary information about each certificate authority you have created.
Type: Array of [CertificateAuthority](API_CertificateAuthority.md) objects

 ** [NextToken](#API_ListCertificateAuthorities_ResponseSyntax) **   <a name="privateca-ListCertificateAuthorities-response-NextToken"></a>
When the list is truncated, this value is present and should be used for the `NextToken` parameter in a subsequent pagination request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.

## Errors
<a name="API_ListCertificateAuthorities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The token specified in the `NextToken` argument is not valid. Use the token returned from your previous call to [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html).
HTTP Status Code: 400

## Examples
<a name="API_ListCertificateAuthorities_Examples"></a>

### Example
<a name="API_ListCertificateAuthorities_Example_1"></a>

This example illustrates one usage of ListCertificateAuthorities.

#### Sample Request
<a name="API_ListCertificateAuthorities_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
X-Amz-Target: ACMPrivateCA.ListCertificateAuthorities
X-Amz-Date: 20180226T150214Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=580fdd5ac17213a3016252fb1b3e1064b507f415f1b55ef1a42c9d7945d620c1

{"MaxResults": 10}
```

### Example
<a name="API_ListCertificateAuthorities_Example_2"></a>

This example illustrates one usage of ListCertificateAuthorities.

#### Sample Response
<a name="API_ListCertificateAuthorities_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 15:56:45 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 5484
x-amzn-RequestId: 9f96be4c-2204-4232-84df-fe5e44d22b22
Connection: keep-alive

{
  "CertificateAuthorities": [{
    "Arn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012",
    "CertificateAuthorityConfiguration": {
      "KeyAlgorithm": "RSA_2048",
      "SigningAlgorithm": "SHA256WITHRSA",
      "Subject": {
        "CommonName": "www.example.com",
        "Locality": "Seattle",
        "Organization": "Example Corporation",
        "OrganizationalUnit": "Operations",
        "State": "Washington"
      }
    },
    "CreatedAt": 1.510085139623E9,
    "LastStateChangeAt": 1.515616539109E9,
    "NotAfter": 1.825445955E9,
    "NotBefore": 1.510085955E9,
    "RevocationConfiguration": {
      "CrlConfiguration": {
        "CustomCname": "https://somename.crl",
        "Enabled": true,
        "ExpirationInDays": 3650,
        "S3BucketName": "your-bucket-name"
      }
    },
    "Serial": "4109",
    "Status": "DISABLED",
    "Type": "SUBORDINATE"
  },
  {
    "Arn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/11111111-2222-3333-4444-555555555555",
    "CertificateAuthorityConfiguration": {
      "KeyAlgorithm": "RSA_4096",
      "SigningAlgorithm": "SHA256WITHRSA",
      "Subject": {
        "CommonName": "www.examplesales.com",
        "Country": "US",
        "Locality": "Spokane",
        "Organization": "Example Sales LLC",
        "OrganizationalUnit": "Corporate",
        "State": "Washington"
      }
    },
    "CreatedAt": 1.517421065699E9,
    "LastStateChangeAt": 1.517421065699E9,
    "RevocationConfiguration": {
      "CrlConfiguration": {
        "CustomCname": "https://somename.crl",
        "Enabled": true,
        "ExpirationInDays": 3650,
        "S3BucketName": "your-bucket-name"
      }
    },
    "Serial": "3611",
    "Status": "PENDING_CERTIFICATE",
    "Type": "SUBORDINATE"
  },
  {
    "Arn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/99999999-4321-1234-4321-4321-888888888888",
    "CertificateAuthorityConfiguration": {
      "KeyAlgorithm": "RSA_2048",
      "SigningAlgorithm": "SHA256WITHRSA",
      "Subject": {
        "CommonName": "www.company.com",
        "Country": "US",
        "Locality": "Seattle",
        "Organization": "Company Ltd.",
        "OrganizationalUnit": "Sales",
        "State": "Washington"
      }
    },
    "CreatedAt": 1.505332492167E9,
    "LastStateChangeAt": 1.505332492167E9,
    "NotAfter": 1.820697079E9,
    "NotBefore": 1.505337079E9,
    "RevocationConfiguration": {
      "CrlConfiguration": {
        "CustomCname": "https://somename.crl",
        "Enabled": true,
        "ExpirationInDays": 3650,
        "S3BucketName": "your-bucket-name"
      }
    },
    "Serial": "4100",
    "Status": "ACTIVE",
    "Type": "SUBORDINATE"
  }
 ]
}
```

## See Also
<a name="API_ListCertificateAuthorities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/ListCertificateAuthorities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ListCertificateAuthorities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
