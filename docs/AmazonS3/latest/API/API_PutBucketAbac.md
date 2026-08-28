---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAbac.html
---

# PutBucketAbac
<a name="API_PutBucketAbac"></a>

Sets the attribute-based access control (ABAC) property of the general purpose bucket. You must have `s3:PutBucketABAC` permission to perform this action. When you enable ABAC, you can use tags for access control on your buckets. Additionally, when ABAC is enabled, you must use the [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) actions to manage tags on your buckets. You can nolonger use the [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html) and [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html) actions to tag your bucket. For more information, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

## Request Syntax
<a name="API_PutBucketAbac_RequestSyntax"></a>

```
PUT /?abac HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<AbacStatus xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Status>{{string}}</Status>
</AbacStatus>
```

## URI Request Parameters
<a name="API_PutBucketAbac_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-header-Bucket"></a>
The name of the general purpose bucket.
Required: Yes

 ** [Content-MD5](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-header-ContentMD5"></a>
The MD5 hash of the `PutBucketAbac` request body.
For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [x-amz-expected-bucket-owner](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-header-ExpectedBucketOwner"></a>
The AWS account ID of the general purpose bucket's owner.

 ** [x-amz-sdk-checksum-algorithm](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-header-ChecksumAlgorithm"></a>
Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see [ Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_PutBucketAbac_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AbacStatus](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-AbacStatus"></a>
Root level tag for the AbacStatus parameters.
Required: Yes

 ** [Status](#API_PutBucketAbac_RequestSyntax) **   <a name="AmazonS3-PutBucketAbac-request-Status"></a>
The ABAC status of the general purpose bucket.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

## Response Syntax
<a name="API_PutBucketAbac_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutBucketAbac_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_PutBucketAbac_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAbac)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAbac)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
