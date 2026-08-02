---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttachedFileError.html
---

# AttachedFileError
<a name="API_AttachedFileError"></a>

Error describing a failure to retrieve attached file metadata through BatchGetAttachedFileMetadata action.

## Contents
<a name="API_AttachedFileError_Contents"></a>

 ** ErrorCode **   <a name="connect-Type-AttachedFileError-ErrorCode"></a>
 Status code describing the failure.
Type: String
Required: No

 ** ErrorMessage **   <a name="connect-Type-AttachedFileError-ErrorMessage"></a>
Why the attached file couldn't be retrieved.
Type: String
Required: No

 ** FileId **   <a name="connect-Type-AttachedFileError-FileId"></a>
The unique identifier of the attached file resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AttachedFileError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttachedFileError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttachedFileError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttachedFileError)
