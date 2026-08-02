---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html
---

# GetBucketIntelligentTieringConfiguration
<a name="API_GetBucketIntelligentTieringConfiguration"></a>

**Note**
This operation is not supported for directory buckets.

Gets the S3 Intelligent-Tiering configuration from the specified bucket.

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective storage access tier, without performance impact or operational overhead. S3 Intelligent-Tiering delivers automatic cost savings in three low latency and high throughput access tiers. To get the lowest storage cost on data that can be accessed in minutes to hours, you can choose to activate additional archiving capabilities.

The S3 Intelligent-Tiering storage class is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. If the size of an object is less than 128 KB, it is not monitored and not eligible for auto-tiering. Smaller objects can be stored, but they are always charged at the Frequent Access tier rates in the S3 Intelligent-Tiering storage class.

For more information, see [Storage class for automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

Operations related to `GetBucketIntelligentTieringConfiguration` include:
+  [DeleteBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html)
+  [PutBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)
+  [ListBucketIntelligentTieringConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketIntelligentTieringConfiguration_RequestSyntax"></a>

```
GET /?intelligent-tiering&id={{Id}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketIntelligentTieringConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketIntelligentTieringConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-request-header-Bucket"></a>
The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.
Required: Yes

 ** [id](#API_GetBucketIntelligentTieringConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-request-uri-querystring-Id"></a>
The ID used to identify the S3 Intelligent-Tiering configuration.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketIntelligentTieringConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketIntelligentTieringConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketIntelligentTieringConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<IntelligentTieringConfiguration>
   <Id>string</Id>
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
   <Status>string</Status>
   <Tiering>
      <AccessTier>string</AccessTier>
      <Days>integer</Days>
   </Tiering>
   ...
</IntelligentTieringConfiguration>
```

## Response Elements
<a name="API_GetBucketIntelligentTieringConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [IntelligentTieringConfiguration](#API_GetBucketIntelligentTieringConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-response-IntelligentTieringConfiguration"></a>
Root level tag for the IntelligentTieringConfiguration parameters.
Required: Yes

 ** [Filter](#API_GetBucketIntelligentTieringConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-response-Filter"></a>
Specifies a bucket filter. The configuration only includes objects that meet the filter's criteria.
Type: [IntelligentTieringFilter](API_IntelligentTieringFilter.md) data type

 ** [Id](#API_GetBucketIntelligentTieringConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-response-Id"></a>
The ID used to identify the S3 Intelligent-Tiering configuration.
Type: String

 ** [Status](#API_GetBucketIntelligentTieringConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-response-Status"></a>
Specifies the status of the configuration.
Type: String
Valid Values: `Enabled | Disabled`

 ** [Tiering](#API_GetBucketIntelligentTieringConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketIntelligentTieringConfiguration-response-Tierings"></a>
Specifies the S3 Intelligent-Tiering storage class tier of the configuration.
Type: Array of [Tiering](API_Tiering.md) data types

## See Also
<a name="API_GetBucketIntelligentTieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketIntelligentTieringConfiguration)
