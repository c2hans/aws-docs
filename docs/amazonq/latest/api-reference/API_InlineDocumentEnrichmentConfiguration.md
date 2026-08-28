---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_InlineDocumentEnrichmentConfiguration.html
---

# InlineDocumentEnrichmentConfiguration
<a name="API_InlineDocumentEnrichmentConfiguration"></a>

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Q Business.

To apply advanced logic, to go beyond what you can do with basic logic, see [`HookConfiguration`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration.html).

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).

## Contents
<a name="API_InlineDocumentEnrichmentConfiguration_Contents"></a>

 ** condition **   <a name="qbusiness-Type-InlineDocumentEnrichmentConfiguration-condition"></a>
The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business. You use this with [`DocumentAttributeTarget`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html) to apply the condition.
For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source\_URI' field. Set the condition that if the 'Source\_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.
Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using `DocumentAttributeTarget`. Amazon Q Business then will map your newly created metadata field to your index field.
Type: [DocumentAttributeCondition](API_DocumentAttributeCondition.md) object
Required: No

 ** documentContentOperator **   <a name="qbusiness-Type-InlineDocumentEnrichmentConfiguration-documentContentOperator"></a>
 `TRUE` to delete content if the condition used for the target attribute is met.
Type: String
Valid Values: `DELETE`
Required: No

 ** target **   <a name="qbusiness-Type-InlineDocumentEnrichmentConfiguration-target"></a>
The target document attribute or metadata field you want to alter when ingesting documents into Amazon Q Business.
For example, you can delete all customer identification numbers associated with the documents, stored in the document metadata field called 'Customer\_ID' by setting the target key as 'Customer\_ID' and the deletion flag to `TRUE`. This removes all customer ID values in the field 'Customer\_ID'. This would scrub personally identifiable information from each document's metadata.
Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using [`DocumentAttributeTarget`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html). Amazon Q Business will then map your newly created document attribute to your index field.
You can also use this with [`DocumentAttributeCondition`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition.html).
Type: [DocumentAttributeTarget](API_DocumentAttributeTarget.md) object
Required: No

## See Also
<a name="API_InlineDocumentEnrichmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/InlineDocumentEnrichmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/InlineDocumentEnrichmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/InlineDocumentEnrichmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
