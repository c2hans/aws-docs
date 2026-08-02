---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_RootDirectory.html
---

# RootDirectory
<a name="API_S3Files_RootDirectory"></a>

Specifies the root directory path and optional creation permissions for newly created directories.

## Contents
<a name="API_S3Files_RootDirectory_Contents"></a>

 ** creationPermissions **   <a name="AmazonS3-Type-S3Files_RootDirectory-creationPermissions"></a>
The permissions to set on newly created directories.
Type: [CreationPermissions](API_S3Files_CreationPermissions.md) object
Required: No

 ** path **   <a name="AmazonS3-Type-S3Files_RootDirectory-path"></a>
The path to use as the root directory for the access point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(\/|(\/(?!\.)+[^$#<>;;`|&?{}^*/\n]+){1,4})`
Required: No

## See Also
<a name="API_S3Files_RootDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/RootDirectory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/RootDirectory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/RootDirectory)
