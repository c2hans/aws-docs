---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html
---

# CreateCertificateAuthority
<a name="API_CreateCertificateAuthority"></a>

Creates a root or subordinate private certificate authority (CA). You must specify the CA configuration, an optional configuration for Online Certificate Status Protocol (OCSP) and/or a certificate revocation list (CRL), the CA type, and an optional idempotency token to avoid accidental creation of multiple CAs. The CA configuration specifies the name of the algorithm and key size to be used to create the CA private key, the type of signing algorithm that the CA uses, and X.500 subject information. The OCSP configuration can optionally specify a custom URL for the OCSP responder. The CRL configuration specifies the CRL expiration period in days (the validity period of the CRL), the Amazon S3 bucket that will contain the CRL, and a CNAME alias for the S3 bucket that is included in certificates issued by the CA. If successful, this action returns the Amazon Resource Name (ARN) of the CA.

**Note**
Both AWS Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see [Access policies for CRLs in Amazon S3](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies).

 AWS Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see [Encrypting Your CRLs](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#crl-encryption).

## Request Syntax
<a name="API_CreateCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityConfiguration": {
      "CsrExtensions": {
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
         "SubjectInformationAccess": [
            {
               "AccessLocation": {
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
               },
               "AccessMethod": {
                  "AccessMethodType": "{{string}}",
                  "CustomObjectIdentifier": "{{string}}"
               }
            }
         ]
      },
      "KeyAlgorithm": "{{string}}",
      "SigningAlgorithm": "{{string}}",
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
   "CertificateAuthorityType": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "KeyStorageSecurityStandard": "{{string}}",
   "RevocationConfiguration": {
      "CrlConfiguration": {
         "CrlDistributionPointExtensionConfiguration": {
            "OmitExtension": {{boolean}}
         },
         "CrlType": "{{string}}",
         "CustomCname": "{{string}}",
         "CustomPath": "{{string}}",
         "Enabled": {{boolean}},
         "ExpirationInDays": {{number}},
         "S3BucketName": "{{string}}",
         "S3ObjectAcl": "{{string}}"
      },
      "OcspConfiguration": {
         "Enabled": {{boolean}},
         "OcspCustomCname": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UsageMode": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityConfiguration](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-CertificateAuthorityConfiguration"></a>
Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500 certificate subject information.
Type: [CertificateAuthorityConfiguration](API_CertificateAuthorityConfiguration.md) object
Required: Yes

 ** [CertificateAuthorityType](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-CertificateAuthorityType"></a>
The type of the certificate authority.
Type: String
Valid Values: `ROOT | SUBORDINATE`
Required: Yes

 ** [IdempotencyToken](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-IdempotencyToken"></a>
Custom string that can be used to distinguish between calls to the **CreateCertificateAuthority** action. Idempotency tokens for **CreateCertificateAuthority** time out after five minutes. Therefore, if you call **CreateCertificateAuthority** multiple times with the same idempotency token within five minutes, AWS Private CA recognizes that you are requesting only certificate authority and will issue only one. If you change the idempotency token for each call, AWS Private CA recognizes that you are requesting multiple certificate authorities.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]*`
Required: No

 ** [KeyStorageSecurityStandard](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-KeyStorageSecurityStandard"></a>
Specifies a cryptographic key management compliance standard for handling and protecting CA keys.
Default: FIPS\_140\_2\_LEVEL\_3\_OR\_HIGHER
Some AWS Regions don't support the default value. When you create a CA in these Regions, you must use `CCPC_LEVEL_1_OR_HIGHER` for the `KeyStorageSecurityStandard` parameter. If you don't, the operation returns an `InvalidArgsException` with this message: "A certificate authority cannot be created in this region with the specified security standard."
For information about security standard support in different AWS Regions, see [Storage and security compliance of AWS Private CA private keys](https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys).
Type: String
Valid Values: `FIPS_140_2_LEVEL_2_OR_HIGHER | FIPS_140_2_LEVEL_3_OR_HIGHER | CCPC_LEVEL_1_OR_HIGHER`
Required: No

 ** [RevocationConfiguration](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-RevocationConfiguration"></a>
Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. By default, both certificate validation mechanisms are disabled.
The following requirements apply to revocation configurations.
+ A configuration disabling CRLs or OCSP must contain only the `Enabled=False` parameter, and will fail if other parameters such as `CustomCname` or `ExpirationInDays` are included.
+ In a CRL configuration, the `S3BucketName` parameter must conform to [Amazon S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
+ A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in a CNAME.
+ In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".
 For more information, see the [OcspConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html) and [CrlConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html) types.
Type: [RevocationConfiguration](API_RevocationConfiguration.md) object
Required: No

 ** [Tags](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-Tags"></a>
Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [UsageMode](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="privateca-CreateCertificateAuthority-request-UsageMode"></a>
Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.
The default value is GENERAL\_PURPOSE.
Type: String
Valid Values: `GENERAL_PURPOSE | SHORT_LIVED_CERTIFICATE`
Required: No

## Response Syntax
<a name="API_CreateCertificateAuthority_ResponseSyntax"></a>

```
{
   "CertificateAuthorityArn": "string"
}
```

## Response Elements
<a name="API_CreateCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateAuthorityArn](#API_CreateCertificateAuthority_ResponseSyntax) **   <a name="privateca-CreateCertificateAuthority-response-CertificateAuthorityArn"></a>
If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`

## Errors
<a name="API_CreateCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgsException **
One or more of the specified arguments was not valid.
HTTP Status Code: 400

 ** InvalidPolicyException **
The resource policy is invalid or is missing a required statement. For general information about IAM policy and statement structure, see [Overview of JSON Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json).
HTTP Status Code: 400

 ** InvalidTagException **
The tag associated with the CA is not valid. The invalid argument is contained in the message field.
HTTP Status Code: 400

 ** LimitExceededException **
An AWS Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.
HTTP Status Code: 400

## Examples
<a name="API_CreateCertificateAuthority_Examples"></a>

### Example
<a name="API_CreateCertificateAuthority_Example_1"></a>

This example illustrates one usage of CreateCertificateAuthority.

#### Sample Request
<a name="API_CreateCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 512
X-Amz-Target: ACMPrivateCA.CreateCertificateAuthority
X-Amz-Date: 20210310T165448Z
User-Agent: aws-cli/1.15.4 Python/2.7.9 Windows/8 botocore/1.10.4
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AWS_Access_Key_ID/20180515/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=6fc58aaf789659cb4e0dd0ba484a2562d982b6b8edd56ea0c5c94c2af9aeafbe

{
   "IdempotencyToken":"98256344",
   "CertificateAuthorityConfiguration":{
      "KeyAlgorithm":"RSA_2048",
      "SigningAlgorithm":"SHA256WITHRSA",
      "Subject":{
         "Locality":"Seattle",
         "Country":"US",
         "CommonName":"www.example.com",
         "State":"WA",
         "Organization":"Example Ltd.",
         "OrganizationalUnit":"Corporate"
      }
   },
   "CertificateAuthorityType":"SUBORDINATE",
   "RevocationConfiguration":{
      "CrlConfiguration":{
         "CustomCname":"CRL",
         "Enabled":true,
         "ExpirationInDays":7,
         "S3BucketName":"amzn-s3-demo-bucket"
      },
      "OcspConfiguration":{
         "Enabled":false
      }
   }
}
```

### Example
<a name="API_CreateCertificateAuthority_Example_2"></a>

This example illustrates one usage of CreateCertificateAuthority.

#### Sample Response
<a name="API_CreateCertificateAuthority_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 10 March 2021 16:54:56 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 127
x-amzn-RequestId: eacb346a-d80b-4be6-a1b2-1732c3ae3c38
Connection: keep-alive

{
  "CertificateAuthorityArn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

## See Also
<a name="API_CreateCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/CreateCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CreateCertificateAuthority)
