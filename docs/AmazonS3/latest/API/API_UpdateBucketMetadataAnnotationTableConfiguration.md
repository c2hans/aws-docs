---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html
---

# UpdateBucketMetadataAnnotationTableConfiguration
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration"></a>

Updates the annotation table configuration for an Amazon S3 bucket's metadata configuration. Use this operation to enable or disable the annotation table, or to update its associated IAM role.

An annotation table is a queryable Iceberg table that contains records of all annotations attached to objects in the bucket. To use this operation, the bucket must have an existing Amazon S3 Metadata configuration.

To use this operation, you must have the `s3:UpdateBucketMetadataAnnotationTableConfiguration` permission. If you are specifying or changing the IAM role, you must also have `iam:PassRole` permission for the role.

The IAM role must have a trust policy that allows the Amazon S3 metadata service to assume it, and a permissions policy that grants the actions needed to read annotations from your bucket. The following examples show a trust policy and a permissions policy that you can adapt for your bucket and account.

The following operations are related to `UpdateBucketMetadataAnnotationTableConfiguration`:
+  [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
+  [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)

## Request Syntax
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax"></a>

```
PUT /?metadataAnnotationTable HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<AnnotationTableConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <ConfigurationState>{{string}}</ConfigurationState>
   <EncryptionConfiguration>
      <KmsKeyArn>{{string}}</KmsKeyArn>
      <SseAlgorithm>{{string}}</SseAlgorithm>
   </EncryptionConfiguration>
   <Role>{{string}}</Role>
</AnnotationTableConfiguration>
```

## URI Request Parameters
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-header-Bucket"></a>
The name of the bucket whose annotation table configuration to update.
Required: Yes

 ** [Content-MD5](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-header-ContentMD5"></a>
Base64-encoded MD5 digest of the message body.

 ** [x-amz-expected-bucket-owner](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner.

 ** [x-amz-sdk-checksum-algorithm](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-header-ChecksumAlgorithm"></a>
Checksum algorithm for the request payload.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AnnotationTableConfiguration](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-AnnotationTableConfiguration"></a>
Root level tag for the AnnotationTableConfiguration parameters.
Required: Yes

 ** [ConfigurationState](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-ConfigurationState"></a>
The new configuration state to apply.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [EncryptionConfiguration](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-EncryptionConfiguration"></a>
 The encryption settings for an S3 Metadata journal table or inventory table configuration.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

 ** [Role](#API_UpdateBucketMetadataAnnotationTableConfiguration_RequestSyntax) **   <a name="AmazonS3-UpdateBucketMetadataAnnotationTableConfiguration-request-Role"></a>
The new IAM role ARN to apply.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_Examples"></a>

### Trust policy
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_Example_1"></a>

This example illustrates one usage of UpdateBucketMetadataAnnotationTableConfiguration.

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
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_Example_2"></a>

This example illustrates one usage of UpdateBucketMetadataAnnotationTableConfiguration.

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
          "aws:ResourceAccount": "123456789012"
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
          "aws:ResourceAccount": "123456789012"
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
            "s3.us-east-1.amazonaws.com"
          ]
        },
        "ArnLike": {
          "kms:EncryptionContext:aws:s3:arn": [
            "arn:aws:s3:::amzn-s3-demo-bucket",
            "arn:aws:s3:::amzn-s3-demo-bucket/*"
          ]
        }
      },
      "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"]
    }
  ]
}
```

## See Also
<a name="API_UpdateBucketMetadataAnnotationTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataAnnotationTableConfiguration)
