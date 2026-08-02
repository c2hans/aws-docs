---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagServerCertificate.html
---

# UntagServerCertificate
<a name="API_UntagServerCertificate"></a>

Removes the specified tags from the IAM server certificate. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

**Note**
For certificates in a Region supported by AWS Certificate Manager (ACM), we recommend that you don't use IAM server certificates. Instead, use ACM to provision, manage, and deploy your server certificates. For more information about IAM server certificates, [Working with server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_UntagServerCertificate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServerCertificateName **
The name of the IAM server certificate from which you want to remove tags.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 **TagKeys.member.N**
A list of key names as a simple array of strings. The tags with matching keys are removed from the specified IAM server certificate.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
Required: Yes

## Errors
<a name="API_UntagServerCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_UntagServerCertificate_Examples"></a>

### Example
<a name="API_UntagServerCertificate_Example_1"></a>

The following example is formatted with line breaks for legibility.

The following example shows how to remove tags that are attached to a server certificate whose name is `ExampleServerCert`.

#### Sample Request
<a name="API_UntagServerCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: https://iam.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.11.143 Python/3.6.1 Linux/3.2.45-0.6.wd.865.49.315.metal1.x86_64 botocore/1.7.1
X-Amz-Date: 20170929T183048Z
Authorization: <auth details>
Content-Length: 74
Content-Type: application/x-www-form-urlencoded

Action=UntagServerCertificate&Version=2010-05-08&ServerCertificateName=ExampleServerCert
       &TagKeys.member.1=Dept
```

#### Sample Response
<a name="API_UntagServerCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE
Content-Type: text/xml
Content-Length: 198
Date: Fri, 29 Sep 2017 18:30:47 GMT

<UntagServerCertificateResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</UntagServerCertificateResponse>
```

## See Also
<a name="API_UntagServerCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UntagServerCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UntagServerCertificate)
