---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html
---

# ListRegionalBuckets
<a name="API_control_ListRegionalBuckets"></a>

**Note**
This operation is not supported by directory buckets.

Returns a list of all Outposts buckets in an Outpost that are owned by the authenticated sender of the request. For more information, see [Using Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and `x-amz-outpost-id` in your request, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html#API_control_ListRegionalBuckets_Examples) section.

## Request Syntax
<a name="API_control_ListRegionalBuckets_RequestSyntax"></a>

```
GET /v20180820/bucket?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
x-amz-outpost-id: {{OutpostId}}
```

## URI Request Parameters
<a name="API_control_ListRegionalBuckets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_control_ListRegionalBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-request-uri-querystring-MaxResults"></a>

Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListRegionalBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-request-uri-querystring-NextToken"></a>

Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [x-amz-account-id](#API_control_ListRegionalBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-request-header-AccountId"></a>
The AWS account ID of the Outposts bucket.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

 ** [x-amz-outpost-id](#API_control_ListRegionalBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-request-header-OutpostId"></a>
The ID of the AWS Outposts resource.
This ID is required by Amazon S3 on Outposts buckets.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_control_ListRegionalBuckets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListRegionalBuckets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListRegionalBucketsResult>
   <RegionalBucketList>
      <RegionalBucket>
         <Bucket>string</Bucket>
         <BucketArn>string</BucketArn>
         <CreationDate>timestamp</CreationDate>
         <OutpostId>string</OutpostId>
         <PublicAccessBlockEnabled>boolean</PublicAccessBlockEnabled>
      </RegionalBucket>
   </RegionalBucketList>
   <NextToken>string</NextToken>
</ListRegionalBucketsResult>
```

## Response Elements
<a name="API_control_ListRegionalBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListRegionalBucketsResult](#API_control_ListRegionalBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-response-ListRegionalBucketsResult"></a>
Root level tag for the ListRegionalBucketsResult parameters.
Required: Yes

 ** [NextToken](#API_control_ListRegionalBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-response-NextToken"></a>
 `NextToken` is sent when `isTruncated` is true, which means there are more buckets that can be listed. The next list requests to Amazon S3 can be continued with this `NextToken`. `NextToken` is obfuscated and is not a real key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [RegionalBucketList](#API_control_ListRegionalBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListRegionalBuckets-response-RegionalBucketList"></a>

Type: Array of [RegionalBucket](API_control_RegionalBucket.md) data types

## Examples
<a name="API_control_ListRegionalBuckets_Examples"></a>

### Sample request to list an account's Outposts buckets
<a name="API_control_ListRegionalBuckets_Example_1"></a>

This request lists regional buckets.

```
            GET /v20180820/bucket HTTP /1.1
            Host:s3-outposts.us-west-2.amazonaws.com
            Content-Length: 0
            x-amz-outpost-id: op-01ac5d28a6a232904
            x-amz-account-id: example-account-id
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Authorization: authorization string
```

## See Also
<a name="API_control_ListRegionalBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListRegionalBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListRegionalBuckets)
