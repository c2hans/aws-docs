---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html
---

# ListResourceTags
<a name="API_ListResourceTags"></a>

Returns all tags on the specified KMS key.

For general information about tags, including the format and syntax, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*. For information about using tags in AWS KMS, see [Tags in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html).

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:ListResourceTags](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [CreateKey](API_CreateKey.md)
+  [ReplicateKey](API_ReplicateKey.md)
+  [TagResource](API_TagResource.md)
+  [UntagResource](API_UntagResource.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ListResourceTags_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_ListResourceTags_RequestSyntax) **   <a name="KMS-ListResourceTags-request-KeyId"></a>
Gets tags on the specified KMS key.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Limit](#API_ListResourceTags_RequestSyntax) **   <a name="KMS-ListResourceTags-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 50, inclusive. If you do not include a value, it defaults to 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [Marker](#API_ListResourceTags_RequestSyntax) **   <a name="KMS-ListResourceTags-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Do not attempt to construct this value. Use only the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_ListResourceTags_ResponseSyntax"></a>

```
{
   "NextMarker": "string",
   "Tags": [
      {
         "TagKey": "string",
         "TagValue": "string"
      }
   ],
   "Truncated": boolean
}
```

## Response Elements
<a name="API_ListResourceTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextMarker](#API_ListResourceTags_ResponseSyntax) **   <a name="KMS-ListResourceTags-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Do not assume or infer any information from this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Tags](#API_ListResourceTags_ResponseSyntax) **   <a name="KMS-ListResourceTags-response-Tags"></a>
A list of tags. Each tag consists of a tag key and a tag value.
Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects

 ** [Truncated](#API_ListResourceTags_ResponseSyntax) **   <a name="KMS-ListResourceTags-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListResourceTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_ListResourceTags_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListResourceTags_Example_1"></a>

This example illustrates one usage of ListResourceTags.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 49
X-Amz-Target: TrentService.ListResourceTags
X-Amz-Date: 20170109T200421Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20170109/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=17706fce40fda00c6768b3297355c353490c1dfdf3b3a9591193612961cd2cb4

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_ListResourceTags_Example_2"></a>

This example illustrates one usage of ListResourceTags.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 09 Jan 2017 20:04:22 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 158
Connection: keep-alive
x-amzn-RequestId: cfb46544-d6a6-11e6-a164-b5365990e84e

{
  "Tags": [{
    "TagKey": "CostCenter",
    "TagValue": "87654"
  }, {
    "TagKey": "CreatedBy",
    "TagValue": "ExampleUser"
  }, {
    "TagKey": "Purpose",
    "TagValue": "Test"
  }],
  "Truncated": false
}
```

## See Also
<a name="API_ListResourceTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListResourceTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListResourceTags)
