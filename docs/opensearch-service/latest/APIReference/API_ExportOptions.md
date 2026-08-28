---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ExportOptions.html
---

# ExportOptions
<a name="API_ExportOptions"></a>

Options to filter the scope of saved objects to export during a migration.

## Contents
<a name="API_ExportOptions_Contents"></a>

 ** includeReferencesDeep **   <a name="opensearchservice-Type-ExportOptions-includeReferencesDeep"></a>
Specifies whether to include all objects referenced by the exported objects, recursively.
Type: Boolean
Required: No

 ** objects **   <a name="opensearchservice-Type-ExportOptions-objects"></a>
A list of specific saved objects to include in the migration, identified by type and ID.
Type: Array of [SavedObjectIdentifier](API_SavedObjectIdentifier.md) objects
Required: No

 ** types **   <a name="opensearchservice-Type-ExportOptions-types"></a>
A list of saved object types to include in the migration. Valid values include `dashboard`, `visualization`, `index-pattern`, `search`, and `query`.
Type: Array of strings
Required: No

## See Also
<a name="API_ExportOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ExportOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ExportOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ExportOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
