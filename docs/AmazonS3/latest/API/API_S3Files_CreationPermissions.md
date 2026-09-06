---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_CreationPermissions.html
---

# CreationPermissions
<a name="API_S3Files_CreationPermissions"></a>

Specifies the permissions to set on newly created directories within the file system.

## Contents
<a name="API_S3Files_CreationPermissions_Contents"></a>

 ** ownerGid **   <a name="AmazonS3-Type-S3Files_CreationPermissions-ownerGid"></a>
The POSIX group ID to assign to newly created directories.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** ownerUid **   <a name="AmazonS3-Type-S3Files_CreationPermissions-ownerUid"></a>
The POSIX user ID to assign to newly created directories.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** permissions **   <a name="AmazonS3-Type-S3Files_CreationPermissions-permissions"></a>
The octal permissions to assign to newly created directories.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 4.
Pattern: `[0-7]{3,4}`
Required: Yes

## See Also
<a name="API_S3Files_CreationPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/CreationPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/CreationPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/CreationPermissions)
