---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_MetadataGenerationRunTypeStat.html
---

# MetadataGenerationRunTypeStat
<a name="API_MetadataGenerationRunTypeStat"></a>

The statistics of the metadata generation run type.

## Contents
<a name="API_MetadataGenerationRunTypeStat_Contents"></a>

 ** status **   <a name="datazone-Type-MetadataGenerationRunTypeStat-status"></a>
The status of the metadata generation run type statistics.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELED | SUCCEEDED | FAILED | PARTIALLY_SUCCEEDED`
Required: Yes

 ** type **   <a name="datazone-Type-MetadataGenerationRunTypeStat-type"></a>
The type of the metadata generation run type statistics.
Type: String
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`
Required: Yes

 ** errorMessage **   <a name="datazone-Type-MetadataGenerationRunTypeStat-errorMessage"></a>
The error message displayed if the action fails to run.
Type: String
Required: No

## See Also
<a name="API_MetadataGenerationRunTypeStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/MetadataGenerationRunTypeStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/MetadataGenerationRunTypeStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/MetadataGenerationRunTypeStat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
