---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_FileInformation.html
---

# FileInformation
<a name="API_FileInformation"></a>

Details about a file.

## Contents
<a name="API_FileInformation_Contents"></a>

 ** contentLength **   <a name="omics-Type-FileInformation-contentLength"></a>
The file's content length.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 5497558138880.
Required: No

 ** partSize **   <a name="omics-Type-FileInformation-partSize"></a>
The file's part size.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 5368709120.
Required: No

 ** s3Access **   <a name="omics-Type-FileInformation-s3Access"></a>
The S3 URI metadata of a sequence store.
Type: [ReadSetS3Access](API_ReadSetS3Access.md) object
Required: No

 ** totalParts **   <a name="omics-Type-FileInformation-totalParts"></a>
The file's total parts.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## See Also
<a name="API_FileInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/FileInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/FileInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/FileInformation)
