---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html
---

# UpdateCertificateAuthority
<a name="API_UpdateCertificateAuthority"></a>

Updates the status or configuration of a private certificate authority (CA). Your private CA must be in the `ACTIVE` or `DISABLED` state before you can update it. You can disable a private CA that is in the `ACTIVE` state or make a CA that is in the `DISABLED` state active again.

**Note**
Both AWS Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see [Access policies for CRLs in Amazon S3](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies).

## Request Syntax
<a name="API_UpdateCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
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
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_UpdateCertificateAuthority_RequestSyntax) **   <a name="privateca-UpdateCertificateAuthority-request-CertificateAuthorityArn"></a>
Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [RevocationConfiguration](#API_UpdateCertificateAuthority_RequestSyntax) **   <a name="privateca-UpdateCertificateAuthority-request-RevocationConfiguration"></a>
Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. If you don't supply this parameter, existing capibilites remain unchanged. For more information, see the [OcspConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html) and [CrlConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html) types.
The following requirements apply to revocation configurations.
+ A configuration disabling CRLs or OCSP must contain only the `Enabled=False` parameter, and will fail if other parameters such as `CustomCname` or `ExpirationInDays` are included.
+ In a CRL configuration, the `S3BucketName` parameter must conform to [Amazon S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
+ A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in a CNAME.
+ In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".
 If you update the `S3BucketName` of [CrlConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html), you can break revocation for existing certificates. In other words, if you call [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) to update the CRL configuration's S3 bucket name, AWS Private CA only writes CRLs to the new S3 bucket. Certificates issued prior to this point will have the old S3 bucket name in your CRL Distribution Point (CDP) extension, essentially breaking revocation. If you must update the S3 bucket, you'll need to reissue old certificates to keep the revocation working. Alternatively, you can use a [CustomCname](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html#privateca-Type-CrlConfiguration-CustomCname) in your CRL configuration if you might need to change the S3 bucket name in the future.
Type: [RevocationConfiguration](API_RevocationConfiguration.md) object
Required: No

 ** [Status](#API_UpdateCertificateAuthority_RequestSyntax) **   <a name="privateca-UpdateCertificateAuthority-request-Status"></a>
Status of your private CA.
Type: String
Valid Values: `CREATING | PENDING_CERTIFICATE | ACTIVE | DELETED | DISABLED | EXPIRED | FAILED`
Required: No

## Response Elements
<a name="API_UpdateCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
A previous update to your private CA is still ongoing.
HTTP Status Code: 400

 ** InvalidArgsException **
One or more of the specified arguments was not valid.
HTTP Status Code: 400

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidPolicyException **
The resource policy is invalid or is missing a required statement. For general information about IAM policy and statement structure, see [Overview of JSON Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json).
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_UpdateCertificateAuthority_Examples"></a>

### Example
<a name="API_UpdateCertificateAuthority_Example_1"></a>

This example illustrates one usage of UpdateCertificateAuthority.

#### Sample Request
<a name="API_UpdateCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 323
X-Amz-Target: ACMPrivateCA.UpdateCertificateAuthority
X-Amz-Date: 20180226T172929Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=f11213b3c4da1754a811fcd72ea637b8acbe41fb7b5e3541806d0418a3323dd8

{
  "Status": "ACTIVE",
  "RevocationConfiguration": {
    "CrlConfiguration": {
      "CustomCname": "https://somename.crl",
      "Enabled": true,
      "S3BucketName": "your-bucket-name",
      "ExpirationInDays": 3650
    }
  },
  "CertificateAuthorityArn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_UpdateCertificateAuthority_Example_2"></a>

This example illustrates one usage of UpdateCertificateAuthority.

#### Sample Response
<a name="API_UpdateCertificateAuthority_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_UpdateCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/UpdateCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/UpdateCertificateAuthority)
