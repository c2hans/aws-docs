---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ImportReferenceSourceItem.html
---

# ImportReferenceSourceItem
<a name="API_ImportReferenceSourceItem"></a>

An genome reference source.

## Contents
<a name="API_ImportReferenceSourceItem_Contents"></a>

 ** status **   <a name="omics-Type-ImportReferenceSourceItem-status"></a>
The source's status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | FINISHED | FAILED`
Required: Yes

 ** description **   <a name="omics-Type-ImportReferenceSourceItem-description"></a>
The source's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ImportReferenceSourceItem-name"></a>
The source's name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** referenceId **   <a name="omics-Type-ImportReferenceSourceItem-referenceId"></a>
The source's reference ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: No

 ** sourceFile **   <a name="omics-Type-ImportReferenceSourceItem-sourceFile"></a>
The source file's location in Amazon S3.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})`
Required: No

 ** statusMessage **   <a name="omics-Type-ImportReferenceSourceItem-statusMessage"></a>
The source's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** tags **   <a name="omics-Type-ImportReferenceSourceItem-tags"></a>
The source's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ImportReferenceSourceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ImportReferenceSourceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ImportReferenceSourceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ImportReferenceSourceItem)
