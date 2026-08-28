---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html
---

# PutBucketTagging
<a name="API_PutBucketTagging"></a>

**Note**
This operation is not supported for directory buckets.

Sets the tags for a general purpose bucket if attribute based access control (ABAC) is not enabled for the bucket. When you [enable ABAC for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html), you can no longer use this operation for that bucket and must use the [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) operations instead.

Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see [Cost Allocation and Tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) and [Using Cost Allocation in Amazon S3 Bucket Tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html).

**Note**
 When this operation sets the tags for a bucket, it will overwrite any current tags the bucket already has. You cannot use this operation to add tags to an existing list of tags.

To use this operation, you must have permissions to perform the `s3:PutBucketTagging` action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

 `PutBucketTagging` has the following special errors. For more Amazon S3 errors see, [Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).
+  `InvalidTag` - The tag provided was not a valid tag. This error can occur if the tag did not pass input validation. For more information, see [Using Cost Allocation in Amazon S3 Bucket Tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html).
+  `MalformedXML` - The XML provided does not match the schema.
+  `OperationAborted` - A conflicting conditional action is currently in progress against this resource. Please try again.
+  `InternalError` - The service was unable to apply the provided tag to the bucket.

The following operations are related to `PutBucketTagging`:
+  [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)
+  [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_PutBucketTagging_RequestSyntax"></a>

```
PUT /?tagging HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <TagSet>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </TagSet>
</Tagging>
```

## URI Request Parameters
<a name="API_PutBucketTagging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-header-Bucket"></a>
The bucket name.
Required: Yes

 ** [Content-MD5](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-header-ContentMD5"></a>
The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a message integrity check to verify that the request body was not corrupted in transit. For more information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt).
For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [x-amz-expected-bucket-owner](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-sdk-checksum-algorithm](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-header-ChecksumAlgorithm"></a>
Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutBucketTagging_RequestBody"></a>

The request accepts the following data in XML format.

 ** [Tagging](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-Tagging"></a>
Root level tag for the Tagging parameters.
Required: Yes

 ** [TagSet](#API_PutBucketTagging_RequestSyntax) **   <a name="AmazonS3-PutBucketTagging-request-TagSet"></a>
A collection for a set of tags
Type: Array of [Tag](API_Tag.md) data types
Required: Yes

## Response Syntax
<a name="API_PutBucketTagging_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutBucketTagging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_PutBucketTagging_Examples"></a>

### Sample Request: Add tag set to a bucket
<a name="API_PutBucketTagging_Example_1"></a>

The following request adds a tag set to the existing `examplebucket` bucket.

```
PUT ?tagging HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Content-Length: 1660
x-amz-date: Thu, 12 Apr 2012 20:04:21 GMT
Authorization: authorization string

<Tagging>
  <TagSet>
    <Tag>
      <Key>Project</Key>
      <Value>Project One</Value>
    </Tag>
    <Tag>
      <Key>User</Key>
      <Value>jsmith</Value>
    </Tag>
  </TagSet>
</Tagging>
```

### Sample Response
<a name="API_PutBucketTagging_Example_2"></a>

This example illustrates one usage of PutBucketTagging.

```
HTTP/1.1 204 No Content
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Oct  2012 12:00:00 GMT
```

## See Also
<a name="API_PutBucketTagging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketTagging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketTagging)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
