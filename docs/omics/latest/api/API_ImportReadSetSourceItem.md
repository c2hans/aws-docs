---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ImportReadSetSourceItem.html
---

# ImportReadSetSourceItem
<a name="API_ImportReadSetSourceItem"></a>

A source for an import read set job.

## Contents
<a name="API_ImportReadSetSourceItem_Contents"></a>

 ** sampleId **   <a name="omics-Type-ImportReadSetSourceItem-sampleId"></a>
The source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** sourceFiles **   <a name="omics-Type-ImportReadSetSourceItem-sourceFiles"></a>
The source files' location in Amazon S3.
Type: [SourceFiles](API_SourceFiles.md) object
Required: Yes

 ** sourceFileType **   <a name="omics-Type-ImportReadSetSourceItem-sourceFileType"></a>
The source's file type.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`
Required: Yes

 ** status **   <a name="omics-Type-ImportReadSetSourceItem-status"></a>
The source's status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | FINISHED | FAILED`
Required: Yes

 ** subjectId **   <a name="omics-Type-ImportReadSetSourceItem-subjectId"></a>
The source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** description **   <a name="omics-Type-ImportReadSetSourceItem-description"></a>
The source's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** generatedFrom **   <a name="omics-Type-ImportReadSetSourceItem-generatedFrom"></a>
Where the source originated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ImportReadSetSourceItem-name"></a>
The source's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** readSetId **   <a name="omics-Type-ImportReadSetSourceItem-readSetId"></a>
The source's read set ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: No

 ** referenceArn **   <a name="omics-Type-ImportReadSetSourceItem-referenceArn"></a>
The source's genome reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: No

 ** statusMessage **   <a name="omics-Type-ImportReadSetSourceItem-statusMessage"></a>
The source's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** tags **   <a name="omics-Type-ImportReadSetSourceItem-tags"></a>
The source's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ImportReadSetSourceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ImportReadSetSourceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ImportReadSetSourceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ImportReadSetSourceItem)
