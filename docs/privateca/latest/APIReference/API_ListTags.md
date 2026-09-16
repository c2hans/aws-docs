---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html
---

# ListTags
<a name="API_ListTags"></a>

Lists the tags, if any, that are associated with your private CA or one that has been shared with you. Tags are labels that you can use to identify and organize your CAs. Each tag consists of a key and an optional value. Call the [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) action to add one or more tags to your CA. Call the [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html) action to remove tags.

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_ListTags_RequestSyntax) **   <a name="privateca-ListTags-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) that was returned when you called the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action. This must be of the form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [MaxResults](#API_ListTags_RequestSyntax) **   <a name="privateca-ListTags-request-MaxResults"></a>
Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the **NextToken** element is sent in the response. Use this **NextToken** value in a subsequent request to retrieve additional items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListTags_RequestSyntax) **   <a name="privateca-ListTags-request-NextToken"></a>
Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of **NextToken** from the response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.
Required: No

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTags_ResponseSyntax) **   <a name="privateca-ListTags-response-NextToken"></a>
When the list is truncated, this value is present and should be used for the **NextToken** parameter in a subsequent pagination request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.

 ** [Tags](#API_ListTags_ResponseSyntax) **   <a name="privateca-ListTags-response-Tags"></a>
The tags associated with your private CA.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_ListTags_Examples"></a>

### Example
<a name="API_ListTags_Example_1"></a>

This example illustrates one usage of ListTags.

#### Sample Request
<a name="API_ListTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm-pca.amazonaws.com
Accept-Encoding: identity
Content-Length: 146
X-Amz-Target: ACMPrivateCA.ListTags
X-Amz-Date: 20180226T164656Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=Access_Key_ID/20180226/AWS_Region/acm-pca/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=59cc6594a1df0f441bd39e466755465e52545f57faa8329d907c715bc8a5f97b

{
"MaxResults": 10,
"CertificateAuthorityArn": "arn:aws:acm-pca:region:AWS_Account:certificate-authority/12345678-1234-1234-1234-123456789012"
}
```

### Example
<a name="API_ListTags_Example_2"></a>

This example illustrates one usage of ListTags.

#### Sample Response
<a name="API_ListTags_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 May 2018 18:25:09 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 69
x-amzn-RequestId: 9893f3cb-1bd8-4a15-8394-4f5364963acf
Connection: keep-alive

  "Tags": [{
    "Key": "Admin",
    "Value": "Alice"
  },
  {
    "Key": "Purpose",
    "Value": "Website"
  }]
}
```

## See Also
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/ListTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ListTags)
