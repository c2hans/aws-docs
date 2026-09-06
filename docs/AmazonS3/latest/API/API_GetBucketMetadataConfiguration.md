---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html
---

# GetBucketMetadataConfiguration
<a name="API_GetBucketMetadataConfiguration"></a>

Retrieves the S3 Metadata configuration for a general purpose bucket. For more information, see [Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

**Note**
You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 metadata configurations. However, if you try to use the V1 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you will receive an HTTP `405 Method Not Allowed` error.

Permissions
To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration` permission. For more information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.
The IAM policy action name is the same for the V1 and V2 API operations.

The following operations are related to `GetBucketMetadataConfiguration`:
+  [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
+  [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
+  [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)
+  [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketMetadataConfiguration_RequestSyntax"></a>

```
GET /?metadataConfiguration HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketMetadataConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketMetadataConfiguration-request-header-Bucket"></a>
 The general purpose bucket that corresponds to the metadata configuration that you want to retrieve.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketMetadataConfiguration-request-header-ExpectedBucketOwner"></a>
 The expected owner of the general purpose bucket that you want to retrieve the metadata table configuration for.

## Request Body
<a name="API_GetBucketMetadataConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketMetadataConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetBucketMetadataConfigurationResult>
   <MetadataConfigurationResult>
      <AnnotationTableConfigurationResult>
         <ConfigurationState>string</ConfigurationState>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <Role>string</Role>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </AnnotationTableConfigurationResult>
      <DestinationResult>
         <TableBucketArn>string</TableBucketArn>
         <TableBucketType>string</TableBucketType>
         <TableNamespace>string</TableNamespace>
      </DestinationResult>
      <InventoryTableConfigurationResult>
         <ConfigurationState>string</ConfigurationState>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </InventoryTableConfigurationResult>
      <JournalTableConfigurationResult>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <RecordExpiration>
            <Days>integer</Days>
            <Expiration>string</Expiration>
         </RecordExpiration>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </JournalTableConfigurationResult>
   </MetadataConfigurationResult>
</GetBucketMetadataConfigurationResult>
```

## Response Elements
<a name="API_GetBucketMetadataConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetBucketMetadataConfigurationResult](#API_GetBucketMetadataConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataConfiguration-response-GetBucketMetadataConfigurationResult"></a>
Root level tag for the GetBucketMetadataConfigurationResult parameters.
Required: Yes

 ** [MetadataConfigurationResult](#API_GetBucketMetadataConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataConfiguration-response-MetadataConfigurationResult"></a>
 The metadata configuration for a general purpose bucket.
Type: [MetadataConfigurationResult](API_MetadataConfigurationResult.md) data type

## See Also
<a name="API_GetBucketMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataConfiguration)
