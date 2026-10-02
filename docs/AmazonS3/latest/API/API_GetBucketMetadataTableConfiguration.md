---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html
---

# GetBucketMetadataTableConfiguration
<a name="API_GetBucketMetadataTableConfiguration"></a>

**Important**
 We recommend that you retrieve your S3 Metadata configurations by using the V2 [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html) API operation. We no longer recommend using the V1 `GetBucketMetadataTableConfiguration` API operation.
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create a live inventory table.

 Retrieves the V1 S3 Metadata configuration for a general purpose bucket. For more information, see [Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

**Note**
You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 metadata table configurations. However, if you try to use the V1 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you will receive an HTTP `405 Method Not Allowed` error.
Make sure that you update your processes to use the new V2 API operations (`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`, and `DeleteBucketMetadataConfiguration`) instead of the V1 API operations.

Permissions
To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration` permission. For more information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.

The following operations are related to `GetBucketMetadataTableConfiguration`:
+  [CreateBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html)
+  [DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketMetadataTableConfiguration_RequestSyntax"></a>

```
GET /?metadataTable HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketMetadataTableConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketMetadataTableConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-request-header-Bucket"></a>
 The general purpose bucket that corresponds to the metadata table configuration that you want to retrieve.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketMetadataTableConfiguration_RequestSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-request-header-ExpectedBucketOwner"></a>
 The expected owner of the general purpose bucket that you want to retrieve the metadata table configuration for.

## Request Body
<a name="API_GetBucketMetadataTableConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketMetadataTableConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetBucketMetadataTableConfigurationResult>
   <MetadataTableConfigurationResult>
      <S3TablesDestinationResult>
         <TableArn>string</TableArn>
         <TableBucketArn>string</TableBucketArn>
         <TableName>string</TableName>
         <TableNamespace>string</TableNamespace>
      </S3TablesDestinationResult>
   </MetadataTableConfigurationResult>
   <Status>string</Status>
   <Error>
      <ErrorCode>string</ErrorCode>
      <ErrorMessage>string</ErrorMessage>
   </Error>
</GetBucketMetadataTableConfigurationResult>
```

## Response Elements
<a name="API_GetBucketMetadataTableConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetBucketMetadataTableConfigurationResult](#API_GetBucketMetadataTableConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-response-GetBucketMetadataTableConfigurationResult"></a>
Root level tag for the GetBucketMetadataTableConfigurationResult parameters.
Required: Yes

 ** [Error](#API_GetBucketMetadataTableConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-response-Error"></a>
 If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.
Type: [ErrorDetails](API_ErrorDetails.md) data type

 ** [MetadataTableConfigurationResult](#API_GetBucketMetadataTableConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-response-MetadataTableConfigurationResult"></a>
 The V1 S3 Metadata configuration for a general purpose bucket.
Type: [MetadataTableConfigurationResult](API_MetadataTableConfigurationResult.md) data type

 ** [Status](#API_GetBucketMetadataTableConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetBucketMetadataTableConfiguration-response-Status"></a>
 The status of the metadata table. The status values are:
+  `CREATING` - The metadata table is in the process of being created in the specified table bucket.
+  `ACTIVE` - The metadata table has been created successfully, and records are being delivered to the table.
+  `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver records. See `ErrorDetails` for details.
Type: String

## See Also
<a name="API_GetBucketMetadataTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfiguration)
