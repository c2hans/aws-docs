---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FileSystemDataSource.html
---

# FileSystemDataSource
<a name="API_FileSystemDataSource"></a>

Specifies a file system data source for a channel.

## Contents
<a name="API_FileSystemDataSource_Contents"></a>

 ** DirectoryPath **   <a name="sagemaker-Type-FileSystemDataSource-DirectoryPath"></a>
The full path to the directory to associate with the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.*`
Required: Yes

 ** FileSystemAccessMode **   <a name="sagemaker-Type-FileSystemDataSource-FileSystemAccessMode"></a>
The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.
Type: String
Valid Values: `rw | ro`
Required: Yes

 ** FileSystemId **   <a name="sagemaker-Type-FileSystemDataSource-FileSystemId"></a>
The file system id.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `(fs-[0-9a-f]{8,})`
Required: Yes

 ** FileSystemType **   <a name="sagemaker-Type-FileSystemDataSource-FileSystemType"></a>
The file system type.
Type: String
Valid Values: `EFS | FSxLustre`
Required: Yes

## See Also
<a name="API_FileSystemDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FileSystemDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FileSystemDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FileSystemDataSource)
