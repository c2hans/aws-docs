---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html
---

# UpdateBucketMetadataInventoryTableConfiguration
<a name="API_UpdateBucketMetadataInventoryTableConfiguration"></a>

Enables or disables a live inventory table for an S3 Metadata configuration on a general purpose bucket. For more information, see [Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
To use this operation, you must have the following permissions. For more information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.
If you want to encrypt your inventory table with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see [ Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.
+  `s3:UpdateBucketMetadataInventoryTableConfiguration`
+  `s3tables:CreateTableBucket`
+  `s3tables:CreateNamespace`
+  `s3tables:GetTable`
+  `s3tables:CreateTable`
+  `s3tables:PutTablePolicy`
+  `s3tables:PutTableEncryption`
+  `kms:DescribeKey`

The following operations are related to `UpdateBucketMetadataInventoryTableConfiguration`:
+  [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
+  [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
+  [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)
+  [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax"></a>

```
PUT /?metadataInventoryTable HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<InventoryTableConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <ConfigurationState>{{string}}</ConfigurationState>
   <EncryptionConfiguration>
      <KmsKeyArn>{{string}}</KmsKeyArn>
      <SseAlgorithm>{{string}}</SseAlgorithm>
   </EncryptionConfiguration>
</InventoryTableConfiguration>
```

## URI Request Parameters
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-header-Bucket"></a>
 The general purpose bucket that corresponds to the metadata configuration that you want to enable or disable an inventory table for.
Required: Yes

 ** [Content-MD5](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-header-ContentMD5"></a>
 The `Content-MD5` header for the inventory table configuration.

 ** [x-amz-expected-bucket-owner](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-header-ExpectedBucketOwner"></a>
 The expected owner of the general purpose bucket that corresponds to the metadata table configuration that you want to enable or disable an inventory table for.

 ** [x-amz-sdk-checksum-algorithm](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-header-ChecksumAlgorithm"></a>
 The checksum algorithm to use with your inventory table configuration.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [InventoryTableConfiguration](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-InventoryTableConfiguration"></a>
Root level tag for the InventoryTableConfiguration parameters.
Required: Yes

 ** [ConfigurationState](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-ConfigurationState"></a>
 The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [EncryptionConfiguration](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-EncryptionConfiguration"></a>
 The encryption configuration for the inventory table.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

## Response Syntax
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_UpdateBucketMetadataInventoryTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
