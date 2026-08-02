---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FileSystemLocation.html
---

# FileSystemLocation
<a name="API_FileSystemLocation"></a>

The details of the file system location for the resource.

## Contents
<a name="API_FileSystemLocation_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-FileSystemLocation-name"></a>
The location name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z ]*`
Required: Yes

 ** path **   <a name="deadlinecloud-Type-FileSystemLocation-path"></a>
The file path.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** type **   <a name="deadlinecloud-Type-FileSystemLocation-type"></a>
The type of file.
Type: String
Valid Values: `SHARED | LOCAL`
Required: Yes

## See Also
<a name="API_FileSystemLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FileSystemLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FileSystemLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FileSystemLocation)
