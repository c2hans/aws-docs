---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html
---

# ListBucketIntelligentTieringConfigurations
<a name="API_ListBucketIntelligentTieringConfigurations"></a>

**Note**
This operation is not supported for directory buckets.

Lists the S3 Intelligent-Tiering configuration from the specified bucket.

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective storage access tier, without performance impact or operational overhead. S3 Intelligent-Tiering delivers automatic cost savings in three low latency and high throughput access tiers. To get the lowest storage cost on data that can be accessed in minutes to hours, you can choose to activate additional archiving capabilities.

The S3 Intelligent-Tiering storage class is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. If the size of an object is less than 128 KB, it is not monitored and not eligible for auto-tiering. Smaller objects can be stored, but they are always charged at the Frequent Access tier rates in the S3 Intelligent-Tiering storage class.

For more information, see [Storage class for automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

Operations related to `ListBucketIntelligentTieringConfigurations` include:
+  [DeleteBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html)
+  [PutBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)
+  [GetBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_ListBucketIntelligentTieringConfigurations_RequestSyntax"></a>

```
GET /?intelligent-tiering&continuation-token={{ContinuationToken}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_ListBucketIntelligentTieringConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_ListBucketIntelligentTieringConfigurations_RequestSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-request-header-Bucket"></a>
The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.
Required: Yes

 ** [continuation-token](#API_ListBucketIntelligentTieringConfigurations_RequestSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-request-uri-querystring-ContinuationToken"></a>
The `ContinuationToken` that represents a placeholder from where this request should begin.

 ** [x-amz-expected-bucket-owner](#API_ListBucketIntelligentTieringConfigurations_RequestSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_ListBucketIntelligentTieringConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBucketIntelligentTieringConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketIntelligentTieringConfigurationsOutput>
   <IsTruncated>boolean</IsTruncated>
   <ContinuationToken>string</ContinuationToken>
   <NextContinuationToken>string</NextContinuationToken>
   <IntelligentTieringConfiguration>
      <Filter>
         <And>
            <Prefix>string</Prefix>
            <Tag>
               <Key>string</Key>
               <Value>string</Value>
            </Tag>
            ...
         </And>
         <Prefix>string</Prefix>
         <Tag>
            <Key>string</Key>
            <Value>string</Value>
         </Tag>
      </Filter>
      <Id>string</Id>
      <Status>string</Status>
      <Tiering>
         <AccessTier>string</AccessTier>
         <Days>integer</Days>
      </Tiering>
      ...
   </IntelligentTieringConfiguration>
   ...
</ListBucketIntelligentTieringConfigurationsOutput>
```

## Response Elements
<a name="API_ListBucketIntelligentTieringConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListBucketIntelligentTieringConfigurationsOutput](#API_ListBucketIntelligentTieringConfigurations_ResponseSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-response-ListBucketIntelligentTieringConfigurationsOutput"></a>
Root level tag for the ListBucketIntelligentTieringConfigurationsOutput parameters.
Required: Yes

 ** [ContinuationToken](#API_ListBucketIntelligentTieringConfigurations_ResponseSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-response-ContinuationToken"></a>
The `ContinuationToken` that represents a placeholder from where this request should begin.
Type: String

 ** [IntelligentTieringConfiguration](#API_ListBucketIntelligentTieringConfigurations_ResponseSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-response-IntelligentTieringConfigurationList"></a>
The list of S3 Intelligent-Tiering configurations for a bucket.
Type: Array of [IntelligentTieringConfiguration](API_IntelligentTieringConfiguration.md) data types

 ** [IsTruncated](#API_ListBucketIntelligentTieringConfigurations_ResponseSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-response-IsTruncated"></a>
Indicates whether the returned list of analytics configurations is complete. A value of `true` indicates that the list is not complete and the `NextContinuationToken` will be provided for a subsequent request.
Type: Boolean

 ** [NextContinuationToken](#API_ListBucketIntelligentTieringConfigurations_ResponseSyntax) **   <a name="AmazonS3-ListBucketIntelligentTieringConfigurations-response-NextContinuationToken"></a>
The marker used to continue this inventory configuration listing. Use the `NextContinuationToken` from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.
Type: String

## See Also
<a name="API_ListBucketIntelligentTieringConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBucketIntelligentTieringConfigurations)
