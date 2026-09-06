---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartReferenceImportJobSourceItem.html
---

# StartReferenceImportJobSourceItem
<a name="API_StartReferenceImportJobSourceItem"></a>

A source for a reference import job.

## Contents
<a name="API_StartReferenceImportJobSourceItem_Contents"></a>

 ** name **   <a name="omics-Type-StartReferenceImportJobSourceItem-name"></a>
The source's name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** sourceFile **   <a name="omics-Type-StartReferenceImportJobSourceItem-sourceFile"></a>
The source file's location in Amazon S3.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})`
Required: Yes

 ** description **   <a name="omics-Type-StartReferenceImportJobSourceItem-description"></a>
The source's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** tags **   <a name="omics-Type-StartReferenceImportJobSourceItem-tags"></a>
The source's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_StartReferenceImportJobSourceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartReferenceImportJobSourceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartReferenceImportJobSourceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartReferenceImportJobSourceItem)
