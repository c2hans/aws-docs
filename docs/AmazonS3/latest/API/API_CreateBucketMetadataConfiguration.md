---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html
---

# CreateBucketMetadataConfiguration
<a name="API_CreateBucketMetadataConfiguration"></a>

Creates an S3 Metadata V2 metadata configuration for a general purpose bucket. For more information, see [Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
To use this operation, you must have the following permissions. For more information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.
If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see [ Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.
If you also want to integrate your table bucket with AWS analytics services so that you can query your metadata table, you need additional permissions. For more information, see [ Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) in the *Amazon S3 User Guide*.
To query your metadata tables, you need additional permissions. For more information, see [ Permissions for querying metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-query-permissions.html) in the *Amazon S3 User Guide*.
+  `s3:CreateBucketMetadataTableConfiguration`
**Note**
The IAM policy action name is the same for the V1 and V2 API operations.
+  `s3tables:CreateTableBucket`
+  `s3tables:CreateNamespace`
+  `s3tables:GetTable`
+  `s3tables:CreateTable`
+  `s3tables:PutTablePolicy`
+  `s3tables:PutTableBucketPolicy`
+  `s3tables:PutTableEncryption`
+  `kms:DescribeKey`
+  `iam:PassRole` - required if you include an `AnnotationTableConfiguration` with an IAM role.

The following operations are related to `CreateBucketMetadataConfiguration`:
+  [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
+  [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)
+  [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)
+  [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)
+  [UpdateBucketMetadataAnnotationTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html)

If you include an `AnnotationTableConfiguration` with an IAM role, the role must have a trust policy that allows the Amazon S3 metadata service to assume it, and a permissions policy that grants the actions needed to read annotations from your bucket. The following examples show a trust policy and a permissions policy that you can adapt for your bucket and account.

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_CreateBucketMetadataConfiguration_RequestSyntax"></a>

```
POST /?metadataConfiguration HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<MetadataConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <JournalTableConfiguration>
      <EncryptionConfiguration>
         <KmsKeyArn>{{string}}</KmsKeyArn>
         <SseAlgorithm>{{string}}</SseAlgorithm>
      </EncryptionConfiguration>
      <RecordExpiration>
         <Days>{{integer}}</Days>
         <Expiration>{{string}}</Expiration>
      </RecordExpiration>
   </JournalTableConfiguration>
   <InventoryTableConfiguration>
      <ConfigurationState>{{string}}</ConfigurationState>
      <EncryptionConfiguration>
         <KmsKeyArn>{{string}}</KmsKeyArn>
         <SseAlgorithm>{{string}}</SseAlgorithm>
      </EncryptionConfiguration>
   </InventoryTableConfiguration>
   <AnnotationTableConfiguration>
      <ConfigurationState>{{string}}</ConfigurationState>
      <EncryptionConfiguration>
         <KmsKeyArn>{{string}}</KmsKeyArn>
         <SseAlgorithm>{{string}}</SseAlgorithm>
      </EncryptionConfiguration>
      <Role>{{string}}</Role>
   </AnnotationTableConfiguration>
</MetadataConfiguration>
```

## URI Request Parameters
<a name="API_CreateBucketMetadataConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-header-Bucket"></a>
 The general purpose bucket that you want to create the metadata configuration for.
Required: Yes

 ** [Content-MD5](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-header-ContentMD5"></a>
 The `Content-MD5` header for the metadata configuration.

 ** [x-amz-expected-bucket-owner](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-header-ExpectedBucketOwner"></a>
 The expected owner of the general purpose bucket that corresponds to your metadata configuration.

 ** [x-amz-sdk-checksum-algorithm](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-header-ChecksumAlgorithm"></a>
 The checksum algorithm to use with your metadata configuration.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_CreateBucketMetadataConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [MetadataConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-MetadataConfiguration"></a>
Root level tag for the MetadataConfiguration parameters.
Required: Yes

 ** [AnnotationTableConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-AnnotationTableConfiguration"></a>
Optional annotation table configuration to include with the metadata configuration.
Type: [AnnotationTableConfiguration](API_AnnotationTableConfiguration.md) data type
Required: No

 ** [InventoryTableConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-InventoryTableConfiguration"></a>
 The inventory table configuration for a metadata configuration.
Type: [InventoryTableConfiguration](API_InventoryTableConfiguration.md) data type
Required: No

 ** [JournalTableConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-CreateBucketMetadataConfiguration-request-JournalTableConfiguration"></a>
 The journal table configuration for a metadata configuration.
Type: [JournalTableConfiguration](API_JournalTableConfiguration.md) data type
Required: Yes

## Response Syntax
<a name="API_CreateBucketMetadataConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateBucketMetadataConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_CreateBucketMetadataConfiguration_Examples"></a>

### Trust policy
<a name="API_CreateBucketMetadataConfiguration_Example_1"></a>

This example illustrates one usage of CreateBucketMetadataConfiguration.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "metadata.s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
                }
            }
        }
    ]
}
```

### Permissions policy
<a name="API_CreateBucketMetadataConfiguration_Example_2"></a>

This example illustrates one usage of CreateBucketMetadataConfiguration.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PermissionForGetAnnotation",
      "Effect": "Allow",
      "Action": [
        "s3:GetObjectAnnotation",
        "s3:GetObjectVersionAnnotation"
      ],
      "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket/*"],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{Account}}"
        }
      }
    },
    {
      "Sid": "PermissionsForListBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:ListBucketVersions"
      ],
      "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket"],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{Account}}"
        }
      }
    },
    {
      "Sid": "PermissionsForDecryptAnnotation",
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Condition": {
        "StringLike": {
          "kms:ViaService": [
            "s3.{{Region}}.amazonaws.com"
          ]
        },
        "ArnLike": {
          "kms:EncryptionContext:aws:s3:arn": [
            "arn:aws:s3:::{{BucketName}}",
            "arn:aws:s3:::{{BucketName}}/*"
          ]
        }
      },
      "Resource": ["arn:aws:kms:{{Region}}:{{Account}}:key/{{KmsKeyId}}"]
    }
  ]
}
```

## See Also
<a name="API_CreateBucketMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateBucketMetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketMetadataConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
