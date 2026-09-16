---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html
---

# TagCertificateAuthority
<a name="API_TagCertificateAuthority"></a>

Adds one or more tags to your private CA. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. You specify the private CA on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. You can apply a tag to just one private CA if you want to identify a specific characteristic of that CA, or you can apply the same tag to multiple private CAs if you want to filter for a common relationship among those CAs. To remove one or more tags, use the [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html) action. Call the [ListTags](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html) action to see what tags are associated with your CA.

**Note**
To attach tags to a private CA during the creation procedure, a CA administrator must first associate an inline IAM policy with the `CreateCertificateAuthority` action and explicitly allow tagging. For more information, see [Attaching tags to a CA at the time of creation](https://docs.aws.amazon.com/privateca/latest/userguide/auth-InlinePolicies.html#policy-tag-ca).

## Request Syntax
<a name="API_TagCertificateAuthority_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagCertificateAuthority_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_TagCertificateAuthority_RequestSyntax) **   <a name="privateca-TagCertificateAuthority-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html). This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [Tags](#API_TagCertificateAuthority_RequestSyntax) **   <a name="privateca-TagCertificateAuthority-request-Tags"></a>
List of tags to be associated with the CA.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Elements
<a name="API_TagCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** InvalidTagException **
The tag associated with the CA is not valid. The invalid argument is contained in the message field.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

 ** TooManyTagsException **
You can associate up to 50 tags with a private CA. Exception information is contained in the exception message field.
HTTP Status Code: 400

## Examples
<a name="API_TagCertificateAuthority_Examples"></a>

### Example
<a name="API_TagCertificateAuthority_Example_1"></a>

This example illustrates one usage of TagCertificateAuthority.

#### Sample Request
<a name="API_TagCertificateAuthority_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 180
X-Amz-Target: ACMPrivateCA.TagCertificateAuthority
X-Amz-Date: 20180226T170330Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=823508ca59a8620ec0981fada8b14a1b85e1db9938103e1fe2a7c394e70b1d0b

{
"CertificateAuthorityArn": "arn:aws:acm-pca:AWS_Region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012",
"Tags": [{
  "Key": "Bob",
  "Value": "DatabaseAdmin"
}]
}
```

### Example
<a name="API_TagCertificateAuthority_Example_2"></a>

This example illustrates one usage of TagCertificateAuthority.

#### Sample Response
<a name="API_TagCertificateAuthority_Example_2_Response"></a>

```
This function does not return a value.
```

## See Also
<a name="API_TagCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/TagCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/TagCertificateAuthority)
