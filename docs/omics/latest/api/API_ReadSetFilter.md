---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReadSetFilter.html
---

# ReadSetFilter
<a name="API_ReadSetFilter"></a>

A filter for read sets.

## Contents
<a name="API_ReadSetFilter_Contents"></a>

 ** createdAfter **   <a name="omics-Type-ReadSetFilter-createdAfter"></a>
The filter's start date.
Type: Timestamp
Required: No

 ** createdBefore **   <a name="omics-Type-ReadSetFilter-createdBefore"></a>
The filter's end date.
Type: Timestamp
Required: No

 ** creationType **   <a name="omics-Type-ReadSetFilter-creationType"></a>
 The creation type of the read set.
Type: String
Valid Values: `IMPORT | UPLOAD`
Required: No

 ** generatedFrom **   <a name="omics-Type-ReadSetFilter-generatedFrom"></a>
 Where the source originated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ReadSetFilter-name"></a>
A name to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** referenceArn **   <a name="omics-Type-ReadSetFilter-referenceArn"></a>
A genome reference ARN to filter on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 127.
Pattern: `$|^arn:.+`
Required: No

 ** sampleId **   <a name="omics-Type-ReadSetFilter-sampleId"></a>
 The read set source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** status **   <a name="omics-Type-ReadSetFilter-status"></a>
A status to filter on.
Type: String
Valid Values: `ARCHIVED | ACTIVATING | ACTIVE | DELETING | DELETED | PROCESSING_UPLOAD | UPLOAD_FAILED`
Required: No

 ** subjectId **   <a name="omics-Type-ReadSetFilter-subjectId"></a>
 The read set source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ReadSetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReadSetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReadSetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReadSetFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
