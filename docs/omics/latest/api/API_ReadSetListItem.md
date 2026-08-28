---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReadSetListItem.html
---

# ReadSetListItem
<a name="API_ReadSetListItem"></a>

A read set.

## Contents
<a name="API_ReadSetListItem_Contents"></a>

 ** arn **   <a name="omics-Type-ReadSetListItem-arn"></a>
The read set's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: Yes

 ** creationTime **   <a name="omics-Type-ReadSetListItem-creationTime"></a>
When the read set was created.
Type: Timestamp
Required: Yes

 ** fileType **   <a name="omics-Type-ReadSetListItem-fileType"></a>
The read set's file type.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`
Required: Yes

 ** id **   <a name="omics-Type-ReadSetListItem-id"></a>
The read set's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** sequenceStoreId **   <a name="omics-Type-ReadSetListItem-sequenceStoreId"></a>
The read set's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** status **   <a name="omics-Type-ReadSetListItem-status"></a>
The read set's status.
Type: String
Valid Values: `ARCHIVED | ACTIVATING | ACTIVE | DELETING | DELETED | PROCESSING_UPLOAD | UPLOAD_FAILED`
Required: Yes

 ** creationType **   <a name="omics-Type-ReadSetListItem-creationType"></a>
 The creation type of the read set.
Type: String
Valid Values: `IMPORT | UPLOAD`
Required: No

 ** description **   <a name="omics-Type-ReadSetListItem-description"></a>
The read set's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** etag **   <a name="omics-Type-ReadSetListItem-etag"></a>
The entity tag (ETag) is a hash of the object representing its semantic content.
Type: [ETag](API_ETag.md) object
Required: No

 ** name **   <a name="omics-Type-ReadSetListItem-name"></a>
The read set's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** referenceArn **   <a name="omics-Type-ReadSetListItem-referenceArn"></a>
The read set's genome reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: No

 ** sampleId **   <a name="omics-Type-ReadSetListItem-sampleId"></a>
The read set's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** sequenceInformation **   <a name="omics-Type-ReadSetListItem-sequenceInformation"></a>
Details about a sequence.
Type: [SequenceInformation](API_SequenceInformation.md) object
Required: No

 ** statusMessage **   <a name="omics-Type-ReadSetListItem-statusMessage"></a>
 The status for a read set. It provides more detail as to why the read set has a status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** subjectId **   <a name="omics-Type-ReadSetListItem-subjectId"></a>
The read set's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ReadSetListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReadSetListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReadSetListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReadSetListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
