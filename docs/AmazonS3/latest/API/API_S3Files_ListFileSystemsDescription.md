---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListFileSystemsDescription.html
---

# ListFileSystemsDescription
<a name="API_S3Files_ListFileSystemsDescription"></a>

Contains information about an S3 File System returned in list operations.

## Contents
<a name="API_S3Files_ListFileSystemsDescription_Contents"></a>

 ** bucket **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-bucket"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Pattern: `(arn:aws[a-zA-Z0-9-]*:s3:::.+)`
Required: Yes

 ** creationTime **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-creationTime"></a>
The time when the file system was created.
Type: Timestamp
Required: Yes

 ** fileSystemArn **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the file system.
Type: String
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40})`
Required: Yes

 ** fileSystemId **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-fileSystemId"></a>
The ID of the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

 ** ownerId **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-ownerId"></a>
The AWS account ID of the file system owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`
Required: Yes

 ** roleArn **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used for S3 access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** status **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-status"></a>
The current status of the file system.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`
Required: Yes

 ** name **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-name"></a>
The name of the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** statusMessage **   <a name="AmazonS3-Type-S3Files_ListFileSystemsDescription-statusMessage"></a>
Additional information about the file system status.
Type: String
Required: No

## See Also
<a name="API_S3Files_ListFileSystemsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListFileSystemsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListFileSystemsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListFileSystemsDescription)
