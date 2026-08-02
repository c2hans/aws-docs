---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_CustomDirectoriesType.html
---

# CustomDirectoriesType
<a name="API_CustomDirectoriesType"></a>

Contains Amazon S3 locations for storing specific types of AS2 message files.

## Contents
<a name="API_CustomDirectoriesType_Contents"></a>

 ** FailedFilesDirectory **   <a name="TransferFamily-Type-CustomDirectoriesType-FailedFilesDirectory"></a>
Specifies a location to store failed AS2 message files.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: Yes

 ** MdnFilesDirectory **   <a name="TransferFamily-Type-CustomDirectoriesType-MdnFilesDirectory"></a>
Specifies a location to store MDN files.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: Yes

 ** PayloadFilesDirectory **   <a name="TransferFamily-Type-CustomDirectoriesType-PayloadFilesDirectory"></a>
Specifies a location to store the payload for AS2 message files.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: Yes

 ** StatusFilesDirectory **   <a name="TransferFamily-Type-CustomDirectoriesType-StatusFilesDirectory"></a>
Specifies a location to store AS2 status messages.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: Yes

 ** TemporaryFilesDirectory **   <a name="TransferFamily-Type-CustomDirectoriesType-TemporaryFilesDirectory"></a>
Specifies a location to store temporary AS2 message files.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: Yes

## See Also
<a name="API_CustomDirectoriesType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/CustomDirectoriesType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/CustomDirectoriesType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/CustomDirectoriesType)
