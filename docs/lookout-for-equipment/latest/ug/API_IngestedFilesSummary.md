---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_IngestedFilesSummary.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# IngestedFilesSummary
<a name="API_IngestedFilesSummary"></a>

Gives statistics about how many files have been ingested, and which files have not been ingested, for a particular ingestion job.

## Contents
<a name="API_IngestedFilesSummary_Contents"></a>

 ** IngestedNumberOfFiles **   <a name="LookoutForEquipment-Type-IngestedFilesSummary-IngestedNumberOfFiles"></a>
Indicates the number of files that were successfully ingested.
Type: Integer
Required: Yes

 ** TotalNumberOfFiles **   <a name="LookoutForEquipment-Type-IngestedFilesSummary-TotalNumberOfFiles"></a>
Indicates the total number of files that were submitted for ingestion.
Type: Integer
Required: Yes

 ** DiscardedFiles **   <a name="LookoutForEquipment-Type-IngestedFilesSummary-DiscardedFiles"></a>
Indicates the number of files that were discarded. A file could be discarded because its format is invalid (for example, a jpg or pdf) or not readable.
Type: Array of [S3Object](API_S3Object.md) objects
Array Members: Minimum number of 0 items.
Required: No

## See Also
<a name="API_IngestedFilesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/IngestedFilesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/IngestedFilesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/IngestedFilesSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
