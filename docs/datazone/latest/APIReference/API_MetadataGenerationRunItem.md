---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_MetadataGenerationRunItem.html
---

# MetadataGenerationRunItem
<a name="API_MetadataGenerationRunItem"></a>

The metadata generation run.

## Contents
<a name="API_MetadataGenerationRunItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-MetadataGenerationRunItem-domainId"></a>
The ID of the Amazon DataZone domain in which the metadata generation run was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-MetadataGenerationRunItem-id"></a>
The ID of the metadata generation run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-MetadataGenerationRunItem-owningProjectId"></a>
The ID of the project that owns the asset for which the metadata generation was ran.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** createdAt **   <a name="datazone-Type-MetadataGenerationRunItem-createdAt"></a>
The timestamp at which the metadata generation run was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-MetadataGenerationRunItem-createdBy"></a>
The user who created the metadata generation run.
Type: String
Required: No

 ** status **   <a name="datazone-Type-MetadataGenerationRunItem-status"></a>
The status of the metadata generation run.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELED | SUCCEEDED | FAILED | PARTIALLY_SUCCEEDED`
Required: No

 ** target **   <a name="datazone-Type-MetadataGenerationRunItem-target"></a>
The asset for which metadata was generated.
Type: [MetadataGenerationRunTarget](API_MetadataGenerationRunTarget.md) object
Required: No

 ** type **   <a name="datazone-Type-MetadataGenerationRunItem-type"></a>
 *This member has been deprecated.*
The type of the metadata generation run.
Type: String
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`
Required: No

 ** types **   <a name="datazone-Type-MetadataGenerationRunItem-types"></a>
The types of the metadata generation run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`
Required: No

## See Also
<a name="API_MetadataGenerationRunItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/MetadataGenerationRunItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/MetadataGenerationRunItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/MetadataGenerationRunItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
