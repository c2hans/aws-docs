---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentEnrichmentConfiguration.html
---

# DocumentEnrichmentConfiguration
<a name="API_DocumentEnrichmentConfiguration"></a>

Provides the configuration information for altering document metadata and content during the document ingestion process.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).

## Contents
<a name="API_DocumentEnrichmentConfiguration_Contents"></a>

 ** inlineConfigurations **   <a name="qbusiness-Type-DocumentEnrichmentConfiguration-inlineConfigurations"></a>
Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.
Type: Array of [InlineDocumentEnrichmentConfiguration](API_InlineDocumentEnrichmentConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** postExtractionHookConfiguration **   <a name="qbusiness-Type-DocumentEnrichmentConfiguration-postExtractionHookConfiguration"></a>
Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.
You can configure your Lambda function using the `PreExtractionHookConfiguration` parameter if you want to apply advanced alterations on the original or raw documents.
If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration`.
You can only invoke one Lambda function. However, this function can invoke other functions it requires.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
Type: [HookConfiguration](API_HookConfiguration.md) object
Required: No

 ** preExtractionHookConfiguration **   <a name="qbusiness-Type-DocumentEnrichmentConfiguration-preExtractionHookConfiguration"></a>
Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.
You can configure your Lambda function using the `PreExtractionHookConfiguration` parameter if you want to apply advanced alterations on the original or raw documents.
If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration`.
You can only invoke one Lambda function. However, this function can invoke other functions it requires.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
Type: [HookConfiguration](API_HookConfiguration.md) object
Required: No

## See Also
<a name="API_DocumentEnrichmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentEnrichmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentEnrichmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentEnrichmentConfiguration)
