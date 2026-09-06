---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CustomFileSystem.html
---

# CustomFileSystem
<a name="API_CustomFileSystem"></a>

A file system, created by you, that you assign to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Contents
<a name="API_CustomFileSystem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EFSFileSystem **   <a name="sagemaker-Type-CustomFileSystem-EFSFileSystem"></a>
A custom file system in Amazon EFS.
Type: [EFSFileSystem](API_EFSFileSystem.md) object
Required: No

 ** FSxLustreFileSystem **   <a name="sagemaker-Type-CustomFileSystem-FSxLustreFileSystem"></a>
A custom file system in Amazon FSx for Lustre.
Type: [FSxLustreFileSystem](API_FSxLustreFileSystem.md) object
Required: No

 ** S3FileSystem **   <a name="sagemaker-Type-CustomFileSystem-S3FileSystem"></a>
A custom file system in Amazon S3. This is only supported in Amazon SageMaker Unified Studio.
Type: [S3FileSystem](API_S3FileSystem.md) object
Required: No

## See Also
<a name="API_CustomFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CustomFileSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CustomFileSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CustomFileSystem)
