---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html
---

# DeleteBucketTagging
<a name="API_DeleteBucketTagging"></a>

**Note**
This operation is not supported for directory buckets.

Deletes tags from the general purpose bucket if attribute based access control (ABAC) is not enabled for the bucket. When you [enable ABAC for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html), you can no longer use this operation for that bucket and must use [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) instead.

To use this operation, you must have permission to perform the `s3:PutBucketTagging` action. By default, the bucket owner has this permission and can grant this permission to others.

The following operations are related to `DeleteBucketTagging`:
+  [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)
+  [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_DeleteBucketTagging_RequestSyntax"></a>

```
DELETE /?tagging HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_DeleteBucketTagging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_DeleteBucketTagging_RequestSyntax) **   <a name="AmazonS3-DeleteBucketTagging-request-header-Bucket"></a>
The bucket that has the tag set to be removed.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_DeleteBucketTagging_RequestSyntax) **   <a name="AmazonS3-DeleteBucketTagging-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_DeleteBucketTagging_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBucketTagging_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteBucketTagging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Examples
<a name="API_DeleteBucketTagging_Examples"></a>

### Sample Request
<a name="API_DeleteBucketTagging_Example_1"></a>

The following DELETE request deletes the tag set from the specified bucket.

```
            DELETE /?tagging HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 14 Dec 2011 05:37:16 GMT
            Authorization: signatureValue
```

### Sample Response
<a name="API_DeleteBucketTagging_Example_2"></a>

The following successful response shows Amazon S3 returning a `204 No Content` response. The tag set for the bucket has been removed.

```
            HTTP/1.1 204 No Content
            Date: Wed, 25 Nov 2009 12:00:00 GMT
            Connection: close
            Server: AmazonS3
```

## See Also
<a name="API_DeleteBucketTagging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketTagging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketTagging)
