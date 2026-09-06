---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_MultipartReadSetUploadListItem.html
---

# MultipartReadSetUploadListItem
<a name="API_MultipartReadSetUploadListItem"></a>

 Part of the response to ListMultipartReadSetUploads, excluding completed and aborted multipart uploads.

## Contents
<a name="API_MultipartReadSetUploadListItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-MultipartReadSetUploadListItem-creationTime"></a>
 The time stamp for when a direct upload was created.
Type: Timestamp
Required: Yes

 ** generatedFrom **   <a name="omics-Type-MultipartReadSetUploadListItem-generatedFrom"></a>
 The source of an uploaded part.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** referenceArn **   <a name="omics-Type-MultipartReadSetUploadListItem-referenceArn"></a>
 The source's reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: Yes

 ** sampleId **   <a name="omics-Type-MultipartReadSetUploadListItem-sampleId"></a>
 The read set source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** sequenceStoreId **   <a name="omics-Type-MultipartReadSetUploadListItem-sequenceStoreId"></a>
 The sequence store ID used for the multipart upload.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** sourceFileType **   <a name="omics-Type-MultipartReadSetUploadListItem-sourceFileType"></a>
 The type of file the read set originated from.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`
Required: Yes

 ** subjectId **   <a name="omics-Type-MultipartReadSetUploadListItem-subjectId"></a>
 The read set source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** uploadId **   <a name="omics-Type-MultipartReadSetUploadListItem-uploadId"></a>
 The ID for the initiated multipart upload.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** description **   <a name="omics-Type-MultipartReadSetUploadListItem-description"></a>
 The description of a read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-MultipartReadSetUploadListItem-name"></a>
 The name of a read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** tags **   <a name="omics-Type-MultipartReadSetUploadListItem-tags"></a>
 Any tags you wish to add to a read set.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MultipartReadSetUploadListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/MultipartReadSetUploadListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/MultipartReadSetUploadListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/MultipartReadSetUploadListItem)
