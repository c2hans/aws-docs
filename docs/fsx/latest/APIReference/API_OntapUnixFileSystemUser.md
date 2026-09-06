---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_OntapUnixFileSystemUser.html
---

# OntapUnixFileSystemUser
<a name="API_OntapUnixFileSystemUser"></a>

The FSx for ONTAP UNIX file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Contents
<a name="API_OntapUnixFileSystemUser_Contents"></a>

 ** Name **   <a name="FSx-Type-OntapUnixFileSystemUser-Name"></a>
The name of the UNIX user. The name can be up to 256 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
Required: Yes

## See Also
<a name="API_OntapUnixFileSystemUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OntapUnixFileSystemUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OntapUnixFileSystemUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OntapUnixFileSystemUser)
