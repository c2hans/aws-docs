---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StorageProfileSummary.html
---

# StorageProfileSummary
<a name="API_StorageProfileSummary"></a>

The details of a storage profile.

## Contents
<a name="API_StorageProfileSummary_Contents"></a>

 ** displayName **   <a name="deadlinecloud-Type-StorageProfileSummary-displayName"></a>
The display name of the storage profile summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** osFamily **   <a name="deadlinecloud-Type-StorageProfileSummary-osFamily"></a>
The operating system (OS) family.
Type: String
Valid Values: `WINDOWS | LINUX | MACOS`
Required: Yes

 ** storageProfileId **   <a name="deadlinecloud-Type-StorageProfileSummary-storageProfileId"></a>
The storage profile ID.
Type: String
Pattern: `sp-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_StorageProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StorageProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StorageProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StorageProfileSummary)
