---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html
---

# PutObjectTagging
<a name="API_PutObjectTagging"></a>

**Note**
This operation is not supported for directory buckets.

Sets the supplied tag-set to an object that already exists in a bucket. A tag is a key-value pair. For more information, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html).

You can associate tags with an object by sending a PUT request against the tagging subresource that is associated with the object. You can retrieve tags by sending a GET request. For more information, see [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html).

For tagging-related restrictions related to characters and encodings, see [Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html). Note that Amazon S3 limits the maximum number of tags to 10 tags per object.

To use this operation, you must have permission to perform the `s3:PutObjectTagging` action. By default, the bucket owner has this permission and can grant this permission to others.

To put tags of any other version, use the `versionId` query parameter. You also need permission for the `s3:PutObjectVersionTagging` action.

 `PutObjectTagging` has the following special errors. For more Amazon S3 errors see, [Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).
+  `InvalidTag` - The tag provided was not a valid tag. This error can occur if the tag did not pass input validation. For more information, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html).
+  `MalformedXML` - The XML provided does not match the schema.
+  `OperationAborted` - A conflicting conditional action is currently in progress against this resource. Please try again.
+  `InternalError` - The service was unable to apply the provided tag to the object.

The following operations are related to `PutObjectTagging`:
+  [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)
+  [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_PutObjectTagging_RequestSyntax"></a>

```
PUT /{Key+}?tagging&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
x-amz-request-payer: {{RequestPayer}}
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
<a name="API_PutObjectTagging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-header-Bucket"></a>
The bucket name containing the object.
 **Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.
 **S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form ` AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [Content-MD5](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-header-ContentMD5"></a>
The MD5 hash for the request body.
For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [Key](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-uri-uri-Key"></a>
Name of the object key.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-uri-querystring-VersionId"></a>
The versionId of the object that the tag-set will be added to.

 ** [x-amz-expected-bucket-owner](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-request-payer](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-header-RequestPayer"></a>
Confirms that the requester knows that she or he will be charged for the tagging object request. Bucket owners need not specify this parameter in their requests.
Valid Values: `requester`

 ** [x-amz-sdk-checksum-algorithm](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-header-ChecksumAlgorithm"></a>
Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutObjectTagging_RequestBody"></a>

The request accepts the following data in XML format.

 ** [Tagging](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-Tagging"></a>
Root level tag for the Tagging parameters.
Required: Yes

 ** [TagSet](#API_PutObjectTagging_RequestSyntax) **   <a name="AmazonS3-PutObjectTagging-request-TagSet"></a>
A collection for a set of tags
Type: Array of [Tag](API_Tag.md) data types
Required: Yes

## Response Syntax
<a name="API_PutObjectTagging_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-version-id: {{VersionId}}
```

## Response Elements
<a name="API_PutObjectTagging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [x-amz-version-id](#API_PutObjectTagging_ResponseSyntax) **   <a name="AmazonS3-PutObjectTagging-response-header-VersionId"></a>
The versionId of the object the tag-set was added to.

## Examples
<a name="API_PutObjectTagging_Examples"></a>

### Sample Request: Add tag set to an object
<a name="API_PutObjectTagging_Example_1"></a>

The following request adds a tag set to the existing object object-key in the `examplebucket` bucket.

```
PUT object-key?tagging HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Content-Length: length
Content-MD5: pUNXr/BjKK5G2UKExample==
x-amz-date: 20160923T001956Z
Authorization: authorization string
<Tagging>
   <TagSet>
      <Tag>
         <Key>tag1</Key>
         <Value>val1</Value>
      </Tag>
      <Tag>
         <Key>tag2</Key>
         <Value>val2</Value>
      </Tag>
   </TagSet>
</Tagging>
```

### Sample Response
<a name="API_PutObjectTagging_Example_2"></a>

This example illustrates one usage of PutObjectTagging.

```
HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Fri, 23 Sep 2016 00:20:19 GMT
```

## See Also
<a name="API_PutObjectTagging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectTagging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectTagging)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
