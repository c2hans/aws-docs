---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetImportJobSourceItem.html
---

# StartReadSetImportJobSourceItem
<a name="API_StartReadSetImportJobSourceItem"></a>

A source for a read set import job.

## Contents
<a name="API_StartReadSetImportJobSourceItem_Contents"></a>

 ** sampleId **   <a name="omics-Type-StartReadSetImportJobSourceItem-sampleId"></a>
The source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** sourceFiles **   <a name="omics-Type-StartReadSetImportJobSourceItem-sourceFiles"></a>
The source files' location in Amazon S3.
Type: [SourceFiles](API_SourceFiles.md) object
Required: Yes

 ** sourceFileType **   <a name="omics-Type-StartReadSetImportJobSourceItem-sourceFileType"></a>
The source's file type.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`
Required: Yes

 ** subjectId **   <a name="omics-Type-StartReadSetImportJobSourceItem-subjectId"></a>
The source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** description **   <a name="omics-Type-StartReadSetImportJobSourceItem-description"></a>
The source's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** generatedFrom **   <a name="omics-Type-StartReadSetImportJobSourceItem-generatedFrom"></a>
Where the source originated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-StartReadSetImportJobSourceItem-name"></a>
The source's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** referenceArn **   <a name="omics-Type-StartReadSetImportJobSourceItem-referenceArn"></a>
The source's reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: No

 ** tags **   <a name="omics-Type-StartReadSetImportJobSourceItem-tags"></a>
The source's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_StartReadSetImportJobSourceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartReadSetImportJobSourceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartReadSetImportJobSourceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartReadSetImportJobSourceItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
