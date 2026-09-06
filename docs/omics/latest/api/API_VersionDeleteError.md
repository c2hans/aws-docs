---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_VersionDeleteError.html
---

# VersionDeleteError
<a name="API_VersionDeleteError"></a>

 The error preventing deletion of the annotation store version.

## Contents
<a name="API_VersionDeleteError_Contents"></a>

 ** message **   <a name="omics-Type-VersionDeleteError-message"></a>
 The message explaining the error in annotation store deletion.
Type: String
Required: Yes

 ** versionName **   <a name="omics-Type-VersionDeleteError-versionName"></a>
 The name given to an annotation store version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

## See Also
<a name="API_VersionDeleteError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/VersionDeleteError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/VersionDeleteError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/VersionDeleteError)
