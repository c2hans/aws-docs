---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListAccessPointsDescription.html
---

# ListAccessPointsDescription
<a name="API_S3Files_ListAccessPointsDescription"></a>

Contains information about an S3 File System Access Point returned in list operations.

## Contents
<a name="API_S3Files_ListAccessPointsDescription_Contents"></a>

 ** accessPointArn **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-accessPointArn"></a>
The Amazon Resource Name (ARN) of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
Required: Yes

 ** accessPointId **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-accessPointId"></a>
The ID of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}|fsap-[0-9a-f]{17,40})`
Required: Yes

 ** fileSystemId **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-fileSystemId"></a>
The ID of the S3 File System.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

 ** ownerId **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-ownerId"></a>
The AWS account ID of the access point owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`
Required: Yes

 ** status **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-status"></a>
The current status of the access point.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`
Required: Yes

 ** name **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-name"></a>
The name of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** posixUser **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-posixUser"></a>
The POSIX identity configured for this access point.
Type: [PosixUser](API_S3Files_PosixUser.md) object
Required: No

 ** rootDirectory **   <a name="AmazonS3-Type-S3Files_ListAccessPointsDescription-rootDirectory"></a>
The root directory configuration for this access point.
Type: [RootDirectory](API_S3Files_RootDirectory.md) object
Required: No

## See Also
<a name="API_S3Files_ListAccessPointsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListAccessPointsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListAccessPointsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListAccessPointsDescription)
