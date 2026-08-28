---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html
---

# ListDirectoryBuckets
<a name="API_ListDirectoryBuckets"></a>

Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request. For more information about directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*.

**Note**
 **Directory buckets ** - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name `. Virtual-hosted-style requests aren't supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide*.

Permissions
You must have the `s3express:ListAllMyDirectoryBuckets` permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource. For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
 **Directory buckets ** - The HTTP Host header syntax is `s3express-control.region.amazonaws.com`.

**Note**
 The `BucketRegion` response element is not part of the `ListDirectoryBuckets` Response Syntax.

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_ListDirectoryBuckets_RequestSyntax"></a>

```
GET /?continuation-token={{ContinuationToken}}&max-directory-buckets={{MaxDirectoryBuckets}} HTTP/1.1
Host: s3.amazonaws.com
```

## URI Request Parameters
<a name="API_ListDirectoryBuckets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [continuation-token](#API_ListDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-ListDirectoryBuckets-request-uri-querystring-ContinuationToken"></a>
 `ContinuationToken` indicates to Amazon S3 that the list is being continued on buckets in this account with a token. `ContinuationToken` is obfuscated and is not a real bucket name. You can use this `ContinuationToken` for the pagination of the list results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [max-directory-buckets](#API_ListDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-ListDirectoryBuckets-request-uri-querystring-MaxDirectoryBuckets"></a>
Maximum number of buckets to be returned in response. When the number is more than the count of buckets that are owned by an AWS account, return all the buckets in response.
Valid Range: Minimum value of 0. Maximum value of 1000.

## Request Body
<a name="API_ListDirectoryBuckets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDirectoryBuckets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyDirectoryBucketsResult>
   <Buckets>
      <Bucket>
         <BucketArn>string</BucketArn>
         <BucketRegion>string</BucketRegion>
         <CreationDate>timestamp</CreationDate>
         <Name>string</Name>
      </Bucket>
   </Buckets>
   <ContinuationToken>string</ContinuationToken>
</ListAllMyDirectoryBucketsResult>
```

## Response Elements
<a name="API_ListDirectoryBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAllMyDirectoryBucketsResult](#API_ListDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-ListDirectoryBuckets-response-ListDirectoryBucketsOutput"></a>
Root level tag for the ListAllMyDirectoryBucketsResult parameters.
Required: Yes

 ** [Buckets](#API_ListDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-ListDirectoryBuckets-response-Buckets"></a>
The list of buckets owned by the requester.
Type: Array of [Bucket](API_Bucket.md) data types

 ** [ContinuationToken](#API_ListDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-ListDirectoryBuckets-response-ContinuationToken"></a>
If `ContinuationToken` was sent with the request, it is included in the response. You can use the returned `ContinuationToken` for pagination of the list response.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## See Also
<a name="API_ListDirectoryBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListDirectoryBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListDirectoryBuckets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
